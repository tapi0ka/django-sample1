# Sample Django アプリ

<!-- TOC -->

- [Sample Django アプリ](#sample-django-アプリ)
  - [各種設定ファイル](#各種設定ファイル)
    - [setting.py](#settingpy)
      - [Debug](#debug)
  - [コマンド](#コマンド)
    - [runserver](#runserver)
    - [shell](#shell)
    - [createsuperuser](#createsuperuser)
    - [makemigrations](#makemigrations)
    - [migrate](#migrate)

<!-- /TOC -->

## 各種設定ファイル

### setting.py

#### Debug

TrueにするとadminでDBを見ることができる。

## コマンド

### runserver

djangoを起動します。

```python
python manage.py runserver
```

今回はenvファイルを読むので以下のようにシェルを叩いたほうがいい。

```shell
bash runserver.sh
```

### shell

shellを起動します。

```python
python manage.py shell
```

### createsuperuser

管理者ユーザを追加します。

```python
python manage.py createsuperuser
```

### makemigrations

DBのTable定義書を作成します。
modelの変更履歴などが管理されます。

```python
python manage.py makemigrations
```

### migrate

makemigrationsを使って作成した定義をDBに反映します。

DBのデータ構造が変わるので注意

```python
python manage.py migrate 
```

[makemigrations]: https://docs.djangoproject.com/en/3.0/topics/migrations/
[migrate]: https://docs.djangoproject.com/en/3.0/topics/migrations/