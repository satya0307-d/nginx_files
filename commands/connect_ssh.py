import os
import paramiko
import keyring
import subprocess
import sys, getopt


param_1= sys.argv[1] 
param_2= sys.argv[2]
param_3= sys.argv[3]

print(param_1)
print(param_2)
print(param_3)

nginx_conf_filename = "config_files/nginx_" + param_1 + ".conf"

subprocess.run(["cp","config_files/nginx_template.conf",nginx_conf_filename])
subprocess.run(["sed", "-i", "-e", "s~<youtube-rtmp>~" + param_2 + "~g",nginx_conf_filename])
subprocess.run(["sed", "-i", "-e", "s~<facebook-rtmp-key>~" + param_3 + "~g",nginx_conf_filename])
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
print ('Executing shell script')
stdin, stdout, stderr = ssh.exec_command('/root/./setup_nginx.sh')
print (stdout.read())
print (stderr.read())
print ('cp nginx conf file')
stdin, stdout, stderr = ssh.exec_command('cp '+ nginx_conf_filename + ' /usr/local/nginx/conf/nginx.conf')
print (stdout.read())
print (stderr.read())
print ('cp stunnel conf file')
stdin, stdout, stderr = ssh.exec_command('cp config_files/stunnel.conf /etc/stunnel/stunnel.conf')
print (stdout.read())
print (stderr.read())

print ('Restarting stunnel')
stdin, stdout, stderr = ssh.exec_command('/etc/init.d/stunnel4 restart')
print (stdout.read())
print (stderr.read())
print ('Restarted stunnel')

print ('Starting nginx')
stdin, stdout, stderr = ssh.exec_command('/usr/local/nginx/sbin/nginx')
print (stdout.read())
print (stderr.read())
print ('Started nginx')
ssh.close()

