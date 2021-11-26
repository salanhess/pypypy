# -*- coding: utf-8 -*-
"""
Created on 2021-9-12 12:36:10

@author: baihao
refer to https://blog.csdn.net/u012328159/article/details/79240652
"""
import matplotlib.pyplot as plt
import os


###### 定义函数可用，将引号中的内容打开即可直接使用 ######
"""
def fig_plot(x, y, title, xlabel_name , ylable_name, x_length, x_interval):
  # 注释：
  # x:图中x轴的输入
  # y:图中y轴的输入，其中x和y的输入长度需一致
  # title:图像的标题
  # xlable_name:x轴所代表的变量名称
  # ylable_name:y轴所代表的变量名称
  # x_length:x轴的总长度
  # x_interval:x轴标记点的间隔
  
  plt.figure(figsize=(16, 8))
  plt.plot(x, y, color='b', linewidth=2.0)
  plt.title(title, fontsize=15)
  tick_spacing = 10
  plt.xlabel(xlabel_name, fontsize=10)  # 横坐标名字
  plt.ylabel(ylable_name, fontsize=10)  # 纵坐标名字
  x_ticks = [i for i in range(0, x_length, x_interval)]
  plt.xticks(x_ticks)  # 横坐标刻度及范围
"""



def Instantaneous_performance():
  path = "D:\\软件测试项目\\930CECSTACK\\3.第三轮测试\\全闪性能测试结果\\vdbench"
  resultpath = path + "\\" + "result"
  if not os.path.exists(resultpath):
    os.makedirs(resultpath)  ##判断目录是否存在，若不存在，创建多层创建目录
  a = os.listdir(path) ##得到文件夹中文件名的列表

  ##生成单个case性能图并存到相应文件夹中
  for i in range(len(a) - 1):
    p0 = []
    f = open(path + "\\" + a[i] + "\\p0.csv")
    lines = f.readlines()
    for li in lines:
      p0.append(li)
    t = [i for i in range(1, len(lines) + 1)]
    t0 = list(t)
    x = t0
    k = p0
    k_float_m = map(float, k)
    k = list(k_float_m)

    plt.figure(figsize=(16, 8))
    plt.plot(x, k, color='b', linewidth=2.0)
    plt.title(a[i], fontsize=15)
    tick_spacing = 10
    plt.xlabel("time(s)", fontsize=10)  # 横坐标名字
    plt.ylabel("iops", fontsize=10)  # 纵坐标名字
    x_ticks = [i for i in range(0, len(lines), 300)]
    plt.xticks(x_ticks)  # 横坐标刻度及范围
    pre_savename = (path + "\\" + a[i] + "\\")
    post_savename = (a[i] + ".png")
    savename = os.path.join(pre_savename, post_savename)
    plt.savefig(savename)
    plt.draw()
    plt.pause(1)
    plt.close()

  ##生成三个子图构成的性能图，并存到新文件夹中
  fig_count = 0  ## 图片计数
  while fig_count < len(a) - 1:
    plt.figure(figsize=(16, 8))
    count = 1  ## 三张图计数
    for i in range(len(a)):
      p0 = []
      f = open(path + "\\" + a[fig_count] + "\\p0.csv")
      lines = f.readlines()
      for li in lines:
        p0.append(li)
      t = [i for i in range(1, len(lines) + 1)]
      t0 = list(t)
      x = t0
      k = p0
      k_float_m = map(float, k)
      k = list(k_float_m)
      plt.subplot(3, 1, count)
      plt.plot(x, k, color='b', linewidth=2.0)  # s-:方形
      plt.title(a[fig_count], fontsize=15)
      tick_spacing = 10
      plt.xlabel("time(s)", fontsize=10)  # 横坐标名字
      plt.ylabel("iops", fontsize=10)  # 纵坐标名字
      x_ticks = [i for i in range(0, len(lines), 300)]
      plt.xticks(x_ticks)  # 横坐标刻度及范围
      count = count + 1
      fig_count = fig_count + 1
      if count == 4:  ## 当图片中有三张图后，跳出循环
        break
      if fig_count == len(a) - 1:
        break
    plt.tight_layout()
    plt.savefig(resultpath + "\\" + str(-(-fig_count // 3)) + ".png")
    plt.draw()
    plt.pause(2)
    plt.close()



Instantaneous_performance()
