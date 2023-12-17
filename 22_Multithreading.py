import logging
import threading


def thread_func(param):
    logging.info("thread id " + str(threading.current_thread().native_id) + " is executing")
    for i in range(0, 10):
        print(i)
        param.append(i)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("before creating thread")
    return_value = []
    sub_thread = threading.Thread(target=thread_func, name="sub_thread", args=(return_value,))
    logging.info("before running thread")
    sub_thread.start()
    logging.info("waiting for sub_thread done")
    sub_thread.join()
    logging.info("return value: {}".format(return_value))
    logging.info("sub_thread done")
    logging.info("all done")
    