


#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: __init__.py
# Date: Wed Dec 25 15:46:52 2013 +0800
# Author: Yuxin Wu <ppwwyyxxc@gmail.com>



def get_extractor(extract_func, **kwargs):
    def f(tup):
        return extract_func(*tup, **kwargs)
    return f