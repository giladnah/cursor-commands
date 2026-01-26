#!/usr/bin/env python3
"""
Arduino Upload Tool for Cursor IDE.

This tool uploads Arduino sketches to Arduino Nano (CH340 clone) devices.
It uses arduino-cli with the old bootloader option required for CH340 clones.

Usage:
    python arduino_upload.py <sketch_path> [port] [--compile-only]
"""

import os
import sys
import subprocess
import logging
import tempfile
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def install_arduino_cli() -> Optional[Path]:
    """
    Download and install arduino-cli on demand to system PATH.

    Installs to default location (usually ~/bin or system bin directory)
    so it's available system-wide.

    Returns:
        Path to installed arduino-cli or None if installation failed.
    """
    print("arduino-cli not found. Downloading and installing to system PATH...")

    # Download and install using official installer script
    install_script_url = "https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh"

    try:
        # Download installer script
        curl_result = subprocess.run(
            ["curl", "-fsSL", install_script_url],
            capture_output=True,
            text=True,
            check=True
        )

        # Save installer script temporarily
        with tempfile.NamedTemporaryFile(mode='w', suffix='.sh', delete=False) as tmp_script:
            tmp_script.write(curl_result.stdout)
            tmp_script_path = tmp_script.name

        # Make executable and run installer (uses default system location)
        os.chmod(tmp_script_path, 0o755)

        install_result = subprocess.run(
            ["bash", tmp_script_path],
            capture_output=True,
            text=True,
            check=False
        )

        # Clean up temp script
        os.unlink(tmp_script_path)

        if install_result.returncode == 0:
            # Check if arduino-cli is now in PATH
            which_result = subprocess.run(
                ["which", "arduino-cli"],
                capture_output=True,
                text=True,
                check=False
            )
            if which_result.returncode == 0:
                cli_path = Path(which_result.stdout.strip())
                print(f"✓ arduino-cli installed successfully to {cli_path}")
                return cli_path
            else:
                print("✓ Installation completed, but arduino-cli not found in PATH")
                print("You may need to restart your terminal or add the install directory to PATH")
                return None
        else:
            print("✗ Installation failed!")
            if install_result.stderr:
                print(install_result.stderr)
            if install_result.stdout:
                print(install_result.stdout)
            return None

    except (subprocess.SubprocessError, OSError) as e:
        print(f"Error installing arduino-cli: {e}")
        print("\nManual installation:")
        print(f"  curl -fsSL {install_script_url} | sh")
        return None


def find_arduino_cli(auto_install: bool = True) -> Optional[Path]:
    """
    Find arduino-cli executable, optionally installing it if not found.

    Checks system PATH first, then installs to system location if not found.

    Args:
        auto_install: If True, automatically install arduino-cli if not found.

    Returns:
        Path to arduino-cli or None if not found and installation failed.
    """
    # Check system PATH first
    which_result = subprocess.run(
        ["which", "arduino-cli"],
        capture_output=True,
        text=True,
        check=False
    )
    if which_result.returncode == 0:
        return Path(which_result.stdout.strip())

    # Not found - install on demand if requested
    if auto_install:
        return install_arduino_cli()

    return None


def find_arduino_port() -> Optional[str]:
    """
    Find Arduino device port.

    Returns:
        Port path (e.g., /dev/ttyUSB0) or None if not found.
    """
    # Check common USB serial ports
    common_ports = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyACM0", "/dev/ttyACM1"]

    for port in common_ports:
        if os.path.exists(port):
            return port

    # Try to find via lsusb (CH340)
    try:
        lsusb_result = subprocess.run(
            ["lsusb"],
            capture_output=True,
            text=True,
            check=False
        )
        if lsusb_result.returncode == 0 and ("CH340" in lsusb_result.stdout or "7523" in lsusb_result.stdout):
            # CH340 found, check for ttyUSB devices
            for port in common_ports:
                if os.path.exists(port):
                    return port
    except (subprocess.SubprocessError, OSError):
        pass

    return None


def ensure_avr_core_installed(arduino_cli: Path) -> bool:
    """
    Ensure Arduino AVR core is installed, installing it if missing.

    Args:
        arduino_cli: Path to arduino-cli executable.

    Returns:
        True if core is available (or was successfully installed), False otherwise.
    """
    # Check if AVR core is installed
    check_cmd = [
        str(arduino_cli),
        "core",
        "list"
    ]

    try:
        result = subprocess.run(
            check_cmd,
            capture_output=True,
            text=True,
            check=False
        )

        # Check if arduino:avr is in the output
        if result.returncode == 0 and "arduino:avr" in result.stdout:
            return True

        # Core not found - install it
        print("Arduino AVR core not found. Installing...")
        install_cmd = [
            str(arduino_cli),
            "core",
            "install",
            "arduino:avr"
        ]

        install_result = subprocess.run(
            install_cmd,
            capture_output=True,
            text=True,
            check=False
        )

        if install_result.returncode == 0:
            print("✓ Arduino AVR core installed successfully!")
            return True
        else:
            print("✗ Failed to install Arduino AVR core!")
            if install_result.stderr:
                print(install_result.stderr)
            if install_result.stdout:
                print(install_result.stdout)
            return False

    except (subprocess.SubprocessError, OSError) as e:
        print(f"Error checking/installing AVR core: {e}")
        return False


def compile_sketch(arduino_cli: Path, sketch_path: Path) -> bool:
    """
    Compile Arduino sketch.

    Args:
        arduino_cli: Path to arduino-cli executable.
        sketch_path: Path to sketch directory or .ino file.

    Returns:
        True if compilation successful, False otherwise.
    """
    # If .ino file provided, use parent directory
    if sketch_path.is_file() and sketch_path.suffix == ".ino":
        sketch_path = sketch_path.parent

    if not sketch_path.exists():
        print(f"Error: Sketch path does not exist: {sketch_path}")
        return False

    # Ensure AVR core is installed
    if not ensure_avr_core_installed(arduino_cli):
        print("Warning: AVR core installation failed, compilation may fail")

    print(f"Compiling sketch: {sketch_path}")
    print("Using old bootloader (required for CH340 clones)...")

    cmd = [
        str(arduino_cli),
        "compile",
        "--fqbn", "arduino:avr:nano:cpu=atmega328old",
        str(sketch_path)
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            print("✓ Compilation successful!")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print("✗ Compilation failed!")
            if result.stderr:
                print(result.stderr)
            if result.stdout:
                print(result.stdout)
            return False

    except (subprocess.SubprocessError, OSError) as e:
        print(f"Error running arduino-cli: {e}")
        return False


def upload_sketch(
    arduino_cli: Path,
    sketch_path: Path,
    port: Optional[str] = None
) -> bool:
    """
    Upload Arduino sketch to device.

    Args:
        arduino_cli: Path to arduino-cli executable.
        sketch_path: Path to sketch directory or .ino file.
        port: Serial port (e.g., /dev/ttyUSB0). If None, will try to auto-detect.

    Returns:
        True if upload successful, False otherwise.
    """
    # If .ino file provided, use parent directory
    if sketch_path.is_file() and sketch_path.suffix == ".ino":
        sketch_path = sketch_path.parent

    if not sketch_path.exists():
        print(f"Error: Sketch path does not exist: {sketch_path}")
        return False

    # Auto-detect port if not provided
    if not port:
        port = find_arduino_port()
        if not port:
            print("Error: Could not find Arduino device.")
            print("Please specify port manually: /dev/ttyUSB0 or /dev/ttyACM0")
            return False

    print(f"Uploading sketch: {sketch_path}")
    print(f"Port: {port}")
    print("Using old bootloader (required for CH340 clones)...")

    cmd = [
        str(arduino_cli),
        "upload",
        "-p", port,
        "--fqbn", "arduino:avr:nano:cpu=atmega328old",
        str(sketch_path)
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            print("✓ Upload successful!")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print("✗ Upload failed!")
            if result.stderr:
                print(result.stderr)
            if result.stdout:
                print(result.stdout)
            print("\nTroubleshooting:")
            print("1. Check that Arduino is connected")
            print("2. Try pressing reset button on Arduino right before upload")
            print("3. Verify port is correct: ls -la /dev/ttyUSB* /dev/ttyACM*")
            print("4. Check user is in dialout group: groups | grep dialout")
            return False

    except (subprocess.SubprocessError, OSError) as e:
        print(f"Error running arduino-cli: {e}")
        return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: arduino_upload.py <sketch_path> [port] [--compile-only]")
        print("\nExamples:")
        print("  python arduino_upload.py blink")
        print("  python arduino_upload.py blink /dev/ttyUSB0")
        print("  python arduino_upload.py blink --compile-only")
        sys.exit(1)

    sketch_path = Path(sys.argv[1]).resolve()
    port = None
    compile_only = False

    # Parse arguments
    for arg in sys.argv[2:]:
        if arg == "--compile-only":
            compile_only = True
        elif not arg.startswith("--"):
            port = arg

    # Find arduino-cli (auto-install if not found)
    arduino_cli = find_arduino_cli(auto_install=True)
    if not arduino_cli:
        print("Error: arduino-cli not found and installation failed!")
        print("\nManual installation options:")
        print("1. Run: curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh")
        print("2. Or install to project: curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | BINDIR=./bin sh")
        sys.exit(1)

    print(f"Using arduino-cli: {arduino_cli}")

    # Compile
    if not compile_sketch(arduino_cli, sketch_path):
        sys.exit(1)

    # Upload (unless compile-only)
    if not compile_only:
        if not upload_sketch(arduino_cli, sketch_path, port):
            sys.exit(1)
    else:
        print("Compile-only mode: skipping upload")

    print("\n✓ Done!")


if __name__ == "__main__":
    main()

