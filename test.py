import time
from threading import Thread
from multi_thread_closing import MultiThreadClosing


class Test(MultiThreadClosing):

    name = "test_thread"

    def start(self):
        t1 = Thread(target=self.process)
        t2 = Thread(target=self.process)
        self.threads.append(t1)
        self.threads.append(t2)
        t1.start()
        t2.start()
        while filter(lambda x:x.is_alive(), self.threads):
            print "main %s.."%self.alive
            time.sleep(1)

    def process(self):
        while self.alive:
            for i in range(20):
                print i
                time.sleep(3)


if __name__ == "__main__":
    Test().start()