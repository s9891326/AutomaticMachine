from websocket_server import WebsocketServer
from NodeUI import sound
import base64
import json
import _thread

class WS():
    def __init__(self, main):
        # type : WebsocketServer
        self.ws = None
        self.main = main

    def Init_Websocket(self):
        self.ws = WebsocketServer(7777, host='127.0.0.1')
        self.ws.set_fn_new_client(self.new_client)
        self.ws.set_fn_message_received(self.on_message)
        self.ws.run_forever()

    def new_client(self, ws, server):
        print("有人加入websocket")

    def on_message(self, ws, client, data):
        # print(client)
        # print(data)

#         通訊協定 json格式 {'order': 自訂指令, 'detail': 發送內容}
        try:
            # 編碼方式
            data = base64.b64decode(data).decode()
            cmd = json.loads(data)
            print(data)
            if cmd['order'] == "push_msg":
                self.send_order_to_all(order='notify', detail=cmd['detail'])
            if cmd['order'] == "close_win":
                self.main.helper_win_hide()
        except Exception as e:
            print("Websocket 接收訊息錯誤格式")
            print(e)

    def send_order_to_all(self, order, detail):
        pack = {'order': order, 'detail': detail}
        # print("Ready send{}".format(pack))
        pack = base64.b64encode(json.dumps(pack).encode())
        sound.speak(detail)
        self.ws.send_message_to_all(pack)


# if __name__ == "__main__":
#     obj = WS()
#     obj.Init_Websocket()