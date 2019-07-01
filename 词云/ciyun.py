from wordcloud import WordCloud
import pymysql
import matplotlib.pyplot as plt
import os

def main():

    instr = input("please input the string: ")
    while input("please input: ")!="exit":
        print("input error")
    
    result = select_data_from_mysql(instr)
    results = []
    for i in result:
        for j in i:
            results.append(j)
            
    print(str(results))
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/msyh.ttc',background_color="white",width=1000, height=860, margin=2).generate(str(results))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    wordcloud.to_file(r"C:\Users\Administrator\Desktop\The last trip\web_demo\docs\img\ciyun.png")

def select_data_from_mysql(instr):
    # 打开数据库连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='final' )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询 
    sql = "SELECT comment_detail from total WHERE tag ='%s' " %(instr)
    cursor.execute(sql)
    data = cursor.fetchall()

    # 关闭数据库连接
    conn.close()
    return data

if __name__ == "__main__":
    main()
        
