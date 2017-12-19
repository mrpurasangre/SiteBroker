import requests, re
from insides.colors import *
from insides.functions import _headers, write, Request

def cloudflare(website):
    write(var="#", color=c, data="Checking For Cloudflare In " + website)
    combo = ("http://api.hackertarget.com/httpheaders/?q=" + str(website))
    request = Request(combo, _timeout=3, _encode=True)
    if "cloudflare" in request:
        write(var="~", color=g, data="Cloudflare Found!\n")
        write(var="#", color=y, data="Trying To Bypass Cloudflare!\n")
        req = "http://www.crimeflare.biz/cgi-bin/cfsearch.cgi"
        pos = {'cfS': website}
        res = requests.post(req, headers=_headers, data=pos).text.encode('utf-8')
        reg = re.findall('<a href=\"http://www.crimeflare.biz/(.*?)">(.*?)</a>', res)
        lis = []
        for x in reg[1]:
            lis.append(x)
        real_ip = lis[1]
        request = Request("http://" + str(real_ip), _timeout=3, _encode=True)
        if not "cloudflare" in request.lower():
            write(var="@", color=c, data="Cloudflare Bypassed!")
            write(var="~", color=g, data="Real IP --> " + fc +str(real_ip))
        else:
            print("[!] Sorry! Cloudflare Wasn't Bypassed :')")
            write(var="!", color=r, data="Sorry! Cloudflare Wasn't Bypassed :')")
    else:
        write(var="$", color=b, data=website + " Is not using Cloudflare!")

# cloudflare("http://mukarramkhalid.com")