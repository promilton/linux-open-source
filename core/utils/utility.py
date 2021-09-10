import os
import queue
from pathlib import PurePath
from typing import Union, List, Optional
from random import randint
from . import report, Meta
from .log import Log


class Utils(metaclass=Meta):

    def __init__(self, data):
        """
        Initialize the class object

        """
        assert isinstance(data, int)

        self._data1: int = data

    def __str__(self):
        return 'Utility class'

    @property
    def data1(self) -> int:
        return self._data1

    @data1.setter
    def data1(self, update: Union[List[int], int, float]):
        if isinstance(update, int):
            self._data1 = update
        else:
            raise TypeError(f'{update} not an integer but {type(update)}')

    @Log
    # @staticmethod
    def reverse_string(self, str_: Optional[str] = None) -> str:
        string = ''
        try:
            for char in str_:
                string = char + string
        except Exception as err:
            print(err.__repr__())
        else:
            return string
        finally:
            print("\n")

    @report
    # @staticmethod
    def catch_signal(self, signal: int) -> List[int]:
        signal_list = []
        while True:
            x = randint(0, 9)
            signal_list.append(x)
            if x == signal or len(signal_list) == 10:
                break
        return signal_list

    @staticmethod
    def is_directory_exist(directory: PurePath) -> bool:
        return os.path.isdir(directory)

    @Log
    def str_rev_using_queue(self, str_):
        q = queue.LifoQueue()
        for char in str_:
            q.put(char)
        while not q.empty():
            print(q.get(), end="")
