<!--
 * @Author: your name
 * @Date: 2021-01-11 19:16:06
 * @LastEditTime: 2021-01-11 19:17:38
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \undefinedc:\Users\HASEE\Desktop\HiCnUnicom\README.md
-->
# HiCnUnicom

## 使用方法

### 1. Fork 本仓库


### 2. 授权仓库可运行Action

![](https://github.com/motao123/motao123-HiCnUnicom/blob/master/assets/actions1.png)
![](https://github.com/motao123/motao123-HiCnUnicom/blob/master/assets/actions2.png)


### 3. 添加secret
进入仓库后点击 `Settings`  
侧栏点击 `Secrets`  
点击 `New secret`  

依次添加 `USER` 和 `APPID`  
值对应为你的 `手机号码,服务密码` 和 `联通app抓包的appd值`。 

其中 `APPID` 为联通app抓包的appid值，最好自己抓包，不会抓包就填后面```secret示例```中的默认值，但不保证这个appid能用，所以最好自己抓包，如果运行登录失败大概率就是appid不对或者失效。`APPID` 也可以不设置，未设置将直接使用默认配置(但不建议)。  

有多个手机号码的情况下,添加`USER`时，格式不变，还是`手机号码,服务密码`，一行一个号码+服务密码，手机号码和服务密码用英文半角逗号 `,` 分隔。  
secret示例：  
USER  
```
12345678910,123456
22345678910,223456
32345678910,323456
```
APPID(翻到下面有如何得到自己的APPID方法)  
```
247b001385de5cc6ce11731ba1b15835313d489d604e58280e455a6c91e5058651acfb0f0b77029c2372659c319e02645b54c0acc367e692ab24a546b83c302d
```


### 3. 手动运行一次
进入到Workflows页面，手动运行一次  

![](https://github.com/motao123/motao123-HiCnUnicom/blob/master/assets/actions3.png)

### 其他

1. 无需抓包获取appid方法(由群友提供)：  
不会抓包的就去手机文件管理器，找到路径为 `/sdcard/Unicom/appid` 的文件打开复制。  
2. 运行开始时间也可以自己修改  
`.github/workflows/HiCnUnicom.yml`文件中`- cron: 05 23 * * *`  
05代表5分，23代表23时，就是`UTC0时区`23：05的意思。中国时区(北京时间)为`UTC+8`  
即`UTC0时区`23:05=`UTC+8`15:05,如你想要它在上午10:30运行，相应的UTC0时区就是02:30  
cron表达式为:`- cron: 30 02 * * *`  

## 感谢
感觉原仓库的`commit`比较乱，所以自己新开了个仓库  

Fork自：https://github.com/mixool/HiCnUnicom  
Workflow参考：https://github.com/hzys/HiCnUnicom  

## 免责申明
    
该项目仅供学习使用，严禁用于商业用途，由此造成的一切后果，本人概不负责。
