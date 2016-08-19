#!/usr/bin/env python
# coding:utf-8
# Created by jethrolin on 2016/8/19

import urllib2
import json
import time, datetime

oneday = datetime.timedelta(days=1)
yesterday = datetime.date.today() - oneday
date = time.strftime('%Y-%m-%d')

_parms = r'http://anm.cfd2.oa.com/cgi-bin/netman2.0/core/getStructedFeatureData.cgi?data=[{"business_name":"7层负载均衡L7","days":1,"date":"%s","query":[{"module_mark":"","module":"L7_RS_STATS","target":"succ_rate","type":"","dimens":{"set":"stgw-深圳-福永-set1-http"}}]}]&user_id=82&user_rtx=rajhuang'
parms = _parms % (yesterday)
html = urllib2.urlopen(parms)

# html = urllib2.urlopen(r'http://anm.cfd2.oa.com/cgi-bin/netman2.0/core/getStructedFeatureData.cgi?data=[{"business_name":"7层负载均衡L7","days":1,"date":"2016-08-18","query":[{"module_mark":"","module":"L7_RS_STATS","target":"succ_rate","type":"","dimens":{"set":"stgw-深圳-福永-set1-http"}}]}]&user_id=82&user_rtx=rajhuang')

dict_lbs = json.loads(html.read())
lbs_result = dict_lbs['result'][0]['dataValue']
# print lbs_result[0]['value']
# print type(lbs_result[0])

total = 0
for i in lbs_result:
    # print(i)['value']
    total += (i)['value']

succ_rate = total / 1440
print yesterday,  succ_rate
