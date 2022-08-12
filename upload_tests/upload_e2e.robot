#
# Copyright (c) 2022 Markus Neifer
# Licensed under the MIT License.
# See file LICENSE in project root directory.
#
*** Settings ***
Documentation    Import end-to-end tests.
Library          FtpLibrary
Library          DatabaseLibrary


*** Test Cases ***
Import E2E Test
    [Documentation]    Testing FTP upload and rows in database.

    Connect Database

    Log To Console    Testing precondition
    Check if not exists in database    select * from article

    Disconnect From Database

    Log To Console    Connecting to %{PUBLICHOST}:%{FTP_PORT} as %{FTP_USER_NAME}
    Ftp Connect       %{PUBLICHOST}    %{FTP_USER_NAME}    %{FTP_USER_PASS}    %{FTP_PORT}
    Upload File       data.csv
    Ftp Close

    Log To Console    Wait for processing
    Sleep    30s

    Connect Database

    Log To Console    Testing postcondition
    Check if exists in database    select * from article

    Disconnect From Database


*** Keywords ***
Connect Database
    Log To Console         Connecting to %{DB_HOST}:%{DB_PORT}, DB %{DB_NAME} as %{DB_USER}
    Connect To Database    pymysql    %{DB_NAME}    %{DB_USER}    %{MYSQL_ROOT_PASSWORD}    %{DB_HOST}    %{DB_PORT}
