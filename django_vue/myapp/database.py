#coding=utf-8
import pymysql
import datetime
import os
import xlrd
import sys
starttime = datetime.datetime.now()
REC_ID = 0
REPORT_NUM = 1
CREATE_TIME = 2
DISTRICT_NAME = 3
DISTRICT_ID = 4
STREET_NAME = 5
STREET_ID = 6
COMMUNITY_NAME = 7
COMMUNITY_ID = 8
EVENT_TYPE_NAME = 9
EVENT_TYPE_ID = 10
MAIN_TYPE_NAME = 11
MAIN_TYPE_ID = 12
SUB_TYPE_NAME = 13
SUB_TYPE_ID = 14
DISPOSE_UNIT_NAME = 15
DISPOSE_UNIT_ID = 16
EVENT_SRC_NAME = 17
EVENT_SRC_ID = 18
OPERATE_NUM = 19
OVERTIME_ARCHIVE_NUM = 20
INTIME_TO_ARCHIVE_NUM = 21
INTIME_ARCHIVE_NUM = 22
EVENT_PROPERTY_ID = 23
EVENT_PROPERTY_NAME = 24
OCCUR_PLACE = 25

def open_database():
    conn = pymysql.connect(host='localhost',
                       user='root',
                       password='wwh990325',
                       db='library'
                       )
    cursor = conn.cursor()
    return  conn, cursor

def close_database(conn):
    cursor = conn.cursor()
    cursor.close()
    conn.commit()
    conn.close()
    return

class statis():
    abcount = 0
    hotcommunitydict        = {}
    propertybydatedict      = {}
    achievebydateandtype    = {}
    main_num = {}
    streeteventbydatedict   = {}
    achievebydatedict       = {}
    abnormalout_2            = []
    streetname              = ['龙田街道', '坪山街道', '碧岭街道', '坑梓街道', '马峦街道', '石井街道']
    streetmain              = ['市容城管', '工业噪声', '占道经营', '绿化养护', '公用部件', '公共交通管理']
    streeteventbydatelist   = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]

    def propertybydate(self, sy='2018', fy='2018', sm='06', fm='10', sd='01', fd='30'):#时间段分类
        conn, cursor = open_database()

        start_time = sy + '-' + sm + '-' + sd
        end_time = fy + '-' + fm + '-' + fd
        self.propertybydatedict['投诉'] = 0
        self.propertybydatedict['咨询'] = 0
        self.propertybydatedict['建议'] = 0
        self.propertybydatedict['感谢'] = 0
        self.propertybydatedict['求决'] = 0
        query = """SELECT EVENT_PROPERTY_NAME FROM data WHERE CREATE_TIME >= '%s' AND CREATE_TIME <= '%s'
                 """
        cursor.execute(query % (start_time, end_time))
        datas = cursor.fetchall()
        for data in datas:
            if data[0] in self.propertybydatedict:
                self.propertybydatedict[data[0]] = \
                    self.propertybydatedict.get(data[0], 0) + 1
        close_database(conn)

    def streeteventbydate(self, sy='2018', sm='10', sd='30', fy='2018', fm='10', fd='30'):  # 街道日期
        conn, cursor = open_database()

        start_time = sy + '-' + sm + '-' + sd
        end_time = fy + '-' + fm + '-' + fd
        query = """SELECT STREET_NAME,MAIN_TYPE_NAME FROM data WHERE CREATE_TIME >= '%s' AND CREATE_TIME <= '%s'
        """
        cursor.execute(query % (start_time, end_time))
        datas = cursor.fetchall()
        for data in datas:
            if data[0] in self.streetname and data[1] in self.streetmain:
                self.streeteventbydatelist[self.streetmain.index(data[1])][
                    self.streetname.index(data[0])] += 1
        close_database(conn)

    def achievebydate(self, sy='2018', sm='10', sd='30', fy='2018', fm='10', fd='30'):  # 结办类型（超时..）
        conn, cursor = open_database()
        self.achievebydateandtype['processing'] = [0, 0, 0, 0, 0, 0]
        self.achievebydateandtype['in_time'] = [0, 0, 0, 0, 0, 0]
        self.achievebydateandtype['over_time'] = [0, 0, 0, 0, 0, 0]
        self.main_num['市容城管'] = 0
        self.main_num['工业噪声'] = 0
        self.main_num['占道经营'] = 0
        self.main_num['绿化养护'] = 0
        self.main_num['公用部件'] = 0
        self.main_num['公共交通管理'] = 0

        in_time = 0
        over_time = 0
        processing = 0
        start_time = sy + '-' + sm + '-' + sd
        end_time = fy + '-' + fm + '-' + fd
        query = """SELECT OVERTIME_ARCHIVE_NUM,INTIME_ARCHIVE_NUM,INTIME_TO_ARCHIVE_NUM,MAIN_TYPE_NAME FROM data 
           WHERE CREATE_TIME >= '%s' AND CREATE_TIME <= '%s'
           """
        cursor.execute(query % (start_time, end_time))
        datas = cursor.fetchall()
        for data in datas:
            if data[0] == '1':
                if data[3] == '市容城管':
                    self.achievebydateandtype['over_time'][0] += 1
                    self.main_num['市容城管'] += 1
                elif data[3] == '工业噪声':
                    self.achievebydateandtype['over_time'][1] += 1
                    self.main_num['工业噪声'] += 1
                elif data[3] == '占道经营':
                    self.achievebydateandtype['over_time'][2] += 1
                    self.main_num['占道经营'] += 1
                elif data[3] == '绿化养护':
                    self.achievebydateandtype['over_time'][3] += 1
                    self.main_num['绿化养护'] += 1
                elif data[3] == '公用部件':
                    self.achievebydateandtype['over_time'][4] += 1
                    self.main_num['公用部件'] += 1
                elif data[3] == '公共交通管理':
                    self.achievebydateandtype['over_time'][5] += 1
                    self.main_num['公共交通管理'] += 1
                over_time += 1
            if data[1] == '1':
                in_time += 1
                if data[3] == '市容城管':
                    self.achievebydateandtype['in_time'][0] += 1
                    self.main_num['市容城管'] += 1
                elif data[3] == '工业噪声':
                    self.achievebydateandtype['in_time'][1] += 1
                    self.main_num['工业噪声'] += 1
                elif data[3] == '占道经营':
                    self.achievebydateandtype['in_time'][2] += 1
                    self.main_num['占道经营'] += 1
                elif data[3] == '绿化养护':
                    self.achievebydateandtype['in_time'][3] += 1
                    self.main_num['绿化养护'] += 1
                elif data[3] == '公用部件':
                    self.achievebydateandtype['in_time'][4] += 1
                    self.main_num['公用部件'] += 1
                elif data[3] == '公共交通管理':
                    self.achievebydateandtype['in_time'][5] += 1
                    self.main_num['公共交通管理'] += 1
            if data[2] == '1':
                processing += 1
                if data[3] == '市容城管':
                    self.achievebydateandtype['processing'][0] += 1
                    self.main_num['市容城管'] += 1
                elif data[3] == '工业噪声':
                    self.achievebydateandtype['processing'][1] += 1
                    self.main_num['工业噪声'] += 1
                elif data[3] == '占道经营':
                    self.achievebydateandtype['processing'][2] += 1
                    self.main_num['占道经营'] += 1
                elif data[3] == '绿化养护':
                    self.achievebydateandtype['processing'][3] += 1
                    self.main_num['绿化养护'] += 1
                elif data[3] == '公用部件':
                    self.achievebydateandtype['processing'][4] += 1
                    self.main_num['公用部件'] += 1
                elif data[3] == '公共交通管理':
                    self.achievebydateandtype['processing'][5] += 1
                    self.main_num['公共交通管理'] += 1

        self.achievebydatedict['over_time'] = over_time
        self.achievebydatedict['in_time'] = in_time
        self.achievebydatedict['processing'] = processing
        close_database(conn)

    def getabnormal(self):
        conn, cursor = open_database()

        abnormal = []
        query = """SELECT * FROM data WHERE INTIME_TO_ARCHIVE_NUM = '1'
        """
        cursor.execute(query)
        datas = cursor.fetchall()
        for data in datas:
            tmp = data[REC_ID] + ' ' + data[CREATE_TIME] + ' ' + data[STREET_NAME] + ' ' + ' ' + data[SUB_TYPE_NAME]
            abnormal.append(tmp)
        abnormal.sort(key=lambda x: x[CREATE_TIME])
        count = 0
        for i in abnormal:
            self.abnormalout_2.append(i)
            count += 1
            if count >= 6:
                break
        close_database(conn)
        return count

    def getabnormal_form(self):
        conn, cursor = open_database()

        self.abcount = 0
        self.abnormalout = {}
        self.abnormalout['REC_ID'] = []
        self.abnormalout['CREATE_TIME'] = []
        self.abnormalout['STREET_NAME'] = []
        self.abnormalout['SUB_TYPE_NAME'] = []
        self.abnormalout['EVENT_SRC_NAME'] = []
        abnormal = []
        query = """SELECT REC_ID,CREATE_TIME,STREET_NAME,SUB_TYPE_NAME,EVENT_SRC_NAME FROM data WHERE INTIME_TO_ARCHIVE_NUM = '1'
        """
        cursor.execute(query)
        datas = cursor.fetchall()
        for data in datas:
            self.abcount += 1
            abnormal.append(data)
        abnormal.sort(key=lambda x: x[1])
        for data in abnormal:
            self.abnormalout['REC_ID'].append(data[0])
            self.abnormalout['CREATE_TIME'].append(data[1][0:10])
            self.abnormalout['STREET_NAME'].append(data[2])
            self.abnormalout['SUB_TYPE_NAME'].append(data[3])
            self.abnormalout['EVENT_SRC_NAME'].append(data[4])

        close_database(conn)

    def gethotcommuniy(self, sy='2018', sm='10', sd='30', fy='2018', fm='10', fd='30'):
        conn, cursor = open_database()

        self.hotcommunitydict = {}
        start_time = sy + '-' + sm + '-' + sd
        end_time = fy + '-' + fm + '-' + fd
        query = """SELECT COMMUNITY_NAME FROM data WHERE 
        CREATE_TIME >= '%s' AND CREATE_TIME <= '%s'
        """
        cursor.execute(query % (start_time, end_time))
        datas = cursor.fetchall()
        for data in datas:
            self.hotcommunitydict[data[0]] = self.hotcommunitydict.get(data[0], 0) + 1
        if '-' in self.hotcommunitydict:
            self.hotcommunitydict.pop('-')

        close_database(conn)

    def achieved(self, ID):
        conn, cursor = open_database()

        query = """UPDATE data SET INTIME_ARCHIVE_NUM = '1',INTIME_TO_ARCHIVE_NUM = '0'
                WHERE REC_ID = %s
                """
        cursor.execute(query % ID)

        close_database(conn)


def getdate8(date):
    year = date[0:4]
    mon = date[4:6]
    day = date[6:8]
    return (str(year), str(mon), str(day))


def propertybydate(date1, date2):
    year1, mon1, day1 = getdate8(date1)
    year2, mon2, day2 = getdate8(date2)
    a.propertybydate(sy=year1, fy=year2, sm=mon1, fm=mon2, sd=day1, fd=day2)
    return a.propertybydatedict


def streeteventbydate(date1, date2):
    year1, mon1, day1 = getdate8(date1)
    year2, mon2, day2 = getdate8(date2)
    a.streeteventbydate(sy=year1, fy=year2, sm=mon1, fm=mon2, sd=day1, fd=day2)
    return a.streeteventbydatelist


def getabnormal():
    a.getabnormal()
    return (a.getabnormal(), a.abnormalout_2)

def getabnormal_form():
    a.getabnormal_form()
    return a.abcount, a.abnormalout


def achievebydate(date1, date2):
    year1, mon1, day1 = getdate8(date1)
    year2, mon2, day2 = getdate8(date2)
    a.achievebydate(sy=year1, fy=year2, sm=mon1, fm=mon2, sd=day1, fd=day2)
    return (a.achievebydatedict, a.main_num, a.achievebydateandtype)


def hotcommunity(date1, date2):
    year1, mon1, day1 = getdate8(date1)
    year2, mon2, day2 = getdate8(date2)
    a.gethotcommuniy(sy=year1, fy=year2, sm=mon1, fm=mon2, sd=day1, fd=day2)
    return a.hotcommunitydict

def achieved(ID):
    a.achieved(ID)


a = statis()

