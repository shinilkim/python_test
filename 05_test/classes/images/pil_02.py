'''
사진 파일명 일괄 변경하기
'''
import glob, os
from PIL import Image
from PIL.ExifTags import TAGS

class MyImage:
  dir = None
  # 생성자
  def __init__(self, dir):
    self.dir = dir

  # 파일명 변경(제조사모델명_yyyy.mm.dd-hhmiss.파일확장자명)
  def rename(self):
    files = glob.glob(os.path.join(self.dir, "*.*"))
    cnt_target = len(files)
    cnt_save = 0
    cnt = 1
    for file in files:
      ctime = self.getCtime(file)
      name = os.path.basename(file)
      ext = os.path.splitext(name)
      tag = self.getTags(file)
      to_file_name = os.path.join(self.dir, tag['Model'].strip()+'_'+str(cnt)+'_'+self.getTargetFileName(ctime)+ext[1])
      cnt = cnt + 1
      if os.path.isdir(self.dir):
        #print(to_file_name)
        os.rename(file, to_file_name)
        cnt_save = cnt_save + 1
    print('전체 파일명 변경 건수 : ',cnt_save,'/',cnt_target)

  # 변경할 파일명
  def getTargetFileName(self, ctime):
    t_ctime = ctime[0:4]+ctime[5:7]+ctime[8:10]+"_"+ctime[11:13]+ctime[14:16]+ctime[17:]
    return t_ctime

  # 이미지 생성일시
  def getCtime(self, file):
    info = Image.open(file)._getexif()
    ctime = info[0x9003]
    return ctime

  # 이미지 속성
  def getTags(self, file):
    ret = {}
    info = Image.open(file)._getexif()
    for tag, value in info.items():
      decoded = TAGS.get(tag, tag)
      ret[decoded] = value
      #print(decoded, value)

    return ret

##################
if __name__ == '__main__':
  dir = 'C:/Users/shinil.kim/Pictures/Camera Roll/SLT-A55V';
  image = MyImage(dir)
  image.rename()