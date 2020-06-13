import os
import paramiko
import keyring
import subprocess

subprocess.run(["scp", "-i", "/root/secret/mykey.pem", "/root/nginx_files/setup_nginx.sh", "root@165.22.209.207:/root/."])

keyfile = os.path.expanduser('/root/secret/mykey.pem')
key = paramiko.RSAKey.from_private_key_file(keyfile)

#k = paramiko.RSAKey.from_private_key_file("/root/secret/mykey.pem")
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("connecting")
ssh.connect('165.22.209.207', username='root', password = '', pkey = key )
ssh.invoke_shell()
print("connected")

stdin, stdout, stderr = ssh.exec_command('ls')
print (stdout.read())
#print ('SCP connecting')
#stdin, stdout, stderr = ssh.exec_command('sudo scp -i /root/secret/mykey.pem /root/nginx_files/setup_nginx.sh root@165.22.209.207:/root/.')
#print (stdout.read())
#print (stderr.read())
ssh.close()
