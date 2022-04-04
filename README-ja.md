# git-commit-bot

GitHubAPI / TwitterAPI を利用して日々のcommit数を集計し、TwitterBotとして投稿可能なpythonソースコードです.

集計はGitHubActionsで自動化されているため、1度の設定で半永続的に使用可能です。


# Requirement
ローカル環境で動作させる場合は、所定のPython環境と以下ライブラリののインストールが必要です。

各バージョンでのみ動作確認しています。

* Python 3.8.12
* pytz 2022.1
* tweepy 4.8.0
* python-dotenv 0.20.0

# Installation

各インストールは、以下のpipコマンドで行ってください。

```python
pip install pytz #　time-zoneを扱うライブラリです。
```

```python
pip install tweepy #　Twitter　APIを扱うライブラリです。
```

```python
pip install python-dotenv # .envを扱うライブラリです。
```


# Note

Twitter APIを利用するためには、[Twitter Developper](https://developer.twitter.com/) から以下のキーを取得する必要があります。

- APIKey
- APIKeySercret
- Access Token
- Access Token Secret

GitHub APIの利用上限を緩和させるためには、[settings](https://github.com/settings/developers)から以下のキーを取得する必要があります。

- Client ID
- Client Secret

上記を含め以下の情報を登録リポジトリのSettingsからSecurity-Secrets-Actions-NewRepositorySecretsにて個別に登録する必要があります。

```python
TWITTER_CONSUMER_API_KEY = "API key"
TWITTER_CONSUMER_API_SECRET_KEY = "API Key Secret"
TWITTER_ACCESS_TOKEN = "Access Token"
TWITTER_ACCESS_TOKEN_SECRET = "Access Token Secret"
GIT_USERNAME = "UserName"
GIT_CLIENT_ID = "Client ID"
GIT_CLIENT_SECRETS = "Client secrets"
```

ローカルで作業する場合には上記の変数を.envに書き込む必要があります。
  
.env.sampleを参考にしてください。

# Usage

local環境で作業する場合は以下のコマンドを実行してください。

```bash
python main.py
```


# Author

* Syuhei.Nara (besumero628)
* [Twitter](https://twitter.com/besumero628)

# License

"Git-Commit-Bot" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
