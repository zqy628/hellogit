#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
用 Python 实现一个简单的微信红包算法
基本思路就是，有多少个红包，就循环多少次，每一次，在剩下的钱里面随机出一个值作为这个红包的金额，然后把金额从总金额中扣除。
这里要注意，需要保证每个人至少能拿得到 1 分钱。只剩最后一个人时，拿走剩下所有的金额。另外，为了保证计算时候方便，采用“分”作为金额的计算单位。
'''
import random

def 
