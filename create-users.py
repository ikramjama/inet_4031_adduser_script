#!/usr/bin/python
import os
import re
import sys
def main():
    #loop through each line of input
    for line in sys.stdin:
        # Check if the line starts with a '#' indicating a comment
        match = re.match("^#", line)
        # Split the line into fields using ':' as delimiter
        fields = line.strip().split(':')
        #skip lines starting with '#' or those without 5 feilds
        if match or len(fields) != 5:
            continue
        #take out username, password, gecos, and groups from fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')
        #creating user account
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)
        #make password for the user
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd) 
        #assign user to specified groups
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)

if __name__ == '__main__':
    main()
