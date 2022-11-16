#-*- codeing = utf-8 -*-
#@time : 2021/11/29 20:01
#@Author : 白剑钟
#@File : demo1.py
#@Software : PyCharm

import os
class task:
    def __init__(self,name:str,arriveTime:int,usedTime:int) -> None:

        self.name = name
        self.arriveTime = arriveTime
        self.usedTime = usedTime
        self.state = ''
if __name__ == '__main__':
    maxNum = int(input("请输入进程数："))
    count = 0  # 时间片，初始值为0
    tasksList = []  # 进程列表
    readyList = []  # 就绪列表
    finishList = []  # 完成列表
    # 创建进程
    for i in range(maxNum):
        name = input("请输入进程名：")
        arriveTime = int(input("请输入进程到达时间："))
        usedTime = int(input("请输入进程所用时间片长度："))
        t = task(name,arriveTime,usedTime)
        tasksList.append(t)
    while True:
        os.system('cls')
        # 判断所有进程是否已完成
        if len(finishList) == maxNum:
            print("所有进程已完成！")
            break
        print("当前时间片：" + str(count))
        # 添加就绪队列
        for each in tasksList:
            if each.arriveTime == count:
                each.state = 'W'
                readyList.append(each)
        if readyList == []:
            print("没有正在执行的进程")
            continue
        # 执行进程
        else:
            runTask = readyList[0]
            runTask.usedTime -= 1
            runTask.state = 'R'
            print("当前正在执行的进程：" + runTask.name)
            if runTask.usedTime == 0:
                readyList.pop(0)
                finishList.append(runTask)
            else:
                readyList.pop(0)
                readyList.append(runTask)
        # 打印就绪进程
        if len(readyList) >= 2:
            print("当前就绪的进程为：",end="")
            for each in readyList[:-1]:
                print(each.name,end=" ")
            print()
        else:
            print("没有就绪进程！")
        # 打印完成的进程
        if not finishList == []:
            print("当前完成的进程为：",end=" ")
            for each in finishList:
                print(each.name,end="")
        else:
            print("没有已完成的进程！")
   
