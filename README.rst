强制关闭子线程程序
=========

INSTALL
-------
ubuntu
>>>>>>
    ::

     (sudo) pip install multi-thread-closing
     git clone https://github.com/ShichaoMa/MultiThreadClosing.git
HELLOWORLD
----------
- 参见 reference_。
.. _reference: https://github.com/ShichaoMa/MultiThreadClosing/blob/master/test.py
DESCRIPTION
-----------
- 使用信号管理主线程子线程关闭及资源回收操作
- 第一次ctrl c开始关闭程序，等待子线程最后一次循环完毕
- 第二次ctrl c强制关闭程序
