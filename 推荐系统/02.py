import pymysql
from jieba import analyse
import pandas as pd 
import numpy as np

def main():

    instr = input("please input the string: ")
    while input("please input: ")!="exit":
        print("input error")

    result = select_data_from_mysql(instr)
    result['total'] = result['download_num'] + result['comment_number']*1000 
    print(result)

    result.sort_values(by='total', axis=0, ascending=False, inplace=True)
    print(result)
    

        

def select_data_from_mysql(instr):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='final' )
    sql_query = "SELECT app_name,download_num,comment_number from total WHERE tag ='%s' " %(instr)
    df = pd.read_sql(sql_query, con=conn)
    conn.close()
    return df



if __name__ == "__main__":
    main()
