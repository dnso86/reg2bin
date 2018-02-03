# reg2bin.py

A simple script to help converting (only) the `REG_BINARY` entries exported from the Registry, to *.bin files.
E.g. turning files containing entries such:

```
#!python

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa\AccessProviders]
"MartaExtension"="ntmarta.dll"
"ProviderOrder"=hex(7):57,00,69,00,6e,00,64,00,6f,00,77,00,73,00,20,00,4e,00,\
  54,00,20,00,41,00,63,00,63,00,65,00,73,00,73,00,20,00,50,00,72,00,6f,00,76,\
  00,69,00,64,00,65,00,72,00,00,00,00,00
```
to a binary file for editing.

Comes with absolutely no warranty.
PRs are welcome.

## Usage

**python reg2bin.py sample.reg**

where *registry_file.reg* is something exported from regedit.exe - starts with "Windows Registry Editor Version 5.00".
The script creates filenames as *Keyname_Valuename.bin*
