import cv2
import numpy as np
import matplotlib.pyplot as plt

# 创建一张黑色图像
img = np.zeros((300,300,3),dtype=np.uint8)

# 画一个绿色矩形
cv2.rectangle(img,(50,50),(250,250),(0,255,0),3)

# 显示图像
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title("UAV Vision Environment OK")
plt.axis("off")
plt.show()