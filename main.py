from pickle import TRUE
import requests,json
import datetime
import tweepy
import settings

# Git の設定
git_username = settings.GIT_USERNAME
git_client_id = settings.GIT_CLIENT_ID
git_client_secrets = settings.GIT_CLIENT_SECRETS


# Twitter APIのキーを設定
consumer_key = settings.TWITTER_CONSUMER_API_KEY
consumer_secret = settings.TWITTER_CONSUMER_API_SECRET_KEY

# Twitter APIのアクセストークンを設定
access_token=settings.TWITTER_ACCESS_TOKEN
access_token_secret =settings.TWITTER_ACCESS_TOKEN_SECRET


# Gitの情報を取得
contributions_url = "https://github-contributions-api.deno.dev/{0}.json".format(git_username)
contributions_text = requests.get(contributions_url).text
contributions = json.loads(contributions_text)
contribution = contributions['contributions'][-1][-2]

start_date = datetime.datetime.strptime(contribution['date'], '%Y-%m-%d')
finish_date = start_date + datetime.timedelta(days=1)
contribution_count = contribution['contributionCount']

w_list = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

# Twitterへの投稿
## TwitterClientの作成
client = tweepy.Client(
  consumer_key=consumer_key, 
  consumer_secret=consumer_secret, 
  access_token=access_token, 
  access_token_secret=access_token_secret
)
## 投稿文
raw_text = '''【Github Commit Bot】
Github Name: {0}
Github URL: https://github.com/{1}
Period : {2}({4}) - {3} ({5})
Total Commit : {6}commit
#GitHub #GitHubCommitBot'''
text = raw_text.format(git_username, git_username, start_date.strftime('%m/%d'), finish_date.strftime('%m/%d'), w_list[start_date.weekday()], w_list[finish_date.weekday()] ,contribution_count)

## 投稿
if type(contribution_count) == int:
  client.create_tweet(text=text)
elif type(contribution_count) == str:
  client.create_tweet(text=contribution_count)
else:
  pass
