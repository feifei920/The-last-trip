import pymysql
from jieba import analyse
import time

def select_data_from_mysql():
    # 打开数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='app' )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute('SELECT app_name,download_time,download_num,good,comment_number,comment_detail FROM total WHERE tag="影音播放" AND download_time=%s',(localtime)) 
    data = cursor.fetchall()
    # 关闭数据库连接
    conn.close()
    return data


def write_to_mysql(i):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='comment')
    cur = db.cursor()
    app_id = '"' + str(i[0]) + '"'
    app_name = '"' + str(i[1]) + '"'
    download_time = '"' + str(i[2]) + '"'
    download_num = '"' + str(i[3]) + '"'
    good = '"' + str(i[4]) + '"'
    comment_number = '"' + str(i[5]) + '"'
    comment_detail = '"' + str(i[6]) + '"'
    
    # SQL 插入语句
    sql = 'INSERT INTO music(app_id,app_name,download_time,download_num,good,comment_number,comment_detail) VALUES (%s, %s, %s, %s, %s, %s, %s)' % (app_id,app_name,download_time,download_num,good, comment_number,comment_detail)
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


if __name__ == "__main__":
    localtime = time.strftime("%Y/%m/%d", time.localtime())
    tfidf = analyse.extract_tags
    result = select_data_from_mysql()
    results = []
    
    for i in range(len(result)):
        app_id = i
        app_name , download_time , download_num, good, comment_number, comment_detail = result[i]
        keywords = tfidf(str(comment_detail))
        comment_detail = ','.join(keywords)
        results.append((app_id, app_name, download_time, download_num, good, comment_number, comment_detail))
    for i in results:
        write_to_mysql(i)  
        
    


