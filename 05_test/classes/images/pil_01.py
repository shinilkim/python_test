'''
썸네일 이미지 만들기
'''
import glob, os, sys
from PIL import Image

dir = 'C:/Users/shinil.kim/Pictures/test/';

def info():

  files = glob.glob(os.path.join(dir, "*.*"))
  for file in files:
    image = Image.open(file)
    info = {
      'size'  : image.size,
      'color' : image.mode,
      'format': image.format,
      'info'  : image.info
    }
    #print(info)
    print(image._getexif())
    #createThumbnail(file, image.size)

# 썸네일 이미지 만들기
def createThumbnail(file, size):
  to_size = (size[0]*0.1, size[1]*0.1) # 썸네일 이미지 크기
  drv = os.path.splitdrive(file) # 드라이브, 경로/파일명
  path = os.path.split(file) # 경로, 파일명
  name = os.path.basename(file)
  ext = os.path.splitext(name)
  to_name = ext[0]+'_thumbnail'+ext[1]

  to_path = os.path.join(dir, 'thumbnail')
  to_file = os.path.join(to_path,to_name)
  if not os.path.exists(to_path): os.makedirs(to_path)
  im = Image.open(file)
  im.thumbnail(to_size, Image.ANTIALIAS)
  im.save(to_file)
  print('create thumbnail success - '+to_file)

##################
info()