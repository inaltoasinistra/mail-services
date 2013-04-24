#!/usr/bin/env python2

DOMAIN = 'the9ull.homelinux.org'

WPATH =  '/home/jonathan/forward/words'
NLINES = 1345

TFORMAT = "%Y-%m-%d %H:%M:%S"
VALIDTIME = 1 * 60*60

FROM = 'forward-bot@'+DOMAIN

import sys
import time
from email.parser import Parser
import linecache
import random

import sendmail
from database import *

def main():
    d = sys.stdin.read()

    log = file('/home/jonathan/forward/log','a')
    #log.write(d)

    p = Parser()
    m = p.parsestr(d, headersonly=True)
    f = m.get('From').split(' ')[-1].strip('<>')

    t = m.get('To').split(' ')[-1].strip('<>')

    if 'one-hour-mail' in t:
        expire =  time.strftime(TFORMAT,time.localtime(time.time()+VALIDTIME))
        service = 'One-hour forward mail service'
        alias = False
    elif 'forward-mail' in t:
        expire = '9999-01-01 00:00:00'
        service = 'Forward mail service'

        alias = getPersistentAlias(f)
    else:
        log.write('Unknown destination (%s)\n'%t)
        return

    #check if new alias already in db
    while not alias:
        alias = get_alias()
        while aliasExists(alias):
            alias = get_alias()
    insert(alias, f, expire)
    log.write('INSERT %s -> %s\n'%(alias,f))

    text =  'New alias:\n%s\n\n' % (alias+'@'+DOMAIN)
    text += 'Love,\nForwardBot\n'

    sendmail.sendMail([f],FROM,service,text)

def get_alias():
    
    w1 = linecache.getline(WPATH,random.randint(0,NLINES))
    w1 = w1.strip().lower()
    w2 = linecache.getline(WPATH,random.randint(0,NLINES))
    w2 = w2.strip().lower()
    n1 = random.randint(0x10,0xff)
    #n2 = random.randint(0x10000000,0xffffffff)

    return 'w%s%s%x'%(w1[:9],w2[:9],n1)


if __name__=="__main__":
    main()
    #print get_alias()
