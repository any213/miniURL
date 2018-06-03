from flask import redirect,render_template, request
from models import db
from util import short_maker as sm
import random
import logging as log

urlform=["https://","http://"]

def send_org_url(org_url):
    if any(s in org_url for s in urlform):
        return redirect(org_url, code=301)
    return redirect(urlform[1]+org_url, code=301)

def send_sht_url(sht_url):
    addr = request.host_url+sht_url
    return render_template("get_sht.html",result=addr)


def get_org_url(sht_url):
    #db에서 숏유알엘로 진짜검색후 리다이렉션
    #1. 캐시 사용시 캐시 검색
    #2. 캐시 미사용시 디비 검색
    log.debug("get_org_url=>"+sht_url)
    m = db.miniURL_db()
    org_url = m.get_cache(sht_url)
    if org_url != ""and org_url is not None and org_url!= "None":
        return send_org_url(org_url)
    org_url = m.get_org_url(sht_url)
    if org_url != ""and org_url is not None and org_url!= "None":
        return send_org_url(org_url)
    else :
        log.error("get_org_url=>")
        return render_template("get_err.html",result="등록되지 않은 url 정보입니다.")
    return

def get_sht_url(org_url):
    #있는건지 검사
    #있으면 돌려주기
    #없으면 진짜를 인코딩하여 숏만들고 디비에넣고 캐시에 넣기
    log.debug("get_org_url=>"+org_url)
    m = db.miniURL_db()
    sht_url = m.get_sht_url(org_url)
    if sht_url != "" and sht_url is not None and sht_url!= "None":
        return send_sht_url(sht_url)
    sht_url = sm.make_short(org_url)[:8]
    exdata =m.get_org_url(sht_url)
    if exdata == None:
        temp_org_url=org_url
        while(exdata!=None):
            temp_org_url = temp_org_url+str(random.random(1,10))
            raw_sht_url = sm.make_short(temp_org_url)
            exdata = m.get_org_url(raw_sht_url)
    m.set_url(org_url, sht_url)
    return send_sht_url(sht_url[:8])

