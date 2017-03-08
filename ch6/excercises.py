#!/usr/bin/env python
# -*- coding=utf-8 -*-

"python 核心编程第六章习题"

import random
N = random.randint(2,100)
randlist = random.sample(xrange(2**31- 1) ,N)
randlist.sort()
print randlist