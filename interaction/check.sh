#!/bin/sh -e

RESULT=$(echo "adam" | nc "$1" "$2")

echo "$RESULT" | grep "Hello brave new challenger"
echo "$RESULT" | grep "Any last words?"
echo "$RESULT" | grep "adam"

