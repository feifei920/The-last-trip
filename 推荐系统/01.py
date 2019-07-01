import numpy as np
import pymysql
import pandas as pd  
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import linear_kernel


def main():

   data = select_data_from_mysql()
   vectorizer=CountVectorizer()
   transformer = TfidfTransformer()
   tfidf = transformer.fit_transform(vectorizer.fit_transform(data['classific']))  
   print (tfidf)
   '''
   tfidf = TfidfVectorizer()
   data['classific'] = data['classific'].fillna('')
   tfidf_matrix = tfidf.fit_transform(data['classific'])
   tfidf_matrix.shape
   #print(tfidf_matrix.shape)
   cosine_sim = linear_kernel(tfidf_matrix,tfidf_matrix)
   indices = pd.Series(data.index,index = data['app_name']).drop_duplicates()
   get_recommendation("QQ")
   '''
   
def select_data_from_mysql():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456',db='final' )
    sql_query = "SELECT app_name,tag,classific,comment_detail from total"
    df = pd.read_sql(sql_query, con=conn)

    conn.close()
    return df

'''
def get_recommendation(title,consine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores,key=lambda x:x[1],reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0]for i in sim_scores]
    return data['app_name'].iloc[movie_indices]
'''

if __name__ == "__main__":
   main()