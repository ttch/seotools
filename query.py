# *.* coding=utf-8 *.*

from bs4 import BeautifulSoup

import os
import string
import urllib
import argparse

def baidu_query(pageindex,keyword):
	url = "http://www.baidu.com/s?wd={1}&pn={0}&oq={1}&tn=baiduhome_pg&ie=utf-8&usm=2&rsv_idx=2&rsv_pq=c82c13df0006bbb0&rsv_t=9891om1wMSOGU1XzMbDpArzyTmGN9a%2FYlSRk9wQUudP4fAMh0rR%2Bg8A1g%2F3GKpmwCCkk".format(pageindex,urllib.quote_plus(keyword))
	output = os.popen("curl \"" + url + "\"")
	res = output.read()
	print "搜索到 > {0}".format(pageindex)

	if( res.find("aiysea") > 0):
		print "搜索到了"
		print "排名在{0}页".format(pageindex / 10)
		return True
	return False

def main():

	parser = argparse.ArgumentParser(description="baidu query ranking command though by keyword")
	parser.add_argument('keyword', metavar='keyword', type=str, nargs='+', help='an string for the keyword')

	args = parser.parse_args()
	print "开始工作"
	for x in range(10,1000,10):
		if baidu_query(x,args.keyword[0]) :
			break
main()
