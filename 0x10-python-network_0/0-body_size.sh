#!/bin/bash
#curl command displaying the bytes size of a given URL.
curl -sI "$1" | wc -c
