
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
# PYTHONPATHに"%jupyterhome%\000_lib"を設定する
# 
###############################################################################
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

if __name__ == '__main__':
    jikou("sikuli")


    