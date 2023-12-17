import logging
import threading

def thread_func():
    logging.info("thread id " + str(threading.current_thread().native_id) + " is executing")
    for i in range(0, 10):
        print(i)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("before creating thread")
    sub_thread = threading.Thread(target=thread_func, name="sub_thread")
    logging.info("before running thread")
    sub_thread.start()
    logging.info("waiting for sub_thread done")
    sub_thread.join()
    logging.info("sub_thread done")
    logging.info("all done")
    