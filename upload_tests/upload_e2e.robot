#
# Copyright (c) 2022 Markus Neifer
# Licensed under the MIT License.
# See file LICENSE in project root directory.
#
*** Settings ***
Documentation    Testing an FTP upload-processing-import process.
Library          FtpLibrary
Library          DatabaseLibrary


*** Test Cases ***
Upload Process Import Test
    [Documentation]    Testing FTP upload and rows in database.

    Connect Database

    Log To Console                Test fixture
    Delete All Rows From Table    article

    Disconnect From Database

    Log To Console    Connecting to %{PUBLICHOST}:%{FTP_PORT} as %{FTP_USER_NAME}
    Ftp Connect       %{PUBLICHOST}    %{FTP_USER_NAME}    %{FTP_USER_PASS}    %{FTP_PORT}
    Upload File       data.csv
    Ftp Close

    Log To Console    Wait for processing
    Sleep             30 seconds

    Connect Database

    Log To Console                 Testing postcondition
    Check if exists in database    select * from article where name = 'Radkappe'

    Disconnect From Database


*** Keywords ***
Connect Database
    Log To Console         Connecting to %{PGHOST}:%{PGPORT}, DB %{PGDATABASE} as %{PGUSER}
    Connect To Database    psycopg2    %{PGDATABASE}    %{PGUSER}    %{PGPASSWORD}    %{PGHOST}    %{PGPORT}
