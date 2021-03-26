import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

def gen_g():
    cpulist = [0.01, 0.02, 0.03, 0.04]
    memlist = [1.2, 2.5, 4.5, 7.3]
    plt.title('F4TH FPGA:Performance: '+datetime.now().strftime("%m/%d/%Y"))
    x = [i for i in range(len(cpulist))]
    y1 = cpulist
    y2 = memlist
    plt.plot(x, y1, label='CPU info')
    plt.plot(x, y2, label='MEM info')
    plt.show()
    
def gen_pi():
    plt.figure(figsize=(6,9)) #调节图形大小
    labels = [u'ZBS',u'FPGA',u'ZBS+JCS',u'CCS'] #定义标签
    sizes = [9,5,3,1] #每块值
    colors = ['red','yellowgreen','lightskyblue','yellow'] #每块颜色定义
    explode = (0,0,0.02,0) #将某一块分割出来，值越大分割出的间隙越大
    patches,text1,text2 = plt.pie(sizes,
                          explode=explode,
                          labels=labels,
                          colors=colors,
                          labeldistance = 1.2,#图例距圆心半径倍距离
                          autopct = '%3.2f%%', #数值保留固定小数位
                          shadow = False, #无阴影设置
                          startangle =90, #逆时针起始角度设置
                          pctdistance = 0.6) #数值距圆心半径倍数距离
    #patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本
    # x，y轴刻度设置一致，保证饼图为圆形
    plt.axis('equal')
    plt.legend()
    plt.show()

    
if __name__ == '__main__':
    gen_g()
    gen_pi()
