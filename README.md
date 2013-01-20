Overview
==============
This script is for UCAS student to login the network in Chinese Academy
of Sciences.

Notice
============
* 若第一次使用，注意先在user_data中的username和password中修改自己的信息。
* Python version: above 2.5 but lower than 3.
  If your Python version is above 3, it will report syntax error.
* In order to display the CAS picture, you need keep the cas.png picture in 
  the same directory with the script.
* In some Linux distribution, the desktop notification will be forced to 
  display 10 seconds. So, maybe the next notification is delayed.


How to use
==============
Run it like:
python cas_login.py option

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

Update History
============
Ver1.1, 20 Jan 2013
	* Add desktop notification when login or logout.

Ver1.0, 20 Dec 2012
	* Login and logout the UCAS net automatically.
	* Three mode to login the net.


Note
=============
Since the author's ability is limited, the software may exist many bugs
that I didn't have found and solve them. Please write them in a file, 
and send to me if possible. I'll appreciate your work very much!

Contact
============
If you want to make contact with me, mail me at this:
zhujinlianghust#gmail.com

-Zhu Jinliang, Dec 2012
