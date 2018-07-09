#!/usr/bin/python
# coding: UTF-8
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print re.findall('python', text, flags=re.IGNORECASE)
print re.sub('python', 'snake', text, flags=re.IGNORECASE)


# 最后的那个例子揭示了一个小缺陷，替换字符串并不会自动跟被匹配字符串的大小写保持
# 一致。 为了修复这个，你可能需要一个辅助函数，就像下面的这样：
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
