import pandas as pd
from sqlalchemy import create_engine
data=pd.read_csv('data.csv')
data = data.drop('linkUrl' ,axis=1)
# 找出其中的index为列表
nulllist=data[data['optName']=='全部'].index.tolist()
# 删除其中的列
data=data.drop(nulllist)
engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format('root', '123456', '127.0.0.1:3306', 'mysql'))
con = engine.connect()#创建连接
data.to_sql(name='classification', con=con, if_exists='append', index=False)
