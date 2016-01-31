# -*- coding: utf-8 -*-
import re


class SMZDMscaner(object):
    def __init__(self, html_text):
        self.text = html_text
        # pass

    def SearchForKeywords(self, keywords):
        result = 0
        for keyword in keywords:

            result_sub = 1
            for k in keyword:
                if not k:
                    result_sub = 0
                result_sub *= (self.text.lower().find(k.lower()) + 1)
            else:
                if not k:
                    result_sub = 0
            result += result_sub
        return result


if __name__ == "__main__":
    keywords_list = [
        ['大王', '纸尿裤'],
        ['babybjorn', 'one'],
        ['Aptamil', 'pre'],
        ['nutrilon'],
        ['贝亲', '宽口径'],
        ['微信'],
        ['移动'],
        ['ERGObaby', '360'],
        ['mountain', 'buggy', 'nano'],
        ['xbox'],
        [''],
        [''],
        [''],
        [''],
        [''],
    ]

    item_title = [
        '<![CDATA[预定中：Microsoft 微软 Xbox One Elite 精英版手柄 1099元]]>',
        '<![CDATA[MEGA BLOKS 美高 DBM49 小凯莉的游泳池派对 149.4元包邮（249元，下单6折）]]>',
        '<![CDATA[SVAKOM 司沃康 Siime 丝米 可拍照高清视频内窥震动棒 179元包邮]]>',
        '<![CDATA[什么值得玩：欧洲神秘浪漫之都捷克布拉格、泰北玫瑰古城清迈等 20160120]]>',
        '<![CDATA[晚间白菜特价包邮 棉拖鞋 足光散 印章水彩笔等 20160120]]>',
        '<![CDATA[GARMIN 佳明 Vivoactive 智能运动手表 1599元包邮]]>',
        '<![CDATA[移动端：Team 十铨 冥神系列 DDR3 1600 16G(8Gx2套装) 台式机内存 479元包邮]]>',
        '<![CDATA[凑单品：Nuby 努比 小怪兽零食盒 29.9元]]>',
        '<![CDATA[UNIQLO 优衣库 161367 女款轻型羽绒夹克 199元包邮]]>',
        '<![CDATA[促销活动：亚马逊中国 进口拼图专场 2件7折]]>',
        '<![CDATA[AUBY 澳贝 启智系列  463457DS 职业体验镇 39元]]>',
        "<![CDATA[移动端：WAIDMANN'S BRAU 猎人 黑啤酒 500ml*12听礼盒装*2份 99元包邮]]>",
        '<![CDATA[Okamoto 冈本 003组合装（白金6片+skin5片+3个随机单片+003超薄系列2片） 39元包邮（需用券）]]>',
        '<![CDATA[SAMSUNG 三星 Galaxy Note 3 (N9006) 联通3G手机 1159元包邮]]>',
        '<![CDATA[移动端：ViewSonic 优派 VG2433smh 24英寸ADS显示器 1239元包邮]]>',
        '<![CDATA[国内&海淘 每日优惠精选 20160120]]>',
        '<![CDATA[微信端：KUYURA 可悠然 美肌沐浴露 欣怡幽香 1000ml*2瓶 84元包邮]]>',
        '<![CDATA[拼单好价：BRAUN 博朗 欧乐B DB4510K 儿童电动牙刷*3 168元包邮（198-30，合56元/个）]]>',
        '<![CDATA[移动端：Midea 美的 YGD30A3 分体双杆挂烫机 263元包邮（288-25）]]>',
        '<![CDATA[20点开始、移动端：PHILIPS 飞利浦 HR2100/60 料理机 99元包邮]]>',
        '<![CDATA[TOSHIBA 东芝 32GB TF存储卡（读取48M/s） 41.9元，赠读卡器]]>',
        '<![CDATA[辉叶 HC-105 电动摇摇按摩椅 1998元包邮（双重优惠）]]>',
        '<![CDATA[Team 十铨 Elite系列 DDR4 2400 8GB 台式机内存 264元包邮（289-25）]]>',
        '<![CDATA[Changdi 长帝 CKF-30BS 30L 多功能电烤箱 179元包邮，送烘焙套装]]>',
        '<![CDATA[蓝月亮 深层洁净护理 洗衣液 500g*24件 93.6元包邮（双重优惠）]]>',
        '<![CDATA[移动端：ASUS 华硕 QM1 便携电脑 （2GB 32GB） 424元包邮（需用满220减25券）]]>',
        '<![CDATA[Kessler-Zink  凯斯勒 雷司令 晚收 甜白葡萄酒 375ml*2瓶 139元包邮]]>',
        '<![CDATA[移动端：Valvoline 胜牌 DURA BLEND 星驰 5W-30 合成机油 946ml 46.9元]]>',
        '<![CDATA[UNIQLO 优衣库 163303  男装 摇粒绒外套 89元包邮]]>',
        '<![CDATA[eneloop 爱乐普 第四代 BK-3HCCA 5号充电电池 89元包邮]]>',
    ]

    for i in range(len(item_title)):
        smzdm = SMZDMscaner(item_title[i])
        if smzdm.SearchForKeywords(keywords_list):
            print(item_title[i])  # , item_link[i])
