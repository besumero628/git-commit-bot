from pickle import TRUE
import requests,json
import datetime
import pytz
import tweepy
import settings

# TimeZone/日付 指定
jp = pytz.timezone('Asia/Tokyo')
finish_date = datetime.datetime.now().astimezone(jp).replace(hour=0,minute=0,second=0,microsecond=0) # 集計終了日（= Today )
start_date = finish_date - datetime.timedelta(1) # 集計開始日（= 1日前）

# Git の設定
git_username = settings.GIT_USERNAME
git_client_id = settings.GIT_CLIENT_ID
git_client_secrets = settings.GIT_CLIENT_SECRETS

# query設定
git_client_id_query = "&client_id=" + git_client_id
git_client_secrets_query = "&client_secret=" + git_client_secrets

# Twitter APIのキーを設定
consumer_key = settings.TWITTER_CONSUMER_API_KEY
consumer_secret = settings.TWITTER_CONSUMER_API_SECRET_KEY

# Twitter APIのアクセストークンを設定
access_token=settings.TWITTER_ACCESS_TOKEN
access_token_secret =settings.TWITTER_ACCESS_TOKEN_SECRET

# 変数初期化
total_commit_count = 0 # 合計commit数
repo_url_page_num = 1 # repository取得の際のpagenation用

# Gitの情報を取得
while True:
  # レポジトリを取得（1ページ最大100件）
  repositories_url = "https://api.github.com/users/{0}/repos?per_page=100&page={1}{2}{3}".format(git_username, repo_url_page_num, git_client_id_query, git_client_secrets_query)
  git_repositories = requests.get(repositories_url).text
  repositories = json.loads(git_repositories)

  if git_repositories == "[]":
    break
  elif type(repositories) != list and "API rate limit exceeded" in repositories["message"] :
    total_commit_count = "Sorry, Today's Github API is limited..."
    break
  else:
    pass

  for repository in repositories:
    # repository の名前/pushed_at（push日）を取得
    repo_name = repository["name"]
    repo_pushed_date = datetime.datetime.fromisoformat(repository["pushed_at"].replace('Z', '+00:00')).astimezone(jp)
    commit_url_page_num = 1

    # updateが集計開始日より後であればcommit情報を取得
    if start_date < repo_pushed_date:
      while True:
        ## 各リポジトリのcommitを取得
        git_commits_url = "https://api.github.com/repos/{0}/{1}/commits?per_page=100&page={2}{3}{4}".format(git_username, repo_name, commit_url_page_num, git_client_id_query, git_client_secrets_query)
        git_commits = requests.get(git_commits_url).text
        commits = json.loads(git_commits)

        # API 取得がlimitを超えてしまった場合の例外処理
        if git_commits == "[]":
          break
        elif type(commits) != list and "API rate limit exceeded" in commits["message"] :
          total_commit_count = "Sorry, Today's Github API is limited..."
          break
        else:
          pass

        # commitの内容を取得
        for commit in commits:
          # commit の日付を取得
          commit_datetime = datetime.datetime.fromisoformat(commit["commit"]["committer"]["date"].replace('Z', '+00:00')).astimezone(jp)

          # commitの日付によって処理を振り分け
          if start_date < commit_datetime:
            if commit_datetime < finish_date:
              # commitの日付が集計開始日より後なら1カウント
              total_commit_count += 1
          else:
            # commitの日付が開始日よりも前ならbreakして次のリポジトリへ
            break
        
        commit_url_page_num += 1 # commit paginationを進める
  repo_url_page_num += 1 # repository paginationを進める

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
text = raw_text.format(git_username, git_username, start_date.strftime('%m/%d'), finish_date.strftime('%m/%d'), w_list[start_date.weekday()], w_list[finish_date.weekday()] ,total_commit_count)

# 投稿
if type(total_commit_count) == int:
  client.create_tweet(text=text)
elif type(total_commit_count) == str:
  client.create_tweet(text=total_commit_count)
else:
  pass
