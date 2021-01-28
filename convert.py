
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
#print(matplotlib.__file__)#找到matplotlib在哪
plt.rcParams['font.sans-serif'] = ['jf-openhuninn-1.1']#告訴matplotlib設定中文字型
# 用Numpy建立樣本
table = np.random.rand(9, 5)
table = np.round(table, 2)


# 用Pandas將樣本轉成DataFrame
table_pd = pd.DataFrame(table)
table_pd.columns=['一', '二', '三', '四', '五']
table_pd.index=['1', '2', '3', '4', ' ', '5', '6', '7', '8']

# DataFrame=>png
plt.figure('123')            # 視窗名稱
ax = plt.axes(frame_on=False)# 不要額外框線
ax.xaxis.set_visible(False)  # 隱藏X軸刻度線
ax.yaxis.set_visible(False)  # 隱藏Y軸刻度線
pd.plotting.table(ax, table_pd, loc='center') #將mytable投射到ax上，且放置於ax的中間
plt.savefig('table.png')     # 存檔'''



#列出目前有的字體
'''import matplotlib.font_manager
 
a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
 
for i in a:
    print(i)'''