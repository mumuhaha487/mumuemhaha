import numpy as np
import pandas as pd
dl={
    'chensghi':['bj','sh'],
    'huanbi':['11','12']
}
d=pd.DataFrame(dl,index=['d1','d2'])
print(d.loc['d1'])
