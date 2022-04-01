from pickle import TRUE
import requests,json
import datetime
import pytz
import tweepy
import settings

# TimeZone/日付 指定
jp = pytz.timezone('Asia/Tokyo')
finish_date = datetime.datetime.now().replace(hour=0,minute=0,second=0,microsecond=0).astimezone(jp) # 集計終了日（= Today )
start_date = finish_date - datetime.timedelta(1) # 集計開始日（= 1日前）

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

# 本日のcommit数初期化
today_commit_count = 0 

# Gitの情報を取得
## Repository全件の取得
git_repositories_url = requests.get("https://api.github.com/users/" + git_username + "/repos?client_id=" + git_client_id +"&client_secret=" + git_client_secrets).text
repositories = json.loads(git_repositories_url)

for repository in repositories:
  # repository の名前/update（更新日）を取得
  repo_name = repository["name"]
  repo_update_date = datetime.datetime.fromisoformat(repository["updated_at"].replace('Z', '+00:00')).astimezone(jp)

  # updateが集計開始日より後であればcommit情報を取得
  if repo_update_date > start_date:
    ## 各リポジトリのcommitを取得
    git_commits_url = requests.get("https://api.github.com/repos/" + git_username + "/" + repo_name + "/commits").text 
    commits = json.loads(git_commits_url)

    # API 取得がlimitを超えてしまった場合の例外処理
    if type(commits) != list and "API rate limit exceeded" in commits["message"] :
      today_commit_count = "Sorry, Today's Github API is limited..."
      break

    # commitの内容を取得
    for commit in commits:
      # commit の日付を取得
      commit_datetime = datetime.datetime.fromisoformat(commit["commit"]["committer"]["date"].replace('Z', '+00:00')).astimezone(jp)

      # commitの日付によって処理を振り分け
      if commit_datetime > start_date:
        # commitの日付が集計開始日より後なら1カウント
        today_commit_count += 1
      else:
        # commitの日付が開始日よりも前ならbreakして次のリポジトリへ
        break

# Twitterへの投稿
## TwitterClientの作成
client = tweepy.Client(
  consumer_key=consumer_key, 
  consumer_secret=consumer_secret, 
  access_token=access_token, 
  access_token_secret=access_token_secret
)
## 投稿文
text = "【Github Oneday Bot】\nGithub Name: " + git_username + "\nGithub URL: https://github.com/" + git_username + "\nToday's Commit : " + str(today_commit_count) + "commit"

## 投稿
if type(today_commit_count) == int:
  client.create_tweet(text=text)
elif type(today_commit_count) == str:
  client.create_tweet(text=today_commit_count)
else:
  pass
  
