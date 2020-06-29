#!/bin/bash

curl -X POST -H "Content-Type: application/json" localhost/api/token \
-d '{"username":"username","password":"password"}'
