import binascii
import codecs
import re
import sys


def main():
    '''Converting the "hex" entries of a Windows registry dump file
    to *.bin files'''
    if len(sys.argv) == 1:
        print('Usage: %s filename.reg' % sys.argv[0])
        sys.exit(1)

    with codecs.open(sys.argv[1], 'r', 'utf16') as rfile:
        first_line = rfile.readline()
        if 'Windows Registry Editor Version 5.00' not in first_line:
            print('"%s" is not a registry file.' % sys.argv[1].upper())
            sys.exit(1)

        lines = [unicode(line.strip('\\\n\r ')) for line in rfile.readlines()]

        keyname = None
        keydata = {}

        for line in lines:
            if not line:
                continue

            if (line[0] == u'[' and line[-1] == u']') or not keyname:
                keyname = line.strip(u'[]').split(u'\\')[-1]
                print('Processing key %s... ' % keyname)
            else:
                if line[0] == u'"':
                    line_split = re.split('["=:]+', line)

                    if u'hex' in line_split[2]:
                        print('Found "%s"' % line_split[1])
                        keydata[(keyname, line_split[1])] = cut_line(line)
                else:
                    keydata[(keyname, line_split[1])] += cut_line(line)

        for value_id in keydata:
            e_filename = '%s_%s.bin' % value_id
            print('Creating %s...' % e_filename)
            with open(e_filename, 'wb') as fbin:
                fbin.write(binascii.unhexlify(''.join(keydata[value_id])))

        print('OK')


def cut_line(line):
    return [
        hexa
        for hexa in line.split(u':')[-1].split(u',')
        if len(hexa)]


if __name__ == '__main__':
    main()
