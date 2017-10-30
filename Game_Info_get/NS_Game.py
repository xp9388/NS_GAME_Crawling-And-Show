import urllib.parse,requests
import time
from urllib import request
import json
import re
import os
import ssl
import pymysql.cursors
#ssl._create_default_https_context = ssl._create_unverified_context
#resp = request.urlopen('https://savecoins.me/games/all')
#html_data = resp.read().decode('utf-8')
#print(html_data)
#soup = bs(html_data, 'html.parser')

#配置数据库链接信息
connect = pymysql.Connect(
    host='45.77.11.232',
    port=3306,
    user='root',
    passwd='Inspur@871',
    db='NS_Game',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()


#标准输出
def myAlign(string, length=0):
    if length == 0:
        return string
    slen = len(string)
    re = string
    if isinstance(string, str):
        placeholder = ' '
    else:
        placeholder = u'　'
    while slen < length:
        re += placeholder
        slen += 1
    return re

#汇率获取
def Get_Rate():
    url = 'http://www.boc.cn/sourcedb/whpj/index_2.html'  # 网址
    html = requests.get(url).content.decode('utf8')  # 获取网页源码（中间涉及到编码问题,这是个大坑，你得自己摸索）
    a = html.index('<td>巴西里亚尔</td>')  # 取得“新西兰元”当前位置
    s = html[a:a + 300]  # 截取新西兰元汇率那部分内容（从a到a+300位置）
    result = re.findall('<td>(.*?)</td>', s)  # 正则获取
    EX_Rate =float(result[5])/100
    return EX_Rate


#解析主源码导入
fl = open('ceshi.txt',"r",encoding= 'gbk')
HtmlSource = fl.read()
HtmlSource.replace(' ','')

#获取游戏各项信息
def getGame(Text):
    #匹配图标地址
    reg_img = r'"image_url":".*?"'
    imgre = re.compile(reg_img)
    imglist = re.findall(imgre,Text)
    #获取图标标准地址
    for index in range(len(imglist)):
        imglist[index] = imglist[index].replace('"image_url":"', '')
        imglist[index] = imglist[index].replace('"', '')
        #print(imglist[index])

    #匹配游戏名
    reg_name = r'"title":".*?"'
    name = re.compile(reg_name)
    namelist = re.findall(name,Text)
    #获取游戏标准名称
    for index in range(len(namelist)):
        namelist[index] = namelist[index].replace('"title":"', '')
        namelist[index] = namelist[index].replace('"', '')
        #namelist[index] = namelist[index].replace(' ', '_')
        namelist[index] = namelist[index].replace('/', '_')
        namelist[index] = namelist[index].replace('\\', '_')
        namelist[index] = namelist[index].replace(':', '_')
        namelist[index] = namelist[index].replace(';', '_')
        namelist[index] = namelist[index].replace('*', '_')
        namelist[index] = namelist[index].replace('?', '_')
        namelist[index] = namelist[index].replace('>', '_')
        namelist[index] = namelist[index].replace('<', '_')
        namelist[index] = namelist[index].replace('"', '_')
        namelist[index] = namelist[index].replace('~', '_')
        namelist[index] = namelist[index].replace('\'', '')
        #print(namelist[index])

    # 匹配游戏上市时间
    reg_date = r'"release_date_order":".*?"'
    date = re.compile(reg_date)
    datelist = re.findall(date, Text)
    # 获取游戏标准名称
    for index in range(len(datelist)):
        datelist[index] = datelist[index].replace('"release_date_order":"', '')
        datelist[index] = datelist[index].replace('"', '')


    # 匹配游戏详情页面
    reg_Game_info = r'"-.*?":{'
    info = re.compile(reg_Game_info)
    infolist = re.findall(info, Text)
    # 获取游戏标准名称
    for index in range(len(infolist)):
        infolist[index] = infolist[index].replace(':{', '')
        infolist[index] = infolist[index].replace('"', '')

    # 匹配游戏是否最新上市
    reg_recent_release = r'"recent_release":.*?,'
    recent_release_info = re.compile(reg_recent_release)
    re_infolist = re.findall(recent_release_info, Text)
    # 匹配游戏是否最新上市
    for index in range(len(re_infolist)):
        re_infolist[index] = re_infolist[index].replace('"recent_release":', '')
        re_infolist[index] = re_infolist[index].replace(',', '')
        re_infolist[index] = re_infolist[index].replace('false', '已经公布')
        re_infolist[index] = re_infolist[index].replace('true', '即将公布')

    # 匹配游戏是否即将上市
    reg_coming_soon = r'"coming_soon":.*?,'
    coming_soon_info = re.compile(reg_coming_soon)
    coming_soon_infolist = re.findall(coming_soon_info, Text)
    # 匹配游戏是否即将上市
    for index in range(len(coming_soon_infolist)):
        coming_soon_infolist[index] = coming_soon_infolist[index].replace('"coming_soon":', '')
        coming_soon_infolist[index] = coming_soon_infolist[index].replace(',', '')
        coming_soon_infolist[index] = coming_soon_infolist[index].replace('false', '已经上市')
        coming_soon_infolist[index] = coming_soon_infolist[index].replace('true', '即将上市')

    # 匹配游戏是否具有试玩版
    reg_has_demo = r'"has_demo":.*?,'
    has_demo_info = re.compile(reg_has_demo)
    has_demo_infolist = re.findall(has_demo_info, Text)
    # 匹配游戏是否具有试玩版
    for index in range(len(has_demo_infolist)):
        has_demo_infolist[index] = has_demo_infolist[index].replace('"has_demo":', '')
        has_demo_infolist[index] = has_demo_infolist[index].replace(',', '')
        has_demo_infolist[index] = has_demo_infolist[index].replace('false', '不能试玩')
        has_demo_infolist[index] = has_demo_infolist[index].replace('true', '能够试玩')

    # 获取游戏价格介绍
    Game_Best_Price=[]
    Game_Best_Price_Country=[]
    EX_Rate=Get_Rate()
    for index in range(len(infolist)):
        #拼接正则,获取完整价格介绍
        reg_Price_all='"'+infolist[index]+'":{"best_prices":.*?}},'
        Price_all_info = re.compile(reg_Price_all)
        Price_all_infolist = re.findall(Price_all_info, Text)
        #print(Price_all_infolist)
        #获取最优价格,第一次筛选
        reg_Price_Best_1='"best_prices":.*?},'
        Price_Best_info_1 = re.compile(reg_Price_Best_1)
        Price_Best_infolist_1 = re.findall(Price_Best_info_1, str(Price_all_infolist))
        #print(Price_Best_infolist_1)
        #获取最优价格,第二次筛选
        reg_Price_Best_2='"regular":.*?},'
        Price_Best_info_2 = re.compile(reg_Price_Best_2)
        Price_Best_infolist_2 = re.findall(Price_Best_info_2, str(Price_Best_infolist_1))
        Price_Best_infolist_2 = str(Price_Best_infolist_2).replace('\'"regular":','')
        Price_Best_infolist_2 = str(Price_Best_infolist_2).replace('},\'', '')
        Price_Best_infolist_2 = str(Price_Best_infolist_2).replace('[]', '0')
        Price_Best_infolist_2 = str(Price_Best_infolist_2).replace('[', '')
        Price_Best_infolist_2 = str(Price_Best_infolist_2).replace(']', '')
        #print(Price_Best_infolist_2)
        #汇率转换，输出最优价格
        Price_Best_infolist_3 ='%.1f' % float(EX_Rate * float (Price_Best_infolist_2))
        if Price_Best_infolist_3=='0.0':
            Price_Best_infolist_3='均价'
        else:
            Price_Best_infolist_3 = Price_Best_infolist_3+''
        Game_Best_Price.append(str(Price_Best_infolist_3))

        #获取最优价格地区
        reg_Price_Best_country='"country_name":".*?",'
        Price_Best_country_info = re.compile(reg_Price_Best_country)
        Price_Best_country_infolist = re.findall(Price_Best_country_info, str(Price_all_infolist))
        Price_Best_country_infolist = str(Price_Best_country_infolist).replace('"country_name":"','')
        Price_Best_country_infolist = str(Price_Best_country_infolist).replace('",', '')
        Price_Best_country_infolist = str(Price_Best_country_infolist).replace('[]', '0')
        Price_Best_country_infolist = str(Price_Best_country_infolist).replace('[', '')
        Price_Best_country_infolist = str(Price_Best_country_infolist).replace(']', '')
        Price_Best_country_infolist = str(Price_Best_country_infolist).replace('\'', '')
        if Price_Best_country_infolist=='0':
            Price_Best_country_infolist='无'
        else:
            Price_Best_country_infolist =Price_Best_country_infolist+''
        Game_Best_Price_Country.append(str(Price_Best_country_infolist))

    #解析结果显示
    print('  ' + myAlign('序号', 5) + myAlign('游戏名称', 55) + myAlign('发售日期', 15) + myAlign('详情地址', 36) + myAlign('公布状况', 10)+myAlign('具有试玩',10)+myAlign('即将上市',10)+myAlign('最优价格',20)+myAlign('最优价格区服',20))
    for index in range(len(datelist)):
        print('  ' + myAlign(str(index + 1), 5) + myAlign(namelist[index], 60) + myAlign(datelist[index], 20) + myAlign(infolist[index], 40) + myAlign(re_infolist[index], 10)+myAlign(has_demo_infolist[index],10)+myAlign(coming_soon_infolist[index],10)+myAlign(Game_Best_Price[index],20),myAlign(Game_Best_Price_Country[index],20))

    #查询数据，选择处理
    insert_num = 0
    update_num = 0
    # for index in range(len(datelist)):
    #     sql = "SELECT Game_Name FROM NS_Game_Index WHERE Info_url='%s'"
    #     data = (infolist[index])
    #     cursor.execute(sql % data)
    #     if cursor.rowcount==0:
    #         #解析结果插入数据库
    #         sql = "INSERT INTO NS_Game_Index (UUID, Game_Name, Game_Name_ZH, Release_date_order, On_sale, Recent_release, Coming_soon, Has_demo, Info_url, Image_url,Best_Price,Best_Price_CHN,Best_Price_country) VALUES ( '%s', '%s',  '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )"
    #         data = (index+1,namelist[index],'', datelist[index],re_infolist[index],re_infolist[index],coming_soon_infolist[index],has_demo_infolist[index],infolist[index],'','',Game_Best_Price[index],Game_Best_Price_Country[index])
    #         cursor.execute(sql % data)
    #         connect.commit()
    #         insert_num=insert_num+cursor.rowcount
    #     else:
    #         #解析结果更新至数据库
    #         sql = "UPDATE NS_Game_Index SET UUID=%d, Game_Name='%s' ,Release_date_order='%s', On_sale='%s', Recent_release='%s', Coming_soon='%s', Has_demo='%s', Info_url='%s', Image_url='%s',Best_Price='%s',Best_Price_CHN='%s',Best_Price_country='%s' WHERE Info_url ='%s'"
    #         data = (index+1,namelist[index], datelist[index],re_infolist[index],re_infolist[index],coming_soon_infolist[index],has_demo_infolist[index],infolist[index],'','',Game_Best_Price[index],Game_Best_Price_Country[index],infolist[index])
    #         #print(sql % data)
    #         cursor.execute(sql % data)
    #         connect.commit()
    #         insert_num = update_num + cursor.rowcount
    #
    # print('成功插入', insert_num, '条数据')
    # print('成功更新', update_num, '条数据')

    # #把筛选的图片地址通过for循环遍历并保存到本地
    # for index in range(len(imglist)):
    #     jN = re.findall("\.jpg", imglist[index])
    #     pN = re.findall("\.png", imglist[index])
    #     if len(jN) > 0:
    #         urllib.request.urlretrieve(imglist[index], 'c:\\NS_Game\\'+namelist[index]+'_'+datelist[index]+'.jpg')
    #     else:
    #         if len(pN) > 0:
    #             urllib.request.urlretrieve(imglist[index], 'c:\\NS_Game\\'+namelist[index]+'_'+datelist[index]+'.png' )
    #         else:
    #             urllib.request.urlretrieve(imglist[index], 'c:\\NS_Game\\'+namelist[index]+'_'+datelist[index]+'.png')
    #

    #把筛选的图片地址通过for循环遍历并保存到本地
    for index in range(210,len(imglist)):
        print(index)
        jN = re.findall("\.jpg", imglist[index])
        pN = re.findall("\.png", imglist[index])
        if len(jN) > 0:
            urllib.request.urlretrieve(imglist[index], 'c:\\NS_Game\\'+infolist[index]+'.jpg')
        else:
            if len(pN) > 0:
                urllib.request.urlretrieve(imglist[index], 'c:\\NS_Game\\'+infolist[index]+'.jpg' )
            else:
                urllib.request.urlretrieve(imglist[index], 'c:\\NS_Game\\'+infolist[index]+'.jpg')


getGame(HtmlSource)
#urllib.request.urlretrieve('https://firebasestorage.googleapis.com/v0/b/savecoins-19940.appspot.com/o/img%2Fgames%2FFireEmblem.png?alt=media&token=a38eb89b-2c2d-4c1a-a500-4f4a77a1fdf5','1.jpg' )
