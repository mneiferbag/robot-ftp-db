"""
 Copyright (c) 2022 Markus Neifer
 Licensed under the MIT License.
 See file LICENSE in project root directory.

 Simple data processor that reads a file named 'data.csv' from an FTP server and
 writes the file content to a database table.
"""
import os
from ftplib import FTP
from time import sleep

import psycopg2
from dotenv import load_dotenv

# Read existing .env file into environment
load_dotenv()

dbName = os.environ["PGDATABASE"]
dbUser = os.environ["PGUSER"]
dbPassword = os.environ["PGPASSWORD"]

ftpHost = os.environ["PUBLICHOST"]
ftpPort = int(os.environ["FTP_PORT"])
ftpUser = os.environ["FTP_USER_NAME"]
ftpPassword = os.environ["FTP_USER_PASS"]

ftp = FTP()
ftp.connect(ftpHost, ftpPort)
ftp.login(user=ftpUser, passwd=ftpPassword)

print(f"Logged in to FTP {ftpHost} as user {ftpUser}")

DATA_FILE = "data.csv"
i = 1

# Just loop for some time to simulate a running data processor service
while i < 200:
    files = ftp.nlst()
    print(f'{i} - {files}')
    if DATA_FILE in files:
        lines = []
        ftp.retrlines(f"RETR {DATA_FILE}", lines.append)
        print(f"Retrieved file {DATA_FILE}")
        with psycopg2.connect(f"dbname={dbName} user={dbUser}") as connection:
            print(f"Connected to database {dbName} as user {dbUser}")
            with connection.cursor() as cursor:
                SQL = "INSERT INTO article (id, name, count, created) VALUES (%s, %s, %s, %s)"
                for line in lines:
                    splitted_line = line.split(',')
                    if splitted_line[0].isdigit() and splitted_line[2].isdigit():
                        cursor.execute(SQL, (int(splitted_line[0]), splitted_line[1], int(
                            splitted_line[2]), splitted_line[3]))
            connection.commit()
            print("Inserted file content into database")
        ftp.delete(DATA_FILE)
        print("Deleted retrieved file")
    i += 1
    sleep(1)

ftp.quit()

print("Logged out of FTP")
