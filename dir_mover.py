import shutil
import os
src_dst_map = {
   r'C:\\folderA' : r'C:\\folderB'
} #ect

for src, dst in src_dst_map.items():
   for root, subdirs, files in os.walk(src):
      for file in files:
         path = os.path.join(root, file)
         shutil.move(path, dst)