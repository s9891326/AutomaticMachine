import os

from View import UI
from Module import Api
from playsound import playsound
from Controller import Websocket
from threading import Thread
import win32gui
import win32con
import time

class main():
    def __init__(self):
        # websocket --> 利用ws:127.0.0.1:7777進行連線，並傳送資料會傳送到前端，進行整合
        self.Ws_App = Websocket.WS(self)
        # self.UI = UI.MainWindow(image="Resource/Hancock.jpg")
        print("init")

    def Run(self):
        # self.UI.setupUi()
        print("run websocket")
        t = Thread(target=self.Ws_App.Init_Websocket)
        t.start()
        self.start_ui()

        # flask -->  輕量級Web應用框架
        print("run flask")
        Api.Services = self
        Api.app.config['JSON_AS_ASCII'] = False
        Api.app.run()

    def push(self, message):
        print("收到推播 :{}".format(message))
        self.Ws_App.send_order_to_all("notify", message)
        self.helper_win_show()
        # playsound("Resource/shout.mp3")
        return message

    def helper_win_show(self):
        hwnd = win32gui.FindWindow(None, 'visual_helper')
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 1000, 0, 0, 0, win32con.SWP_NOSIZE)
        print("{} is show".format(hwnd))

    def helper_win_hide(self):
        hwnd = win32gui.FindWindow(None, 'visual_helper')
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 1000, 0, 0, 0, win32con.SWP_NOSIZE)
        print("{} is hide".format(hwnd))

    def start_ui(self):
        cd = Thread(target=os.chdir, args=["./NodeUI"])
        cd.start()
        start = Thread(target=os.system, args=["npm start"])
        start.start()

if __name__ == '__main__':
    obj = main()
    obj.Run()
    # obj.helper_win_show()
    # time.sleep(3)
    # obj.helper_win_hide()
