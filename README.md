[日本語版README.mdはこちら](https://github.com/besumero628/git-commit-bot/blob/main/README-ja.md)

# git-commit-bot

This is a python source code that can post as a TwitterBot using GitHubAPI / TwitterAPI to count the number of commits on a daily basis.

Aggregation is automated by GitHubActions, so it can be set up once and used semi-permanently.


# Requirement
To run in a local environment, you need to install the Python environment and the following libraries.

We have confirmed that it works only with each version of Python.

* Python 3.8.12
* pytz 2022.1
* tweepy 4.8.0
* python-dotenv 0.20.0

# Installation

Each installation should be performed with the following pip command.

```python
pip install pytz #　Library for time-zone.
```

```python
pip install tweepy #　Library for twitter API.
```

```python
pip install python-dotenv #　Library .env.
```


# Note

The following keys and tokens must be obtained from [Twitter Developper](https://developer.twitter.com/) to use the Twitter API.

- APIKey
- APIKeySercret
- Access Token
- Access Token Secret

To relax the usage limit of the GitHub API, you must obtain the following OAuth key from the [settings](https://github.com/settings/developers)

- Client ID
- Client Secret

The following information registration, including the above, must be registered individually by clicking on Security-Secrets-Actions-NewRepositorySecrets from the repository settings.


```python
TWITTER_CONSUMER_API_KEY = "API key"
TWITTER_CONSUMER_API_SECRET_KEY = "API Key Secret"
TWITTER_ACCESS_TOKEN = "Access Token"
TWITTER_ACCESS_TOKEN_SECRET = "Access Token Secret"
GIT_USERNAME = "UserName"
GIT_CLIENT_ID = "Client ID"
GIT_CLIENT_SECRETS = "Client secrets"
```

If you are working locally, you will need to write the above variables to .env.
  
Please refer to the .env.sample.

# Usage

To run in local environment

```bash
python main.py
```


# Author

* Syuhei.Nara (besumero628)
* [Twitter](https://twitter.com/besumero628)

# License

"Git-Commit-Bot" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
