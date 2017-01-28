import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('127.0.0.1',username='anjan',password='reddy')
stdin,stdout,stderr=ssh.exec_command('show ip interface in brief')
output = stdout.raedlines()
print '\n'.join(output)