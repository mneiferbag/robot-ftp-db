#
# Copyright (c) 2022 Markus Neifer
# Licensed under the MIT License.
# See file LICENSE in project root directory.
#
import os
import pymysql.cursors
from ftplib import FTP
from time import sleep

dbHost = os.environ.get('DB_HOST')
dbPort = int(os.environ.get('DB_PORT'))
dbName = os.environ.get('DB_NAME')
dbUser = os.environ.get('DB_USER')
dbPassword = os.environ.get('MYSQL_ROOT_PASSWORD')

ftpHost = os.environ.get('PUBLICHOST')
ftpPort = int(os.environ.get('FTP_PORT'))
ftpUser = os.environ.get('FTP_USER_NAME')
ftpPassword = os.environ.get('FTP_USER_PASS')

connection = pymysql.connect(host=dbHost,
                         port=dbPort,
                         user=dbUser,
                         password=dbPassword,
                         database=dbName,
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
ftp = FTP()
ftp.connect(ftpHost, ftpPort)
ftp.login(user=ftpUser, passwd=ftpPassword)
i = 1

while i < 60:
    files = ftp.nlst()
    print(f'{i} - {files}')
    if 'data.csv' in files:
        ftp.delete('data.csv')
        with connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO article (name, count, created) VALUES (%s, %s, %s)"
                cursor.execute(sql, ('Radkappe', 1, '2020-01-01'))
            connection.commit()
    i += 1
    sleep(1) 

ftp.quit()
