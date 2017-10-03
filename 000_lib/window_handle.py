# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
# 
###############################################################################
import win32gui,win32con,time,sys

class window_ope():
    '''
    windowのオペレーションをまとめます
    '''
    def __init__(self):
        self.taisho_name = ""
        self.mlst=[]

    def window_enum_handler(self,hwnd,resultList):
#         if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
            resultList.append((hwnd, win32gui.GetWindowText(hwnd)))

    def get_app_list(self,handles=[]):
        self.mlst.clear()
        handles.clear()
        win32gui.EnumWindows(self.window_enum_handler, handles)
        for handle in handles:
            self.mlst.append(handle)

    def hyoji(self,handle_n):
        win32gui.SetWindowPos(handle_n,win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)
        win32gui.ShowWindow( handle_n, win32con.SW_SHOWMAXIMIZED)
    
    def kaijyo(self,handle_n):
        win32gui.SetWindowPos(handle_n,win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_SHOWWINDOW)

    def get_handle(self):
        self.get_app_list()
        for i in self.mlst:
            try:
                aa=i[1].encode("utf-8","ignore")
                if aa.find(self.taisho_name.encode("utf-8","ignore")) != -1:
                    self.handle=i[0]
            except:
                print("error")
                
    def window_hyoji(self):
        self.hyoji(self.handle)
        time.sleep(0.2)
        self.kaijyo(self.handle)
        
    def window_close(self):
        win32gui.PostMessage(self.handle,win32con.WM_CLOSE,0,0)

if __name__ == '__main__':
    # time.sleep(20)
    obj=window_ope()
    obj.taisho_name=sys.argv[1]
    # obj.taisho_name="Market Speed"
    obj.get_handle()
    obj.window_hyoji()
    print(obj.taisho_name)
