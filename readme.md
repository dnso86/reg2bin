# reg2bin.py

A simple script to help converting (only) REG_BINARY entries exported from the Windows Registry, to *.bin files.

Comes with absolutely no warranty.
PRs are welcome.

## Usage

**python reg2bin.py registry_file.reg**

where *registry_file.reg* is something exported from regedit.exe - starts with "Windows Registry Editor Version 5.00".
The script creates filenames as Keyname_Valuename.bin