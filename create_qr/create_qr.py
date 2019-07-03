# 方法一生成qrcode
import qrcode
import os
import sys
import time
 
qr = qrcode.QRCode(     
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)   #设置图片格式
print("输入要写入的东西，按回车键")
data = input()  #运行时输入数据
qr.add_data(data)
qr.make(fit=True)
 
img = qr.make_image()
img.save('test.png')  #生成图片
 
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
plt.imshow(img) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
 
# 方法二——生成qrcode
import qrcode
import os
import sys
import time
 
qr = qrcode.QRCode(     
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)   #设置图片格式
print("输入要写入的东西，按回车键")
data = input()  #运行时输入数据
qr.add_data(data)
qr.make(fit=True)
 
img = qr.make_image()
img.save('test.png')  #生成图片
 
import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
plt.imshow(img) # 显示图片
plt.axis('off') # 不显示坐标轴
plt.show()
