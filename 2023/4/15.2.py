import pandas as pd
dl={
    'chensghi':['bj','sh'],
    'huanbi':['11','12']
}
d=pd.DataFrame(dl,index=['d2','d1'])
print(d)
d=d.reindex(index=['d1','d2'])
print(d)
d=d.reindex(columns=['huanbi','chensghi'])
print(d)
newc=d.columns.insert(2,'66')#注意！'2'为第几个从0开始记，不能超过其个数
newd=d.reindex(columns=newc,fill_value=200)
print(newd)
