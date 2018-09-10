# -*- coding: utf-8 -*-

"""
数据生成器模块
~~~~~~~~~~~
一些生成器方法，包括生成随机数，手机号，连续数字等等

@Time: 2018/9/10 14:27
@author: ying.zhang01
@File: data_generator.py
"""

import random
from faker import Factory


fake = Factory().create('zh_CN')


def random_phone_number():
    """生成随机手机号"""
    return fake.phone_number()


def random_name():
    """生成随机姓名"""
    return fake.name()


def random_address():
    """生成随机地址"""
    return fake.address()


def random_email():
    """生成随机邮件"""
    return fake.email()


def random_str(min_chars=0, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)


def factory_generate_ids(starting_id=1, increment=1):
    """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids


def factory_choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
    def choice_generator():
        my_list = list(values)
        # rand = random.Random()
        while True:
            yield random.choice(my_list)
    return choice_generator


if __name__ == '__main__':
    print(random_name())
    print(random_phone_number())
    print(random_address())
    print(random_str(4, 10))
