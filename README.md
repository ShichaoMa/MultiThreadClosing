# 强制关闭子线程程序<br/>
├── multi_thread_closing.py<br/>
├── README.md<br/>
└── test.py<br/>

ubuntu

INSTALL

    git clone https://github.com/ShichaoMa/MultiThreadClosing.git

HELLOWORLD

    ```
        # 参见test.py
    ```

说明：
    第一次ctrl c开始关闭程序，等待子线程最后一次循环完毕
    第二次ctrl c强制关闭所有子线程
    第三次ctrl c最终关闭所有线程
    理论上两次ctrl c就可以全部关闭了，但对于子线程有阻塞的情况，
    有的时候可能会卡住，需要多按几遍ctrl c
