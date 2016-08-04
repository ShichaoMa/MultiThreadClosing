# 强制关闭子线程程序<br/>
# 使用信号管理主线程子线程关闭及资源回收操作<br/>

ubuntu

INSTALL

    git clone https://github.com/ShichaoMa/MultiThreadClosing.git

HELLOWORLD

    ```
        # 参见test.py
    ```

说明：
    第一次ctrl c开始关闭程序，等待子线程最后一次循环完毕
    第二次ctrl c强制关闭程序
