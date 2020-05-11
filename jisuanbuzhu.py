'''
计算补助
'''
from datetime import datetime
import datetime as datetime0
while 1:
    print("——————————————————出差餐补计算器——————————————————————")
    startTime = input("输入开始时间（形如20200505表示2020年5月5日）\n")
    stopTime = input("输入结束时间\n")

    工作日价格 = input("输入工作日价格（数字）\n")
    休息日价格 = input("输入休息日价格\n")
    if (int(stopTime) - int(startTime)) > 0 and 工作日价格.isdigit() and 休息日价格.isdigit():
        # today = datetime.now().weekday() + 1
        工作日 = 0
        休息日 = 0
        begin = datetime0.date(int(startTime[0:4]),int(startTime[4:6]),int(startTime[6:8]))
        end = datetime0.date(int(stopTime[0:4]),int(stopTime[4:6]),int(stopTime[6:8]))
        for eachDay in range((end - begin).days+1):
            eachDay = str(begin + datetime0.timedelta(days=eachDay)).split("-")

            week = datetime.strptime(eachDay[0]+eachDay[1]+eachDay[2], "%Y%m%d").weekday() + 1
            if week > 0 and week < 6:
                工作日 += 1
            else:
                休息日 += 1
        print("一共有工作日{}天，休息日{}天".format(工作日, 休息日))
        print("出差补贴一共为{}元".format(工作日 * int(工作日价格) + 休息日 * int(休息日价格)))
    else:
        print("输入数据格式有误")
