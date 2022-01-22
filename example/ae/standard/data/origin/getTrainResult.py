#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import inspect, re


def main():
    # csv 写入
    initArray = ['sentence', 'attribute', 'entity', 'entity_offset', 'attribute_value', 'attribute_value_offset']
    # 打开文件，追加a
    out = open('Result.csv', 'a', newline='')
    # 设定写入模式
    csv_write = csv.writer(out, dialect='excel')
    # 写入具体内容
    csv_write.writerow(initArray)

    file = open("input.txt", encoding='utf-8')
    while 1:
        line = file.readline()
        if not line:
            break
        namelist = line.split('.')  # 将文件名按照.符号进行分割

        if len(namelist[0].split(' ')) >= 2:  # 如果文件名的第一项用空格分割是个长度超过1的list，那么则可以认为该文件用空格分割
            namelist = line.split(' ')  # 将文件名按照空格进行分割
        counter = 0
        for item in namelist:
            print('The', counter, 'is:', namelist[counter])
            counter += 1

        entityNum = input("其中的剧名的后序号(一般是第0号)是第: ")
        Season = input("其中的季数(S01,S01-S02,Complete)是第: ")
        Year = input("其中的年份(2022,2021)是第: ")
        Res = input("其中的分辨率（1080p，2160p)是第: ")
        Codex = input("其中的编码格式（x264,x265)是第: ")

        indexArray = [entityNum, Season, Year, Codex, Res]
        writeArray = [0 for x in range(0, 6)]

        if indexArray[1] != '':  # Season输入
            writeArray[0] = line
            writeArray[1] = 'Season'
            writeArray[2] = ' '.join(namelist[:int(indexArray[0]) + 1])
            writeArray[3] = 0
            writeArray[4] = namelist[int(indexArray[1])]
            writeArray[5] = 0  # 以累加的方式算offset
            for i in range(int(indexArray[1])):
                writeArray[5] += len(namelist[i]) + 1
            csv_write.writerow(writeArray)

        if indexArray[2] != '':  # Year输入
            writeArray[0] = line
            writeArray[1] = 'Year'
            writeArray[2] = ' '.join(namelist[:int(indexArray[0]) + 1])
            writeArray[3] = 0
            writeArray[4] = namelist[int(indexArray[2])]
            writeArray[5] = 0  # 以累加的方式算offset
            for i in range(int(indexArray[2])):
                writeArray[5] += len(namelist[i]) + 1
            writeArray[5] += 1  # 修正offset
            csv_write.writerow(writeArray)

        if indexArray[3] != '':  # Codex输入
            writeArray[0] = line
            writeArray[1] = 'Codex'
            writeArray[2] = ' '.join(namelist[:int(indexArray[0]) + 1])
            writeArray[3] = 0
            writeArray[4] = namelist[int(indexArray[3])]
            writeArray[5] = 0  # 以累加的方式算offset
            for i in range(int(indexArray[3])):
                writeArray[5] += len(namelist[i]) + 1
            writeArray[5] += 1  # 修正offset
            csv_write.writerow(writeArray)

        if indexArray[4] != '':  # Res输入
            writeArray[0] = line
            writeArray[1] = 'Res'
            writeArray[2] = ' '.join(namelist[:int(indexArray[0]) + 1])
            writeArray[3] = 0
            writeArray[4] = namelist[int(indexArray[4])]
            writeArray[5] = 0  # 以累加的方式算offset
            for i in range(int(indexArray[4])):
                writeArray[5] += len(namelist[i]) + 1
            writeArray[5] += 1  # 修正offset
            csv_write.writerow(writeArray)

    file.close()


if __name__ == '__main__':
    main()
