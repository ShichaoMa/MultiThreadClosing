#强制关闭子线程程序<br/>
### 代码更新并合并到了(ParallelMonitor)[https://github.com/ShichaoMa/toolkit/blob/master/toolkit/monitors.py]中，请使用最新代码。
#INSTALL
##ubuntu
```bash
    (sudo) pip install multi-thread-closing

     or

     git clone https://github.com/ShichaoMa/MultiThreadClosing.git
```
#HELLOWORLD
参见[test.py](https://github.com/ShichaoMa/MultiThreadClosing/blob/master/test.py)
#DESCRIPTION
使用信号管理主线程子线程关闭及资源回收操作<br/>
第一次ctrl c开始关闭程序，等待子线程最后一次循环完毕<br/>
第二次ctrl c强制关闭程序
