# DjangoJinjer出勤・退勤自動化システム #

## 必要環境(Require)

* Visual Studio Code
* Google Cloud Platformのアカウント
* Google VM Instance (Ubuntu)
* 気合

## 使用方法(Usage) ##

開発環境で動かしたい場合

プロジェクト直下に.envファイルを作成する。

```txt
DJANGO_JINJER_COMPANY_CODE=1234 # 会社コード
DJANGO_JINJER_EMAIL=123 # 社員ID
DJANGO_JINJER_PASSWORD="aiueo" # 社員パスワード
```

開発環境で動かしたい場合

```shell
docker-compose up --build
```

本番環境で動かしたい場合（公開したい場合）

```shell
docker-compose -f docker-compose.prod.yml up --build
```

管理者ユーザ追加

```shell
docker ps #ContainerIDを確認
docker exec -it {Container ID} bash
# コンテナログイン後
python manage.py createsuperuser
# インタラクティブ形式でユーザ名,パスワードを入力
```

POSTリクエストするためのAPIを取得

```shell
curl -X POST -H "Content-Type: application/json" -d '{"username": "ユーザ名", "password": "パスワード"}' {ホスト名}/api/token
# Responseのaccessの値をコピーなりなんなりしておく
```

出勤する場合

```shell
curl -X POST -H "Authorization: Bearer {APIキー}" {ホスト名}/api/jinjer/checkin
```

退勤する場合

```shell
curl -X POST -H "Authorization: Bearer {APIキー}" {ホスト名}/api/jinjer/checkout
```

成功時はsuccessが帰ってくる

自動化（crontab追記）


```shell
crontab -e
# crontab に以下を記述
50 8 * * 1-5  bash ${HOME}/workspace/django-sample1/checkin.sh
35 17 * * 1-5  bash ${HOME}/workspace/django-sample1/checkout.sh
```


## 機能(Function)

* POSTリクエストによる自動出勤・自動退勤
* JWT(JSON Web Token)によるAPI認証
* 今の所cronなどでAPI叩くような形でしか出勤・退勤できない

## やりたいことリスト

* Slack連携
* 出勤・退勤事前通知(5分前に出勤しても良いかを通知するみたいな感じ)
* カレンダー連携
