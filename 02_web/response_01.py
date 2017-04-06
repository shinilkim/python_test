# python3
import sys
import urllib
import urllib.error
import urllib.request


def req_01():
	if len(sys.argv) == 1:
		url = 'http://www.naver.com'
	else:
		url = sys.argv[1]

	try:
		info = urllib.request.urlopen(url).info()
		print(info)
	except urllib.error.URLError as e:
		print('req_01 exception: ',e)


if __name__ == "__main__":
	req_01()
