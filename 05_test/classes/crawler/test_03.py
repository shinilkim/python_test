'''
야설을 다운로드 받자
'''
import urllib.request, os, time, glob, logging
from bs4 import BeautifulSoup

class Crawler3:
  FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
  logger = logging.getLogger('Crawler3')

  def page1(self, url, wr_id):
    start_time = time.time()
    hdr = {'User-Agent':'Mozilla/5.0', 'referer':'https://yajoa.net'}
    req = urllib.request.Request(url,headers=hdr)
    data = urllib.request.urlopen(req).read()

    bs = BeautifulSoup(data, 'html.parser')
    #img = bs.find_all('img')
    #dir = wr_id+'_'+bs.select('div > h1')[0].text
    # src = ele.get('src')
    path = 'D:/P01_Download/01_야설/01_춘자넷/'
    if not os.path.exists(path):
      os.makedirs(path)

    f = None
    verbose = False

    try:
      try:
        title = wr_id + '-' + bs.select('header > #bo_v_title')[0].text.strip() + '.txt'
        title = title.replace('(淫亂丈母:근친의 덫)','-')
        title = title.replace(' (부제: 사랑하는 나의 아들)','')
        fileName = path + title
        content = bs.find('div', {'id': 'bo_v_con'}).text
      except IndexError as e:
        self.logger.error('['+wr_id+'] 삭제된 게시물입니다. > Error: ',e)
        return False

      if os.path.exists(fileName):
        self.logger.error('['+wr_id+'] 이미 존재하는 파일 입니다.')
        return False

      f = open(fileName, 'w', encoding='UTF-8', newline='')
      f.write(content)
      verbose = True
    except UnicodeEncodeError as e:
      print('['+wr_id+'] except: download failed - ' + title)
      self.logger.error('Exception: ',e)
    except:
      self.logger.error('['+wr_id+'] except: download failed - '+title)
      f = open(fileName, 'w')
      f.write(content)
    finally:
      if f is not None:
        f.close()

    if verbose:
      print("Download Elapsed %.02f sec " % (time.time()-start_time), '{fileName:',title,'}')

  #
  def download(self):
    start_time = time.time()
    cnt = 0
    pageNo = 1873
    for no in range(0, (pageNo-1)):
      wr_id = str(pageNo - no)
      if wr_id in ['0']:
        url = "https://www.chunja19.net/bbs/board.php?bo_table=ya01&wr_id="+wr_id
        #print(str(no)+'/'+str(pageNo)+ ' 다운로드... - ',url)
        c.page1(url, wr_id)
        cnt = cnt + 1
    print("["+wr_id+"] Download Completed %.02f sec " % (time.time() - start_time), ' : count', cnt)

###############################################
if __name__ == "__main__":
  c = Crawler3()
  c.download()
