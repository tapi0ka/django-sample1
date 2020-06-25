#!/bin/bash

API_KEY="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTkzNTI1MzE5LCJqdGkiOiJkYmUxNjZhMTAyOGM0MTFlYjI4OThjY2E1ODhmMTA3MiIsInVzZXJfaWQiOjF9.e42GSU8ar7Icc-6LEBVkgr9hiHwXLypdnRGoQ2rlOKM"

curl -X POST -H "Authorization: Bearer ${API_KEY}" localhost:8000/api/jinjer/checkout