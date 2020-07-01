#!/bin/bash

# スクリプトの絶対パスを取得
SCRIPT_DIR=$(cd $(dirname $0); pwd)

# .envから設定情報取得
set -a; . ${SCRIPT_DIR}/.env; set +a;

if [ -z "${REST_API_KEY}" ]; then
  REST_API_KEY="1234567890"
fi

curl -X POST -H "Authorization: Bearer ${REST_API_KEY}" localhost/api/jinjer/checkin
