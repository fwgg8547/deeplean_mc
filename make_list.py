from absl import app, flags, logging
from absl.flags import FLAGS
import glob
import os

#C:\2.Tool\Script\kerastest\yolov3-tf2\data\mindata\JPEGImages

flags.DEFINE_string('path', '', 'path to JPEGImages')

def main(argv):  
  in_path = FLAGS.path  
  files = glob.glob(in_path + '/*')
  
  for f in files:
    name = os.path.basename(f)
    name_wo_ext = os.path.splitext(name)[0]
    print(name_wo_ext)

if __name__ == '__main__':
  app.run(main)
