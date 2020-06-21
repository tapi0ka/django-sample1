#!/bin/bash

#
# 初期プロジェクト作成シェル
# create_envを実行下後に実行してください
#

PROJECT_NAME="$(basename `pwd`)"

django-admin startproject ${PROJECT_NAME} .