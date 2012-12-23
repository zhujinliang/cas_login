#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhu Jinliang
# Email: zhujinlianghust#gmail.com
"""
This script is for login the network in Chinese Academy of Sciences.
"""
# 若第一次使用，注意先在user_data中的username和password中修改自己的信息


import sys
import urllib
import urllib2
import cookielib

user_data = {
			"username": "2012***", # 用你的密码替换2012*** 
			"password": "{TEXT}123456", # 用你的密码替换123456，注意保留{TEXT}
			"drop": "3", 
			"type": "1", 
			"n": "100" 
			}


def login():
	"""
	For user to login to web.
	"""
	host_url = "http://auth.ucas.ac.cn"

	# 设置一个cookie处理器，负责从服务器下载cookie到本地，并且发送请求时带上本地cookie
	cj = cookielib.LWPCookieJar()
	cookie = urllib2.HTTPCookieProcessor(cj)
	opener = urllib2.build_opener(cookie, urllib2.HTTPHandler)
	urllib2.install_opener(opener)
	# 打开一个登录主页面
	h = opener.open(host_url)
	return opener


def use_net(opener, post_data):
	"""
	When user login the web, he can use net.
	"""
	login_url = "http://auth.ucas.ac.cn/cgi-bin/do_login"
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:17.0) Gecko/20100101 Firefox/17.0', 
			'Accept': 'pplication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Referer': 'http://auth.ucas.ac.cn/'
			 }
	# 给post数据编码
	post_data = urllib.urlencode(post_data)
	# 发送POST请求
	request = urllib2.Request(login_url, post_data, headers)
	try:
		response = opener.open(request)
		print user_data['username'], u"你已经成功登录"
	except urllib2.URLError:
		print user_data['username'], u"登录失败"

def logout(opener, user_data):
	logout_url = 'http://auth.ucas.ac.cn/cgi-bin/do_logout'
	opener.open(logout_url)
	print user_data['username'], u"你已经成功登出"


if __name__ == "__main__":
	mode = {"0": "4",
			"1": "1",
			"2": "3",
			"3": "0"}
	display_mode = {"1": u"城域",
					"2": u"国内",
					"3": u"国际"}	
	help_info = """\
Usage: python cas_login.py [option]
You can only input one option.
Options are as follows:
0: 登出
1: 连接城域
2: 连接国内
3: 连接国际

For example: 
When you want to connect to international, input this:
python cas_login.py 3
When you want to logout, input this:
python cas_login.py 0
"""
	opener = login()
	if (len(sys.argv) < 2) or (len(sys.argv) > 2):
		print "Option Error. No action specified."
		print help_info
		sys.exit()
	elif sys.argv[1] != "0": 
	    if sys.argv[1] in mode:
			option = sys.argv[1]
			# Change connection mode
			user_data["drop"] = mode[option]
			print u"连接%s..."% display_mode[option]
			use_net(opener, user_data)
	else:
		print u"正在登出..."
		logout(opener, user_data)


