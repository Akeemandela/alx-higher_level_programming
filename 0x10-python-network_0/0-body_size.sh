#!/bin/bash
#curl command displaying the bytes size of a given URL.
curl -sI "$1" | grep Content-Length | cut -d " " -f2
