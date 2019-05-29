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
#---------------------------pandas ------------------------------------
"""
pandas sample 時系列
"""
import datetime
i=1000
now=datetime.datetime.now()
li=[now,i,i+10,i-10,i+5]
df = pd.DataFrame([li])

for p in range(3000):
    i=i+10
    if p != 2:
        li=[now+datetime.timedelta(seconds=p*45),i,i+10,i-10,i+5]
    else:
        li=[now+datetime.timedelta(seconds=p*45)," ","","",""]
#     df.replace(' ', '')
    df=df.append([li], ignore_index=True)
df.columns=["time", "open","high","low","close"]
df.to_csv("test.csv", index=False)

"""
pandas sample 普通
"""
df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9],'D':["ddd","drh","dsh"]})
df.to_csv("test_other.csv", index=False)

"""
pd.Timestamp
"""
today = pd.Timestamp(date.today())
pd.Timestamp(2019,12,15,9,10,1) #2019年12月15日9時10分1秒

"""
pandas 時系列　
"""
df=pd.read_csv("test_time.csv", header=0, index_col='time', parse_dates=True,na_values=[" ", 0],dtype="float")#読み込み 
df.index=pd.DatetimeIndex(df.index)#インデックスを時間に指定
df=df.between_time('9:00', '11:30')#特定の時間のみを取り出す（日時は関係なし）
df_temp = df[df.index >= pd.Timestamp(2019,1,25)]#2019年1月25日以降のデータを出す

"""
pandas 読み込み codec error 読み込み時にcodecのエラーが出る
"""
import codec
with codecs.open("file.csv", "r", "Shift-JIS", "ignore") as file:
    df = pd.read_table(file, delimiter=",")

"""
pandas 読み込み 数値
"""
df=pd.read_csv( "test.csv", header=0, dtype="int")
df=pd.read_csv( "test.csv", header=0, dtype="float")

"""
pandas 読み込み 文字列　
"""
df=pd.read_csv( "test_other.csv", header=0, dtype="str")#文字列

"""
pandas 読み込み sqlite3
"""
import pandas as pd
import sqlite3
mei=7974
db_name = os.path.join(os.environ['userprofile'], "Documents" , (str(mei) + ".db"))
conn = sqlite3.connect(db_name)
df=pd.read_sql_query('select * from {}'.format('stock_data'), conn, index_col='時間')
df.index=pd.DatetimeIndex(df.index)
df = df.replace([' ', '  :  ',"nan","  :  :  "], [np.nan, np.nan, np.nan, np.nan])
conn.close()
"""
pandas 読み込み web
"""
url = 'http://www.jma.go.jp/jp/warn/329_table.html'
fetched_dataframes = pd.io.html.read_html(url)

"""
欠損値nanの扱い　Nan NaN https://note.nkmk.me/python-pandas-nan-dropna-fillna/
"""
df = df.replace([' ', '  :  ',"nan","  :  :  "], [np.nan, np.nan, np.nan, np.nan])#特定の文字列をnanに変更
df=df.dropna() #nanの行を削除（行内に一つでもnanがあれば　行を削除）
df.dropna(axis=1) #nanの列を削除（列内に一つでもnanがあれば　列を削除）
df.dropna(how='all') #すべての値が欠損値である行を削除する
df.dropna(how='all', axis=1) #すべての値が欠損値である列を削除する
df.dropna(how='all').dropna(how='all', axis=1) #行列両方に適用
df.dropna(subset=['age', 'state']) # 特定の列に欠損値がある行を削除する
df.dropna(subset=[0, 4], axis=1) #subsetで指定した行に欠損値がある列を削除
df.fillna(0)#引数に置き換えたい値を指定するとすべての欠損値NaNがその値で置き換わる
df.fillna({'name': 'XXX', 'age': 20, 'point': 0})#引数に辞書を指定すると、列ごとに異なる値が代入
df.fillna(method='ffill') #前の値で置き換え
df.fillna(method='bfill') #後ろの値で置き換え
df.apply(pd.Series.interpolate)#前後の線形の値で埋めたい場合 https://openbook4.me/projects/183/sections/777

"""
inf弾く
"""
import numpy as np
df.replace([np.inf, -np.inf], np.nan)

"""
pandas 書き込み
"""
df.to_csv("test.csv", index=True)
df.to_csv("test.csv", index=False)
"""
pandas dataframeのデータに関数適用　新しい列に結果をついか map, applymap, apply
https://note.nkmk.me/python-pandas-map-applymap-apply/
func：適用する関数
df['D']に　row['A'] + row['B'] + row['C']　の計算結果を追加する
"""
def func(row):
    return row['A'] + row['B'] + row['C']
df = pd.DataFrame({'A':[1,2,3],'B':[10,20,30],'C':[100,200,300]})
df['D'] = df.apply( func, axis=1)

"""
pandas 型
"""
df.dtypes # 型確認
"""
'b'       boolean
'i'       (signed) integer
'u'       unsigned integer
'f'       floating-point
'c'       complex-floating point
'O'       (Python) objects
'S', 'a'  (byte-)string
'U'       Unicode
'V'       raw data (void)
"""
df=df.apply(pd.to_numeric, errors='ignore') #型変更（数字に変換）エラーは無視
df['現在値'].apply(pd.to_numeric, errors='coerce') #型変更（数字に変換）エラーはnanとなる
df['i'].astype(str) #数値を文字列に変換
    #整数intに変換
df['i'].astype(float) #浮動小数点floatに変換

"""
pandas 文字列 すべてのセルの文字数を8個にする
"""
moji = lambda x: x + " "* (8-len(x))
a=moji(str(253)) #253 -> 253     
print(a,len(a)) # 253      8
df= df.applymap(moji) #すべてのセルの文字数を8個にする
"""
pandas 文字列 各列の文字列を結合  https://qiita.com/piroyoung/items/dd209801ca60a0b00c11
"""
df=df.assign(text_output=lambda df: df.apply(lambda row: "".join(row), axis=1))

"""
pandas index を指定
"""
df=df.set_index("時間")
df.index=pd.DatetimeIndex(df.index)



"""
pandas data 抽出　pandas.DataFrameの行を条件で抽出するquery
https://note.nkmk.me/python-pandas-query/

query の場合　Noneや欠損値NaNがある列に対して文字列メソッドを適用して条件とするとエラーになるので注意。
"""
df[df['age'] < 25] #比較演算子で条件指定
df[df.a > 0]  # aというカラムが0より大きいものを抽出
df[~df.a > 0] # aというカラムが0より大きいもの"以外"を抽出
df.query('age < 25')#条件を文字列で指定
df.query('not age < 25') #否定はnot
df.query('24 <= age < 50') #条件指定のように範囲を指定可能
df.query('age < point / 3')#列と列との比較や、算術演算子で計算して比較
df.query('state == "CA"') #一致、==
df.query('state != "CA"')#不一致は!=
df[df['state'].isin(['NY', 'TX'])]#in演算子で条件指定
df.query('state in ["NY", "TX"]')#上記と同意
df.query('name.str.endswith("e")', engine='python')# 特定の文字列で終わる
df.query('name.str.contains("li")', engine='python')#特定の文字列を含む
df.query('name.str.match(".*i.*e")', engine='python')#正規表現のパターンに一致する
df.query('index % 2 == 0')#index列に対する条件
val = 80 #変数を使う
df.query('point > @val')
df[(df['age'] < 25) & (df['point'] > 65)]#複数条件を指定
df.query('age < 25 and point > 65')#&でもOK
df.query('age < 25 or point > 65')#|でもOK
df.query('not age < 25 and not point > 65')#否定はnot
"""
3つ以上での条件も同様だが、andのほうがorより優先順位が高いなど順番によって結果が異なるので、先に処理したいまとまりを括弧で囲んだほうが無難。
"""
df.query('(age == 24 | point > 80) & state == "CA"')
df.query('age_year > 25', inplace=True)#引数inplaceで元のオブジェクトを更新

"""
pandas データフレームの中からリストにある列の選択
 li = ['現在値','出来高',.....]
"""
df1=df[li]

"""
pandas plot グラフ　図　可視化
python matplotlibで見栄えの良い色, グラフを作るTips　https://www.procrasist.com/entry/matplotlib-visual-tips
"""
df1.plot(subplots=True,figsize=(20,15))

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
"""
pandas iterrows
# 縦方向にループ
"""
for i, v in df.iterrows(): #下記の場合は、X,Yの列名があり、行方向へのループ（列の場合は行名を入れる）
    print (i, v['X'], v['Y'])    # iは行または列名　v は Series
"""
pandas iterrows
# 横方向にループ
"""
for i, v in df.iteritems():
    print (i, v['a'], v['b'], v['c'])   # v は Series

"""
pandas 選択
"""
df.iloc[0,0] #行列を数字で選択
df.iat[0,0] #行列を数字で選択 こちらの方が早い
df.iat[0, df.columns.get_loc('volume')] #行列を数字で選択
df.loc['Bob', 'age'] #行列を名前で選択
df.at['Bob', 'age'] #行列を名前で選択

"""
セルに値を代入
"""
df.iat[0, df.columns.get_loc('volume')] = df['出来高'][0]

"""
列番号を列名から取得する
"""
df.columns.get_loc('volume')

"""
pandas 重複　http://ailaby.com/duplicated/
"""
df.duplicated().any() #重複チェック
df.duplicated(['x', 'y']).any() #部分的な重複チェック x と y 列の重複チェックは True
df.drop_duplicates(['x', 'y']) # 重複データを削除　前のデータを残す
df.drop_duplicates(['x', 'y'], keep='last') #重複データを削除　後のデータを残す
"""
pandasの列操作
"""
df=df.drop("high", axis=1)#列の削除
df=df.loc[:,["x","y","z"]]#列の順番を変更["y","x","Z"]を["x","y","z"]に並び替える

"""
pandas 全体像をつかむ https://qiita.com/h_kobayashi1125/items/02039e57a656abe8c48f
"""
import pandas_profiling
pandas_profiling.ProfileReport(df)

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