'''
description : 수동으로 특정 URL에 망가를 다운로드한다.
http://s0106.mytoon1.com/bbs/board.php?bo_table=yasisi2&sca=&sop=and&sfl=wr_subject&stx=%EB%89%B4+%ED%9E%88%EB%A1%9C%EC%9D%B8
http://alltoon.org/bbs/board.php?bo_table=adt2&page=2
date : 2018.01.06
'''
import urllib.request, os, time
from bs4 import BeautifulSoup

class Crawler:
  def download(self, param):
    start_time = time.time()
    domain = param["url"][param["url"].find('//')+2:]
    domain = domain[:domain.find('/')]

    start_time = time.time()
    hdr = {'User-Agent': 'Mozilla/5.0', 'referer': domain}
    req = urllib.request.Request(param["url"], headers=hdr)
    data = urllib.request.urlopen(req).read()

    bs = BeautifulSoup(data, 'html.parser')
    img = bs.find_all('img')

    # title( h1 > id[bo_v_title]
    title = bs.find('h1',{'id':'bo_v_title'}).text.strip()

    # download directory check
    title = title.replace('?','')
    title = title.replace('.', '')
    title = title.replace(':', '')
    #title = '오네코레(お姉コレ)#2'
    dir = param['path'] + title
    if not os.path.exists(dir):
      os.makedirs(dir)

    # images download
    self.write(hdr, img, dir)

    print("Download Elapsed %.02f sec " % (time.time() - start_time), ' : '+title)

  def write(self, hdr, img, dir):
    page_no = 0
    file_name_src = dir + '/' + param['idx'] + "-"
    for ele in img:
      val = ele.get('class')
      if val is not None and val[0] == 'img-tag':
        page_no = page_no + 1
        src = ele.get('src')
        ext = src[src.rindex('.'):]
        file_name = file_name_src + self.getPageNo(page_no)+ ext
        f = open(file_name, 'wb')
        try:
          hdr['referer'] = src
          img_req = urllib.request.Request(src, headers=hdr)
          f.write(urllib.request.urlopen(img_req).read())
        except:
          print('############# except: download failed - ' + src)
        finally:
          f.close()

  def getPageNo(self, no):
    no = str(no)
    for i in range(len(no), 3):
      no = '0'+no
    return no

  def download_list(self, param, list):
    start_time = time.time()
    print( '[download start] total : '+str(len(list)) )
    for wr_id in list:
      param['url'] = 'https://s0105.mytoon1.com/bbs/board.php?bo_table=yasisi3&wr_id='+str(wr_id)
      self.download(param)

    print("Download Elapsed %.02f sec " % (time.time() - start_time))

  def download_range(self, param, idx_start, idx_end, bo_table):
    idx_end += 1
    start_time = time.time()
    print( '[download start] total : '+str(idx_end-idx_start) )
    for wr_id in range(idx_start, idx_end):
      param['url'] = 'https://s0105.mytoon1.com/bbs/board.php?bo_table='+bo_table+'&wr_id='+str(wr_id)
      self.download(param)

    print("Download Elapsed %.02f sec " % (time.time() - start_time))

if __name__ == "__main__":
  param = {
    'url' : 'https://s0105.mytoon1.com/bbs/board.php?bo_table=yasisi3&wr_id=589',
    'path' : 'D:/P01_Download/00_망가/만화책_03/',
    'idx' : 'A01'
  }

  cl = Crawler()
  # 단권 다운로드
  #cl.download(param)
  
  # 리스트 배열로 시리즈 다운로드
  #cl.download_list(param, list = [2638,2637,2636,2635,2634,2633,2632,2631]) # 스콜
  #cl.download_list(param, list=[2419,2418,2417,2416,2415,2414,2413,2412,2411,2410,2409,2408,2407]) # 노출처 레이코
  #cl.download_list(param, list=[2426,2425,2424,2423,2422,2421,2420])  # 국립유부녀학원
  #cl.download_list(param, list=[2518,2436,2435,2434,2433,2432,2431,2430,2429,2428,2427])  # 뉴 히로인
  
  # 인덱스로 시리즈 다운로드
  #cl.download_range(param, 576, 589, 'yasisi3')  # 엄마실격-앨리트모자의M돼지
  #cl.download_range(param, 2373, 2379, 'yasisi3')  # 아네모네
  #cl.download_range(param,2392,2400, 'yasisi3' )  # 수치의 밀월
  #cl.download_range(param,2353, 2362, 'yasisi3')  # 거유와 빈유
  #cl.download_range(param,2347,2352, 'yasisi3')  # 유혹 오피스
  #cl.download_range(param,2293,2302, 'yasisi3' )  # 이웃집 사모님의 비밀이야기
  #cl.download_range(param,2281,2292, 'yasisi3' )  # 하츠키 카오루의 참을 수 없는 이야기
  #cl.download_range(param,2213, 2222, 'yasisi3')  # H한 체험 알려드립니다.
  #cl.download_range(param,154, 165, 'yasisi3')  # 신 정말로 있었던 H한 체험
  #cl.download_range(param,145, 152, 'yasisi3')  # 신 정말로 있었던 H한 체험
  #cl.download_range(param,2170, 2176, 'yasisi3')  # 유부녀와 센세이
  #cl.download_range(param,2031,2039, 'yasisi3' )  # 유부녀 에미의 부탁해
  #cl.download_range(param,1954,1962, 'yasisi3' )  # 스필트 밀트
  #cl.download_range(param,1754,1763, 'yasisi3' )  # 산제물인엄마
  #cl.download_range(param,1709,1716, 'yasisi3' )  # 오가와가의 모녀
  #cl.download_range(param,1684,1693, 'yasisi3' )  # 연상의 여동생
  #cl.download_range(param,2067,2076, 'yasisi2' )  # 근친연인
  #cl.download_range(param,1675,1689, 'yasisi2')  # 모간
  #cl.download_range(param,1,9, 'yasisi2')  # 가정의 사정
  #cl.download_range(param,10,17, 'yasisi2')  # 음란한 소질
  #cl.download_range(param,1205,1212, 'yasisi2')  # 엄마를 거부하지 못하는 나
  #cl.download_range(param,71,80, 'yasisi2')  # 선정적 가족
  #cl.download_range(param,103,116, 'yasisi2')  # 모녀 상간
  #cl.download_range(param,136,145, 'yasisi2')  # 근친강간
  #cl.download_range(param,157,167, 'yasisi2')  # 동정백서
  #cl.download_range(param,187,194, 'yasisi2')  # 누나교생
  #cl.download_range(param,226,233, 'yasisi2')  # 메비우스
  #cl.download_range(param,298,308, 'yasisi2')  # 엄마에게 빠지다
  #cl.download_range(param,289,297, 'yasisi2')  # 에로 누나
  #cl.download_range(param,280,288, 'yasisi2')  # 엄마가 간다.
  #cl.download_range(param,319,328, 'yasisi2')  # 음란한 엄마
  #cl.download_range(param,1610,1618, 'yasisi2')  # 음란한 엄마 사춘기의 나
  #cl.download_range(param,329,338, 'yasisi2')  # 삼매일체
  #cl.download_range(param,339,349, 'yasisi2')  # 러브레터
  #cl.download_range(param,350,360, 'yasisi2')  # 엄마젖짜기
  #cl.download_range(param,361,370, 'yasisi2')  # 엄마는 천연의 맛
  #cl.download_range(param,371,378, 'yasisi2')  # 아네이모
  #cl.download_range(param,379,389, 'yasisi2')  # CHANGE
  #cl.download_range(param,387,397, 'yasisi2')  # 카나코와 삼촌
  #cl.download_range(param,410,416, 'yasisi2')  # 나의 모친
  #cl.download_range(param,417,426, 'yasisi2')  # 데이지
  #cl.download_range(param,427,436, 'yasisi2')  # 엄마강간
  #cl.download_range(param,455,463, 'yasisi2')  # 음모교육일지
  #cl.download_range(param,464,471, 'yasisi2')  # 누나의 부탁
  #cl.download_range(param,472,480, 'yasisi2')  # 어느새인가 소녀는
  #cl.download_range(param,481,485, 'yasisi2')  # 비밀신호
  #cl.download_range(param,486,495, 'yasisi2')  # 시스터즈엣찌
  #cl.download_range(param,501,506, 'yasisi2')  # 엄마에서 연인으로 1권
  #cl.download_range(param,496,500, 'yasisi2')  # 엄마에서 연인으로 2권
  #cl.download_range(param,507,509, 'yasisi2')  # 의모
  #cl.download_range(param,1317,1323, 'yasisi2')  # 데리마마
  #cl.download_range(param,1217,1217, 'yasisi2')  # 그런 이유로,알몸으로 엄마에게 부탁해 보았다
  #cl.download_range(param,510,511, 'yasisi2')  # 갑작스레
  #cl.download_range(param,514,515, 'yasisi2')  # 근친 상간 향연
  #cl.download_range(param,518,519, 'yasisi2')  # 모자상간
  #cl.download_range(param,516,516, 'yasisi2')  # 엄마를 따먹자
  #cl.download_range(param,524,533, 'yasisi2')  # 엄마를 따먹자
  #cl.download_range(param,517,517, 'yasisi2')  # 몰래 몰래
  #cl.download_range(param,520,523, 'yasisi2')  # 마지막 파일
  #cl.download_range(param,534,534, 'yasisi2')  # 엄마♡러브
  #cl.download_range(param,535,536, 'yasisi2')  # 엄마는 나의 인형이다
  #cl.download_range(param,537,538, 'yasisi2')  # 엄마의 애정
  #cl.download_range(param,539,548, 'yasisi2')  # 엄마그녀
  #cl.download_range(param,560,571, 'yasisi2')  # 누님들과 함께
  #cl.download_range(param,572,584, 'yasisi2')  # 여동생은 동인소녀
  #cl.download_range(param,585,593, 'yasisi2')  # 누나의 향기
  #cl.download_range(param,594,601, 'yasisi2')  # 067 누나의 몸에 흥미
  #cl.download_range(param,602,609, 'yasisi2')  # 마더 콤플렉스
  #cl.download_range(param,610,619, 'yasisi2')  # 육가
  #cl.download_range(param,627,637, 'yasisi2')  # 음모사육
  #cl.download_range(param,638,651, 'yasisi2')  # 염모
  #cl.download_range(param,652,660, 'yasisi2')  # 엄마실격 음침한 소년의 복수 하렘조교계획
  #cl.download_range(param,661,671, 'yasisi2')  # 073 엄마가 수정해줄게
  #cl.download_range(param,678,686, 'yasisi2')  # 음란성 쌍둥이
  #cl.download_range(param,687,690, 'yasisi2')  # S-에스
  #cl.download_range(param,691,698, 'yasisi2')  # 페라 퓨어
  #cl.download_range(param,699,706, 'yasisi2')  # 좋아해 좋아해
  #cl.download_range(param,222,225, 'yasisi2')  # 078 임신가족
  #cl.download_range(param,1102,1107, 'yasisi2')  # 섹스 뒤의 서로 사랑
  #cl.download_range(param,707,718, 'yasisi2')  # 정조관념 ZERO
  #cl.download_range(param,719,726, 'yasisi2')  # 081 카야 누나
  #cl.download_range(param,727,736, 'yasisi2')  # 오네코레
  #cl.download_range(param,737,748, 'yasisi2')  # 083 Positive
  #cl.download_range(param,749,755, 'yasisi2')  # 오프 더 레코드
  #cl.download_range(param,756,764, 'yasisi2')  # 마마x푹푹
  #cl.download_range(param,772,782, 'yasisi2')  # 발정은 하렘 노트
  #cl.download_range(param,783,792, 'yasisi2')  # 일그러진 사랑
  #cl.download_range(param,793,804, 'yasisi2')  # 패미콤
  #cl.download_range(param,805,813, 'yasisi2')  # 시이바의 또 다른 얼굴
  #cl.download_range(param,822,831, 'yasisi2')  # 시스터 천국
  #cl.download_range(param,832,840, 'yasisi2')  # 의부 유리코
  #cl.download_range(param,841,846, 'yasisi2')  # 모자의 늪
  #cl.download_range(param,847,857, 'yasisi2')  # 쇼타먹기
  #cl.download_range(param,858,869, 'yasisi2')  # 누나랑 여동생은 내 신부
  #cl.download_range(param,870,880, 'yasisi2')  # 거의 모든 누나는 H를 하고 싶어해
  #cl.download_range(param,881,891, 'yasisi2')  # 맘마미아
  #cl.download_range(param,892,895, 'yasisi2')  # 암컷숙모 미사오
  #cl.download_range(param,896,904, 'yasisi2')  # 핥아줄께요
  #cl.download_range(param,905,909, 'yasisi2')  # 피인금지구역
  #cl.download_range(param,910,912, 'yasisi2')  # 할아버지는 들어가면 안되요
  #cl.download_range(param,913,920, 'yasisi2')  # 우리집의 마마
  #cl.download_range(param,930,938, 'yasisi2')  # 여동생의 구멍
  #cl.download_range(param,939,945, 'yasisi2')  # Incest Taboo
  #cl.download_range(param,953,956, 'yasisi2')  # 자고있는 누나는 질내사정 섹스에 삼매경
  '''
  cl.download_range(param,957,959, 'yasisi2')  # 장모님이 거유니까 해버리자
  cl.download_range(param,960,962, 'yasisi2')  # 시게오 피버
  cl.download_range(param,963,965, 'yasisi2')  # 아내가 일하는 동안 장모가 목걸이하다
  cl.download_range(param,966,968, 'yasisi2')  # 쭉쭉빵빵 거유의 이모와 야한짓하자
  cl.download_range(param,969,981, 'yasisi2')  # 모자상담
  cl.download_range(param,996,1003, 'yasisi2')  # 마인드 오브 시스터즈
  cl.download_range(param,1004,1012, 'yasisi2')  # 오빠, 세상에서 제일 행복하게 해줄게
  cl.download_range(param,1013,1022, 'yasisi2')  # 모금상
  cl.download_range(param,1023,1028, 'yasisi2')  # 시아버지
  cl.download_range(param,1058,1072, 'yasisi2')  # 누나 느낌
  cl.download_range(param,1076,1078, 'yasisi2')  # 이모를 유혹하자
  cl.download_range(param,1093,1101, 'yasisi2')  # 손녀먹는 영감과 엄마윤간하기
  cl.download_range(param,1108,1115, 'yasisi2')  # 이런애로 만든건
  cl.download_range(param,1116,1125, 'yasisi2')  # 사랑투성이
  cl.download_range(param,1138,1149, 'yasisi2')  # 엄마의 구멍 쓰게 해 줘
  cl.download_range(param,1160,1167, 'yasisi2')  # 범하고싶은 기분
  cl.download_range(param,1182,1188, 'yasisi2')  # 시스 브라 Sister Brother
  cl.download_range(param,1189,1190, 'yasisi2')  # 親子羊
  cl.download_range(param,1191,1203, 'yasisi2')  # 잊지마
  cl.download_range(param,1214,1214, 'yasisi2')  # 엄마가 풀어준다
  cl.download_range(param,1215,1216, 'yasisi2')  # 엄마를 먹다
  cl.download_range(param,1222,1226, 'yasisi2')  # 엄마러브
  cl.download_range(param,1227,1234, 'yasisi2')  # 숙모를 먹다
  cl.download_range(param,1264,1267, 'yasisi2')  # 128 내일부터의 우리들
  cl.download_range(param,1268,1279, 'yasisi2')  # 엄마먹기
  cl.download_range(param,1280,1284, 'yasisi2')  # Dear My Master
  cl.download_range(param,1285,1293, 'yasisi2')  # 미다라 북스
  cl.download_range(param,1294,1305, 'yasisi2')  # 이지리몬
  cl.download_range(param,1306,1316, 'yasisi2')  # 트로피컬 모녀
  cl.download_range(param,1331,1338, 'yasisi2')  # 여장남자
  cl.download_range(param,1339,1347, 'yasisi2')  # 누님 천국
  cl.download_range(param,1369,1369, 'yasisi2')  # 유부녀 누나
  cl.download_range(param,1370,1370, 'yasisi2')  # 누나 뺏기
  cl.download_range(param,1472,1476, 'yasisi2')  # 母子の虜
  cl.download_range(param,1506,1518, 'yasisi2')  # 아이요쿠
  cl.download_range(param,1528,1536, 'yasisi2')  # 심술쟁이가 사랑을 하여
  cl.download_range(param,1549,1555, 'yasisi2')  # 私、思春期チ
  cl.download_range(param,1630,1637, 'yasisi2')  # 큰어머니
  cl.download_range(param,1638,1648, 'yasisi2')  # 음즙자매
  cl.download_range(param,1649,1655, 'yasisi2')  # 성적인 그녀
  cl.download_range(param,195,203, 'yasisi2')  # 누나의 가슴
  '''




  cl.download_range(param,1699,1706, 'yasisi2')  # 음화백탁
  cl.download_range(param,1707,1714, 'yasisi2')  # 내살에 무리지어 모여
  cl.download_range(param,1715,1725, 'yasisi2')  # 오빠정액
  cl.download_range(param,1726,1737, 'yasisi2')  # 사랑꿀 캐러멜리제
  cl.download_range(param,1738,1744, 'yasisi2')  # 우리들의 금기
  cl.download_range(param,1745,1752, 'yasisi2')  # 교절유부녀
  cl.download_range(param,1775,1785, 'yasisi2')  # 자모간계
  cl.download_range(param,1870,1886, 'yasisi2')  # 독처클럽
  cl.download_range(param,1905,1908, 'yasisi2')  # 나의 의붓
  cl.download_range(param,1909,1917, 'yasisi2')  # 연밀 프레이그런스
  cl.download_range(param,1942,1954, 'yasisi2')  # 그녀느낌
  cl.download_range(param,1955,1962, 'yasisi2')  # Mamazuri
  cl.download_range(param,177,186, 'yasisi2')  # 마더 룰
  cl.download_range(param,1973,1983, 'yasisi2')  # 음탕한 웃음의 간호사
  cl.download_range(param,2542,2552, 'yasisi2')  # 빠져드는 백일몽
  '''
  '''
  #cl.download_range(param,, ,'yasisi2')  #
  #cl.download_list(param, list=[])  #

'''
http://s0115.mytoon1.com/bbs/board.php?bo_table=yasisi2
http://alltoon.org/bbs/board.php?bo_table=adt2&page=58&page=54
http://alltoon.org/bbs/board.php?bo_table=adt2&page=2
  '''