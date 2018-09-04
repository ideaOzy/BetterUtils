# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:08:52 2018

@author: ying.zhang01
"""
import os
import json


class JsonReader:
    """json配置文件读取类。"""

    def __init__(self, filepath):
        """初始化。

        Args:
            filepath: string--需要读取excel的文件路径
        """
        if os.path.exists(filepath):
            self.filepath = filepath
        else:
            raise FileNotFoundError('json文件不存在!')
        self._data = None

    @property
    def data(self):
        """"""
        if self._data is None:
            with open(self.filepath, 'rb') as f:
                self._data = json.load(f)
        return self._data


class Config:
    """配置读取类。"""

    def __init__(self, config):
        """初始化excel表读取类。

        Args:
            config: string--需要读取的json配置文件的路径。
        """
        self.config = JsonReader(config).data

    def get(self, element):
        """根据key名称获取配置文件中相应的数据。

        Args:
            element: string--json配置文件的key名称。
        """
        return self.config[element]


if __name__ == '__main__':
    config = Config()
    print(config.get('report')["title"])
