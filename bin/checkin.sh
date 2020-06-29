#!/bin/bash

set -a; . .env; set +a;

if [ -z "${REST_API_KEY}" ]; then
  REST_API_KEY="1234567890"
fi

curl -X POST -H "Authorization: Bearer ${REST_API_KEY}" localhost/api/jinjer/checkin
