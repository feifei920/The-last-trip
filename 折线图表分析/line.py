import numpy as np
import pymysql
import pandas as pd  
import matplotlib.pyplot as plt  
import matplotlib 


def main():
    instr = input("please input the string: ")
    while input("please input: ")!="exit":
        print("input error")
    
    plt.rcParams['font.sans-serif'] = ['FangSong']
    plt.rcParams['axes.unicode_minus'] = False
    data = select_data_from_mysql(instr)
    data = data[0:8]
    data = data.sort_values(by = "comment_number", ascending = True)
    x = list(data.app_name)
    y = list(data.comment_number)
    
    plt.plot(x,y,"g--")
    plt.xlabel("app_name") 
    plt.ylabel("comment_number")
    plt.title("comment trend chart")
    
    plt.savefig(r'C:\Users\Administrator\Desktop\The last trip\web_demo\docs\img\line.png')
    plt.show()
   
def select_data_from_mysql(instr):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='final' )
    sql_query = 'SELECT app_name,comment_number from total WHERE tag="%s" ' %(instr)
    df = pd.read_sql(sql_query, con=conn)

    conn.close()
    return df

if __name__ == "__main__":
   main()