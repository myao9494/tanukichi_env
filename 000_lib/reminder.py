#カウントダウン機能を付けたい！
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) Mineo Sudo
#
###############################################################################
import winspeech
import sys,datetime,time
from winsound import Beep
from tkinter import *
from tkinter import messagebox
import win32gui,win32con
import pandas as pd

winspeech.initialize_recognizer(winspeech.INPROC_RECOGNIZER)

def callback1():
    hwnd = int(root.wm_frame(),0)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,0,0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
def callback2():
    hwnd = int(root.wm_frame(),0)
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0,0,0,0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

root = Tk()
root.geometry("1000x500")


class remind():
    '''
    リマインド機能をまとめています
    '''
    def __init__(self):
        self.dn=datetime.datetime.now()
        self.tg_time_ji=0
        self.tg_time_hun=0
        self.yoyu_min=0
        self.message = ""
        self.basho=""

    def main(self):
        self.target_time = datetime.datetime(self.dn.year,
                                      self.dn.month,
                                      self.dn.day,
                                      self.tg_time_ji,
                                      self.tg_time_hun,0)
        self.wait_time=(self.target_time-self.dn).total_seconds()-self.yoyu_min*60
        self.say_message()
        time.sleep(self.wait_time)
        self.say_message()
        self.msg_box()

#----------------以下は呼び出される関数--------------------------
    def say_message(self):
        winspeech.say(self.target_time)
        winspeech.say("予定は"+self.message+"です。場所は"+self.basho+"です")

    def msg_box(self):
        la = Label(root, text=str(self.target_time)+"予定は"+self.message+"です。場所は"+self.basho+"です",
                   font=("",20),
                   bg="#00ffff")
        la.place(x = 100,y = 500)
        la.pack()

        root.after(100, callback1) #0.1sec後に前面固定
        root.after(10000, callback2) #10sec後に前面固定やめる
        root.mainloop()

if __name__ == '__main__':
    obj=remind()
    df = pd.read_excel('reminder.xlsx')
    df=df.T
#     input_lines1 = sys.stdin.readlines()
    li=df.values.tolist()[0]
    obj.tg_time_ji=int(li[0])
    obj.tg_time_hun=int(li[1])
    obj.message=str(li[2])
    obj.basho=str(li[3])
    obj.yoyu_min=int(li[4])
    # print(obj.tg_time_ji)
    # print(obj.tg_time_hun)
    # print(obj.message)
    # print(obj.basho)
    # print(obj.yoyu_min)
    obj.main()
