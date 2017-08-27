#買うんtダウンｋのう\\\\
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

winspeech.initialize_recognizer(winspeech.INPROC_RECOGNIZER)

class remind():
    '''
    リマインド機能をまとめています
    '''
    def __init__(self,tg_time_ji,tg_time_hun,message,yoyu_min):
        self.dn=datetime.datetime.now()
        self.target_time = datetime.datetime(self.dn.year,
                                      self.dn.month,
                                      self.dn.day,
                                      tg_time_ji,
                                      tg_time_hun,0)
        self.yoyu_min=yoyu_min
        self.wait_time=(self.target_time-self.dn).total_seconds()-self.yoyu_min*60
        self.message = message
        
    def main(self):
        self.say_message()
        time.sleep(self.wait_time)
        self.say_message()
        
#----------------以下は呼び出される関数--------------------------
    def say_message(self):
        winspeech.say(self.target_time)
        winspeech.say("予定は"+self.message+"です")
        
    def msg_box(self):
        top = Tk()
        top.geometry("500x100")
#         def hello():
#             messagebox.showinfo("Say Hello", "Hello World")
#         B1 = Button(top, text = "Say Hello", command = hello)
        B1 = Button(top, text = "予定は"+self.message+"です")
        B1.place(x = 35,y = 50)
        top.mainloop()

# if __name__ == '__main__':
#     obj=remind(tg_time_ji=6,tg_time_hun=46,message="test")