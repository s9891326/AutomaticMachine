import os

from Module import Api, ConnectDB, MySQLDB
from playsound import playsound
from Controller import Websocket
from threading import Thread
from datetime import datetime
import win32gui
import win32con

class main:
    def __init__(self):
        # websocket --> 利用ws:127.0.0.1:7777進行連線，並傳送資料會傳送到前端，進行整合
        self.Ws_App = Websocket.WS(self)
        self.DB = ConnectDB.ConnectDB()
        self.id = 0
        # self.MySql = MySQLDB.Mysql()
        self.mysql_id = 0
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

    def push(self, message, request):
        print("收到推播 :{}".format(message))
        url = request.url
        address = request.remote_addr
        create_time = datetime.now()
        self.id = self.DB.insert(url, address, message, create_time)
        # self.mysql_id = self.MySql.insert(url, address, message, create_time)
        self.Ws_App.send_order_to_all("notify", message)
        self.helper_win_show()
        # playsound("Resource/shout.mp3")
        return message

    def update_query_time(self, query_time):
        if self.id != 0:
            self.DB.update(query_time, self.id)
        # if self.mysql_id != 0:
        #     self.MySql.update(query_time, self.mysql_id)

    def helper_win_show(self):
        hwnd = win32gui.FindWindow(None, 'visual_helper')
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 1000, 0, 0, 0, win32con.SWP_NOSIZE)
        print("{} is show".format(hwnd))

    def helper_win_hide(self):
        hwnd = win32gui.FindWindow(None, 'visual_helper')
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 1000, 0, 0, 0, win32con.SWP_NOSIZE)
        print("{} is hide".format(hwnd))

    def start_ui(self):
        cd = Thread(target=os.chdir, args=["NodeUI"])
        cd.start()
        start = Thread(target=os.system, args=["npm start"])
        start.start()

if __name__ == '__main__':
    obj = main()
    obj.Run()
    # obj.helper_win_show()
    # time.sleep(3)
    # obj.helper_win_hide()
