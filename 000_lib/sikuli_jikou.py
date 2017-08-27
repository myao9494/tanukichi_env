# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
# 環境変数　SIKULI_HOMEに"runsikulix.cmd"があるpathを設定する
# 
###############################################################################

import subprocess,os
'''
sikuliの起動と
sikuliスクリプトを実行する関数です
'''

def open_sikuli_ide():
    hp=os.environ['SIKULI_HOME']
    path1 = os.path.join(hp, 'runsikulix.cmd')
    args=[path1]
    p=subprocess.Popen(args)
    print("sikuliを起動しました")
    
def jikou_sikuli(path2):
    print("starting_sikuli please Wait about7seconds")
    hp=os.environ['SIKULI_HOME']
    path1 = os.path.join(hp, 'runsikulix.cmd')
    args=[path1,"-r",path2]
    p=subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_value = p.communicate()[0]
    k=stdout_value
    print(k)