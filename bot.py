#!/usr/bin/python 
import urllib2
import urllib
import sys
import time
import random
import re
import os
import string
from sys import platform

proxylisttext = "proxylist.txt" #nama list proxy

useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
                   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
                   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
                   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
                   'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
                   'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
                   'Microsoft Internet Explorer/4.0b1 (Windows 95)',
                   'Opera/8.00 (Windows NT 5.1; U; en)',
                   'amaya/9.51 libwww/5.4.0',
                   'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
                   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
                   'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
                   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
                   'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]',
                   "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
                   "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
                   "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
                   "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
                   "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
                   "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
                   "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
                   "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
                   "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"]
 
referer = ['http://google.com','http://bing.com','http://facebook.com','http://twitter.com']
link    = 'http://wonderwoman.team' #input link
 
def Autoclicker(proxy1):
    try:
        proxy = proxy1.split(":")
        print 'Proxy :',proxy1
        proxy_set = urllib2.ProxyHandler({"http" : "%s:%d" % (proxy[0], int(proxy[1]))})
        opener = urllib2.build_opener(proxy_set, urllib2.HTTPHandler)
        opener.addheaders = [('User-agent', random.choice(useragent)),
                                                ('Referer', random.choice(referer))]
        urllib2.install_opener(opener)
        f = urllib2.urlopen(link)
        if "http://wonderwoman.team" in f.read(): #input link
           print "[X] Link Berhasil Di Kunjungi ..."
        else:
           print "[X] Link gagal di kunjungi !"
           print "[X] Proxy failed"
 
    except:
           print "[X] Running ~ "
           pass
 
def loadproxy():
    try:
        get_file = open(proxylisttext, "r")
        proxylist = get_file.readlines()
        count = 0
        proxy = []
        while count < len(proxylist):
              proxy.append(proxylist[count].strip())
              count += 1
        for i in proxy:
            Autoclicker(i)
    except IOError:
        print "\n[-] Error: Check your proxylist path\n"
        sys.exit(1)
 
def main():
   print """

 /$$   /$$             /$$      /$$$$$$  /$$       /$$$$$$$   /$$$$$$  /$$$$$$$$
| $$$ | $$            | $$     /$$__  $$| $$      | $$__  $$ /$$__  $$|__  $$__/
| $$$$| $$  /$$$$$$  /$$$$$$  | $$  \ $$| $$$$$$$ | $$  \ $$| $$  \ $$   | $$   
| $$ $$ $$ |____  $$|_  $$_/  |  $$$$$$$| $$__  $$| $$$$$$$ | $$  | $$   | $$   
| $$  $$$$  /$$$$$$$  | $$     \____  $$| $$  \ $$| $$__  $$| $$  | $$   | $$   
| $$\  $$$ /$$__  $$  | $$ /$$ /$$  \ $$| $$  | $$| $$  \ $$| $$  | $$   | $$   
| $$ \  $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$  | $$| $$$$$$$/|  $$$$$$/   | $$   
|__/  \__/ \_______/   \___/   \______/ |__/  |__/|_______/  \______/    |__/   
                       Website Visitor w/Proxy
               Created by NathX - Suryanjana | @nat9h                                                                            

"""
   loadproxy()
if __name__ == '__main__':
        main()