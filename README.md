# 將Panda table轉成圖檔並儲存
文章參考:https://ithelp.ithome.com.tw/m/articles/10231378 

#解決matplotlib中文亂碼問題
文章參考:https://pyecontech.com/2020/03/27/python%E6%95%99%E5%AD%B8-%E5%A6%82%E4%BD%95%E8%A7%A3%E6%B1%BAmatplotlib%E4%B8%AD%E6%96%87%E4%BA%82%E7%A2%BC%E5%95%8F%E9%A1%8C/

解決步驟如下:
步驟一 
下載喜歡的字體

步驟二 
用以下指令找到matplotlib位置
import matplotlib
print(matplotlib.__file__)

#matplotlib位置如下，把剛下載的字體放入matplotlib中的mpl-data\fonts\ttf
( D:\python3.7\Lib\site-packages\matplotlib\mpl-data\fonts\ttf )

步驟三 
到\.matplotlib刪除快取(快取會記錄原使用的字體)刪除fontList.json
 C:\Users\你電腦的名字\.matplotlib
( 到C:\Users\dxgh\.matplotlib 刪除fontList.json )

步驟四
檢查字型是否成功安裝
import matplotlib.font_manager 
a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
for i in a:
    print(i)

使用說明:
使用前指定字型
plt.rcParams['font.sans-serif] = ['字型名稱']
我使用 jf-openhuninn-1.1 (圓體)
