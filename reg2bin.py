import sys
import codecs
import re
import binascii

# Converting the "hex" entries of a Windows registry dump file to *.bin files

def cut_line(line):
	return [hex for hex in line.split(u':')[-1].split(u',') if len(hex) != 0]

if len(sys.argv) == 1:
	print 'Usage: %s filename.reg' % sys.argv[0]
	sys.exit(1)

with codecs.open(sys.argv[1], 'r', 'utf16') as f:
	if 'Windows Registry Editor Version 5.00' not in f.readline():
		print '"%s" is not a registry file.' % sys.argv[1].upper()
		sys.exit(1)
	
	lines = [line.strip('\\\n\r ') for line in f.readlines()]
	
	keyname = None
	valuename = ''
	keydata = {}
	
	for line in lines:
		if len(line) == 0:
			continue
		
		if (line[0] == u'[' and line[-1] == u']') or (keyname == None):
			keyname = line.strip(u'[]').split(u'\\')[-1]
			print 'Processing key %s... ' % keyname
		else:
			if line[0] == u'"':
				line_split = re.split('["=:]+', line)
				
				if line_split[2] == u'hex':
					print 'Found "%s"' % line_split[1]
					keydata[(keyname, line_split[1])] = cut_line(line)
			else:
				keydata[(keyname, line_split[1])] += cut_line(line)

	for value_id in keydata:
		e_filename = '%s_%s.bin' % value_id
		print 'Creating %s...' % e_filename
		with open(e_filename, 'wb') as f:
			f.write(binascii.unhexlify(''.join(keydata[value_id])))

	print 'OK'
