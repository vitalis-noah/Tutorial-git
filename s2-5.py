# s2-5 マルチスレッド:threadingモジュール (p.018)
#    https://docs.python.jp/3/library/threading.html
# memo: 意味不明。結果もテキストと不一致。

# Threadのメインで実行
print('\n\n◆Threadのクラスで実行')
import threading

def function(number):
    for i in range(5):
        print(str(number + 1) + \
            '番目のスレッド:' + str(i))

def main():
    for i in range(3):
        thread_test = threading. \
            Thread(target=function,args=(i,))
        thread_test.start()
    thread_test.join()

if __name__ == "__main__":
    main()


# Threadのサブクラスで実行
print('\n\n◆Threadのサブクラスで実行')
import threading

class TestThread(threading.Thread):
    def __init__(self, number):
        super(TestThread, self).__init__()
        self.number = number

    def run(self):
        for i in range(5):
            print(str(self.number + 1) + \
                '番のスレッド:' + str(i))

def main():
    for i in range(3):
        thread_test = TestThread(i)
        thread_test.start()
    thread_test.join()

if __name__ == "__main__":
    main()


# Lockオブジェクト
print('\n\n◆同期:Lockオブジェクト')
import threading

def function(lock_test, number):
    lock_test.acquire()
    for i in range(5):
        print(str(number + 1) + \
            '番目のスレッド:' + str(i))
    lock_test.release()

def main():
    lock_test = threading.Lock()
    for i in range(3):
        thread_test = threading.Thread( \
            target=function,args=(lock_test,i))
        thread_test.start()
    thread_test.join()

if __name__ == "__main__":
    main()




















