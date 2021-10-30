import time
import threading

lock = threading.Lock()


class MyThread(threading.Thread):
    def run(self):
        lock.acquire()
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)
        lock.release()


def main():
    print("Start main threading")

    threads = [MyThread() for i in range(3)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print("End Main threading")


if __name__ == '__main__':
    main()
