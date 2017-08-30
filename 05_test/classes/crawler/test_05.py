'''
망가를 다운로드 받자
'''
import urllib.request, os, time, glob
from bs4 import BeautifulSoup

class Crawler2:
  def page1(self, url, no, wr_id):
    start_time = time.time()
    hdr = {'User-Agent':'Mozilla/5.0', 'referer':url}
    req = urllib.request.Request(url,headers=hdr)
    data = urllib.request.urlopen(req).read()

    bs = BeautifulSoup(data, 'html.parser')
    img = bs.find_all('img')

    idx = 0
    path = 'D:/P01_Download/02_야사/01_몰카/'
    if not os.path.exists(path):
      os.makedirs(path)

    for ele in img:
      val = ele.get('class')
      #<img border="0" src="https://1.bp.blogspot.com/-zCki_eQNCAY/WPhXFOdY8II/AAAAAAAAc3g/r1usKv8hGbIpdbxZidmvjRqACQcqAyn5gCLcB/s1600/001.jpg" style="cursor: move;"/>
      #print(val[0])
      if val is not None and val[0] == 'img-tag':
      #if self.isTarget(ele):
        idx = idx + 1
        #print(ele)
        src = ele.get('src')
        fileName = path + no + '-'+self.getFileName(idx) + '.jpg'
        f = open(fileName, 'wb')
        try:
          src = src.replace("http:","https:")
          #print(src)
          hdr['referer']=src
          img_req = urllib.request.Request(src,headers=hdr)
          f.write(urllib.request.urlopen(img_req).read())
        except:
          print('############# except: download failed - '+src)
        finally:
          f.close()
    print("Download Elapsed %.02f sec " % (time.time()-start_time), ' : {count:',idx, ', dir:',dir,'}')
    return idx

  # filter
  def isTarget(self, ele):
    verbose = False
    upper = str(ele).upper()
    src = ele.get('src')
    if '.JPG' in upper and ele.get('alt') is None or '.JPG' in str(ele.get('alt')).upper():
      print('Y : ', ele)
      verbose = True
    elif 'http://i1.media.daumcdn.net' in src or 'uf.daum.net/image' in src:
      print('Y : ',ele)
      verbose = True
    elif ele.get('class') is not None and 'content-image' in ele.get('class'):
      print('Y : ',ele)
      verbose = True
    else:
      print('N : ', ele)
    val = ele.get('style')
    return verbose

  # 1 507
  def download_test(self):
    start_time = time.time()
    cnt = 0
    for no in range(1, 507):
      wr_id = str(no)
      if no != 0:
        cnt = cnt + 1
        url = "https://avnana.com/bbs/board.php?bo_table=dt04&wr_id="+wr_id
        print(wr_id, ' - ', no, '/', cnt, ' 다운로드... - ',url)
        c.page1(url, c.getFileName(no), wr_id)
    print("["+wr_id+"] Download Completed %.02f sec " % (time.time() - start_time), ' : count', cnt)

  # 108
  def download(self):
    start_time = time.time()
    cnt = 591
    for no in range(0, (cnt+1)):
      wr_id = str(857 - no)
      url = "https://mooya7.net/bbs/board.php?bo_table=manga&wr_id="+wr_id
      print(wr_id, ' - ', no, '/', cnt, '권 다운로드... - ',url)
      c.page1(url, c.getFileName(no), wr_id)
    print("["+wr_id+"] Download Completed %.02f sec " % (time.time() - start_time), ' : count', cnt)

  # 파일명 일괄변경
  def rename(self):
    pre_fix = "B"
    path = "D:/P01_Download/00_망가/만화책/"
    files = glob.glob( os.path.join(path, "*.zip") )
    src_cnt = len(files)
    tgt_cnt = 0
    for file in files:
      src_name = os.path.basename(file)
      tgt_name = pre_fix + src_name
      #print(src_name, " > ", tgt_name)
      if src_name[0:1] is not pre_fix:
        os.rename(file, os.path.join(path, tgt_name))
        tgt_cnt = tgt_cnt + 1
    print("총 {0}건 중에서 {1}건 파일명을 변경하였습니다.".format(src_cnt, tgt_cnt))

  # 디렉토리별 파일갯수 체크( 파일이 0개 인 디렉토리 찾기 )
  def checkDirectorySize(self):
    path = "D:/P01_Download/00_망가/"
    dirs = os.listdir(path)
    cnt_zero = 0
    for dir in dirs:
      files = glob.glob( os.path.join( os.path.join(path,dir), "*.*") )
      src_cnt = len(files)
      if src_cnt == 0:
        cnt_zero = cnt_zero + 1
        print(dir, " : ", src_cnt)

    if cnt_zero == 0:
      print("파일갯수가 0개인 디렉토리가 없습니다.")

  # 디렉토리를 검사해서 파일 갯수가 0개 인것을 찾아서 재작업한다.
  def retry(self):
    start_time = time.time()
    list = []
    path = "D:/P01_Download/00_망가/"
    dirs = os.listdir(path)
    for dir in dirs:
      files = glob.glob( os.path.join( os.path.join(path,dir), "*.*") )
      src_cnt = len(files)
      if src_cnt == 0:
        list.append(dir[0:3])

    cnt = 591
    for no in range(0, (cnt+1)):
      wr_id = str(857 - no)
      if wr_id in list:
        url = "https://mooya7.net/bbs/board.php?bo_table=manga&wr_id="+wr_id
        print(wr_id, ' - ', no, '/', cnt, '권 다운로드... - ',url)
        c.page1(url, c.getFileName(no), wr_id)
    print("["+wr_id+"] Download Completed %.02f sec " % (time.time() - start_time), ' : count', cnt)

  # 파일명 시퀀스 구하기
  def getFileName(self, no):
    no = str(no)
    for i in range(len(no), 3):
      no = '0'+no
    return no

###############################################
if __name__ == "__main__":
  c = Crawler2()
  #c.rename()
  #c.checkDirectorySize()
  #c.retry()
  c.download_test()
  #c.download()





  #for list in lists:
  #  idx = c.page1(dir, list, idx)