import matplotlib.pyplot as plt
import matplotlib
import numpy as np
a=np.arange(10)
plt.ylabel('我是yy',fontproperties='SimHei')
plt.plot(a,a*1.5,'go-',a,a**2,'rx-',a,a*4.5,'b-.')
plt.savefig('123',dpi=600)
plt.show()
