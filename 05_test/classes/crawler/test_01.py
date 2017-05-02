'''
망가를 다운로드 받자
'''
import urllib.request, os, time
from bs4 import BeautifulSoup

class Crawler:
  def page1(self, dir, url, no):
    start_time = time.time()
    hdr = {'User-Agent':'Mozilla/5.0', 'referer':'https://yajoa.net'}
    req = urllib.request.Request(url,headers=hdr)
    data = urllib.request.urlopen(req).read()

    bs = BeautifulSoup(data, 'html.parser')
    img = bs.find_all('img')

    idx = 0
    path = 'D:/P01_Download/00_망가/' + dir + '/'
    if not os.path.exists(path):
      os.makedirs(path)

    for ele in img:
      val = ele.get('class')
      # <img alt="NXf9VyJ.jpg" class="img-tag img-tag pointer" content="http://i.imgur.com/NXf9VyJ.jpg" itemprop="image" src="http://i.imgur.com/NXf9VyJ.jpg" style="width:690px;"/>
      if val is not None and val[0] == 'img-tag':
        idx = idx + 1
        #print(ele)
        src = ele.get('src')
        fileName = path + no + '-'+self.getFileName(idx) + '.jpg'
        f = open(fileName, 'wb')
        try:
          #print(src)
          hdr['referer']=src
          img_req = urllib.request.Request(src,headers=hdr)
          f.write(urllib.request.urlopen(img_req).read())
        except:
          print('############# except: download failed - '+src)
        finally:
          f.close()
    print("Download Elapsed %.02f sec " % (time.time()-start_time), ' : count',idx)
    return idx

  # 파일명 시퀀스 구하기
  def getFileName(self, no):
    no = str(no)
    for i in range(len(no), 3):
      no = '0'+no
    return no

  #
  def download_02(self):
    dir = "02_리얼섹스-체험담"
    for no in range(1, 25):
      wr_id = str(154 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=2"
      c.page1(dir, url, c.getFileName(no))

  def download_03(self):
    dir = "03_타인의 아내"
    for no in range(1, 6):
      wr_id = str(166 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=1"
      c.page1(dir, url, c.getFileName(no))

  # 159 - 157
  def download_04(self):
    cnt = 3
    dir = "04_마조 마마"
    for no in range(1, (cnt+1)):
      wr_id = str(160 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=1"
      print(dir, ' - ', no, '/', cnt, '권을 다운로드중 입니다.')
      c.page1(dir, url, c.getFileName(no))
    print(dir,' download completed.')

  # 156 - 154
  def download_05(self):
    cnt = 3
    dir = "05_누나의 소망"
    for no in range(1, (cnt+1)):
      wr_id = str(157 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=1"
      print(dir, ' - ', no, '/', cnt, '권 다운로드... - ',url)
      c.page1(dir, url, c.getFileName(no))
    print(dir,' download completed.')

  # 128 127
  def download_06(self):
    cnt = 2
    dir = "06_타락 악마"
    for no in range(1, (cnt+1)):
      wr_id = str(129 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=1"
      print(dir, ' - ', no, '/', cnt, '권 다운로드... - ',url)
      c.page1(dir, url, c.getFileName(no))
    print(dir,' download completed.')

  # 126 125
  def download_07(self):
    cnt = 4
    dir = "07_행복을 주는 섹스"
    for no in range(1, (cnt+1)):
      wr_id = str(127 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=3"
      print(dir, ' - ', no, '/', cnt, '권 다운로드... - ',url)
      c.page1(dir, url, c.getFileName(no))
    print(dir,' download completed.')

  # 121 117
  def download_08(self):
    cnt = 4
    dir = "08_여름날의 약속"
    for no in range(1, (cnt+1)):
      wr_id = str(122 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=3"
      print(dir, ' - ', no, '/', cnt, '권 다운로드... - ',url)
      c.page1(dir, url, c.getFileName(no))
    print(dir,' download completed.')

  # 116
  def download_09(self):
    start_time = time.time()
    cnt = 4
    dir = "09_처녀 여교사 육단지 수업"
    for no in range(1, (cnt+1)):
      wr_id = str(117 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=3"
      print(dir, ' - ', no, '/', cnt, '권 다운로드... - ',url)
      c.page1(dir, url, c.getFileName(no))
    print("["+dir+"] Download Completed %.02f sec " % (time.time() - start_time), ' : count', cnt)

  # 112
  def download_10(self):
    start_time = time.time()
    cnt = 4
    dir = "10_에이치"
    for no in range(1, (cnt+1)):
      wr_id = str(113 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=3"
      print(dir, ' - ', no, '/', cnt, '권 다운로드... - ',url)
      c.page1(dir, url, c.getFileName(no))
    print("["+dir+"] Download Completed %.02f sec " % (time.time() - start_time), ' : count', cnt)

  # 108
  def download_11(self):
    start_time = time.time()
    cnt = 2
    dir = "11_거부할수없는 미끈 엄마"
    for no in range(1, (cnt+1)):
      wr_id = str(109 - no)
      url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=3"
      print(dir, ' - ', no, '/', cnt, '권 다운로드... - ',url)
      c.page1(dir, url, c.getFileName(no))
    print("["+dir+"] Download Completed %.02f sec " % (time.time() - start_time), ' : count', cnt)
    print("")

  # 108
  def download_12(self):
    start_time = time.time()

    lists = [
      #{'page': 106, 'cnt': 3, 'dir': '12_비이커 속의 욕망'},
      #{'page': 103, 'cnt': 1, 'dir': '13_나츠미 마마'},
      #{'page': 102, 'cnt': 1, 'dir': '14_트리플 키스'},
      #{'page': 101, 'cnt': 1, 'dir': '15_한지붕 아래'},
      #{'page': 100, 'cnt': 4, 'dir': '16_찰랑 찰랑'},
      #{'page': 96, 'cnt': 3, 'dir': '17_젖삐져 나온 누나'},
      #{'page': 91, 'cnt': 4, 'dir': '18_사랑 빛깔로 우는 목소리'},
      #{'page': 87, 'cnt': 4, 'dir': '19_그립고 보고 싶어서'},
      #{'page': 83, 'cnt': 3, 'dir': '20_너를 갖고 싶어'},
      #{'page': 80, 'cnt': 4, 'dir': '21_욕정녀'},
      #{'page': 74, 'cnt': 4, 'dir': '22_비너스 랩소드'},
      #{'page': 70, 'cnt': 4, 'dir': '23_응석 부리는 여자'},
      #{'page': 66, 'cnt': 4, 'dir': '24_여동생은 나의 아내'},
      #{'page': 62, 'cnt': 3, 'dir': '25_게임은 프로 섹스는 아마추어'},
      #{'page': 59, 'cnt': 2, 'dir': '26_지독한 첫 경험'},
      #{'page': 57, 'cnt': 3, 'dir': '27_욕정 유부녀'},
      #{'page': 54, 'cnt': 10, 'dir': '28_남의 아내'},
      #{'page': 44, 'cnt': 1, 'dir': '29_슬라임의 장난감'},
      #{'page': 43, 'cnt': 1, 'dir': '30_교간 합숙'},
      #{'page': 42, 'cnt': 4, 'dir': '31_노예 여교사 유리코'},
      #{'page': 38, 'cnt': 4, 'dir': '32_거유 파워'},
      #{'page': 34, 'cnt': 4, 'dir': '33_포토밭 연인들'},
      #{'page': 30, 'cnt': 4, 'dir': '34_만개 을녀'},
      #{'page': 26, 'cnt': 4, 'dir': '35_프리티 걸'},
      #{'page': 23, 'cnt': 4, 'dir': '36_러브 어페어'},
      #{'page': 19, 'cnt': 3, 'dir': '37_커밍 이벤트'},
      #{'page': 16, 'cnt': 6, 'dir': '38_외로운 여인'},
      {'page': 10, 'cnt': 1, 'dir': '39_배덕처'},
      {'page': 9, 'cnt': 1, 'dir': '40_헤프닝'},
      {'page': 8, 'cnt': 1, 'dir': '41_친구의 엄마 따묵기'},
      {'page': 7, 'cnt': 2, 'dir': '43_몸이 뜨거운 여인'},
      {'page': 5, 'cnt': 5, 'dir': '44_기분이 좋아지는 섹스'},
    ]

    for list in lists:
      for no in range(1, (list['cnt']+1)):
        wr_id = str(list['page'] - no + 1)
        if wr_id=='77': wr_id='76'
        url = "https://yajoa.net/bbs/board.php?bo_table=Adultmanga&wr_id=" + wr_id + "&page=6"
        print(list['dir'], ' - ',no,'/', list['cnt'], '권 다운로드... - ', url)
        c.page1(list['dir'], url, c.getFileName(no))
      print("[" + list['dir'] + "] Download Completed %.02f sec " % (time.time() - start_time), ' : count', list['cnt'])




###############################################
if __name__ == "__main__":
  c = Crawler()
  c.download_12()
  #c.download_11()
  #c.download_10()
  #c.download_09()
  #c.download_08()
  #c.download_07()
  #c.download_06()
  #c.download_05()
  #c.download_04()
  #c.download_03()
  #c.download_02()




  #for list in lists:
  #  idx = c.page1(dir, list, idx)