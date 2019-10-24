# 機械設計業務（構造系）の技術者+金融のpandasチートシートです

## 追加でインストール
- dataframeをマークダウン形式の表で出力する

```
pip install pytablewriter
```
```pytablewriter.py
import pytablewriter
writer = pytablewriter.MarkdownTableWriter()
writer.from_dataframe(df)
writer.write_table()
```

## サンプルの作成
- testデータを作る

```test_data.py
import pandas as pd
df = pd.DataFrame([1,2,3,4,5],columns=["対象列"])

df = pd.DataFrame([[1,1],[2,2],[3,3],[4,4],[5,5]],columns=["対象列1","対象列2"])
# 上と同じ
df = pd.DataFrame({"対象列1":[1,2,3,4,5],
                   "対象列2":[1,2,3,4,5]
                  })
```
|対象列1|対象列2|
|------:|------:|
|      1|      1|
|      2|      2|
|      3|      3|
|      4|      4|
|      5|      5|


- 時系列のサンプル

```timeseries.py
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
```
## テーブルの表示設定
```sette.py
pd.options.display.max_columns = None
pd.options.display.max_rows = 100
```

## pandas tableを綺麗に表示

```table.py
from plotly.offline import init_notebook_mode, iplot
import plotly.figure_factory as ff
iplot(ff.create_table(df))
```

## テーブル間のdiff,差分
データを変更した際に、変更箇所のみを抽出したい時に使う  
【use case】:レッドマインのチケットをcsvで纏めて変更した際に、サーバへ反映するチケットidを抽出する

```diff.py
import pandas as pd
df = pd.DataFrame([["リンゴ",1],["オレンジ",2],["いちご",3],["レモン",4],["マンゴー",5]],columns=["id","数量"])
df_edit = df.copy()
df_edit.loc[df_edit['id']=="レモン", '数量']=15
df_diff = pd.concat([df,df_edit])
df_diff = df_diff.drop_duplicates(keep=False)
# keep="last"でdf_edit側の値を残す
df_diff.drop_duplicates(subset="id",keep="last")
```

## よく使うグラフ  
- 散布図

```graph_1.py
'''marker   https://matplotlib.org/api/markers_api.html
.:point ,o:circle, v:下三角, ^:上三角, s:四角 +:plus
linestyle   https://matplotlib.org/gallery/lines_bars_and_markers/linestyles.html?highlight=linestyle
solid,dotted,dashed,dashdot
color   https://matplotlib.org/examples/color/named_colors.html
b:青 (Blue) g:緑 (Green) r:赤 (Red) c:シアン (Cyan) m:マゼンタ (Magenta) y:黄 (Yellow) k:黒 (Black) w:白 (White)
'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()# SeabornのデフォルトStyleを使用
fig = plt.figure(figsize=(8,4))# グラフのサイズを設定(横×縦)
ax = fig.add_subplot(111)
df.plot(x='x', y='z', ax=ax,
        linestyle='dashed', #線種
        marker='o', #マーカー
        color='darkgreen', #色
        linewidth = 0.5) #線の幅
df.plot(x='x', y='y', ax=ax,
        linestyle='dashed', #線種
        marker='o', #マーカー
        color='darkblue', #色
        linewidth = 0.5) #線の幅
ax.set_title("TEST")# TITLEを設定
ax.set_xlim(0,2*np.pi)# X軸の範囲
ax.set_ylim(-1,1)# Y軸の範囲
ax.set_xticks([0, np.pi, np.pi*2])# X軸のTick（目盛）の位置を設定
ax.set_xticklabels([0, 'π', '2π'])# X軸のTick（目盛）の表記を設定
ax.set_yticks([-1, -0.5, 0, 0.5, 1])# Y軸のTick（目盛）の位置を設定
ax.set_xlabel('X [RAD]')# X軸のラベルを設定
ax.set_ylabel('X [RAD]')# Y軸のラベルを設定
plt.show()# グラフ表示
```

- 動くグラフ

```g.py
%matplotlib inline
import pandas as pd
import cufflinks as cf
cf.set_config_file(offline=True, theme="white", offline_show_link=False)
cf.go_offline()

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

```


## 既存の列を使って処理して、新しい列を作成する

- 同一行内の計算
dataseriesにして計算すれば、エクセルと同じイメージで計算できる  
ずらしたい場合は、ずらしたdataseriesを作成して計算すればよい

```cal.py
df["計算"] = df["対象列1"] + df["対象列2"]
```

|対象列1|対象列2|計算|
|------:|------:|---:|
|      1|      1|   2|
|      2|      2|   4|
|      3|      3|   6|
|      4|      4|   8|
|      5|      5|  10|

- 累積和 cumsum  
イメージ：excelで積分。材料力学の梁の計算で、荷重からSFDを求める際など

```cumsum.py
df["累積和"] = df["対象列"].cumsum()
```
|対象列|累積和|
|-----:|-----:|
|     1|     1|
|     2|     3|
|     3|     6|
|     4|    10|
|     5|    15|
- 差分 diff  
イメージ：excelで微分。材料力学の梁の計算で、SFDから荷重を求める際など  
オプションで範囲を指定することができる

```diff.py
df["差分"] = df["対象列"].diff()
```

|対象列|差分|
|-----:|---:|
|     1| NaN|
|     2|   1|
|     3|   1|
|     4|   1|
|     5|   1|

- 関数を使用する  
イメージ：excelで各セルを使って関数を適用。

```apply.py
df["関数"]= df.apply(lambda d: d['対象列1'] + d['対象列2'], axis=1)

#上と同じ
def func(df):
    d = df['対象列1'] + df['対象列2']
    return d
df["関数"] = df.apply(func, axis=1)
```
|対象列1|対象列2|関数|
|------:|------:|---:|
|      1|      1|   2|
|      2|      2|   4|
|      3|      3|   6|
|      4|      4|   8|
|      5|      5|  10|


## 欠損値nanの扱い  

```dropna.py
df.dropna() #nanの行を削除（行内に一つでもnanがあれば　行を削除）
df.dropna(axis=1) #nanの列を削除（列内に一つでもnanがあれば　列を削除）
df.dropna(how='all') #すべての値が欠損値である行を削除する
df.dropna(how='all', axis=1) #すべての値が欠損値である列を削除する
df.dropna(how='all').dropna(how='all', axis=1) #行列両方に適用
df.dropna(subset=['age', 'state']) # 特定の列に欠損値がある行を削除する
df.dropna(subset=[0, 4], axis=1) #subsetで指定した行に欠損値がある列を削除
```
```fillna.py
df.fillna(0)#引数に置き換えたい値を指定するとすべての欠損値NaNがその値で置き換わる
df.fillna({'name': 'XXX', 'age': 20, 'point': 0})#引数に辞書を指定すると、列ごとに異なる値が代入
df.fillna(method='ffill') #前の値で置き換え
df.fillna(method='bfill') #後ろの値で置き換え
```
```apply.py
df.apply(pd.Series.interpolate)#nanを前後の線形の値で埋めたい場合 https://openbook4.me/projects/183/sections/777
```

## 文字列の置換
```replace.py
df = df.replace([' ', '  :  ',"nan","  :  :  "], [np.nan, np.nan, np.nan, np.nan])#特定の文字列をnanに変更
```
  
## 列への処理
- 列volumeの名前をVolumeに変更　inplace=Trueで上書き

```rename.py
df.rename(columns = {'volume':'Volume'}, inplace=True)
```

- 列番号を列名から取得する

```get_loc.py
df.columns.get_loc('volume')
```

- 条件を付けて行の削除

```row_drop.py
df.drop(df.query('age < 25').index)
```


- 列の削除

```drop.py
df=df.drop("high", axis=1)#列の削除
```

- 列の並べ替え

```get_loc.py
df=df.loc[:,["x","y","z"]]#列
の順番を変更["y","x","Z"]を["x","y","z"]に並び替える
```

## 型
- 型を確認

```type.py
df.dtypes # 型確認
```

- 型の種類
'b'       boolean
'i'       (signed) integer
'u'       unsigned integer
'f'       floating-point
'c'       complex-floating point
'O'       (Python) objects
'S', 'a'  (byte-)string
'U'       Unicode
'V'       raw data (void)

- 型変更

```type_1.py
df=df.apply(pd.to_numeric, errors='ignore') #型変更（数字に変換）エラーは無視
df['現在値'].apply(pd.to_numeric, errors='coerce') #型変更（数字に変換）エラーはnanとなる
df['i'].astype(str) #数値を文字列に変換
df['i'].astype(int)   #整数intに変換
df['i'].astype(float) #浮動小数点floatに変換
```

## 条件を与えて、データを抽出する

``` data.py
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
df.query('age_year > 25', inplace=True)#引数inplaceで元のオブジェクトを更新
df.query('not age < 25 and not point > 65')#否定はnot
```

3つ以上での条件も同様だが、andのほうがorより優先順位が高いなど順番によって結果が異なるので、先に処理したいまとまりを括弧で囲んだほうが無難。

``` data_2.py
df.query('(age == 24 | point > 80) & state == "CA"')
```

pandas データフレームの中からリストにある列の選択


``` data_3.py
li = ['現在値','出来高',.....]
df1=df[li]
```

## 重複の確認と処理

``` juhuku.py
df.duplicated().any() #重複チェック
df.duplicated(['x', 'y']).any() #部分的な重複チェック x と y 列の重複チェックは True
df.drop_duplicates(['x', 'y']) # 重複データを削除　前のデータを残す
df.drop_duplicates(['x', 'y'], keep='last') #重複データを削除　後のデータを残す
```

## イタレーション（おすすめしない）
- 縦方向にループ

```iterrows.py
for i, v in df.iterrows(): #下記の場合は、X,Yの列名があり、行方向へのループ（列の場合は行名を入れる）
    print (i, v['X'], v['Y'])    # iは行または列名　v は Series
```

- 横方向にループ

```iteritems.py
for i, v in df.iteritems():
    print (i, v['a'], v['b'], v['c'])   # v は Series
```

## 上下反転(逆順)

```upsidedown.py
df.iloc[::-1]
```

## 列の順序を反転

```retsu.py
df[df.columns[::-1]]
```

## セルの選択
```select.py
df.loc[df['項目']=="レモン", '数量'] #項目列レモンの数量列を選択
df.iloc[0,0] #行列を数字で選択
df.iat[0,0] #行列を数字で選択 こちらの方が早い
df.iat[0, df.columns.get_loc('volume')] #行列を数字で選択
df.loc['Bob', 'age'] #行列を名前で選択
df.at['Bob', 'age'] #行列を名前で選択
```

## 書き込み
- csv

```csv_write.py
df.to_csv("test.csv", index=True)
df.to_csv("test.csv", index=False)
```

## 文字列 すべてのセルの文字数を8個にする
```8moji.py
moji = lambda x: x + " "* (8-len(x))
a=moji(str(253)) #253 -> 253     
print(a,len(a)) # 253      8
df= df.applymap(moji) #すべてのセルの文字数を8個にする
"""
pandas 文字列 各列の文字列を結合  https://qiita.com/piroyoung/items/dd209801ca60a0b00c11
"""
df=df.assign(text_output=lambda df: df.apply(lambda row: "".join(row), axis=1))
```

## indexの指定
```index.py
df=df.set_index("時間")
df.index=pd.DatetimeIndex(df.index)
```

## 時系列
```timestamp.py
today = pd.Timestamp(date.today())
pd.Timestamp(2019,12,15,9,10,1) #2019年12月15日9時10分1秒
```

## pandas 読み込み
- 時系列データ

```time_read.py
df=pd.read_csv("test_time.csv", header=0, index_col='time', parse_dates=True,na_values=[" ", 0],dtype="float")#読み込み 
df.index=pd.DatetimeIndex(df.index)#インデックスを時間に指定
 df=df.between_time('9:00', '11:30')#特定の時間のみを取り出す（日時は関係なし）
df_temp = df[df.index >= pd.Timestamp(2019,1,25)]#2019年1月25日以降のデータを出す
```

- codec error 読み込み時にcodecのエラーが出る場合

```codec.py
import codec
with codecs.open("file.csv", "r", "Shift-JIS", "ignore") as file:
    df = pd.read_table(file, delimiter=",")
```

- 数値で読み込み（タイプを指定）

``` numerical.py
df=pd.read_csv( "test.csv", header=0, dtype="int")
df=pd.read_csv( "test.csv", header=0, dtype="float")
```

- 文字列で読み込み（タイプを指定）

```str.py
df=pd.read_csv( "test_other.csv", header=0, dtype="str")#文字列
```

- sqliteから読み込み

```sqlite.py
import pandas as pd
import sqlite3
mei=7974
db_name = os.path.join(os.environ['userprofile'], "Documents" , (str(mei) + ".db"))
conn = sqlite3.connect(db_name)
df=pd.read_sql_query('select * from {}'.format('stock_data'), conn, index_col='時間')
df.index=pd.DatetimeIndex(df.index)
df = df.replace([' ', '  :  ',"nan","  :  :  "], [np.nan, np.nan, np.nan, np.nan])
conn.close()
```

- webから読み込み

```web.py
url = 'http://www.jma.go.jp/jp/warn/329_table.html'
fetched_dataframes = pd.io.html.read_html(url)
```



