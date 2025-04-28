import sys
import os
import shutil

input_dir = sys.argv[1]
output_dir = sys.argv[2]
for dirpath, dirnames, filenames in os.walk(input_dir):
    for filename in filenames:
        shutil.move(filename, output_dir)
        