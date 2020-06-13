import os
import paramiko
import keyring
import subprocess
import sys, getopt


param_1= sys.argv[1] 
print(param_1)
subprocess.run(["scp", "-i", "/root/secret/mykey.pem", "/root/nginx_files/setup_nginx.sh", "root@"+param_1+":/root/."])

keyfile = os.path.expanduser('/root/secret/mykey.pem')
key = paramiko.RSAKey.from_private_key_file(keyfile)

#k = paramiko.RSAKey.from_private_key_file("/root/secret/mykey.pem")
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
ssh.connect(param_1, username='root', password = '', pkey = key )
ssh.invoke_shell()
print("connected")

stdin, stdout, stderr = ssh.exec_command('ls')
print (stdout.read())
print ('Change chmod')
stdin, stdout, stderr = ssh.exec_command('chmod 777 /root/./setup_nginx.sh')
print (stdout.read())
print (stderr.read())
#print ('Executing shell script')
#stdin, stdout, stderr = ssh.exec_command('/root/./setup_nginx.sh')
#print (stdout.read())
#print (stderr.read())
ssh.close()

