#!/bin/bash
# script that send custom headers
curl -s -H "X-School-User-Id: 98" "$1"
