#!/usr/bin/env python3
# -*-encoding=utf8 -*-

import urllib.request
import bs4
import os

def get_rss_feed(arg):
    request = urllib.request.Request(arg)
    request.add_header('user-agent', 'Mozilla/5.0')
    response = urllib.request.urlopen(request)

    return response.read().decode('utf-8')

def rss_feed_parse(arg):
    soup = bs4.BeautifulSoup(arg, 'xml', from_encoding='utf-8')
    items = soup.find_all('item')

    print('total items: %d' % len(items))

    if len(items) == 0:
        print('nothing')
        exit(0)
    else:
        while 1:
            address = input('Where do you want to save this file: ')
            name = input('file name: ')
            address_name = address + name
            try:
                fp = open(address_name, 'w')
                fp.write(arg.strip())
                fp.flush()
                fp.close()
                break
            except:
                print('No this address')

    results = []

    for item in items:
        temp = {}
        
        temp = {'title': item.find('title').get_text(),\
        'link': item.find('link').get_text(),\
        'description': item.find('description').get_text()}
        
        results.append(temp)

    return results

def main():

    while 1:
        iptemp = input('please, url: ')
        ipt = 'http://' + iptemp
        ipts = 'https://' + iptemp

        try:
            cnt = get_rss_feed(ipt)
            break
        except:
            try:
                cnt = get_rss_feed(ipts)
                break
            except:
                print('url failed')

    results = rss_feed_parse(cnt)

    while 1:
        try:
            number = input('Which item do you want to get[enter quit to leave]: ')
    
            if number == 'quit':
                print('leaving')
                break
    
            number = int(number) - 1
            print('title: %s;\nlink: %s;\n' % (results[number]['title'], results[number]['link']))
        
            is_sure = input('Do you want to get the description[y/n]: ')
        
            if is_sure == 'y':
                print('description: %s;' % results[number]['description'])

        except:
            print('wrong number')

    return 0

if __name__ == '__main__':
    main()
