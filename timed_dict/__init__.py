import time
from threading import Lock


class TimedDict(dict):
    def __init__(self, max_size: int, ttl: int):
        super(TimedDict, self).__init__(self)

        self.data = dict()
        self.data_times = dict()
        self.max_size = max_size
        self.current_size = 0
        self.ttl = ttl
        self.lock = Lock()
        self.instance_attributes = self.__dict__.keys()

    def __getitem__(self, item):
        with self.lock:
            data = self.data[item]
            data_time = self.data_times[item]
            if self.ttl > time.time() - data_time:
                return data

            self.data.pop(item)
            self.data_times.pop(item)

            raise KeyError("Key expired")

    def __setitem__(self, key, value):
        with self.lock:
            if self.current_size > self.max_size:
                if key not in self.data.keys():
                    oldest_key = sorted(self.data_times.items(), key=lambda obj: obj[1])
                    self.data.pop(oldest_key[0])
                    self.data_times.pop(oldest_key[0])
                else:
                    self.current_size += 1

            self.data[key] = value
            self.data_times[key] = time.time()

    def __getattribute__(self, item):
        if str(item).startswith("__"):
            return object.__getattribute__(self, item)

        attributes = object.__getattribute__(self, "instance_attributes")
        if item not in attributes:
            return object.__getattribute__(self, "data").__getattribute__(item)

        return object.__getattribute__(self, item)
