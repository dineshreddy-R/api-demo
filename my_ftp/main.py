from ftplib import FTP

ftp_host = "test.rebex.net"
ftp_user = "demo"
ftp_pass = "password"

ftp = FTP(ftp_host)
ftp.login(user= ftp_user,passwd= ftp_pass)

print("connected to the website",ftp.getwelcome())

ftp.set_pasv(False)
fies = ftp.retrlines('LIST')

ftp.quit()
