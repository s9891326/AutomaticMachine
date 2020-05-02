# AutomaticMachine

### 流程圖
![流程圖](Resource/flow.png)

### 功能圖

### 使用到的技術

**WebSocket**
* 是一種讓瀏覽器與伺服器進行一段互動通訊的技術。這個 API 在不必輪詢（poll）伺服器下，讓使用者傳送訊息至伺服器並接受事件驅動回應。
* ws://127.0.0.1:7777
![websocket method](Resource/websocketMethod.PNG)

**Flask框架**
* 是一個使用 Python 撰寫的輕量級 Web 應用程式框架，由於其輕量特性，也稱為 micro-framework（微框架）


**Vue**

### 架設Ubuntu
> - 設定固定ip
>> - ifconfig 確定一下自己網卡型號 (ex: ens33) 
>> - cd /etc/network
>> - sudo vi interfaces 新增網路相關設定
>> - reboot
> - 安裝ssh server
>> - sudo apt-get install openssh-server
> - ping 到外部網址
>> - ping google.com
> - 再透過MobaXterm連接上該Ubuntu

#### 安裝MySQL
> - 安裝MySQL
>> - ```sudo apt-get install mysql-server```
>> - ```sudo apt install mysql-client```
>> - ```sudo apt install libmysqlclient-dev```
> - 設置MySQL允許遠端訪問
>> - 編輯 mysql.cnf
>>> - ```sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf``` (把 bind-addresss = 127.0.0.1 註解掉
>> - 進入MySQL
>>> - ```mysql -u root -p```
>>> - 密碼 直接 ENTER
>> - 創建新使用者
>>> - ```create user 'eddy'@'%' identified by '你的密碼'; ```
>> - 執行授權命令
>>> - ```GRANT ALL PRIVILEGES ON *.* TO 'eddy'@'%' IDENTIFIED BY '你的密碼' WITH GRANT OPTION;```
>> - 更新設定
>>> - ```flush privileges; ```
>> - 退出 MySQL 服務
>>> - ```exit```
> - 重啟MySQL
>> - ```service mysql restart``` 


參考網址
> https://github.com/Pithikos/python-websocket-server
> https://medium.cm/enjoy-life-enjoy-coding/javascript-websocket-%E8%AE%93%E5%89%8D%E5%BE%8C%E7%AB%AF%E6%B2%92%E6%9C%89%E8%B7%9D%E9%9B%A2-34536c333e1b
> https://andy6804tw.github.io/2019/01/29/ubuntu-mysql-setting/#1-%E7%B7%A8%E8%BC%AF-mysqldcnf