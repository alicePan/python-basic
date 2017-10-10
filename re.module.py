# -*- coding: UTF-8 -*-
# reference:http://www.runoob.com/python/python-reg-expressions.html
import re

"""
re.match(patern, string, flag) attemp to match from the start of string. 
If matched, return the matched object, else return None.
"""
email_pattern = '^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$'

print re.match(email_pattern, 'xxx.yyy@gmail.com,xxx@qq.com').group()

"""
re.search方法
re.search 扫描整个字符串并返回第一个成功的匹配
"""
print re.search(email_pattern,'my email address is xxx.yyy@gmail.com').group()


"""
Python 的 re 模块提供了re.sub用于替换字符串中的匹配项
re.sub(pattern, repl, string, count=0, flags=0)
repl 参数可以是一个函数, 或者是要被替换成的字符串
返回结果是被替换成的字符串
"""
new = re.sub(email_pattern, 'well, well, well', 'hxxx.@gmail.com', count=0, flags=0)
print new