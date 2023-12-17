from collections.abc import Callable, Iterable, Mapping
from typing import *
import time
import threading
from typing import Any


class DaemonService(threading.Thread):
    def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
    
    def run(self) -> None:
        while (True):
            time.sleep(0.1)
            print(f"{threading.active_count()} active thread(s): {threading.enumerate()}")
        return super().run()
    

if __name__ == "__main__":
    daemon_thread = DaemonService(name="daemon_service", daemon=True)
    daemon_thread.start()
    
    time.sleep(1)