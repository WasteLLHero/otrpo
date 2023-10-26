from ftplib import FTP
from datetime import date

Host = 'localhost'
User = 'Waste'
Password ='123'

with FTP(host=Host) as  ftp:
    ftp.login(user=User, passwd=Password)
    print(ftp.getwelcome())
    # if (not date.today in ftp.nlst):
    #     ftp.mkd(f"{date.today}")
    print(ftp.nlst())
    print(ftp.pwd())
    ftp.quit()
