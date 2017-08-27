
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
    jupyterの繰り返し作業を纏めました。便利になるはず！
    '''
    def __init__(self):
        self.file_name = ""
        self.t_path = ""
        self.c_path = ""
        self.markup_code = ""
        self.file_path = os.getcwd() #実行しているファイルのpathを取得する
        self.files = [f for f in os.listdir(self.file_path) if os.path.isfile(os.path.join(self.file_path, f))] #ファイル一覧を取得
        self.folders = [f for f in os.listdir(self.file_path) if os.path.isdir(os.path.join(self.file_path, f))] #フォルダ一覧を取得
                
    def add_file_no_folder(self, file_name): #フォルダを作らずにテンプレートファイrからファイルを作る
        try:
            self.file_name=file_name
            self.t_path=os.path.join(os.environ["jupyter_home"],'991_template/template.ipynb')
            self.c_path= file_name + ".ipynb"
            self.markup_code="# [" + file_name + "](" + self.c_path + ")"
            shutil.copyfile(self.t_path, self.c_path)
            print("下記をコピペ、markdownのセルへ")
            print(self.markup_code)
        except:
            print("Error! 既にファイルがないことを確認して下さい")

    def add_file(self, file_name): #引数のフォルダを作成し、引数のファイル名でフォルダ内にファイルを作成
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
            
    def child_notebook_filelist(self): #フォルダ内のipynbファイルをリストで表示
        print("下記をコピペ、markdownのセルへ")
        for file in self.files:
            if (file.find('.ipynb') != -1 and file.find('.ipynb')!= 0 ):
                print ("# [" + file[:file.find('.ipynb')] + "](" + file + ")")
                
    def child_folder(self): #フォルダ内のふぉるだを表示
        print("下記をコピペ、markdownのセルへ")
        for file in self.folders:
            if (file.find('ipynb_checkpoints') == -1 and file.find("__pycache__" )==-1 ) :
                print ("# [" + file + "](" + file + ")")
                
    def tree(self): #フォルダ以下のtreeを表示
        print("下記をコピペ、markdownのセルへ")
        oya_path=""
        for root, dirs, files in os.walk(self.file_path):
            level = root.replace(self.file_path, '').count(os.sep) #階層の深さ
            if level==1:
                oya_path=os.path.basename(root)+"/"
                print("")
            if (os.path.basename(root).find('ipynb_checkpoints') == -1 and os.path.basename(root).find("__pycache__" )==-1 and level!=0 and level<3) :
                print("")
                if level==1:
                    print( '#' * 1 * (level) + ' [' +os.path.basename(root) + ']' + '(' + os.path.basename(root) + ')')
                else:
                    print( '#' * 1 * (level) + ' [' +os.path.basename(root) + ']' + '(' + oya_path + os.path.basename(root) + ')')
                        
            for f in files:
                if (f.find('.ipynb') != -1 and f.find('ipynb')!= 0 and f.find('checkpoint')== -1):
                    a=os.path.basename(root)+ '/'
                    a=a.replace(oya_path,"")
                    print('>' + '#' * 1 * (level + 1) +' [' + f + ']' + '(' + oya_path + a  + f +')')
                
if __name__ == '__main__':
    obj=jupyter_tanuki()