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
