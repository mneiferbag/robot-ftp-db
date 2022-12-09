"""
 Copyright (c) 2022 Markus Neifer
 Licensed under the MIT License.
 See file LICENSE in project root directory.
"""
import os
from ftplib import FTP
from time import sleep

import psycopg2
from dotenv import load_dotenv

load_dotenv()

dbName = os.environ.get('PGDATABASE')
dbUser = os.environ.get('PGUSER')
dbPassword = os.environ.get('PGPASSWORD')

ftpHost = os.environ.get('PUBLICHOST')
ftpPort = int(os.environ.get('FTP_PORT'))
ftpUser = os.environ.get('FTP_USER_NAME')
ftpPassword = os.environ.get('FTP_USER_PASS')

connection = psycopg2.connect("dbname=" + dbName + " user=" + dbUser)
ftp = FTP()
ftp.connect(ftpHost, ftpPort)
ftp.login(user=ftpUser, passwd=ftpPassword)
i = 1

while True:
    files = ftp.nlst()
    print(f'{i} - {files}')
    if 'data.csv' in files:
        ftp.delete('data.csv')
        with connection:
            with connection.cursor() as cursor:
                SQL = "INSERT INTO article (name, count, created) VALUES (%s, %s, %s)"
                cursor.execute(SQL, ('Radkappe', 1, '2020-01-01'))
            connection.commit()
    i += 1
    sleep(1)

ftp.quit()
