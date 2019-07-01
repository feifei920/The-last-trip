import numpy as np
import pymysql
import pandas as pd  
import matplotlib.pyplot as plt  
import matplotlib 


def main():
   plt.rcParams['font.sans-serif'] = ['FangSong']
   plt.rcParams['axes.unicode_minus'] = False
   data = select_data_from_mysql()

   data = data.sort_values(by = "comment_number", ascending = True)
   x = list(data.app_name)
   y = list(data.comment_number)
   

   plt.plot(x,y,"g--")
   plt.xlabel("app_name") 
   plt.ylabel("comment_number")
   plt.title("comment trend chart")
   plt.show()
   plt.savefig(r'C:\Users\Administrator\Desktop\The last trip\折线图表分析\travel_line.png')

   
def select_data_from_mysql():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='final' )
    sql_query = 'SELECT app_name,comment_number from total WHERE tag="旅游出行" '
    df = pd.read_sql(sql_query, con=conn)

    conn.close()
    return df

if __name__ == "__main__":
   main()