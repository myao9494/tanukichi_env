"""
参考　https://www.procrasist.com/entry/python-tips
"""
#---------------------------正規表現 ------------------------------------
"""
サルにもわかる正規表現入門 https://www.mnet.ne.jp/~nakama/
.   なんでもいい１文字
.*  なんでもいい文字の連続
|   いずれかの文字列
[ ] 指定した文字のどれか
"""
#---------------------------command cmd コマンドプロンプト バッチ シェル　shell ------------------------------------
"""
jupyter notebook %jupyter_home%
%sikuli_home%/runsikulix.cmd
%sikuli_home%/runsikulix.cmd -r ***.sikuli >>***Log.txt
"""
#---------------------------bush command ------------------------------------
"""
ps ux | grep fess  "fess"を含む自分が立ち上げているプロセスを表示
kill プロセスid  プロセスを終了
kill -9 プロセスid　プロセスを強制終了
"""
#---------------------------git command ------------------------------------
"""
git show HEAD^:presentation.pptx > temp.pptx #ひとつ前のコミットを別ファイルとして取りだし+-
git add -A 全ての変更をステージング
git commit -m "コメント"　ステージングした変更をコミット
git push リモートに反映

git reset --soft "HEAD^"　　コミットの削除　--softは変更はそのままにするという意味

"""
#---------------------------辞書　dict ------------------------------------
d = {}
d['k3'] = 3
#---------------------------import lib library------------------------------------
%matplotlib inline
import pandas as pd
import cufflinks as cf
cf.set_config_file(offline=True, theme="white", offline_show_link=False)
cf.go_offline()
"""
ライブラリのリロード
"""
import importlib
importlib.reload(foo)

"""
inf弾く
"""
import numpy as np
df.replace([np.inf, -np.inf], np.nan)


"""
pandas plot グラフ　図　可視化
python matplotlibで見栄えの良い色, グラフを作るTips　https://www.procrasist.com/entry/matplotlib-visual-tips
"""

import matplotlib.pyplot as plt
import seaborn as sns

# SeabornのデフォルトStyleを使用
sns.set()
# グラフのサイズを設定
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111)
# DataFrameのPlotを使用する
df.plot(x='rad', y=['sin','cos'], ax=ax,
        linestyle='dashed', #線種
        color=['darkgreen', 'darkblue'], #色
        linewidth = 0.5 #線の幅
)
# TITLEを設定
ax.set_title("TEST")
# X軸の範囲
ax.set_xlim(0,2*np.pi)
# Y軸の範囲
ax.set_ylim(-1,1)
# X軸のTick（目盛）の位置を設定
ax.set_xticks([0, np.pi, np.pi*2])
# X軸のTick（目盛）の表記を設定
ax.set_xticklabels([0, 'π', '2π'])
# Y軸のTick（目盛）の位置を設定
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
# X軸のラベルを設定
ax.set_xlabel('X [RAD]')
# Y軸のラベルを設定
ax.set_ylabel('X [RAD]')
# グラフ表示
plt.show()

"""
pandas plot 動くグラフ　図　可視化 https://www.sejuku.net/blog/61788
https://qiita.com/inoory/items/7c8ca9fd5e1aca3e2e72
"""
df.iplot(xTitle="X軸名", yTitle="Y軸名", title="タイトル")
df.iplot(kind="scatter" ,mode='markers', x="col1", y=["col2"]) # 散布図
df.iplot(kind="scatter" ,mode='lines+markers', x="col1", y=["col2"]) # 散布図　線つき
df.iplot(kind="scatter" ,mode='lines', x="col1", y=["col2"]) # 散布図　線のみ
df.iplot(subplots=True, shape=(2,1), shared_xaxes=True)#subplot
"""
pandas plot 動くグラフ　図　可視化
 figの中身はdict型
"""
fig = df.figure(secondary_y="col2", yTitle="ylabel", xTitle="xlabel")
fig.layout.yaxis2.title = "y2label"
df.iplot(fig)

"""
pandas table 表　綺麗
 data_matrix : リスト
 df pandas dataframe
"""
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff
# iplot(ff.create_table(data_matrix))
iplot(ff.create_table(df))

#-------------------------windows --------------------
"""
popup message without tk 
https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
"""
import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
"""
beep音を出す　音を出す　知らせる
"""
import winsound
winsound.Beep(1000,800)
"""
ショートカットを作成
"""
import win32com.client
ws = win32com.client.Dispatch("wscript.shell")
scut = ws.CreateShortcut('run_idle.lnk')
scut.TargetPath = '"c:/python27/python.exe"'
scut.Arguments = '-m idlelib.idle'
scut.Save()

#---------------------------pyhton datetime ------------------------------------
"""
string ⇨ datetime フォーマットに気をつける。
"""
from datetime import datetime as dt
tstr1 = '2019-01-01 00:00:00'
tdatetime = dt.strptime(tstr1, '%Y-%m-%d %H:%M:%S')
tstr2 = '2019/01/01 00:00:00'
tdatetime = dt.strptime(tstr2, '%Y/%m/%d %H:%M:%S')
"""
datetime ⇨ string
"""
from datetime import datetime as dt
tdatetime = dt.now()
tstr1 = tdatetime.strftime('%Y-%m-%d') # 2018-1-18
tstr2 = tdatetime.strftime('%Y/%m/%d %H:%M:%S') # 2018/1/18 12:34:56
"""
datetimeの足し算引き算
"""
now = datetime.now()
tomorrow = now + datetime.timedelta(days = 1) #今より1日後
nextweek = now + datetime.timedelta(weeks = 1) #今より一週間後

#---------------------------pyhton database ------------------------------------
"""
database sqlite データベース　作成　テーブル作成　レコードを追加
sqlite3.connect() でデータベースファイルを指定すると、データベースへの接続（sqlite3.Connection オブジェクト）を取得できます。 
指定したデータベースファイルが存在しない場合は新規に作成されます。
SQL コマンドを実行するには、Connection#cursor() により sqlite3.Cursor オブジェクトを作成し、execute() メソッドを呼び出します。 
次の例では、データベースに新しいテーブル memo を作成しています。
テーブルを作成するのと同様に、Cursor#execute() を使ってレコードを追加できます。
"""
import sqlite3
conn = sqlite3.connect('sample.db')

cur = conn.cursor() # Create a 'Cursor' object from 'Connection' object.
cur.execute('''CREATE TABLE memo(date TEXT, title TEXT, body TEXT)''')# Create a table
cur.execute("""INSERT INTO memoVALUES('2007-01-01', 'Memo1', 'Body1')""")# Insert a record
conn.commit()# コミット
conn.close()# コネクションをクローズ
#---------------------------pyhton 図形 ------------------------------------
"""
ポイントを時計回りに並べ替える　
pnt -- list points ex) [[-0.4, -1.52], [-1.8, -0.36],[-0.1, 0.8], [0.27, 0.4], [0.42, 0.28]]
"""
def _angle_between(refvec):
    origin=[0,0]
    ang1 = np.arctan2(*origin[::-1])
    ang2 = np.arctan2(*refvec[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

pnt = sorted(pnt, key=_angle_between)#時計回り
pnt = sorted(pnt, key=_angle_between,reverse=True)#反時計回り

#---------------------------pyhton 数値計算 ------------------------------------
"""
数字の表示　e E CAE 浮動小数点　eで表示
"""
a=1.5/10000 #0.00015
b="{:.4e}".format(a) #'1.5000e-04'
c = b.replace("e","E") #''1.5000E-04'

#---------------------------pyhton 文字列 ------------------------------------
i = i.replace("4,500", "")#【置き換え】
tes = "ssssaaaa"
tes.find("aaa") #最初から探す 【特定の文字列を見つける】
tes.rfind("aaa") #最後から探す 【特定の文字列を見つける】
s="株 （1株単位）"
s=s[s.find("株 （")+len( "株 （"):s.find("株単位）" ) ]
def cut_text_rss(src):#【文字列を抜き出す】
    tai="取引結果"
    l=len(tai)
    n=src.find(tai)
    src2=src[n+l:]
    n=src2.find(tai)
    src2=src2[:n]
    return src2

def decodef(src):#【デコード】
    try:
        src=src.decode('utf-8')
        return src
    except:
        print("decode error")

#---------------------------selenium ------------------------------------
"""
selenium chrome driverにpathを通しておく必要あり
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost:50001/startp")
driver.quit()

#---------------------------pyhton subprocess ------------------------------------
"""
subprocess http://qiita.com/mokemokechicken/items/a84b0aa96b94d1931f08
"""
import os,subprocess
args=["C:\Program Files (x86)\MarketSpeed\MLauncher\MLauncher.exe" ,"MarketSpeed"]
p1=subprocess.Popen(args)
p1.wait()#処理待ちしない場合は、これを消す

#---------------------------jupyter ------------------------------------
"""
jupyterのマジックコマンド
 %who : 宣言されている変数一覧の表示
 %whos : 宣言されている変数一覧の詳細表示(型と値)
 obj? : Objectの型と値の表示
 %quickref : サポートされるMagic Commandの一覧の表示
 %matplotlib inline : jupyter内に表示させる
"""
"""
テーブルの表示設定
"""
pd.options.display.max_columns = None
pd.options.display.max_rows = 100

#---------------------------file/folder操作 ファイル、フォルダ------------------------------------
"""
ファイルの操作
"""
f = open("write.txt","w")
f.write("Pythonでファイルに書き込みました！")
f.close()

f = open("write.txt","r")
for row in f:
    print(row)
f.close()
"""
フォルダの操作　
"""
if not os.path.exists(os.path.dirname(f_path_copy)):#フォルダが無ければ作成する
    os.makedirs(os.path.dirname(f_path_copy))
shutil.rmtree("diff_env")#フォルダの削除
os.mkdir("diff_env")#フォルダの作成
#---------------------------環境変数 ------------------------------------
os.environ['userprofile']#環境変数を取得
sys.path.append("/Users/username/Desktop")#ライブラリを読み込むパスを追加（一時的にpythonpathに追加）
#---------------------------環境づくり ------------------------------------
"""
pip
 pip freeze インストールされているライブラリ
"""

"""
アンダースコア"_"の役割
 アンダースコア二つで定義される関数は外部の参照を受けないもの。この場合、アンダースコアで囲う。
 アンダースコア一つで定義される関数は参照はできるが、基本的に外部から参照しない ということを慣習化させたものらしい。
"""
#---------------------------class ------------------------------------
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
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