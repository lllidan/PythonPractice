import urllib
import time
import queue
import threading

hosts=["http://baidu.com",
       "http://jianshu.com",
       "http://taobao.com"
       "http://tmall.com",
       "http://jd.com"]

queue = queue.Queue()

class ThreadUrl(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue

    def run(self):
        while True:
            host=self.queue.get()
            url= urllib.urlopen(host)
            print(url.geturl())
            print(url.getName())

            print (self.getName())
            self.queue.task_done()

start=time.time()

def main():
    for i in range(5):
        t=ThreadUrl(queue)
        t.setDaemon(True)
        t.start()

    for host in hosts:
        queue.put(host)
    queue.join()

if __name__=="__main__":
    main()

print("it use time:%s" %(time.time()-start))