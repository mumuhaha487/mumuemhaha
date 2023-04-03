from PIL import Image
import numpy as np
im=np.array(Image.open("daeeb5e9a462be056af2c1a468977d77.jpg").convert('L'))#daeeb5e9a462be056af2c1a468977d77.jpg为图片文件
print(im.shape,im.dtype)
depth=10
im_sum=np.gradient(im)#初步梯度归一化
im_x,im_y=im_sum
im_x=im_x/100
im_y=im_y/100


count1=np.pi/2.2#变为弧度
count2=np.pi/4.
dx=np.cos(count1)*np.cos(count2)
dy=np.cos(count1)*np.sin(count2)
dz=np.sin(count1)

A=np.sqrt(im_x**2+im_y**2+1)#归一化
count1=im_x/A
count2=im_y/A
count3=1./A
b=255*(dx*count1+dy*count2+dz*count3)
b=b.clip(0,255)
im=Image.fromarray(b.astype('uint8'))
im.save("122.jpg")#保存图片为123.jpg
