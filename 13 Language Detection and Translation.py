# -*- coding: utf-8 -*-
from textblob import TextBlob

# languge prediction
#translate to spanish
en_blob = TextBlob(u'Simple is better than complex.')
print(en_blob.translate(to='es'))

#convert to english
chinese_blob = TextBlob(u"美丽优于丑陋")
print(chinese_blob.translate(from_lang="zh-CN", to='en'))

#detecting a language
b = TextBlob(u"بسيط هو أفضل من مجمع")
print(b.detect_language())