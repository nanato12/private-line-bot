# private-line-bot
非公式LINEBot

ライブラリは非公開です。

submoduleでprivateにしてます。

## 環境変数ファイルの作成

`python manage.py gen:env` を使用して環境変数を作成する。

### **new**: 必要な環境変数を記述するためのコマンド

```bash
$ python manage.py gen:env new
Generate success! settings/.env
```

作成された `.env`


```conf
LINE_PRIVATE_BOT_EMAIL = 'INPUT YOUR LINE EMAIL'
LINE_PRIVATE_BOT_PASSWORD = 'INPUT YOUR LINE PASSWORD'
```

### **init**: 対話形式で必要な環境変数を記述するためのコマンド

```sh
$ python manage.py gen:env init
input email >>> hogehoge@hogehoge.com
input password >>> HogeHoge
Generate success! settings/.env
```

作成された `.env`

```conf
LINE_PRIVATE_BOT_EMAIL = 'hogehoge@hogehoge.com'
LINE_PRIVATE_BOT_PASSWORD = 'HogeHoge'
```

## コマンドの生成

`python manage.py gen:command {コマンド名}` で生成する。

```sh
$ python manage.py gen:command /help
Generate success! commands/help_command.py
```

生成されたファイル

```python
# Generated by CommandGenerator on 20XX-XX-XX XX:XX:XX

from core.base.commnad import BaseCommand


class HelpCommand(BaseCommand):
    cmd = '/help'
    description = 'Please input here command description.'
```
