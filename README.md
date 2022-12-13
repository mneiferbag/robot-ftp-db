# Robot Framework - FTP and Database Example

Licensed under the MIT License. See file [LICENSE](./LICENSE).

Robot Framework FTP and database example. Example includes code written in Robot Framework and Python.

[![CodeQL](https://github.com/mneiferbag/robot-ftp-db/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/mneiferbag/robot-ftp-db/actions/workflows/codeql-analysis.yml)

## Robot Framework

Installation

    pip install robotframework
    pip install robotframework-ftplibrary
    pip install robotframework-databaselibrary

Or use existing `requirements.txt`. Check installation with `robot --version`.

Start servers with `docker compose up -d`.

Run test with `robot --outputdir ./log ./upload_tests/upload_e2e.robot`

The Docker files and test files assume that a `.env` file exists with the following content.

    PUBLICHOST=<ftp server name>
    FTP_PORT=<ftp server port>
    FTP_USER_NAME=<ftp user name>
    FTP_USER_PASS=<ftp user password>
    FTP_USER_HOME=<ftp user home path>
    POSTGRES_DB=<postgresql database name>
    POSTGRES_USER=<postgresql user name>
    POSTGRES_PASSWORD=<postgresql user password>
    PGHOST=<db server name>
    PGPORT=<db server port>
    PGDATABASE=<postgresql database name>
    PGUSER=<postgresql user name>
    PGPASSWORD=<postgresql user password>

## Python

Create virtual environment with `python -m venv .venv`.

Activate environment, for example with `.venv\Scripts\activate.bat` on Windows and list packages with `pip list`.

Restore environment with `pip install -r requirements.txt`.

Save environment after adding packages with `pip freeze > requirements.txt`.

## PostgreSQL

Initialize a database cluster in directory `psqldb` with `initdb -D psqldb`.

Start server with `pg_ctl start -D psqldb -l log\psql.log`.

Create database with `createdb robotdb`.

Create database schema with `bin\createSchema.bat`.

Connect to database with `psql robotdb`.

Quit the psql program with `\q` or `\quit`.

Stop server with `pg_ctl stop -D psqldb -m smart`.

## Links

- Robot Framework
  - [DatabaseLibrary](https://github.com/franz-see/Robotframework-Database-Library)
  - [DatabaseLibrary Doc](https://franz-see.github.io/Robotframework-Database-Library/api/0.5/DatabaseLibrary.html)
  - [FtpLibrary](https://kowalpy.github.io/Robot-Framework-FTP-Library/FtpLibrary.html)
  - [Robot Framework](https://robotframework.org/)
  - [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- Python
  - [ftplib — FTP protocol client](https://docs.python.org/3/library/ftplib.html)
  - [Psycopg](https://www.psycopg.org/) - PostgreSQL adapter for the Python programming language
  - [python-dotenv](https://github.com/theskumar/python-dotenv) - reads key-value pairs from a .env file and can set them as environment variables
- PostgreSQL
  - [Documentation](https://www.postgresql.org/docs/)

## Tasks

- [ ] Create DB schema on DB container build
- [ ] Replace hard coded insert in src/processor.py with ftp file content
