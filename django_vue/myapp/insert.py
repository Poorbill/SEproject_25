#coding=utf-8
import pymysql
import os
import xlrd
import sys
import time
sql = """INSERT INTO data
         VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
         """
add = './data2.xlsx'
book = xlrd.open_workbook(add)
sheet = book.sheets()[0]
for i in range(2,3135):
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='wwh990325',
                           db='library'
                           )

    cursor = conn.cursor()

    data = sheet.row_values(i)
    data1 = data[0]
    data2 = data[1]
    data3 = data[2]
    data4 = data[3]
    data5 = data[4]
    data6 = data[5]
    data7 = data[6]
    data8 = data[7]
    data9 = data[8]
    data10 = data[9]
    data11 = data[10]
    data12 = data[11]
    data13 = data[12]
    data14 = data[13]
    data15 = data[14]
    data16 = data[15]
    data17 = data[16]
    data18 = data[17]
    data19 = data[18]
    data20 = '1'
    data21 = '0'
    data22 = '1'
    data23 = '0'
    data24 = data[23]
    data25 = data[24]
    data26 = data[25]
    '''
    VALUES = (
                str(data1),
                str(data2),
                str(data3),
                str(data4),
                str(data5),
                str(data6),
                str(data7),
                str(data8),
                str(data9),
                str(data10),
                str(data11),
                str(data12),
                str(data13),
                str(data14),
                str(data15),
                str(data16),
                str(data17),
                str(data18),
                str(data19),
                str(data20),
                str(data21),
                str(data22),
                str(data23),
                str(data24),
                str(data25),
                str(data26)
                    )
    '''
    '''
    VALUES = (
        data1,
        data2,
        data3,
        data4,
        data5,
        data6,
        data7,
        data8,
        data9,
        data10,
        data11,
        data12,
        data13,
        data14,
        data15,
        data21,
        data22,
        data23,
        data24,
        data25,
        data26
                    )
    '''
    cursor.execute(sql%(data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,
data18,data19,data20,data21,data22,data23,data24,data25,data26))
    time.sleep(1)

    cursor.close()
    conn.commit()
    conn.close()
