
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
# PYTHONPATHに"%jupyterhome%\000_lib"を設定する
#
###############################################################################
import pyperclip
import subprocess,os

def jikou(exe_path=""):
    if exe_path == "" :
        print("pathが入力されていません")

    elif exe_path == "code" :
        args=[os.environ["code_exe_path"]]
        p=subprocess.Popen(args) 

    elif exe_path == "sikuli" :
        args=[os.path.join(os.environ["SIKULI_HOME"],"runsikulix.cmd")]
        p=subprocess.Popen(args) 

    else:
        args=[[exe_path]]
        p=subprocess.Popen(args)

def delete_equal():
    b=""
    tex=pyperclip.paste()
    for i in range(tex.count("\r\n")+1):
        a=tex[:tex.find('=')]
        tex=tex[tex.find("\r\n")+2:]
        b=b+a+"\r\n"
    pyperclip.copy(b)

def delete_kaigyo():
    tex=pyperclip.paste()
    tex=tex.replace("\r\n","")
    pyperclip.copy(tex)

def delete_under_bar():
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

