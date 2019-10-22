
# モチベーション
私は通常、jupyterを使って仕事をしている機械系エンジニアなのですが、現在所属している会社では紙でのアウトプットが求められており、これの対応に苦慮しています。
jupyterで会社指定のフォーマットに紙で出力するのは難しいので、現在は、MS　officeにjupyterでの検討結果を貼り付けて対応しているのですが、設計計算書の数式系がメンドくさかったので、pythonのsympyでやってみました。

# 環境
- windows10
- anaconda
- python 3.7.1

# つまづきポイント
1. ギリシャ文字をjupyrerの中で使う  
   jupyterのcode上で、”\sigma + tab”で、σが使えるようになる。便利!
2. 単位をsympyでつける  
   ググれば直ぐに見つかると思いきや、なかなか見つからなかった。。。  
   結果的には、単位用のSymbolを作って、それを*で繋げればOK
3. sympyでの上付き表示などの方法がわからなかった。  
   LaTexのコマンドがだいたい使えることが分かった。下記サイトがよくまとっていてGOOD！  
　　http://www1.kiy.jp/~yoka/LaTeX/latex.html

# やったこと
集中荷重片持ち梁の計算をやってみました。荷重、長さ、断面係数をインプットすると、計算書で使えるアウトプットを出力しています。jupyterにインポートして使うことを想定しています。

```python:beam.py
from sympy import Symbol,pi,Eq
from IPython.display import display
from sympy.interactive import printing
printing.init_printing(use_latex=True)

#使用するシンボルはグローバルで定義
σmax= Symbol('σ_max')
eσmax= Symbol('σ_max')
MPa= Symbol('(MPa)')
Mmax= Symbol('M_max')
eMmax= Symbol('M_max')
N_mm= Symbol('(N \cdot mm)')
Z= Symbol('Z')
eZ= Symbol('Z')
mm3= Symbol('({mm^3})')
F= Symbol('F')
eF= Symbol('F')
N= Symbol('(N)')
L= Symbol('L')
eL= Symbol('L')
mm= Symbol('(mm)')

paramater_dict= {
    "σmax":["曲げ応力","MPa"],
    "Mmax":["曲げモーメント","N_mm"],
    "Z":["断面係数","mm3"],
    "F":["荷重","N"],
    "L":["梁の長さ","mm"]
    }

def siki_hyoji(atai,unit_opp = True):
    """sympyで式を表示する関数です
    　　（ a = b [mm]　の形で返す）
    Arguments:
        atai {str} -- パラメータ名
    
    Keyword Arguments:
        unit_opp {bool} -- 単位の表示有無 (default: {True}単位を表示する)
    
    Returns:
        [sympy] -- sympyの式をかえします
    """
    ns = globals()
    hidari = ns["e"+atai]
    migi = ns[atai]
    unit = ns[paramater_dict[atai][1]]
    if unit_opp == True:
        siki = Eq(hidari,migi*unit)
    else:
        siki = Eq(hidari,migi)
    return siki

def katamochi_bari(paramater):
    """片持ち梁の計算書ネタを作成します[荷重,長さ,断面係数]
    
    Arguments:
        paramater {list} -- [荷重,長さ,断面係数]
    """
    
    global σmax,Mmax,Z,F,L #global変数を編集可能にする
    print("曲げ応力は以下の式で表される")
    σmax = Mmax/Z
    Mmax = F*L
    display(siki_hyoji("σmax",False),siki_hyoji("Mmax",False))

    print("各パラメータの値を以下に示す")
    F = paramater[0]
    L = paramater[1]
    Z = paramater[2]
    display(siki_hyoji("F"),siki_hyoji("L"),siki_hyoji("Z"))

    print("以上より")
    Mmax = F*L
    σmax = Mmax/Z
    σmax = round(σmax)
    display(siki_hyoji("Mmax"),siki_hyoji("σmax"))

```

# 実行方法
jupyterファイルを同じフォルダにbeam.pyを置きます。
以下の通り実行すると、計算書のネタが完成！

![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/274127/a145464c-7fc9-dc74-5bac-17a39856f3a5.png)

## ソースコード
https://github.com/myao9494/sympy_calculation_sheet

sympy用のsymbolを作るのが、めんどくさかったので、utility.pyで、パラメータの辞書からsymbolを作成できるようにしています。


# ひとりごと
今後、拡張していくと、作業が楽になりそう。
日本語変数、イケてない。。。けど使ってしまう
今回が、初投稿です！
