#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json


def readfile(f):
    # 打开文件
    fo = open(f, "rw+")
    print "文件名为: ", fo.name
    hostlist ,inslist ,fiplist ,fip_addrlist = [] ,[],[],[]
    for line in fo.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        #print "读取的数据为: %s" % line
        hostlist.append(line.split(" ")[0])
        inslist.append(line.split(" ")[1])
        fiplist.append(line.split(" ")[2])
        fip_addrlist.append(line.split(" ")[3])
    fo.close()
    return hostlist, inslist, fiplist, fip_addrlist


def writejson(f):
    with open(f, 'r+') as f:
        data = json.load(f)
        # hostlist=["test_env_online_hb_f4th_76_18","test_env_online_hb_f4th_76_10"]
        # inslist = ["ins1", "ins2"]
        # fiplist=["fip1", "fip2"]
        # fip_addrlist=["addr1", "addr2"]
        index = 0
        for host in hostlist:
            data[host]["jcs_maps"]["vol-instanceid"]["instanceid"] = inslist[index]
            data[host]["jcs_maps"]["vol-instanceid"]["fip"] = fiplist[index]
            data[host]["jcs_maps"]["vol-instanceid"]["fip_addr"] = fip_addrlist[index]
            index += 1
        f.seek(0)         # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()
    print "writejson done"


if __name__ == '__main__':
    hostlist, inslist, fiplist, fip_addrlist = readfile("ins.txt")
    print hostlist, inslist, fiplist, fip_addrlist
    writejson('data.json')
