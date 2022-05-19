import time
from ClassFunc import Func as ClassFunc
from ClassFunc import Color as ClassFunc


# 時間

setHoure = 1
setMin = 10
setSec = 2

# 換算成秒數
houre = setHoure * 60 * 60
min = setMin * 60
sec = setSec

totleSec = int(houre + min + sec)

print("總計時秒數:" + str(totleSec) + "秒")

# 換算成 小時+分鐘+秒
setHoure = str(totleSec // 60 // 60)
setMin = str(totleSec // 60 % 60)
setSec = str(totleSec % 60)




nameArray = ["fu fred", "bob wu"]

name = {
    "lastName": "",
    "fristName": ""
}

lastName = name["lastName"]
fristName = name["fristName"]

print(name)

print("倒數:" + setHoure + "小時" + setMin + "分鐘" + setSec + "秒鐘")

"""
物件(Object)
屬性(Attribute)
方法(Method)
類別(Class)


"""
