# -*- coding:utf-8 -*-
import sys
import os


if len(sys.argv) <= 4:
    print "usage: ./file_replace.py  old_text  new_text  filename  (--bak)"

old_text, new_text = sys.argv[1], sys.argv[2]
file_name = sys.argv[3]
# print sys.argv

f = open(file_name, 'rb')
new_file = open('%s..bak' % file_name, 'wb')
for line in f.xreadlines():
    new_file.write(line.replace(old_text, new_text))
f.close()
new_file.close()

if '--bak' in sys.argv:
    os.rename(file_name, '%s.bak' % file_name)  # 原先的文件改成.bak
    os.rename('%s..bak' % file_name, file_name)  # 原先生成的..bak改成原有名
else:
    pass
