import os
import shutil

for f in os.listdir():
    if f.endswith('.txt'):
        shutil.move(f, '[www.baidu.com]' + f)
