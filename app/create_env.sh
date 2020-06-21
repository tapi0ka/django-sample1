#!/bin/bash

#
# 環境作成シェル（超適当）
#
echo "[$(date)] Start Shell."
echo "Python開発環境を作成します"

SCRIPT_DIR=$(cd $(dirname $0); pwd)
ENV_DIR_NAME="$(basename `pwd`)-env"

if [ -d ${ENV_DIR_NAME} ]; then
  echo "環境がすでに存在しています"
else
  echo "Pythonの仮想環境を作成します"
  virtualenv ${ENV_DIR_NAME}
fi

. "./${ENV_DIR_NAME}/bin/activate"

if [ -f "requirements.txt" ]; then
  echo "Pythonのパッケージをインストールします"
  pip install -r requirements.txt
fi

echo "[$(date)] End Shell."