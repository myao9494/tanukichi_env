【置き換え】
i = "4,500"
i = i.replace(",", "")
print(int(i))

【特定の文字列を見つける】
tes.find("デイトレ助言")　#最初から探す
tes.rfind("デイトレ助言")　#最後から探す

【文字列を抜き出す】
s="株 （1株単位）"
s=s[s.find("株 （")+len( "株 （"):s.find("株単位）" ) ]
print(s.find("株 （"),s.find( "株単位）" ) ,s)

【文字列を抜き出す】
def cut_text_rss(src):
    tai="取引結果"
    l=len(tai)
    n=src.find(tai)
    src2=src[n+l:]
    n=src2.find(tai)
    src2=src2[:n]
    return src2
    
【デコード】
def decodef(src):
    try:
        src=src.decode('utf-8')
        return src
    except:
        print("decode error")
