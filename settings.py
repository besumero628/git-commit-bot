import os
from os.path import join, dirname
from dotenv import load_dotenv

# 環境変数のセッティング
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TWITTER_CONSUMER_API_KEY = os.environ.get("TWITTER_CONSUMER_API_KEY")
TWITTER_CONSUMER_API_SECRET_KEY = os.environ.get("TWITTER_CONSUMER_API_SECRET_KEY")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

GIT_USERNAME = os.environ.get("GIT_USERNAME")
GIT_CLIENT_ID = os.environ.get("GIT_CLIENT_ID")
GIT_CLIENT_SECRETS = os.environ.get("GIT_CLIENT_SECRETS")