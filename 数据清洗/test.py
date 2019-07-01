import pymysql
from jieba import analyse


def select_data_from_mysql():
    # 打开数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='final' )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute('SELECT app_name,comment_detail FROM total ') 
    data = cursor.fetchall()
    # 关闭数据库连接
    conn.close()
    return data


def write_to_mysql(i):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='final')
    cur = db.cursor()
    app_name = '"' + str(i[0]) + '"'
    comment_detail = '"' + str(i[1]) + '"'   
    print(comment_detail)
    sql = 'UPDATE total SET comment_detail = %s WHERE app_name = %s' % (comment_detail,app_name)
    #print(sql)
    try:
        
        cur.execute(sql)
        
        db.commit()
    except:
        
        db.rollback()
    
    db.close()    


if __name__ == "__main__":
    
    tfidf = analyse.extract_tags
    result = select_data_from_mysql()

    results = []
    
    for i in range(len(result)):
        app_name,comment_detail = result[i]      
        keywords = tfidf(str(comment_detail))
        comment_detail = ','.join(keywords)
        results.append((app_name,comment_detail))

    
    for i in results:
        write_to_mysql(i)  
    
    


