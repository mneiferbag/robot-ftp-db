#
# Copyright (c) 2022 Markus Neifer
# Licensed under the MIT License.
# See file LICENSE in project root directory.
#
*** Settings ***
Documentation    Testing an FTP upload-processing-import process.
Library          FtpLibrary
Library          DatabaseLibrary
Test Setup       Reset Database


*** Test Cases ***
Upload Process Import Test
    [Documentation]    Testing FTP upload and rows in database.

    Log To Console    Connecting to %{PUBLICHOST}:%{FTP_PORT} as %{FTP_USER_NAME}
    Ftp Connect       %{PUBLICHOST}    %{FTP_USER_NAME}    %{FTP_USER_PASS}    %{FTP_PORT}
    Upload File       data.csv
    Ftp Close

    Log To Console    Waiting for processing
    Sleep             10 seconds

    Log To Console                 Test postcondition
    Connect Database
    Check if exists in database    SELECT * FROM article WHERE id = 1 AND name = 'Radkappe' AND count = 1 AND created = '2020-01-01'
    Disconnect From Database


*** Keywords ***
Connect Database
    Log To Console         Connecting to %{PGHOST}:%{PGPORT}, DB %{PGDATABASE} as %{PGUSER}
    Connect To Database    psycopg2    %{PGDATABASE}    %{PGUSER}    %{PGPASSWORD}    %{PGHOST}    %{PGPORT}

Reset Database
    Log To Console              Test precondition
    Connect Database
    Execute Sql Script          src${/}testPrecondition.sql
    Disconnect From Database
