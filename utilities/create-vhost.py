#!/usr/bin/env python

import sys
import os

APACHE_PATH="/etc/apache2/sites-enabled/"

def get_arg(arg, option):
    try:
        return sys.argv[arg]
    except IndexError:
        return raw_input('%s (Enter to empty): ' % option)

def get_filename(server):
    if server:
        return APACHE_PATH + server +'.conf'

    return APACHE_PATH + 'new_host.conf'

def create_host(server, root):
    f = open(get_filename(server), 'w')
    f.write('<VirtualHost *:80>\n')
    f.write('    ServerName %s\n' % server)
    f.write('    DocumentRoot %s\n' % root)
    f.write('    <Directory %s>\n' % root)
    f.write('        Options Indexes FollowSymLinks\n')
    f.write('        AllowOverride All\n')
    f.write('        Require all granted\n')
    f.write('    </Directory>\n')
    f.write('</VirtualHost>\n')
    return f

f = create_host(get_arg(1, 'ServerName'), get_arg(2, 'DocumentRoot'))
f.close()

print(f.name)
os.system('cat %s' % f.name)
