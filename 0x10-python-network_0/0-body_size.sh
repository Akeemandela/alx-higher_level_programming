#!/bin/bash
#curl command displaying the bytes size of a given URL
curl -s "$1" | wc -c
