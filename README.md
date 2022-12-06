# Robot Framework FTP and Database Example

Licensed under the MIT License. See file [LICENSE](./LICENSE).

Robot Framework FTP and database example. Example includes code written in Robot Framework and Python.

[![CodeQL](https://github.com/mneiferbag/robot-ftp-db/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/mneiferbag/robot-ftp-db/actions/workflows/codeql-analysis.yml)

## Robot Framework

Installation

    pip install robotframework
    pip install robotframework-ftplibrary
    pip install robotframework-databaselibrary

Or use existing `requirements.txt`. Check installation with `robot --version`.

Start servers with `docker compose up`.

Run test with `robot --outputdir ./log ./upload_tests/upload_e2e.robot`

## Python

Create virtual environment.

    python -m venv .venv

Activate environment, for example with `.venv\Scripts\activate.bat` on Windows and list packages.

    pip list

Restore environment.

    pip install -r requirements.txt

Save environment after adding packages.

    pip freeze > requirements.txt

## PostgreSQL

Initialize a database cluster in directory `data` with `initdb -D data`.

Start server with `pg_ctl -D data -l log\pgsql.log start`.

Create database with `createdb robot`.

Connect to database with `psql robot`.

Stop server with `pg_ctl stop -D data -m smart`.

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
- PostgreSQL
  - [Documentation](https://www.postgresql.org/docs/)

## Tasks

- [ ] Create DB schema on DB container build
- [X] Switch to PostgreSQL
