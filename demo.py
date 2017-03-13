# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:41:33 2017


"""

import hashlib
md5_hash = hashlib.md5()
print(" text to be hashed is \" this is my Document \" ")
print ('MD5 - hash')
md5_hash.update("this is my Document")
print (md5_hash.hexdigest())


print('sha 256 - hash ')
sha256_hash = hashlib.sha256("this is my Document")
print(sha256_hash.hexdigest())
