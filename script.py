import sys
import os
import shutil

input_dir = sys.argv[1]
output_dir = sys.argv[2]
#цикл с функцией обхода взят из видео: https://www.youtube.com/watch?v=tJxcKyFMTGo&t=339s
for dirpath, dirnames, filenames in os.walk(input_dir):
    for filename in filenames:
        src_path = os.path.join(dirpath, filename)
        dst_path = os.path.join(output_dir, filename)
        shutil.copyfile(src_path, dst_path)
        