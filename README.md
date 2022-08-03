# ImageConvert - OpenCV

### Some image convert function.

1. Read image as byte type, always use by webAPI.
2. Read 1 (1-bit pixels, black and white, stored with one pixel per byte) by openCV.
3. Read image which filename contain chinese.
4. Auto resize image with the best width and height which not reduce too much DPI.

### 一些影像轉換或處理的方程式

1. 讀取影像透過byte格式而非本地路徑讀取，通常用於api request接收.
2. 讀取部分mode 1-bit poxels 黑白影像，轉換為opencv可以使用的格式，很常時後掃描機掃上來選黑白opencv無法讀取，透過此方法可解決.
3. 透過opencv讀取含有中文檔名影像.
4. 自動調整影像長寬，在不失去解析度的情況下自動調整.


#### create by Josh
