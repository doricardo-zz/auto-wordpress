import paramiko

def put_file(machinename, username, dirname, filename, data):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(machinename, username=username)
    sftp = ssh.open_sftp()
    try:
        sftp.mkdir(dirname)
    except IOError:
        pass
    f = sftp.open(dirname + '/' + filename, 'w')
    f.write(data)
    f.close()
    ssh.close()


data = 'This is arbitrary data\n'.encode('ascii')
put_file('ftp.doricardo.com', '', '/tmp/dir', 'file.bin', data)