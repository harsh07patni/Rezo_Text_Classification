# -*- coding: utf-8 -*-
import re

file = open('input.txt','r')
# removin html tags
html_cleaner = re.compile('<.*?>')
at_tags_cleaner = re.compile('@.*? ')
hash_tags_cleaner = re.compile('#.*? ')

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)


remove_all_special_chars = re.compile('[^A-Za-z0-9 ]+')


for line in file:
    line = line.strip()
    line = re.sub(html_cleaner, '', line)
    line = re.sub(at_tags_cleaner, '', line)
    line = re.sub(hash_tags_cleaner, '', line)
    line = re.sub(emoji_pattern,'',line)
    line = re.sub(remove_all_special_chars,'',line)

file.close()