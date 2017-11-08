
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
# PYTHONPATHに"%jupyterhome%\000_lib"を設定する
# 
###############################################################################
import os, shutil

class jupyter_tanuki():
    '''
    jupyterを使っていて、見つけた繰り返し作業を纏めました。便利になるはず！
    add_file：直下にフォルダを作成してテンプレートファイルを作成
    child_notebook_filelist：フォルダ内のjupyterファイルを見つけてmarkdown形式で返してくれる
    '''
    def __init__(self):
        self.file_name = ""
        self.t_path = ""
        self.c_path = ""
        self.markup_code = ""
        self.file_path = os.getcwd()
        self.files = os.listdir(self.file_path)

    def add_file(self, file_name):
        try:
            self.file_name=file_name
            self.t_path=os.path.join(os.environ["jupyter_home"],'991_template/template.ipynb')
            self.c_path=file_name + "/" + file_name + ".ipynb"
            self.markup_code="# [" + file_name + "](" + self.c_path + ")"

            print("直下のフォルダを作成して、テンプレートファイルを作成")
            os.mkdir(self.file_name)
            shutil.copyfile(self.t_path, self.c_path)
            print("下記をコピペ、markdownのセルへ")
            print(self.markup_code)
        except:
            print("Error! 既にフォルダがないこと,フォルダ名を入れているかを確認して下さい")

    def child_notebook_filelist(self):
        print("下記をコピペ、markdownのセルへ")
        for file in self.files:
            if (file.find('.ipynb') != -1 and file.find('.ipynb')!= 0):
                print ("# [" + file[:file.find('.ipynb')] + "](" + file + ")")

if __name__ == '__main__':
    obj=jupyter_tanuki()