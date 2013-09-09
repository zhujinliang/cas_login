#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: Zhu Jinliang
# Email: zhujinlianghust#gmail.com
# Description: login the net in University of Chinese Academy of Sciences in command.

# 若第一次使用，注意先在user_data中的username和password中修改自己的信息

import sys
import os
import urllib
import urllib2
import cookielib

user_data = {
    'username': '2012***', # 用你的用户名替换2012*** 
    'password': '{TEXT}123456', # 用你的密码替换123456，注意保留{TEXT}
    'drop': '3', 
    'type': '1', 
    'n': '100' 
}

def notify(message):
    image = 'cas.png'
    notify_command = 'notify-send -i %s '%s''% (image, message)
    os.system(notify_command)


def login():
    '''
    For user to login to web.
    '''
    host_url = 'http://auth.ucas.ac.cn'

    cj = cookielib.LWPCookieJar()
    cookie = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    h = opener.open(host_url)
    return opener


def use_net(opener, post_data):
    '''
    When user login the web, he can use net.
    '''
    login_url = 'http://auth.ucas.ac.cn/cgi-bin/do_login'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:17.0) Gecko/20100101 Firefox/17.0', 
        'Accept': 'pplication/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://auth.ucas.ac.cn/'
     }

    post_data = urllib.urlencode(post_data)
    request = urllib2.Request(login_url, post_data, headers)
    try:
        response = opener.open(request)
        msg =  user_data['username'] + ' ' +  u'你已经成功登录'
        print msg
        notify(msg)
    except urllib2.URLError:
        msg =  user_data['username'] + ' ' + u'登录失败'
        print msg
        notify(msg)

def logout(opener, user_data):
    logout_url = 'http://auth.ucas.ac.cn/cgi-bin/do_logout'
    opener.open(logout_url)
    msg = user_data['username'] + ' ' + u'你已经成功登出'
    print msg
    notify(msg)


if __name__ == '__main__':
    mode = {
        '0': '4',
        '1': '1',
        '2': '3',
        '3': '0'
    }
    display_mode = {
        '1': u'城域',
        '2': u'国内',
        '3': u'国际'
    }  
    help_info = '''\
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
'''
    opener = login()
    if (len(sys.argv) < 2) or (len(sys.argv) > 2):
        print 'Option Error. No action specified.'
        print help_info
        sys.exit()
    elif sys.argv[1] != '0': 
        if sys.argv[1] in mode:
            option = sys.argv[1]
            # Change connection mode
            user_data['drop'] = mode[option]
            msg = u'连接%s...'% display_mode[option]
            print msg
            notify(msg)
            use_net(opener, user_data)
    else:
        print u'正在登出...'
        notify(u'正在登出...')
        logout(opener, user_data)
