調べることをまとめました。都度更新です

## pythonの作法
### アンダースコア"_"の役割
 - アンダースコア二つで定義される関数は外部の参照を受けないもの。この場合、アンダースコアで囲う。
 - アンダースコア一つで定義される関数は参照はできるが、基本的に外部から参照しない ということを慣習化させたものらしい。

## jupyter関係
### jupyterのマジックコマンド
 - %who : 宣言されている変数一覧の表示
 - %whos : 宣言されている変数一覧の詳細表示(型と値)
 - obj? : Objectの型と値の表示
 - %quickref : サポートされるMagic Commandの一覧の表示
 - %matplotlib inline : jupyter内に表示させる

## numpy
- inf弾く

```inf.py
import numpy as np
df.replace([np.inf, -np.inf], np.nan)
```

## 辞書
- 辞書への入力と出力

```dict_input_output.py
dict_test = {}
retu_mei = ["現在値","出来高","前日終値"]

for key in retu_mei:
    dict_test[key] = 10
    
for key in dict_test:
    print(key , dict_test[key])
```

- 辞書型一般

```dict.py
mydict = {"papa":"L", "O":"Orage", "G":"Grapes"}
mydict.keys() #keyの表示
list(mydict.items()) #リスト化
```

## ライブラリのリロード
```reload.py
import importlib
importlib.reload(foo)
```
## 例外処理

- 例外処理した際のエラーメッセージを表示させる

```try_except_trackback.py
import traceback
try:
   aaa
except:
   traceback.print_exc()
```



## windows関係
- メッセージをポップアップ（tkを使わない）
https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python

```message.py
import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
```

- beep音を出す　音を出す　知らせる

``` beep.py
import winsound
winsound.Beep(1000,800)
```

- ショートカットを作成

```cut.py
import win32com.client
ws = win32com.client.Dispatch("wscript.shell")
scut = ws.CreateShortcut('run_idle.lnk')
scut.TargetPath = '"c:/python27/python.exe"'
scut.Arguments = '-m idlelib.idle'
scut.Save()
```

## 時間

- string ⇨ datetime フォーマットに気をつける。

``` str2datetime.py
from datetime import datetime as dt
tstr1 = '2019-01-01 00:00:00'
tdatetime = dt.strptime(tstr1, '%Y-%m-%d %H:%M:%S')
tstr2 = '2019/01/01 00:00:00'
tdatetime = dt.strptime(tstr2, '%Y/%m/%d %H:%M:%S')
```

- datetime ⇨ string

``` datetime2str.py
from datetime import datetime as dt
tdatetime = dt.now()
tstr1 = tdatetime.strftime('%Y-%m-%d') # 2018-1-18
tstr2 = tdatetime.strftime('%Y/%m/%d %H:%M:%S') # 2018/1/18 12:34:56
```

- datetimeの足し算引き算

``` cal_time.py
now = datetime.now()
tomorrow = now + datetime.timedelta(days = 1) #今より1日後
nextweek = now + datetime.timedelta(weeks = 1) #今より一週間後
```

## sqlite関係 
作成　テーブル作成　レコードを追加

```sqlite.py
import sqlite3
conn = sqlite3.connect('sample.db')

cur = conn.cursor() # Create a 'Cursor' object from 'Connection' object.
cur.execute('''CREATE TABLE memo(date TEXT, title TEXT, body TEXT)''')# Create a table データベースファイルが存在しない場合は新規に作成
cur.execute("""INSERT INTO memoVALUES('2007-01-01', 'Memo1', 'Body1')""")# Insert a record
conn.commit()# コミット
conn.close()# コネクションをクローズ
```


## ポイントを時計回りに並べ替える　
``` point_resample.py
pnt = [[-0.4, -1.52], [-1.8, -0.36],[-0.1, 0.8], [0.27, 0.4], [0.42, 0.28]]

def _angle_between(refvec):
    origin=[0,0]
    ang1 = np.arctan2(*origin[::-1])
    ang2 = np.arctan2(*refvec[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

pnt = sorted(pnt, key=_angle_between)#時計回り
pnt = sorted(pnt, key=_angle_between,reverse=True)#反時計回り
```

## 数字の表示 for CAE (浮動小数点　eまたはEで表示)
``` sample.py
a=1.5/10000 #0.00015
b="{:.4e}".format(a) #'1.5000e-04'
c = b.replace("e","E") #''1.5000E-04'
```

## 文字列
- decode

``` str.py
def decodef(src):#【デコード】
    try:
        src=src.decode('utf-8')
        return src
    except:
        print("decode error")
```

## selenium
selenium chrome driverにpathを通しておく必要あり

``` selenium.py
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:50001/startp")
driver.quit()
```


## subprocess
subprocess http://qiita.com/mokemokechicken/items/a84b0aa96b94d1931f08

```subprocess.py
import os,subprocess
args=["C:\Program Files (x86)\MarketSpeed\MLauncher\MLauncher.exe" ,"MarketSpeed"]
p1=subprocess.Popen(args)
p1.wait()#処理待ちしない場合は、これを消す
````


# file/folder操作

- フォルダの中のファイルをリストで取得する

``` file_mei.py
import os
data_folder = os.path.join(os.getcwd(),"../data")
stocks = [i for i in os.listdir(data_folder) if '.csv' in i]
```



- fileを読み込んで、listにする

``` read.py
with open(r"C:\***.txt") as f:
    li = f.readlines()
print(li)

li_replace = [s.replace('\n', '') for s in li]
print(li_replace)
```

- csvへ書き込み

``` csv_write.py
l = [[0, 1, 2], ['a\nb', 'x', 'y']]

with open('data/temp/sample_writer_linebreak.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(l)
```

- フォルダの操作　

``` folder.py
if not os.path.exists(os.path.dirname(f_path_copy)):#フォルダが無ければ作成する
    os.makedirs(os.path.dirname(f_path_copy))

shutil.rmtree("diff_env")#フォルダの削除

os.mkdir("diff_env")#フォルダの作成
```

## for文

- インデックスを取得してfor文を回す enumerate

```index.py
for no,data in enumerate(scaled_data):
    print(no,data)
```

- 2つのリストを平行にループする zip

```zip.py
for a, b in zip(scaled_data, scaled_parameters):
    print(a,b)
```

## 環境変数
``` environ.py
os.environ['userprofile']#環境変数を取得
sys.path.append("/Users/username/Desktop")#ライブラリを読み込むパスを追加（一時的にpythonpathに追加）
```
## クラスのテンプレ
``` class.py
#---------------------------class ------------------------------------
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) ***
#
###############################################################################
from redminelib import Redmine

module_path = os.path.dirname(__file__)

class redmine_tanuki(object):
    '''
    自分自身が使いやすい環境を構築する
    '''
    def __init__(self,url,user_name,pass_word):
        self.redmine = Redmine(url, username=user_name, password=pass_word)

if __name__ == '__main__':
    obj=redmine_tanuki('a','b','c')
```
