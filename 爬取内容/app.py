import json
import math
import re

import pymysql
import requests


def main(appNum):
    url_origin = 'https://www.wandoujia.com/wdjweb/api/top/more'
    pageAppNum = page_app_num(url_origin)
    pageNum = math.ceil(appNum / pageAppNum)
    items = []
    for page in range(1,pageNum+1):
        url = url_origin + '?page=' + str(page)
        #print(url)
        html = request_wandoujia(url)
        items.append(parse_result(html)) 
       

    for item in items:
        for i in item:
            write_item_to_mysql(i)
    


def page_app_num(url):
    html = request_wandoujia(url)
    pattern = re.compile('<div class=.*?name.*?">(.*?)</a>.*?<span class=.*?install-count.*?>(.*?)</span>.*?<div class=.*?comment.*?>(.*?)</div>.*?<a class=.*?tag-link.*?>(.*?)</a>.*?class=.*?detail-check-btn.*?href=(.*?)>查看 </a>',re.S)
    items = re.findall(pattern,html)
    return len(items)

def request_wandoujia(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    pattern = re.compile('class=.*?detail-check-btn.*?href=(.*?)>查看 </a>',re.S)
    items = re.findall(pattern,html)
    print(items)
    return items


# 将数据写入数据库
def write_item_to_mysql(i):

    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='app')
    cur = db.cursor()
    app_link = str(i).replace("\\","") 
    print(app_link)
    # SQL 插入语句
    sql = 'INSERT INTO app(app_link) VALUES (%s)' % (app_link)
    try:

        # 执行sql语句
        cur.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()
    # 关闭数据库连接
    db.close()

#主函数
if __name__ == "__main__":
    appNum = int(500)
    main(appNum)
