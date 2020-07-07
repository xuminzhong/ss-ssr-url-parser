#!/usr/bin/python
# -*- coding: UTF-8 -*-

import base64

__author__ = 'Zhong'

'''
A method of decoding ss url and ssr url.
'''


def fill(b64):
    return b64 + "=" * (4 - len(b64) % 4)


def clear_ss(deb64):
    pos = deb64.rfind('#')
    return deb64[:pos] if pos > 0 else deb64


def ssr_parse(txt):
    # ssr://server:port:protocol:method:obfs:password_base64/?params_base64
    ssrurl = bytes.decode(base64.urlsafe_b64decode(fill(txt))).split('/?')
    conf = ssrurl[0].split(':')
    conf_dict = dict()
    conf_dict["ip"] = conf[0]
    conf_dict["port"] = conf[1]
    conf_dict["protocol"] = conf[2]
    conf_dict["method"] = conf[3]
    conf_dict["obfs"] = conf[4]
    conf_dict["password"] = bytes.decode(base64.urlsafe_b64decode(fill(conf[5])))

    if len(ssrurl) > 1 and ssrurl[1].rfind('&') > 0:
        for pv in map(lambda param: param.split('=', 1), ssrurl[1].split('&')):
            conf_dict[pv[0]] = bytes.decode(base64.urlsafe_b64decode(pv[1]))

    return conf_dict


def ss_parse(txt):
    # method:password@server:port
    conf = clear_ss(bytes.decode(base64.urlsafe_b64decode(fill(txt))))
    conf_list = []
    for part in conf.split('@'):
        conf_list += part.split(':')
    conf_dict = dict()
    conf_dict["method"] = conf_list[0]
    conf_dict["password"] = conf_list[1]
    conf_dict["ip"] = conf_list[2]
    conf_dict["port"] = conf_list[3]
    return conf_dict


def parse(txt):
    if 'ssr://' in txt:
        return ssr_parse(txt.replace('ssr://', ''))
    if 'ss://' in txt:
        return ss_parse(txt.replace('ss://', ''))
    raise Exception('ss url or ssr url format error.')


if __name__ == '__main__':
    print(parse('ss://YWVzLTEyOC1jdHI6dmllbmNvZGluZy5jb21AMTUyLjg5LjIwOC4xNDY6MjMzMw'))
    print(parse('ssr://MTUyLjg5LjIwOC4xNDY6MjMzMzphdXRoX3NoYTFfdjQ6YWVzLTEyOC1jdHI6cGxhaW46ZG1sbGJtTnZaR2x1Wnk1amIyMA'))
    print(parse('ssr://eHh4LmNvbTo4MDgwOm9yaWdpbjpBRVMtMTI4LUNGQjpodHRwX3Bvc3Q6TVRJek5EVTIvP29iZnNwYXJhbT1lSGg0TG5GeExtTnZiUT09JnByb3RvcGFyYW09WVdKalpEcGtaV1puUFQwPSZyZW1hcmtzPWFHcz0mZ3JvdXA9YzNOeUxYWndiZz09='))
