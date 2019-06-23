"""
pandasで要素、行、列に関数を適用するmap, applymap, apply
Seriesの各要素に適用: map(), apply()
DataFrameの各要素に適用: applymap()
DataFrameの各行・各列に適用: apply()
"""
df_ret = df.apply(lambda d: d['a'] + d['c'], axis=1)
def func(d):
    df = d['a'] + d['c']
    return df
df["ss"] = df.apply(func, axis=1)


"""列名の書き換え
"""
df["ss"] = df.apply(func, axis=1)
df.rename(columns = {'volume':'Volume'}, inplace=True)

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
