
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
# PYTHONPATHに"%jupyterhome%\000_lib"を設定する
#
###############################################################################
import pyperclip,json
import pandas as pd

def numpy_viz(numpy_array):
    """numpyをグラフに表示します
    
    Args:
        numpy_array (numpy array): 見える化したいnumpy行列
    """

    df = pd.DataFrame(numpy_array)
    df_viz(df)
    
def df_viz(df):
    """pandas dataframeをグラフ化します
    
    Args:
        df (pandas dataframe): 見える化したいデータフレーム
    """

    df.plot(subplots=True,figsize=(16,10))


def make_muru_list(li):
    """追いかけたいであろうオブジェクトのリストを返します。実際にはこのリストからリストを作成してmiruへ入力
    
    Args:
        li (list): dir(object)　対象オブジェクトの名前一覧
    
    Returns:
        list: 追いかけたいであろう変数のリスト
    """
    # ignore_listに含まれている変数は除外されます
    ignore_list=["In","NamespaceMagics","Out","exit","get_ipython", 'get_ipython','getsizeof','json','np',
                 'quit','var_dic_list','yapf_reformat','i', 'ignore_list', 'li', 'new_list']
    new_list=[]
    for i in li:
        if i.find("_") != 0 and i not in ignore_list:
            new_list.append(i)
    return new_list

def miru(miru_list,var_dict):
    """対象オブジェクト内のオブジェクトを分析します。miru.jsonにjson形式で保存されます
    
    Args:
        miru_list (list): オブジェクトの名前
        var_dict (dict): vars(object) 対象オブジェクトの変数一覧
    
    Returns:
        dict: miru_dict　変数一覧
        dict: pandas_dict　pandas一覧
        dict: numpy_dict　numpy一覧
        dict: function_dict　function一覧
    """

    miru_dict={}
    pandas_dict={}
    numpy_dict={}
    function_dict={}
    for i in miru_list:
        try:
            if str(type(var_dict[i])).find("DataFrame") != -1:
                pandas_dict[i] = "pandas dataframe"
            elif str(type(var_dict[i])).find("numpy.ndarray") != -1:
                numpy_dict[i] = "numpy"
            elif len(str(var_dict[i])) :
                miru_dict[i] = str(var_dict[i])
        except:
            function_dict[i] = "function"

    with open('miru.json' , "w" ) as f:
        json.dump(miru_dict , f, indent= 4 )
    return miru_dict,pandas_dict,numpy_dict,function_dict

def delete_equal():
    """クリップボード内の文字列から=前のみを抽出します
    """

    b=""
    tex=pyperclip.paste()
    for i in range(tex.count("\r\n")+1):
        a=tex[:tex.find('=')]
        tex=tex[tex.find("\r\n")+2:]
        b=b+a+"\r\n"
    pyperclip.copy(b)

def delete_kaigyo():
    """クリップボード内の文字列から改行を削除します
    """

    tex=pyperclip.paste()
    tex=tex.replace("\r\n","")
    pyperclip.copy(tex)

def replace_under_bar():
    """クリップボード内の文字列内の_をスペースに置き換えます
    """

    tex=pyperclip.paste()
    tex=tex.replace("_"," ")
    pyperclip.copy(tex)

if __name__ == '__main__':
    """test_delete_equal
    """
    test='self.chg_posi = self.obs_posi[-self.step_len:]\r\nself.chg_posi_var = self.obs_posi_var[-self.step_len:]\r\nself.chg_posi_entry_cover = self.obs_posi_entry_cover[-self.step_len:]\r\nself.chg_price = self.obs_price[-self.step_len:]\r\nself.chg_price_mean = self.obs_price_mean[-self.step_len:]\r\nself.chg_reward_fluctuant = self.obs_reward_fluctuant[-self.step_len:]\r\nself.chg_makereal = self.obs_makereal[-self.step_len:]\r\nself.chg_reward = self.obs_reward[-self.step_len:]'
    pyperclip.copy(test)
    delete_equal()
    print(pyperclip.paste())
    """delete_kaigyo
    """
    test='self.chg_posi = self.obs_posi[-self.step_len:]\r\nself.chg_posi_var = self.obs_posi_var[-self.step_len:]\r\nself.chg_posi_entry_cover = self.obs_posi_entry_cover[-self.step_len:]\r\nself.chg_price = self.obs_price[-self.step_len:]\r\nself.chg_price_mean = self.obs_price_mean[-self.step_len:]\r\nself.chg_reward_fluctuant = self.obs_reward_fluctuant[-self.step_len:]\r\nself.chg_makereal = self.obs_makereal[-self.step_len:]\r\nself.chg_reward = self.obs_reward[-self.step_len:]'
    test='self.chg_posi self.chg_posi_var self.chg_posi_entry_cover self.chg_price self.chg_price_mean self.chg_reward_fluctuant self.chg_makereal self.chg_reward '
    pyperclip.copy(test)
    delete_kaigyo()
    print(pyperclip.paste())
    """delete_under_bar
    """
    test="delete_under_bar"
    pyperclip.copy(test)
    delete_under_bar()
    print(pyperclip.paste())

