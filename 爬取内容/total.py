import re

import pymysql
import requests
import time


def main():
    localtime = time.strftime("%d", time.localtime())
    print ("本地时间为 :", localtime)
    results = select_data_from_mysql()
    #a = []
    print(len(results))
    for i in range(len(results)):
        result = results[i]
        result = "".join(result)
        IndexHtml = request_Index_wandoujia(result)
        items,classific,comments = parse_index_result(IndexHtml) 
        try:
            app_name, download_num, good, comment_number, tag = items[0]
        except:
            continue

        if not tag:
            tag = ""
        
        if '万' in download_num:
            dispose = download_num.replace('万', '')
            result_numb = int(float(dispose) * 10000)
            #print(result_numb)
        elif '亿' in download_num:
            dispose = download_num.replace('亿', '')
            result_numb = int(float(dispose) * 100000000)
            #print(result_numb)
        else:
            result_numb = int(download_num)
            #print(result_numb)

        download_num = str(result_numb)

        #print(app_name, download_num, good, comment_number, tag)
        download_time = localtime
        app_id = i
        #a.append()
        
        write_comment_to_mysql((app_id, app_name, download_time , download_num, good, comment_number,tag ,download_time),classific,comments)
        
def request_Index_wandoujia(result):
    try:
        response = requests.get(result)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None   


def parse_index_result(IndexHtml):
    pattern = re.compile('<span class=.title. itemprop=.name.>(.*?)</span>.*?<i itemprop=.interactionCount.*?>(.*?)</i>.*?<b>次下载</b>.*?item love.*?<i>(.*?)</i>.*?<a.*?查看评论.*?<i>(.*?)</i>.*?<dd class=.tag-box.>.*?SoftwareApplicationCategory. data-track=.detail-click-appTag.>(.*?)</a>.*?</dd>',re.S)
    items = re.findall(pattern,str(IndexHtml))
    #print(items)
    pattern = re.compile('<div class="tag-box"><a href=.*?>(.*?)</a></div>',re.S)
    classific = re.findall(pattern,str(IndexHtml))
    pattern = re.compile('cmt-content.*?><span>(.*?)</span></p>',re.S)
    comments = re.findall(pattern,str(IndexHtml))
    return items,classific,comments


def write_comment_to_mysql(j,classific,comments):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='final')
    cur = db.cursor()
    app_id = '"' + str(j[0]) + '"'
    app_name = '"' + str(j[1]) + '"'
    download_time = '"' + str(j[2]) + '"'
    download_num = '"' + str(j[3]) + '"'
    good = '"' + str(j[4]) + '"'
    comment_number = '"' + str(j[5]) + '"'
    tag = '"' + str(j[6]) + '"'
    classific = '"' + ','.join(classific) + '"'
    comment_detail = '"' + ','.join(comments) + '"'
    # SQL 插入语句
    sql = 'INSERT ignore INTO total VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)' % (app_id, app_name, download_time, download_num, good, comment_number,tag,classific,comment_detail)
    print(sql)
    
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
    

def select_data_from_mysql():
    # 打开数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='app' )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT app_link from app")
    data = cursor.fetchall()
    # 关闭数据库连接
    conn.close()
    return data
    

#主函数
if __name__ == "__main__":
    main()
