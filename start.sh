#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo "Error: No command-line argument provided. Please provide a value for RUN_DATE."
    exit 1
fi

# Load environment variables from the .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

RUN_DATE=$1

python3 src/main.py