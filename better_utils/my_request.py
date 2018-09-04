# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:53:12 2018

@author: ying.zhang01
"""

import json
import requests
import Log


class MyRequest:
    """自封装http请求类。"""

    def __init__(self):
        """构造函数，初始化相关属性"""
        self.headers = {
                "Accept": "application/json",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Cache-Control": "no-cache",
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
                }

    def get(self, url, params):
        """get请求。"""
        # 检查传入的url
        if url is None:
            Log.error("get请求错误：url为空!!!")
            return None

        # 检查传入的参数
        try:
            params_dict = json.loads(params)
        except Exception as e:
            Log.error("get请求错误：参数格式错误!!!"+str(repr(e)))
            return None

        # get请求
        try:
            r = requests.get(url,
                             params=params_dict,
                             headers=self.headers,
                             timeout=5)
        except Exception as e:
            Log.error("get请求异常,异常提示："+str(repr(e)))
            return None

        if r.status_code != 200:
            Log.error("get请求响应错误：%d" % r.status_code)
            return None

        # 如果都没有错误，返回请求结果
        Log.info("get请求成功!")
        return r.text

    def post(self, url, params):
        """post请求。"""
        # 检查传入的url
        if url is None:
            Log.error("post请求错误：url为空!!!")
            return None

        # 检查传入的参数
        try:
            params_dict = json.loads(params)
        except Exception as e:
            Log.error("post请求错误：参数格式错误!!!"+str(repr(e)))
            return None

        # post请求
        try:
            r = requests.post(url,
                              data=params_dict,
                              headers=self.headers,
                              timeout=5)
        except Exception as e:
            Log.error("post请求异常,异常提示："+str(repr(e)))
            return None

        if r.status_code != 200:
            Log.error("post请求响应错误：%d" % r.status_code)
            return None

        # 如果都没有错误，返回请求结果
        Log.info("post请求成功!")
        return r.text
