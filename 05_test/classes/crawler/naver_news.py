'''
[네이비 뉴스 다운로드]
크러울러 참조 사이트 : https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
'''
import urllib.request, os, time, glob
from bs4 import BeautifulSoup

import time
from datetime import datetime, timedelta

class NaverNews:
  down_dir = "C:/Users/shinil.kim/Downloads/00_utorrent/Z03_ebook/text/naver_new/"
  gisa = ""
  def get_news_list_download(self, url, uri, list_size):
    start_time = time.time()
    for no in range(1,list_size):
      url2 = url + uri + str(no)
      hdr = {'User-Agent':'Mozila/5.0', 'referer':url2}
      req = urllib.request.Request(url2,headers=hdr)
      data = urllib.request.urlopen(req).read()

      bs = BeautifulSoup(data, 'html.parser')
      ########################################################
      if no == 1 :
        self.print_title(bs)
      ########################################################

      idx = 1
      ul = bs.find_all('li', {'class':'_rcount'})
      for li in ul:
        try:
          title = li.find("a").find("div").find("span").find("strong").text
        except AttributeError as e:
          #print(e)
          #print(li)
          title = li.find("span",{"class":"r_news_tit"}).find("strong").text
          print(title)
        finally:
          print()
          print("["+str(no)+"-"+str(idx)+"] "+title)

        title = str(no) +"_"+str(idx)+"_"+title
        href = url + li.find("a").get('href')
        self.news_download(title, href)
        idx = idx + 1
        #break

      datetime_now = datetime.now()  # datetime 형식으로 현재 시간 알아오기
      date = str(datetime_now)[0:10]
      file_name = "Naver_news_"+date+".txt"
      self.file_download(self.down_dir+file_name, self.gisa)

  def news_download(self, title, url):
    print(url)
    hdr = {'User-Agent': 'Mozila/5.0', 'referer': url}
    req = urllib.request.Request(url, headers=hdr)
    data = urllib.request.urlopen(req).read()
    bs = BeautifulSoup(data, 'html.parser')
    txt = None
    try:
      txt = bs.find("html").find("body").find(id="ct").find_all("div", {"class":"news_text"})
      txt = txt[0].find("font").text
    except AttributeError as e1: # 이미지가 있는 뉴스
      print('[AttributeError] '+str(e1))
      txt = bs.find_all(id="dic_area")[0].text
    except IndexError as e: # 동영상이 있는 뉴스
      print('[IndexError] '+str(e))
      txt = bs.find_all("div",{"id":"dic_area"})[0].text

    # 뉴스 개발 다운로드
    #file_name = self.down_dir+title+".txt"
    #self.file_download(file_name, txt)
    # 뉴스를 하나의 파일로 다운로드
    self.gisa = self.gisa+"\n\n["+title+"]\n"+txt


  def file_download(self, file_name, txt):
    try:
      if not os.path.exists(self.down_dir):
        os.makedirs(self.down_dir)
      f = open(file_name, 'w', encoding='UTF-8', newline='')
      f.write(txt)
    except TypeError as e:
      print(e)
    except OSError as e1:
      print(e1)

  def print_title(self, bs):
    div = "###############################################"
    print(div)
    print("# "+bs.title.name + " : " + bs.title.string)  # title 태그명 및 태그내용
    print(div)
    # print( bs.prettify()) # html 내용 출력력




if __name__ == "__main__":
  list_size = 8
  url = "http://m.news.naver.com"
  uri = "/newsflash.nhn?mode=LS2D&sid1=101&sid2=260&page="
  news = NaverNews()
  news.get_news_list_download(url, uri, list_size)


