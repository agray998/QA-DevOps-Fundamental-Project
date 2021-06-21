#!/bin/bash
# Prior to running this script the following environment vars should be set:
#   DATABASE_URI - the URI for the mysql database being used
#   SECRET_KEY - a secret key to allow WTForms CSRF protection to work
#   MYSQL_ROOT_PASSWORD - the root password for the mysql database being used
#   MYSQL_DATABASE - the name of the mysql database being used

if [ -z $DATABASE_URI ] || [ -z $SECRET_KEY ] || [ -z $MYSQL_DATABASE ] || [ -z $MYSQL_ROOT_PASSWORD ]
then
    echo "One or more variables is not set"
    exit 1
fi

sed \
    -e 's,{{DATABASE_URI}},'$DATABASE_URI',g;' \
    -e 's,{{SECRET_KEY}},'$SECRET_KEY',g;' \
    -e 's,{{MYSQL_ROOT_PASSWORD}},'$MYSQL_ROOT_PASSWORD',g;' \
    -e 's,{{MYSQL_DATABASE}},'$MYSQL_DATABASE',g;' secrets.yaml | kubectl delete -f -