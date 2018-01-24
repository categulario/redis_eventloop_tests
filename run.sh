#!/bin/bash
if [ ! $1 ]; then
    echo "Usage: $0 file.py"
    exit 1
fi

python $1 &
PID=$!
top -p $PID
