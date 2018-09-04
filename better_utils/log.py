# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:53:12 2018

@author: ying.zhang01
"""

import os
import logging
import time

LOG_DIR = ""


class Log:
    """自封装日志输出。"""

    def info(text):
        """info级别信息输出。"""
        # 初始化日志器
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # 创建一个handler,将log写入文件
        # 每分钟生成一个新的文件
        now = time.strftime("%Y-%m-%d %Hh", time.localtime(time.time()))
        filepath = os.path.join(LOG_DIR, now+"_log.txt")
        fh = logging.FileHandler(filepath)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler,将log输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 设置输出格式
        formatter1 = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s : %(message)s"
                )
        formatter2 = logging.Formatter(
                "[%(levelname)s] %(message)s"
                )

        # 组装
        fh.setFormatter(formatter1)
        ch.setFormatter(formatter2)
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 输出信息
        logger.info(text)

        # 移除handler
        logger.removeHandler(fh)
        logger.removeHandler(ch)

    def error(text):
        """error级别信息输出。"""
        # 初始化日志器
        logger = logging.getLogger('__name__ ')
        logger.setLevel(logging.DEBUG)

        # 创建一个handler,将log写入文件
        # 每分钟生成一个新的文件
        now = time.strftime("%Y-%m-%d %Hh", time.localtime(time.time()))
        filepath = os.path.join(LOG_DIR, now+"_log.txt")
        fh = logging.FileHandler(filepath)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler,将log输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 设置输出格式
        formatter1 = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s : %(message)s"
                )
        formatter2 = logging.Formatter(
                "[%(levelname)s] %(message)s"
                )

        # 组装
        fh.setFormatter(formatter1)
        ch.setFormatter(formatter2)
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 输出信息
        logger.error(text)

        # 移除handler
        logger.removeHandler(fh)
        logger.removeHandler(ch)
