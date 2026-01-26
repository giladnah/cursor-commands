# Upload Arduino Sketch

Upload Arduino sketches to Arduino Nano (CH340 clone) devices using arduino-cli with the old bootloader option.

## Usage

Invoke this command with:
```
@arduino-upload <sketch_path> [port] [--compile-only]
```

Or simply:
```
@arduino-upload <sketch_path>
```
The tool will auto-detect the Arduino port if not specified.

## Parameters

- **sketch_path** (required): Path to the Arduino sketch
  - Can be a directory containing `.ino` file: `blink` or `blink/`
  - Or the `.ino` file directly: `blink/blink.ino`
  - Can be relative or absolute path

- **port** (optional): Serial port for Arduino device
  - Examples: `/dev/ttyUSB0`, `/dev/ttyACM0`
  - If not specified, tool will auto-detect (checks `/dev/ttyUSB0`, `/dev/ttyUSB1`, `/dev/ttyACM0`, `/dev/ttyACM1`)
  - Auto-detection looks for CH340 devices via `lsusb`

- **--compile-only** (optional): Only compile the sketch, don't upload
  - Useful for checking if code compiles before uploading
  - Example: `@arduino-upload blink --compile-only`

## What This Command Does

1. **Finds or installs arduino-cli** - Checks for arduino-cli in:
   - System PATH (checks if already installed)
   - **Auto-installs** to system location if not found (downloads on demand)
   - Installation uses official Arduino installer (installs to ~/bin or system bin)

2. **Ensures AVR core is installed** - Checks for Arduino AVR boards core:
   - **Auto-installs** if missing using `arduino-cli core install arduino:avr`

3. **Compiles the sketch** - Uses arduino-cli with:
   - Board: `arduino:avr:nano`
   - Bootloader: `cpu=atmega328old` (required for CH340 clones)

4. **Uploads to device** - Uploads compiled sketch to Arduino:
   - Auto-detects port if not specified
   - Uses old bootloader option for CH340 compatibility
   - Provides troubleshooting tips on failure

## Example Usage

### Upload blink sketch (auto-detect port):
```
@arduino-upload blink
```

### Upload to specific port:
```
@arduino-upload blink /dev/ttyUSB0
```

### Upload from full path:
```
@arduino-upload /home/user/projects/blink
```

### Compile only (no upload):
```
@arduino-upload blink --compile-only
```

### Upload specific .ino file:
```
@arduino-upload blink/blink.ino
```

## Requirements

### Hardware
- Arduino Nano (or compatible) with CH340 USB-to-serial chip
- USB cable connected to computer

### Software
- **arduino-cli** - **Installed automatically on demand**
  - Tool downloads and installs to system location (usually ~/bin) if not found
  - Uses official Arduino installer script
  - Installed system-wide, available in PATH
  - Manual installation: `curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh`
- **Arduino AVR boards** core - **Installed automatically on demand**
  - Tool checks and installs using `arduino-cli core install arduino:avr` if missing
  - No manual intervention needed

### Permissions
- User must be in `dialout` group to access serial ports
  - Check: `groups | grep dialout`
  - Add user: `sudo usermod -a -G dialout $USER` (then log out and back in)

## Board Configuration

This command is configured for:
- **Board**: Arduino Nano
- **Bootloader**: Old bootloader (`atmega328old`)
  - Required for CH340 clones
  - Standard bootloader won't work with CH340 chips

## Integration with Tools

This command uses the `tools/arduino_upload.py` tool. The tool:
- **Downloads and installs arduino-cli on demand** to system PATH if not found
- **Installs Arduino AVR core on demand** if missing
- Locates arduino-cli automatically (checks system PATH)
- Auto-detects Arduino port
- Compiles with correct bootloader settings
- Uploads with proper configuration
- Provides clear error messages and troubleshooting

**Tool Path**: `tools/arduino_upload.py` (relative to `.cursor/` directory)

**Direct Tool Usage** (from repository root):
```bash
python .cursor/tools/arduino_upload.py <sketch_path> [port] [--compile-only]
```

## Troubleshooting

### Arduino-cli Installation Failed
**Error**: "arduino-cli not found and installation failed!"

**Note**: The tool automatically tries to install arduino-cli to system PATH if not found. If installation fails:

**Solutions**:
1. Check internet connection (installer downloads from GitHub)
2. Check write permissions to install directory (usually ~/bin)
3. Manual installation:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
   ```
4. After installation, restart terminal or run: `source ~/.bashrc` (or equivalent)
5. Verify installation: `which arduino-cli`

### Port Not Found
**Error**: "Could not find Arduino device"

**Solutions**:
1. Check device is connected: `lsusb | grep CH340`
2. Check available ports: `ls -la /dev/ttyUSB* /dev/ttyACM*`
3. Specify port manually: `@arduino-upload blink /dev/ttyUSB0`
4. Check permissions: `groups | grep dialout`
5. Add user to dialout: `sudo usermod -a -G dialout $USER` (then log out/in)

### Upload Failed - Sync Error
**Error**: "not in sync: resp=0x2d"

**Solutions**:
1. **Press reset button** on Arduino right before upload
2. Try uploading again
3. Check USB cable connection
4. Try different USB port
5. Verify bootloader option is correct (tool uses old bootloader automatically)

### Permission Denied
**Error**: "Permission denied" when accessing port

**Solutions**:
1. Check user is in dialout group: `groups | grep dialout`
2. Add user to dialout: `sudo usermod -a -G dialout $USER`
3. Log out and log back in (or restart)
4. Verify: `ls -la /dev/ttyUSB0` shows `dialout` group

### Compilation Errors
**Error**: Compilation fails

**Solutions**:
1. Check sketch syntax
2. Verify all libraries are installed
3. Check board selection matches hardware
4. Review error messages for specific issues

### Wrong Bootloader
**Error**: Upload succeeds but Arduino doesn't work

**Solutions**:
1. Verify using old bootloader (tool does this automatically)
2. Check board type matches (Arduino Nano)
3. Try re-uploading with reset button press

## Best Practices

1. **Test compilation first**: Use `--compile-only` to check code before uploading
2. **Auto-detect when possible**: Let tool find port automatically
3. **Check connections**: Ensure USB cable is secure
4. **Press reset if needed**: Some uploads require reset button press
5. **Use consistent ports**: If you have multiple devices, specify ports explicitly

## Related Commands

- Other Arduino-related commands may be added in the future

## Notes

- Tool automatically uses old bootloader (`atmega328old`) for CH340 compatibility
- Auto-detection checks common ports: `/dev/ttyUSB0`, `/dev/ttyUSB1`, `/dev/ttyACM0`, `/dev/ttyACM1`
- Tool looks for arduino-cli in project's `bin/` directory first, then system PATH
- All paths are resolved relative to current working directory
- Sketch can be specified as directory or `.ino` file (both work)

