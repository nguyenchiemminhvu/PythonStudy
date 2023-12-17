from collections.abc import Callable, Iterable, Mapping
from typing import *
import time
import threading
from typing import Any


class SampleThread(threading.Thread):
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
    
    def run(self) -> None:
        self.arr = []
        for i in range(0, 10):
            time.sleep(0.1)
            self.arr.append(i)
        return super().run()


class DaemonService(threading.Thread):
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
    
    def run(self) -> None:
        while (True):
            time.sleep(0.1)
            print(f"{threading.active_count()} active thread(s): {threading.enumerate()}")
        return super().run()


def thread_func(param):
    for i in range(0, 10):
        time.sleep(0.1)
        param.append(i)


if __name__ == "__main__":
    
    daemon_thread = DaemonService(name="daemon_service", daemon=True)
    daemon_thread.start()
    
    return_value = []
    sub_thread = threading.Thread(target=thread_func, name="sub_thread", args=(return_value,))
    sub_thread.start()
    sub_thread.join()
    print("return value from thread {}: {}".format(sub_thread.name, return_value))
    
    another_sub_thread = SampleThread()
    another_sub_thread.start()
    another_sub_thread.join()
    print("return value from thread {}: {}".format(another_sub_thread.name, another_sub_thread.arr))
    
    time.sleep(1)