# Practicing Git

# ./getTPandNtp_All_Link.py ==> 利用selenium 將所有頁面的source code抓下來再擷取ID
#
# ./crawler591.py           ==> 利用getTPandNtp_All_Link.py 擷取出來的ID，找出下列資訊後並存成JSON格式

##  -出租者(陳先生)
##  -出租者身份
##  -聯絡電話
##  -型態
##  -現況
##  -性別要求
#

# ./insertToDB.py            ==> 將資料丟進 DB中
# ./GetDatas.py              ==> 搜尋特定條件的資料後，存成json
# ./API/app_ShowQuery.py     ==> 建立server並將Json資料上拋至127.0.0.1/5000 的各個節點
# ./API/index.html           ==> 這個網頁方便進入各個節點觀看資料
# ./DB591                    ==> 整體資料庫jaon檔
