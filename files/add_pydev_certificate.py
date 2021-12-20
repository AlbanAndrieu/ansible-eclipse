#!/usr/bin/python
# -*- coding: utf-8 -*-
# Add PyDev's certificate to Java's key and certificate database
# Certificate file here: http://pydev.org/pydev_certificate.cer
import os

import pexpect
import urllib2


def find_java_home():

    if os.environ['JAVA_HOME']:
        return os.environ['JAVA_HOME']

    import subprocess
    return_value = subprocess.call('which java', stdin=java_path)

    if not return_value:
        return java_path.replace('bin/java', '')

    # fall back to original path..
    return '/usr/lib/jvm/default-java'


def main():
    # NOTE: You may have to update the path to your system's cacerts file

    certs_file = os.path.join(find_java_home(), 'jre/lib/security/cacerts')
    if not os.path.isfile(certs_file):
        raise ValuError('Wrong path to certs file')

    pydev_certs_url = 'http://pydev.org/pydev_certificate.cer'
    print('Adding pydev_certificate.cer to %s' % (certs_file))
    pydev_cert = open('pydev_certificate.cer', 'w')
    pydev_cert.write(urllib2.urlopen(pydev_certs_url).read())
    pydev_cert.close()
    cmd = 'keytool -import -file ./pydev_certificate.cer -keystore %s' % (
        certs_file
    )
    child = pexpect.spawn(cmd)
    child.expect('Enter keystore password:')
    child.sendline('changeit')
    if child.expect(['Trust this certificate?', 'already exists']) == 0:
        child.sendline('yes')
    # try:
    #    child.interact()
    # except OSError:
    #    pass
    print('done')


if __name__ == '__main__':
    main()
