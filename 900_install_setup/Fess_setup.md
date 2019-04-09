---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.0'
      jupytext_version: 1.0.5
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# 概要
以下を実施すれば、検索が可能となる。
## setup
https://qiita.com/n-i-e/items/4dd6fb7232cb1403a33b


1. JREが無ければ、JREを入れる
1. binの下にあるfess.batに以下を追加（先頭の方に入れる）
>SET JAVA_HOME=C:\Program Files\Java\jre1.8.0_202
1. fess.batをダブルクリックして立ち上げる
1. しばらく待ちます
>logsの下にログが出る。立ち上がらなければ、ここを確認（情報: Boot successful: url -> http://localhost:8080　）が出ればOK


## クローラー設定
1. http://localhost:8080/admin へアクセス
1. admin/admin　でログイン
1. クローラー　-> ファイルシステム -> 新規作成
>名前とパスを入れる（パスは　file:/c:/.... で入れる　nas等の場合は　file://///nas/....1)　-> chromeに入れてファイルが出てくればOK

## Gitbbucketのクローラの設定
https://qiita.com/kw_udon/items/06d385b88dafed4bd609

1. gitbucket fess plugin をダウンロードして、gitbucket pluginに入れる
1. リポジトリアクセスのためのトークンを発行 [GitBucket側]
1. Fess側で、クローラー　-> データストア -> 新規作成
>下記を設定する
> - 名前
>- ハンドラ:GitBucketDataStore
> - パラメータ:
>>url=http://localhost:8080/
>>token=GitBucket側で発行したトークン

## クロールさせる
1. システム -> スケジューラー -> 	Default Crawler -> 今すぐ開始
1. システム情報 -> クロール情報 -> 	セッションIDが出ていればOK
> JREにserverがない場合は、クロールできない（ログで確認できる）

## スケジューラの設定
1. スケジュール
設定したスケジュールでジョブが実行されます。記述形式はCron形式で「分 時 日 月 曜日」の形式で記述します。 たとえば、「0 12 * * 3」の場合は、毎週水曜日の12:00pmにジョブを実行