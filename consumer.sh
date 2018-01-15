#!/usr/bin/env bash

# Load the .env vars
export $(cat settings/.env | xargs)

# Get the log
filename="$DATA_FOLDER/$DATA_FILE"
consumer -v $VHOST -u $USER -p $PASSWORD -q AllEvents >> $filename
