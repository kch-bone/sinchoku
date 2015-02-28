#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# 必要なライブラリをインポート
import tweepy
import sys
 
# コンシューマキーとかアクセスキーをセット
CK = '' # Consumer Key
CS = '' # Consumer Secret
AT = '' # Access Token
AS = '' # Accesss Token Secert

# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"
 
if __name__ == '__main__':

	argvs = sys.argv  # コマンドライン引数を格納したリストの取得
	argc = len(argvs) # 引数の個数
	if (argc <= 1):   # 引数が足りない場合は、その旨を表示
		print "デフォルト"
		# ツイート本文


		# tweepyでtwitterに画像付きで投稿する
		auth = tweepy.OAuthHandler(CK, CS)
		auth.set_access_token(AT, AS)
		api = tweepy.API(auth)
		status = "テスト"
		api.update_status(status)

	else:
		name = argvs[1]
		# tweepyでtwitterに画像付きで投稿する
		auth = tweepy.OAuthHandler(CK, CS)
		auth.set_access_token(AT, AS)
		api = tweepy.API(auth)
		status = name
		filename = "./output.png"
		api.update_with_media(filename, status)





