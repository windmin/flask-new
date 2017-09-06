# 网线长度 1m=100cm 1cm=10mm
CABLE_LENGTH = [1500, 2000, 3000, 5000, 8000, 10000, 12000] #mm

# 挂纤轮本身直径
WHEEL = 103
WHEEL_D = 62 #小直径

# 13个挂纤轮底部圆弧到底部的距离，每个间距228
WHEEL_DISTANCE = [3047, 2819, 2591, 2363, 2135, 1907, 1679, 1451, 1223, 995, 767, 539, 311]
# WHEEL_DISTANCE = {
#     '1': 3150,
#     '2': 2922,
#     '3': 2694,
#     '4': 2466,
#     '5': 2238,
#     '6': 2010,
#     '7': 1782,
#     '8': 1554,
#     '9': 1326,
#     '10': 1098,
#     '11': 870,
#     '12': 642,
#     '13': 414
# }

# 大线环1、2本身直径
LINE = 56

# 正面大线环1底边框到底部的距离（每块slot的border-bottom到底部距离）,每个间距340
BIGLINE_DISTANCE = {
    '1': 2886,
    '2': 2546,
    '3': 2206,
    '4': 1866,
    '5': 1526,
    '6': 1186,
    '7': 846,
    '8': 506,
    '9': 166
}

#大线环2底边框到底部距离，（每个大线环2之间340mm），（大线环1和大线环2之间83mm），（大线环2本身高度67mm）
BIGLINE2_DISTANCE = {
    '1': 2803,
    '2': 2463,
    '3': 2123,
    '4': 1783,
    '5': 1443,
    '6': 1103,
    '7': 763,
    '8': 423,
    '9': 83
}


# 组合线环底边框到底部距离，每个组合线环之间169mm，每4个之间相距527mm
COMBINATION_RING = {
    '1': 3035,
    '2': 2866,
    '3': 2697,
    '4': 2528,
    '5': 2001,
    '6': 1832,
    '7': 1663,
    '8': 1494,
    '9': 967,
    '10': 798,
    '11': 629,
    '12': 460
}

# 72芯配线单元ABCD EFGH IJKL
PEIXIAN_DANYUAN = {
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I',
    '10': 'J',
    '11': 'K',
    '12': 'L'
}


# 计算每块slot的端口数，用户template模板渲染
def calculate_slot(rows,cols,list):
    cols = range(1,cols+1)
    rows = range(1,rows+1)
    for r in rows:
        for c in cols:
            list.append((r,c))
    return list

# 计算同一设备、同side、正面，跳纤方式
def calculate_one_front_front(jiechushebei_radio,jierushebei_radio, \
                              jiechushebei_slot_rows,jiechushebei_slot_cols, \
                              jierushebei_slot_rows,jierushebei_slot_cols, \
                              jiechushebei,jierushebei):
    step_list = []
    log_list = []
    json_list = ['相同机架的96芯设备单元与96芯设备单元跳纤']
    from_point = jiechushebei_radio
    to_point = jierushebei_radio
    from_slot_rows = jiechushebei_slot_rows
    from_slot_cols = jiechushebei_slot_cols
    to_slot_rows = jierushebei_slot_rows
    to_slot_cols = jierushebei_slot_cols
    from_name = jiechushebei
    to_name = jierushebei
    print('from_point'+str(from_point))
    print('to_point'+str(to_point))
    # 1. 先往下走到小线环
    distance_step_1 = (len(from_slot_rows) - int(from_point[1]) + 1) * 35
    print('1. 先从'+from_name+'的'+from_point[0]+'('+from_point[1]+','+from_point[2]+')'+'端口出来往下经过下方最近的8位小线环:' + str(distance_step_1))
    # log[0]
    log_list.append('1. 先从'+from_name+'的96芯设备单元'+from_point[0]+'('+from_point[1]+','+from_point[2]+')'+'端口出来往下经过下方邻近的8位小线环。')
    pic_step1 = (215+(int(from_point[2])-1)*17, 290+(int(from_point[0])-1)*320+(int(from_point[1])-1)*35)
    pic_step2 = (pic_step1[0], pic_step1[1]+35*(5-int(from_point[1])))
    step_list.append(pic_step1)  # [0]
    step_list.append(pic_step2)  # [1]
    print('pic_step1:'+str(pic_step1))
    print('pic_step2:'+str(pic_step2))
    # json[1]
    json_list.append(from_point[0]+'('+from_point[1]+','+from_point[2]+')')

    # 2. 往右穿过中线环，最后一个端口到slot边框/中线环是26mm，（到大线环1左边框是99mm，）,从中线环顶边到大线环2底边是190mm
    if int(from_point[2]) < 12 :
        distance_step_2 = (len(from_slot_cols) - int(from_point[2])) * 18 + 12 + 26 + 140
    else:
        distance_step_2 = (len(from_slot_cols) - int(from_point[2])) * 18 + 26 + 140
    print('2. 再经过中线环到大线环1:' + str(distance_step_2))
    # log[1]
    log_list.append('2. 往右穿过中线环再到设备单元'+from_point[0]+'的大线环1。')
    pic_step3 = (pic_step2[0]+distance_step_2-140,pic_step2[1])
    pic_step4 = (pic_step3[0]+80,pic_step3[1]+50)
    step_list.append(pic_step3)  # [2]
    step_list.append(pic_step4)  # [3]
    print(pic_step3)
    print(pic_step4)
    # json[2]
    json_list.append(from_point[0]+'-大线环1')

    # 3. 往上走先到高于from_pront的挂纤轮，再往下走直到侧面最下面那个挂纤轮调头向上走
    # 大线环1到高于其的挂纤轮
    wheel_above = []
    wheel_bottom = []
    for wheel_d in WHEEL_DISTANCE:
        if wheel_d + WHEEL_D > (BIGLINE_DISTANCE[from_point[0]] + LINE):
            wheel_above.append(wheel_d)
    wheel_above.sort()
    print('穿过大线环1后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。')
    distance_step_3_1 = wheel_above[0]+WHEEL - (BIGLINE_DISTANCE[from_point[0]]+LINE)
    # 高挂纤轮到最下面的挂纤轮
    print('再到最下面的挂纤轮')
    distance_step_3_2 = wheel_above[0]+WHEEL - WHEEL_DISTANCE[-1]
    # 调头向上到高于to_point的挂纤轮
    if int(to_point[0]) == 9:
        wheel_bottom.append(WHEEL_DISTANCE[-2])
    else:
        for wheel_d in WHEEL_DISTANCE:
            if wheel_d + WHEEL_D > (BIGLINE_DISTANCE[to_point[0]] + LINE):
                wheel_bottom.append(wheel_d)
        wheel_bottom.sort()
    print('调头向上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')
    distance_step_3_3 = wheel_bottom[0] + WHEEL - WHEEL_DISTANCE[-1]

    distance_step_3 = distance_step_3_1 + distance_step_3_2 + distance_step_3_3

    # log[2]
    print('3. 从大线环1出去，向上经过高于from_point的挂纤轮，向下到最下面的挂纤轮，再向上到高于to_point的挂纤轮：' + str(distance_step_3))
    log_list.append('1. 穿过设备单元'+from_point[0]+'大线环1后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。再到最下面的挂纤轮'+'，调头向上绕过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')
    pic_step5 = (255,470+(int(from_point[0])-1)*320)
    pic_step6 = (590,230+(WHEEL_DISTANCE.index(wheel_above[0])+1-1)*215) #高于from_point的挂纤轮 step_list[5]
    pic_step7 = (590,230+(WHEEL_DISTANCE.index(wheel_bottom[0])+1-1)*215) #高于to_point的挂纤轮 step_list[6]
    step_list.append(pic_step5)  # [4]
    step_list.append(pic_step6)  # [5]
    step_list.append(pic_step7)  # [6]
    print('pic_step5'+str(pic_step5))
    print('pic_step6'+str(pic_step6))
    print('pic_step7'+str(pic_step7))
    # json[3]
    json_list.append('挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_above[0])+1))
    json_list.append('挂纤轮-13')  # json[4]
    json_list.append('挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_bottom[0])+1))  # json[5]

    # 4. 进入to_point大线环1
    distance_step_4 = wheel_bottom[0] + WHEEL - (BIGLINE_DISTANCE[to_point[0]] + LINE)
    print(distance_step_4)
    print('进入to_point大线环1')
    # log[3]
    log_list.append('2. 往下进入'+to_name+'的96芯设备单元'+to_point[0]+'的大线环1。')
    pic_step8 = (255,470+(int(to_point[0])-1)*320)
    step_list.append(pic_step8)  # [7]
    json_list.append(to_point[0]+'-大线环1')  # json[6]

    # 6. 往左进入slot的中线环，进入该端口邻近的8位小线环
    if int(to_point[2]) < 12 :
        distance_step_6 = (len(to_slot_cols) - int(to_point[2])) * 18 + 12 + 26 + 140
    else:
        distance_step_6 = (len(to_slot_cols) - int(to_point[2])) * 18 + 26 + 140
    print('6. 往左进入slot的中线环，进入该端口邻近的8位小线环:' + str(distance_step_6))
    # log[4]
    log_list.append('1. 从'+to_name+'的96芯设备单元'+to_point[0]+'的大线环1出来后，往左进入'+to_name+'设备单元'+to_point[0]+'的中线环，并将线嵌入邻近的8位小线环中。') #[6]
    pic_step9 = (215+(int(to_point[2])-1)*17, 290+(int(to_point[0])-1)*320+(int(to_point[1])-1)*35)
    pic_step10 = (pic_step9[0] , pic_step9[1]+35*(5-int(to_point[1])))
    pic_step11 = (pic_step10[0]+distance_step_6-140,pic_step10[1])
    pic_step12 = (pic_step11[0]+80,pic_step11[1]+50)
    step_list.append(pic_step9)  # [8]
    step_list.append(pic_step10)  # [9]
    step_list.append(pic_step11)  # [10]
    step_list.append(pic_step12)  # [11]
    print('pic_step12'+str(pic_step12))
    print('pic_step11'+str(pic_step11))
    print('pic_step10'+str(pic_step10))
    print('pic_step9'+str(pic_step9))

    # 7. 往上插入端口
    distance_step_7 = (len(to_slot_rows) - int(to_point[1]) + 1) * 35
    print('往上插入端口:' + str(distance_step_7))
    # log[5]
    log_list.append('2. 最后往上将线插入'+to_name+'96芯设备单元'+to_point[0]+'('+to_point[1]+','+to_point[2]+')的端口中。') #[7]
    used_distance = distance_step_1+distance_step_2+distance_step_3+distance_step_4+distance_step_6+distance_step_7
    print('总共需要线长：' + str(used_distance))
    cable_list = []
    for cable in CABLE_LENGTH:
        if cable > used_distance:
            cable_list.append(cable)
    cable_list.sort()
    shengyu_xianchang = cable_list[0]-used_distance
    print('剩余线长：'+ str(shengyu_xianchang))
    # json[7]
    json_list.append(to_point[0]+'('+to_point[1]+','+to_point[2]+')')

    # 调整上下挂纤轮
    index_above = ''
    index_bottom = ''
    if shengyu_xianchang > 456:
        if WHEEL_DISTANCE.index(wheel_above[0]) != 0:
            i = WHEEL_DISTANCE.index(wheel_above[0]) - 1
            while i >= 0:
                if shengyu_xianchang - (WHEEL_DISTANCE[i] - wheel_above[0])*2 > 0:
                    index_above = i
                    break
                else:
                    i -= 1
            if index_above != '':
                wheel_above[0] = WHEEL_DISTANCE[index_above]
                print('调整上挂纤轮为：'+str(index_above))

            distance_step_3_1 = wheel_above[0]+WHEEL - (BIGLINE_DISTANCE[from_point[0]]+LINE)
            distance_step_3_2 = wheel_above[0]+WHEEL - WHEEL_DISTANCE[-1]
            distance_step_3 = distance_step_3_1 + distance_step_3_2 + distance_step_3_3
            used_distance = distance_step_1+distance_step_2+distance_step_3+distance_step_4+distance_step_6+distance_step_7
            shengyu_xianchang = cable_list[0]-used_distance
            print('剩余线长2：'+ str(shengyu_xianchang))

    if shengyu_xianchang > 456:
        if WHEEL_DISTANCE.index(wheel_bottom[0]) != 0:
            i = WHEEL_DISTANCE.index(wheel_bottom[0]) - 1
            while i >= 0:
                if shengyu_xianchang - (WHEEL_DISTANCE[i] - wheel_bottom[0])*2 > 0:
                    index_bottom = i
                    break
                else:
                    i -= 1
            if index_bottom != '':
                wheel_bottom[0] = WHEEL_DISTANCE[index_bottom]
                print('调整下挂纤轮为：'+str(index_bottom))

            distance_step_3_3 = wheel_bottom[0] + WHEEL - WHEEL_DISTANCE[-1]
            distance_step_3 = distance_step_3_1 + distance_step_3_2 + distance_step_3_3
            distance_step_4 = wheel_bottom[0] + WHEEL - (BIGLINE_DISTANCE[to_point[0]] + LINE)
            used_distance = distance_step_1+distance_step_2+distance_step_3+distance_step_4+distance_step_6+distance_step_7
            shengyu_xianchang = cable_list[0]-used_distance
            print('剩余线长3：'+ str(shengyu_xianchang))
    log_list[2] = ('1. 穿过大线环1后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。再到最下面的挂纤轮'+'，调头向上绕过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')
    step_list[5] = (590, 230+(WHEEL_DISTANCE.index(wheel_above[0])+1-1)*215) #高于from_point的挂纤轮 step_list[5] pic_step6
    step_list[6] = (590, 230+(WHEEL_DISTANCE.index(wheel_bottom[0])+1-1)*215) #高于to_point的挂纤轮 step_list[6] pic_step7
    log_list.append('请选择一根长度为：' + str(int(cable_list[0] / 1000)) + '米的网线。') #log[6]
    json_list[3] = '挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_above[0]) + 1)
    json_list[5] = '挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_bottom[0]) + 1)


    print(step_list)
    print(log_list)
    return step_list, log_list, json_list


# 计算同一设备、同side、背面，跳纤方式
def calculate_one_back_back(jiechushebei_radio,jierushebei_radio, \
                              jiechushebei,jierushebei):
    log_list = ['']
    step_list = []
    json_list = ['相同机架的72芯配线单元与72芯配线单元跳纤']
    from_point = jiechushebei_radio
    to_point = jierushebei_radio
    from_name = jiechushebei
    to_name = jierushebei
    print('from_point'+str(from_point))
    print('to_point'+str(to_point))
    # 1. 先从第几排托盘往左出来
    distance_step_1 = 84 + 20.5 * (int(from_point[2])-1)
    print('1. 先从'+from_name+'的'+from_point[0]+'号72芯配线单元的('+str(from_point[1])+','+str(from_point[2])+')托盘出来:' + str(distance_step_1))
    # log[1]
    log_list.append('1. 先从'+from_name+'的72芯配线单元'+PEIXIAN_DANYUAN[from_point[0]]+'('+str(from_point[1])+','+str(from_point[2])+')端口出来。' )
    if int(from_point[0]) <= 4:
        pic_step1 = (325 + (int(from_point[2]) - 1) * 20, 205 + (int(from_point[0]) - 1) * 160 + (int(from_point[1]) - 1) * 25)
    elif int(from_point[0]) > 4 and int(from_point[0]) <= 8:
        pic_step1 = (325 + (int(from_point[2]) - 1) * 20, 205 + (int(from_point[0]) - 1) * 160 + (int(from_point[1]) - 1) * 25 +335)
    elif int(from_point[0]) > 8 and int(from_point[0]) <= 12:
        pic_step1 = (325 + (int(from_point[2]) - 1) * 20, 205 + (int(from_point[0]) - 1) * 160 + (int(from_point[1]) - 1) * 25 +335 * 2)
    pic_step2 = (250, pic_step1[1])
    step_list.append(pic_step1)  # [0]
    step_list.append(pic_step2)  # [1]
    print('pic_step1:'+str(pic_step1))
    print('pic_step2:'+str(pic_step2))
    # json[1]
    json_list.append(PEIXIAN_DANYUAN[from_point[0]]+'('+from_point[1]+','+from_point[2]+')')


    # 2. 进入组合线环#XX中的小孔
    distance_step_2 = 34 + 26 * (6 - int(from_point[1]))
    print('2. 进入组合线环'+str(from_point[0])+'中的小孔:' + str(distance_step_2))
    # log[2]
    log_list.append('2. 进入'+from_name+'的72芯配线单元'+PEIXIAN_DANYUAN[from_point[0]]+'组合线环的小孔。')
    if int(from_point[0]) <= 4:
        pic_step3 = (250, 360 + 160 * (int(from_point[0])-1))
    elif int(from_point[0]) > 4 and int(from_point[0]) <= 8:
        pic_step3 = (250, 360 + 160 * (int(from_point[0]) - 1) + 340)
    elif int(from_point[0]) > 8 and int(from_point[0]) <= 12:
        pic_step3 = (250, 360 + 160 * (int(from_point[0]) - 1) + 340 * 2)
    step_list.append(pic_step3)  # [2]
    print('pic_step3'+str(pic_step3))
    # json[2]
    json_list.append(PEIXIAN_DANYUAN[from_point[0]]+'-小孔')

    # 3. 进入组合线环#XX+1的大孔
    if from_point[0] == '4' or from_point[0] == '8':
        distance_step_3 = 527  # 每四个之间相距527mm
    else:
        distance_step_3 = 169  # 组合线环之间相距169mm
    print('3. 进入组合线环'+str(int(from_point[0])+1)+'中的大孔:'+str(distance_step_3))
    # log[3]
    log_list.append('3. 进入'+from_name+'的72芯配线单元'+PEIXIAN_DANYUAN[str(int(from_point[0])+1)]+'组合线环的大孔。')
    if int(from_point[0]) + 1 <= 4:
        pic_step4 = (250, 360 + 160 * int(from_point[0]))
        pic_step5 = (1080, 340 + 160 * int(from_point[0]))
    elif int(from_point[0]) + 1 > 4 and int(from_point[0]) + 1 <= 8:
        pic_step4 = (250, 360 + 160 * int(from_point[0]) + 340)
        pic_step5 = (1080, 340 + 160 * int(from_point[0]) + 340)
    elif int(from_point[0]) + 1 > 8 and int(from_point[0]) + 1 <= 12:
        pic_step4 = (250, 360 + 160 * int(from_point[0]) + 340 * 2)
        pic_step5 = (1080, 340 + 160 * int(from_point[0]) + 340 * 2)
    step_list.append(pic_step4)  # [3]
    step_list.append(pic_step5)  # [4]
    print('pic_step4:'+str(pic_step4))
    print('pic_step5:'+str(pic_step5))
    # json[3]
    json_list.append(PEIXIAN_DANYUAN[str(int(from_point[0])+1)]+'-大孔')

    # 4. 往上至高于from_point的挂纤轮，再往下走直到侧面最下面那个挂纤轮调头向上走
    wheel_above = []
    wheel_bottom = []
    for wheel_d in WHEEL_DISTANCE:
        if (wheel_d + WHEEL_D) > (COMBINATION_RING[from_point[0]]):
            wheel_above.append(wheel_d)
    wheel_above.sort()
    print('穿过大孔后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。')
    distance_step_4 = wheel_above[0]+WHEEL - COMBINATION_RING[str(int(from_point[0])+1)]
    # 高挂纤轮到最下面的挂纤轮
    print('再到最下面的挂纤轮')
    distance_step_5_1 = wheel_above[0]+WHEEL - WHEEL_DISTANCE[-1]
    # 调头向上到高于to_point的挂纤轮
    for wheel_d in WHEEL_DISTANCE:
        if (wheel_d + WHEEL_D) > (COMBINATION_RING[to_point[0]]):
            wheel_bottom.append(wheel_d)
    wheel_bottom.sort()
    print('调头向上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')
    distance_step_5_2 = wheel_bottom[0] + WHEEL - WHEEL_DISTANCE[-1]
    distance_step_5 = distance_step_5_1 + distance_step_5_2
    # log[4]
    log_list.append('1. 从72芯配线单元'+PEIXIAN_DANYUAN[str(int(from_point[0])+1)]+'的大孔穿出后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。再到最下面的挂纤轮。调头向上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')

    # pic_step5 = (180, 260 + (WHEEL_DISTANCE.index(wheel_above[0])+1-1) * 215)  # wheel_above
    pic_step6 = (590, 230 + (WHEEL_DISTANCE.index(wheel_above[0])+1-1) * 215)  # wheel_above
    pic_step7 = (590, 230 + (WHEEL_DISTANCE.index(wheel_bottom[0])+1-1) * 215)  # wheel_bottom
    step_list.append(pic_step6)  # [5]
    step_list.append(pic_step7)  # [6]
    print('pic_step6:' + str(pic_step6))
    print('pic_step7:' + str(pic_step7))
    # json[4]
    json_list.append('挂纤轮-'+str(WHEEL_DISTANCE.index(wheel_above[0])+1))
    json_list.append('挂纤轮-13')  # json[5]
    json_list.append('挂纤轮-'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1))  # json[6]


    # 5. 往下进入to_point组合线环#XX+1的大孔
    if int(to_point[0]) < 12:
        distance_step_6 = wheel_bottom[0]+WHEEL - COMBINATION_RING[str(int(to_point[0])+1)]
        print('2. 往下进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(to_point[0])+1)]+'组合线环的大孔。')
        # log[5]
        log_list.append('2. 往下进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(to_point[0])+1)]+'组合线环的大孔。')
        json7 = PEIXIAN_DANYUAN[str(int(to_point[0])+1)]
        if int(to_point[0])+1 <= 4:
            pic_step8 = (1080, 340 + 160 * int(to_point[0]))
        elif int(to_point[0])+1 > 4 and int(to_point[0])+1 <= 8:
            pic_step8 = (1080, 340 + 160 * int(to_point[0]) + 340)
        elif int(to_point[0])+1 > 8 and int(to_point[0])+1 <= 12:
            pic_step8 = (1080, 340 + 160 * int(to_point[0]) + 340 * 2)
    elif int(to_point[0]) == 12:
        distance_step_6 = wheel_bottom[0]+WHEEL - COMBINATION_RING[str(int(to_point[0]))]
        print('2. 往下进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(to_point[0]))]+'组合线环的大孔。')
        # log[5]
        log_list.append('2. 往下进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(to_point[0]))]+'组合线环的大孔。')  # log[5]
        json7 = PEIXIAN_DANYUAN[str(int(to_point[0]))]
        if int(to_point[0]) <= 4:
            pic_step8= (1080, 340 + 160 * (int(to_point[0])-1))
        elif int(to_point[0]) > 4 and int(to_point[0]) <= 8:
            pic_step8 = (1080, 340 + 160 * (int(to_point[0])-1) + 340)
        elif int(to_point[0]) > 8 and int(to_point[0]) <= 12:
            pic_step8 = (1080, 340 + 160 * (int(to_point[0])-1) + 340 * 2)
    step_list.append(pic_step8)  # [7]
    print('pic_step8:' + str(pic_step8))
    # json[7]
    json_list.append(json7+'-大孔')

    # 6. 再向上进入to_point组合线环#XX的小孔
    if int(to_point[0]) < 12 :
        distance_step_7 = COMBINATION_RING[to_point[0]] - COMBINATION_RING[str(int(to_point[0])+1)]
        if int(to_point[0]) <= 4:
            pic_step9 = (1080, 340 + 160 * (int(to_point[0]) - 1))
        elif int(to_point[0]) > 4 and int(to_point[0]) <= 8:
            pic_step9 = (1080, 340 + 160 * (int(to_point[0]) - 1) + 340)
        elif int(to_point[0]) > 8 and int(to_point[0]) <= 12:
            pic_step9 = (1080, 340 + 160 * (int(to_point[0]) - 1) + 340 * 2)
    elif int(to_point[0]) == 12:
        distance_step_7 = 0
        pic_step9 = (pic_step8[0], pic_step8[1])
    step_list.append(pic_step9)  # [8]
    print('pic_step9:'+str(pic_step9))
    print('3. 再进入' + to_name + '72芯配线单元' + PEIXIAN_DANYUAN[str(int(to_point[0]))] + '组合线环的小孔。')
    # log[6]
    log_list.append('3. 再进入' + to_name + '72芯配线单元' + PEIXIAN_DANYUAN[str(int(to_point[0]))] + '组合线环的小孔。')
    # json[8]
    json_list.append(PEIXIAN_DANYUAN[str(int(to_point[0]))]+'-小孔')

    # 7. 往右进入指定托盘
    distance_step_8 = 34 + 26 * (6 - int(to_point[1])) + 84 + 20.5 * (int(to_point[2])-1)
    print('1. 往右进入'+to_name+'的'+str(to_point[0])+'号72芯配线单元的('+str(to_point[1])+','+str(to_point[2])+')托盘:'+str(distance_step_8))
    # log[7]
    log_list.append('1. 从'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[to_point[0]]+'组合线环的小孔出穿出。')
    # log[8]
    log_list.append('2. 往右进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(to_point[0])]+'('+str(to_point[1])+','+str(to_point[2])+')端口。')

    if int(to_point[0]) <= 4:
        pic_step10 = (250, 360 + 160 * (int(to_point[0])-1))
        pic_step12 = (325 + (int(to_point[2]) - 1) * 20, 205 + (int(to_point[0]) - 1) * 160 + (int(to_point[1]) - 1) * 25)
    elif int(to_point[0]) > 4 and int(to_point[0]) <= 8:
        pic_step10 = (250, 360 + 160 * (int(to_point[0]) - 1) + 340)
        pic_step12 = (325 + (int(to_point[2]) - 1) * 20, 205 + (int(to_point[0]) - 1) * 160 + (int(to_point[1]) - 1) * 25 + 335)
    elif int(to_point[0]) > 8 and int(to_point[0]) <= 12:
        pic_step10 = (250, 360 + 160 * (int(to_point[0]) - 1) + 340 * 2)
        pic_step12 = (325 + (int(to_point[2]) - 1) * 20, 205 + (int(to_point[0]) - 1) * 160 + (int(to_point[1]) - 1) * 25 + 335 * 2)
    pic_step11 = (250, pic_step12[1])
    step_list.append(pic_step10)
    step_list.append(pic_step11)
    step_list.append(pic_step12)
    print('pic_step10:'+str(pic_step10))
    print('pic_step11:'+str(pic_step11))
    print('pic_step12:'+str(pic_step12))
    # json[9]
    json_list.append(PEIXIAN_DANYUAN[to_point[0]]+'('+to_point[1]+','+to_point[2]+')')

    used_distance = distance_step_1 + distance_step_2 + distance_step_3 + distance_step_4 + \
                    distance_step_5 + distance_step_6 + distance_step_7 + distance_step_8
    print('总共需要线长：' + str(used_distance))
    cable_list = []
    for cable in CABLE_LENGTH:
        if cable > used_distance:
            cable_list.append(cable)
    cable_list.sort()
    shengyu_xianchang = cable_list[0] - used_distance
    print('剩余线长：' + str(shengyu_xianchang))

    # 调整上下挂纤轮
    index_above = ''
    index_bottom = ''
    if shengyu_xianchang > 456:
        if WHEEL_DISTANCE.index(wheel_above[0]) != 0:
            i = WHEEL_DISTANCE.index(wheel_above[0]) - 1
            while i >= 0:
                if shengyu_xianchang - (WHEEL_DISTANCE[i] - wheel_above[0]) * 2 > 0:
                    index_above = i
                    break
                else:
                    i -= 1
            if index_above != '':
                wheel_above[0] = WHEEL_DISTANCE[index_above]
                print('调整上挂纤轮为：' + str(index_above+1))

            distance_step_4 = wheel_above[0] + WHEEL - COMBINATION_RING[str(int(from_point[0]) + 1)]
            distance_step_5_1 = wheel_above[0] + WHEEL - WHEEL_DISTANCE[-1]
            distance_step_5 = distance_step_5_1 + distance_step_5_2
            used_distance = distance_step_1 + distance_step_2 + distance_step_3 + distance_step_4 + \
                    distance_step_5 + distance_step_6 + distance_step_7 + distance_step_8
            shengyu_xianchang = cable_list[0] - used_distance
            print('剩余线长2：' + str(shengyu_xianchang))

    if shengyu_xianchang > 456:
        if WHEEL_DISTANCE.index(wheel_bottom[0]) != 0:
            i = WHEEL_DISTANCE.index(wheel_bottom[0]) - 1
            while i >= 0:
                if shengyu_xianchang - (WHEEL_DISTANCE[i] - wheel_bottom[0]) * 2 > 0:
                    index_bottom = i
                    break
                else:
                    i -= 1
            if index_bottom != '':
                wheel_bottom[0] = WHEEL_DISTANCE[index_bottom]
                print('调整下挂纤轮为：' + str(index_bottom+1))

            distance_step_5_2 = wheel_bottom[0] + WHEEL - WHEEL_DISTANCE[-1]
            distance_step_5 = distance_step_5_1 + distance_step_5_2
            used_distance = distance_step_1 + distance_step_2 + distance_step_3 + distance_step_4 + \
                            distance_step_5 + distance_step_6 + distance_step_7 + distance_step_8
            shengyu_xianchang = cable_list[0] - used_distance
            print('剩余线长3：' + str(shengyu_xianchang))
    log_list[4] = ('1. 从72芯配线单元'+PEIXIAN_DANYUAN[str(int(from_point[0])+1)]+'的大孔穿出后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。再到最下面的挂纤轮。调头向上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')
    # step_list[5] = (180, 260 + (WHEEL_DISTANCE.index(wheel_above[0]) + 1 - 1) * 215)  # wheel_above
    step_list[5] = (590, 230 + (WHEEL_DISTANCE.index(wheel_above[0])+1-1) * 215)  # wheel_above
    step_list[6] = (590, 230 + (WHEEL_DISTANCE.index(wheel_bottom[0]) + 1 - 1) * 215)  # wheel_bottom
    print('请选择一根长度为：' + str(int(cable_list[0] / 1000)) + '米的网线。')
    log_list.append('请选择一根长度为：' + str(int(cable_list[0] / 1000)) + '米的网线。')  # log[9]
    # json[4]
    json_list[4] = '挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_above[0]) + 1)
    # json_list[5] = '挂纤轮-13'  # json[5]
    json_list[6] = '挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_bottom[0]) + 1)  # json[6]


    print(step_list)
    print(log_list)
    return step_list, log_list, json_list


# 计算不同设备、同side、正面，跳纤方式
def calculate_two_front_front(jiechushebei_radio,jierushebei_radio, \
                              jiechushebei_slot_rows,jiechushebei_slot_cols, \
                              jierushebei_slot_rows,jierushebei_slot_cols, \
                              jiechushebei,jierushebei,\
                              shebei_count):
    step_list = []
    log_list = []
    json_list = ['不同机架的96芯设备单元与96芯设备单元跳纤']
    from_point = jiechushebei_radio
    to_point = jierushebei_radio
    from_slot_rows = jiechushebei_slot_rows
    from_slot_cols = jiechushebei_slot_cols
    to_slot_rows = jierushebei_slot_rows
    to_slot_cols = jierushebei_slot_cols
    from_name = jiechushebei
    to_name = jierushebei
    print('from_point'+str(from_point))
    print('to_point'+str(to_point))
    # 1. 先往下走到小线环
    distance_step_1 = (len(from_slot_rows) - int(from_point[1]) + 1) * 35
    print('1. 先从'+from_name+'的'+from_point[0]+'('+from_point[1]+','+from_point[2]+')'+'端口出来往下经过下方最近的8位小线环:' + str(distance_step_1))
    # log[0]
    log_list.append('1. 先从'+from_name+'的96芯设备单元'+from_point[0]+'('+from_point[1]+','+from_point[2]+')'+'端口出来往下经过下方邻近的8位小线环。')
    pic_step1 = (215+(int(from_point[2])-1)*17, 290+(int(from_point[0])-1)*320+(int(from_point[1])-1)*35)
    pic_step2 = (pic_step1[0], pic_step1[1]+35*(5-int(from_point[1])))
    step_list.append(pic_step1)  # [0]
    step_list.append(pic_step2)  # [1]
    print('pic_step1:'+str(pic_step1))
    print('pic_step2:'+str(pic_step2))
    # json[1]
    json_list.append(from_point[0]+'('+from_point[1]+','+from_point[2]+')')


    # 2. 往右穿过中线环，最后一个端口到slot边框/中线环是26mm，（到大线环1左边框是99mm，）,从中线环顶边到大线环2底边是190mm/到大线环1的底边是130mm
    # 从中线环到水平走线槽边是230
    if int(from_point[2]) < 12 :
        distance_step_2_1 = (len(from_slot_cols) - int(from_point[2])) * 18 + 12 + 26 + 230
    else:
        distance_step_2_1 = (len(from_slot_cols) - int(from_point[2])) * 18 + 26 + 230
    print('2. 再经过中线环到水平走线槽:' + str(distance_step_2_1))
    # 经过N个机架到to_point的大线环2
    distance_step_2_2 = (shebei_count-1) * 748 + 70
    distance_step_2 = distance_step_2_1 + distance_step_2_2

    # log[1]
    log_list.append('2. 往右穿过'+from_name+'96芯设备单元'+from_point[0]+'的中线环，再到水平走线槽，沿着水平走线槽经过'+str(shebei_count-1)+'个机架到'+to_name+'96芯设备单元'+from_point[0]+'的大线环2。')
    pic_step3 = (pic_step2[0]+distance_step_2_1-230,pic_step2[1])
    pic_step4 = (pic_step3[0]+80,pic_step3[1]+130)
    step_list.append(pic_step3)
    step_list.append(pic_step4)
    print('pic_step3:'+str(pic_step3))
    print('pic_step4'+str(pic_step4))
    # json[2]
    json_list.append(from_point[0]+'-大线环2')

    # 3. 往上走先到高于from_pront的挂纤轮，再往下走直到侧面最下面那个挂纤轮调头向上走
    # 大线环1到高于其的挂纤轮
    wheel_above = []
    wheel_bottom = []
    for wheel_d in WHEEL_DISTANCE:
        if (wheel_d + WHEEL_D) > (BIGLINE_DISTANCE[from_point[0]] + LINE):
            wheel_above.append(wheel_d)
    wheel_above.sort()
    print('穿过大线环2后，往上经过'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。')
    distance_step_3_1 = wheel_above[0]+WHEEL - (BIGLINE_DISTANCE[from_point[0]]+LINE)
    # 高挂纤轮到最下面的挂纤轮
    print('再到最下面的挂纤轮')
    distance_step_3_2 = wheel_above[0]+WHEEL - WHEEL_DISTANCE[-1]
    # 调头向上到高于to_point的挂纤轮
    if int(to_point[0]) == 9:
        wheel_bottom.append(WHEEL_DISTANCE[-2])
    else:
        for wheel_d in WHEEL_DISTANCE:
            if (wheel_d + WHEEL_D) > (BIGLINE_DISTANCE[to_point[0]] + LINE):
                wheel_bottom.append(wheel_d)
        wheel_bottom.sort()
    print('调头向上经过'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')
    distance_step_3_3 = wheel_bottom[0] + WHEEL - WHEEL_DISTANCE[-1]

    distance_step_3 = distance_step_3_1 + distance_step_3_2 + distance_step_3_3

    # log[2]
    print('3. 从大线环2出去，向上经过高于from_point的挂纤轮，向下到最下面的挂纤轮，再向上到高于to_point的挂纤轮：' + str(distance_step_3))
    log_list.append('1. 从'+to_name+'96芯设备单元'+from_point[0]+'的大线环2穿出，往上经过'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。再到最下面的挂纤轮'+'，调头向上绕过'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')
    pic_step5 = (235,550+(int(from_point[0])-1)*320) #step_list[4]
    pic_step6 = (590,230+(WHEEL_DISTANCE.index(wheel_above[0])+1-1)*215) #高于from_point的挂纤轮 step_list[5]
    pic_step7 = (590,230+(WHEEL_DISTANCE.index(wheel_bottom[0])+1-1)*215) #高于to_point的挂纤轮 step_list[6]
    step_list.append(pic_step5)  # [4]
    step_list.append(pic_step6)  # [5]
    step_list.append(pic_step7)  # [6]
    print('pic_step5'+str(pic_step5))
    print('pic_step6'+str(pic_step6))
    print('pic_step7'+str(pic_step7))
    # json[3]
    json_list.append('挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_above[0])+1))
    json_list.append('挂纤轮-13')  # json[4]
    json_list.append('挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_bottom[0])+1))  # json[5]

    # 4. 进入to_point大线环1
    distance_step_4 = wheel_bottom[0] + WHEEL - (BIGLINE_DISTANCE[to_point[0]] + LINE)
    print(distance_step_4)
    print('进入to_point大线环1')
    # log[3]
    log_list.append('2. 往下进入'+to_name+'的96芯设备单元'+to_point[0]+'的大线环1。')
    pic_step8 = (255,470+(int(to_point[0])-1)*320)
    step_list.append(pic_step8)  # [7]
    json_list.append(to_point[0]+'-大线环1')  # json[6]

    # 6. 往左进入slot的中线环，进入该端口邻近的8位小线环
    if int(to_point[2]) < 12 :
        distance_step_6 = (len(to_slot_cols) - int(to_point[2])) * 18 + 12 + 26 + 140
    else:
        distance_step_6 = (len(to_slot_cols) - int(to_point[2])) * 18 + 26 + 140
    print('6. 往左进入slot的中线环，进入该端口邻近的8位小线环:' + str(distance_step_6))
    # log[4]
    log_list.append('1. 从'+to_name+'的96芯设备单元'+to_point[0]+'的大线环1出来后，往左进入'+to_name+'设备单元'+to_point[0]+'的中线环，并将线嵌入邻近的8位小线环中。') #[6]
    pic_step9 = (215+(int(to_point[2])-1)*17, 290+(int(to_point[0])-1)*320+(int(to_point[1])-1)*35)
    pic_step10 = (pic_step9[0] , pic_step9[1]+35*(5-int(to_point[1])))
    pic_step11 = (pic_step10[0]+distance_step_6-140,pic_step10[1])
    pic_step12 = (pic_step11[0]+80,pic_step11[1]+50)
    step_list.append(pic_step9)  # [8]
    step_list.append(pic_step10)  # [9]
    step_list.append(pic_step11)  # [10]
    step_list.append(pic_step12)  # [11]
    print('pic_step12'+str(pic_step12))
    print('pic_step11'+str(pic_step11))
    print('pic_step10'+str(pic_step10))
    print('pic_step9'+str(pic_step9))

    # 7. 往上插入端口
    distance_step_7 = (len(to_slot_rows) - int(to_point[1]) + 1) * 35
    print('往上插入端口:' + str(distance_step_7))
    # log[5]
    log_list.append('2. 最后往上将线插入'+to_name+'96芯设备单元'+to_point[0]+'('+to_point[1]+','+to_point[2]+')的端口中。') #[7]
    used_distance = distance_step_1+distance_step_2+distance_step_3+distance_step_4+distance_step_6+distance_step_7
    print('总共需要线长：' + str(used_distance))
    cable_list = []
    for cable in CABLE_LENGTH:
        if cable > used_distance:
            cable_list.append(cable)
    cable_list.sort()
    shengyu_xianchang = cable_list[0]-used_distance
    print('剩余线长：'+ str(shengyu_xianchang))
    # json[7]
    json_list.append(to_point[0]+'('+to_point[1]+','+to_point[2]+')')

    # 调整上下挂纤轮
    index_above = ''
    index_bottom = ''
    if shengyu_xianchang > 456:
        if WHEEL_DISTANCE.index(wheel_above[0]) != 0:
            i = WHEEL_DISTANCE.index(wheel_above[0]) - 1
            while i >= 0:
                if shengyu_xianchang - (WHEEL_DISTANCE[i] - wheel_above[0])*2 > 0:
                    index_above = i
                    break
                else:
                    i -= 1
            if index_above != '':
                wheel_above[0] = WHEEL_DISTANCE[index_above]
                print('调整上挂纤轮为：'+str(index_above))

            distance_step_3_1 = wheel_above[0]+WHEEL - (BIGLINE_DISTANCE[from_point[0]]+LINE)
            distance_step_3_2 = wheel_above[0]+WHEEL - WHEEL_DISTANCE[-1]
            distance_step_3 = distance_step_3_1 + distance_step_3_2 + distance_step_3_3
            used_distance = distance_step_1+distance_step_2+distance_step_3+distance_step_4+distance_step_6+distance_step_7
            shengyu_xianchang = cable_list[0]-used_distance
            print('剩余线长2：'+ str(shengyu_xianchang))

    if shengyu_xianchang > 456:
        if WHEEL_DISTANCE.index(wheel_bottom[0]) != 0:
            i = WHEEL_DISTANCE.index(wheel_bottom[0]) - 1
            while i >= 0:
                if shengyu_xianchang - (WHEEL_DISTANCE[i] - wheel_bottom[0])*2 > 0:
                    index_bottom = i
                    break
                else:
                    i -= 1
            if index_bottom != '':
                wheel_bottom[0] = WHEEL_DISTANCE[index_bottom]
                print('调整下挂纤轮为：'+str(index_bottom))

            distance_step_3_3 = wheel_bottom[0] + WHEEL - WHEEL_DISTANCE[-1]
            distance_step_3 = distance_step_3_1 + distance_step_3_2 + distance_step_3_3
            distance_step_4 = wheel_bottom[0] + WHEEL - (BIGLINE_DISTANCE[to_point[0]] + LINE)
            used_distance = distance_step_1+distance_step_2+distance_step_3+distance_step_4+distance_step_6+distance_step_7
            shengyu_xianchang = cable_list[0]-used_distance
            print('剩余线长3：'+ str(shengyu_xianchang))
    log_list[2] = '1. 从'+to_name+'96芯设备单元'+from_point[0]+'的大线环2穿出，往上经过'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。再到最下面的挂纤轮'+'，调头向上绕过'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。'
    step_list[5] = (590, 230+(WHEEL_DISTANCE.index(wheel_above[0])+1-1)*215) #高于from_point的挂纤轮 step_list[5] pic_step6
    step_list[6] = (590, 230+(WHEEL_DISTANCE.index(wheel_bottom[0])+1-1)*215) #高于to_point的挂纤轮 step_list[6] pic_step7
    log_list.append('请选择一根长度为：' + str(int(cable_list[0] / 1000)) + '米的网线。') #log[6]
    json_list[3] = '挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_above[0]) + 1)
    json_list[5] = '挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_bottom[0]) + 1)

    print(step_list)
    print(log_list)
    return step_list, log_list, json_list


# 计算不同设备、同side、背面，跳纤方式
def calculate_two_back_back(jiechushebei_radio,jierushebei_radio, \
                              jiechushebei,jierushebei,\
                              shebei_count):
    log_list = ['']
    step_list = []
    json_list = ['不同机架的72芯配线单元与72芯配线单元跳纤']
    from_point = jiechushebei_radio
    to_point = jierushebei_radio
    from_name = jiechushebei
    to_name = jierushebei
    print('from_point'+str(from_point))
    print('to_point'+str(to_point))
    # 1. 先从第几排托盘往左出来
    distance_step_1 = 84 + 20.5 * (int(from_point[2])-1)
    print('1. 先从'+from_name+'的'+from_point[0]+'号72芯配线单元的('+str(from_point[1])+','+str(from_point[2])+')托盘出来:' + str(distance_step_1))
    # log[1]
    log_list.append('1. 先从'+from_name+'的72芯配线单元'+PEIXIAN_DANYUAN[from_point[0]]+'('+str(from_point[1])+','+str(from_point[2])+')端口出来。' )
    if int(from_point[0]) <= 4:
        pic_step1 = (325 + (int(from_point[2]) - 1) * 20, 205 + (int(from_point[0]) - 1) * 160 + (int(from_point[1]) - 1) * 25)
    elif int(from_point[0]) > 4 and int(from_point[0]) <= 8:
        pic_step1 = (325 + (int(from_point[2]) - 1) * 20, 205 + (int(from_point[0]) - 1) * 160 + (int(from_point[1]) - 1) * 25 +335)
    elif int(from_point[0]) > 8 and int(from_point[0]) <= 12:
        pic_step1 = (325 + (int(from_point[2]) - 1) * 20, 205 + (int(from_point[0]) - 1) * 160 + (int(from_point[1]) - 1) * 25 +335 * 2)
    pic_step2 = (250, pic_step1[1])
    step_list.append(pic_step1)  # [0]
    step_list.append(pic_step2)  # [1]
    print('pic_step1:'+str(pic_step1))
    print('pic_step2:'+str(pic_step2))
    # json[1]
    json_list.append(PEIXIAN_DANYUAN[from_point[0]]+'('+from_point[1]+','+from_point[2]+')')


    # 2. 进入组合线环#XX中的小孔
    distance_step_2 = 34 + 26 * (6 - int(from_point[1]))
    print('2. 进入组合线环'+str(from_point[0])+'中的小孔:' + str(distance_step_2))
    # log[2]
    log_list.append('2. 进入'+from_name+'的72芯配线单元'+PEIXIAN_DANYUAN[from_point[0]]+'组合线环的小孔。')
    if int(from_point[0]) <= 4:
        pic_step3 = (250, 360 + 160 * (int(from_point[0])-1))
    elif int(from_point[0]) > 4 and int(from_point[0]) <= 8:
        pic_step3 = (250, 360 + 160 * (int(from_point[0]) - 1) + 340)
    elif int(from_point[0]) > 8 and int(from_point[0]) <= 12:
        pic_step3 = (250, 360 + 160 * (int(from_point[0]) - 1) + 340 * 2)
    step_list.append(pic_step3)  # [2]
    print('pic_step3'+str(pic_step3))
    # json[2]
    json_list.append(PEIXIAN_DANYUAN[from_point[0]]+'-小孔')

    # 3. 进入组合线环#XX+1的大孔
    if from_point[0] == '4' or from_point[0] == '8':
        distance_step_3 = 527  # 每四个之间相距527mm
    else:
        distance_step_3 = 169  # 组合线环之间相距169mm
    print('3. 进入组合线环'+str(int(from_point[0])+1)+'中的大孔:'+str(distance_step_3))
    # log[3]
    log_list.append('3. 进入'+from_name+'的72芯配线单元'+PEIXIAN_DANYUAN[str(int(from_point[0])+1)]+'组合线环的大孔。')
    if int(from_point[0]) + 1 <= 4:
        pic_step4 = (250, 360 + 160 * int(from_point[0]))
        pic_step5 = (1080, 340 + 160 * int(from_point[0]))
    elif int(from_point[0]) + 1 > 4 and int(from_point[0]) + 1 <= 8:
        pic_step4 = (250, 360 + 160 * int(from_point[0]) + 340)
        pic_step5 = (1080, 340 + 160 * int(from_point[0]) + 340)
    elif int(from_point[0]) + 1 > 8 and int(from_point[0]) + 1 <= 12:
        pic_step4 = (250, 360 + 160 * int(from_point[0]) + 340 * 2)
        pic_step5 = (1080, 340 + 160 * int(from_point[0]) + 340 * 2)
    step_list.append(pic_step4)  # [3]
    step_list.append(pic_step5)  # [4]
    print('pic_step4:'+str(pic_step4))
    print('pic_step5:'+str(pic_step5))
    # json[3]
    json_list.append(PEIXIAN_DANYUAN[str(int(from_point[0])+1)]+'-大孔')

    # 4. 往上至高于from_point的挂纤轮，再往下走直到侧面最下面那个挂纤轮调头向上走
    wheel_above = []
    wheel_bottom = []
    for wheel_d in WHEEL_DISTANCE:
        if (wheel_d + WHEEL_D) > (COMBINATION_RING[from_point[0]]):
            wheel_above.append(wheel_d)
    wheel_above.sort()
    print('穿过大孔后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。')
    distance_step_4_1 = wheel_above[0]+WHEEL - COMBINATION_RING[str(int(from_point[0])+1)]
    # 高挂纤轮到from_point大线环2
    distance_step_4_2 = wheel_above[0]+WHEEL - (BIGLINE2_DISTANCE[from_point[0]]+LINE)
    print('往下到'+from_name+'96芯设备单元'+from_name[0]+'的大线环2')
    # 大线环2到水平走线槽边缘42mm，经过几个走线槽到from_point大线环2
    distance_step_4_3 = (shebei_count-1) * 748 + 42
    print('沿水平走线槽经过'+str(shebei_count-1)+'个机架到'+to_name+'96芯设备单元'+from_point[0]+'的大线环2')
    # 大线环2到机架2高挂纤轮
    distance_step_4_4 = wheel_above[0]+WHEEL - (BIGLINE2_DISTANCE[from_point[0]]+LINE)
    print('从大线环2穿出，往上到'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。')
    distance_step_4 = distance_step_4_1 + distance_step_4_2 + distance_step_4_3 + distance_step_4_4
    # 高挂纤轮到最下面的挂纤轮
    print('再到最下面的挂纤轮')
    distance_step_5_1 = wheel_above[0]+WHEEL - WHEEL_DISTANCE[-1]
    # 调头向上到高于to_point的挂纤轮
    for wheel_d in WHEEL_DISTANCE:
        if (wheel_d + WHEEL_D) > (COMBINATION_RING[to_point[0]]):
            wheel_bottom.append(wheel_d)
    wheel_bottom.sort()
    print('调头向上经过'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')
    distance_step_5_2 = wheel_bottom[0] + WHEEL - WHEEL_DISTANCE[-1]
    distance_step_5 = distance_step_5_1 + distance_step_5_2
    # log[4]
    log_list.append('1. 从'+from_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(from_point[0])+1)]+'的大孔穿出后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。')
    # log[5]
    log_list.append('2. 往下到'+from_name+'96芯设备单元'+from_point[0]+'的大线环2。')
    # log[6]
    log_list.append('1. 从'+from_name+'96芯设备单元'+from_point[0]+'的大线环2出来后，'+'沿水平走线槽经过'+str(shebei_count-1)+'个机架到'+to_name+'96芯设备单元'+from_point[0]+'的大线环2'+\
                    '从大线环2穿出，往上到'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。再到最下面的挂纤轮。调头向上经过'+\
                    to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。')

    pic_step6 = (590, 230 + (WHEEL_DISTANCE.index(wheel_above[0])+1-1) * 215)  # wheel_above
    pic_step7 = (590, 230 + (WHEEL_DISTANCE.index(wheel_bottom[0])+1-1) * 215)  # wheel_bottom
    step_list.append(pic_step6)  # [5]
    step_list.append(pic_step7)  # [6]
    print('pic_step6:' + str(pic_step6))
    print('pic_step7:' + str(pic_step7))
    # json[4]
    json_list.append('挂纤轮-'+str(WHEEL_DISTANCE.index(wheel_above[0])+1))
    json_list.append('挂纤轮-13')  # json[5]
    json_list.append('挂纤轮-'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1))  # json[6]


    # 5. 往下进入to_point组合线环#XX+1的大孔
    if int(to_point[0]) < 12:
        distance_step_6 = wheel_bottom[0]+WHEEL - COMBINATION_RING[str(int(to_point[0])+1)]
        print('2. 往下进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(to_point[0])+1)]+'组合线环的大孔。')
        # log[6]
        log_list.append('2. 往下进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(to_point[0])+1)]+'组合线环的大孔。')
        json7 = PEIXIAN_DANYUAN[str(int(to_point[0])+1)]
        if int(to_point[0])+1 <= 4:
            pic_step8 = (1080, 340 + 160 * int(to_point[0]))
        elif int(to_point[0])+1 > 4 and int(to_point[0])+1 <= 8:
            pic_step8 = (1080, 340 + 160 * int(to_point[0]) + 340)
        elif int(to_point[0])+1 > 8 and int(to_point[0])+1 <= 12:
            pic_step8 = (1080, 340 + 160 * int(to_point[0]) + 340 * 2)
    elif int(to_point[0]) == 12:
        distance_step_6 = wheel_bottom[0]+WHEEL - COMBINATION_RING[str(int(to_point[0]))]
        print('2. 往下进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(to_point[0]))]+'组合线环的大孔。')
        # log[8]
        log_list.append('2. 往下进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(to_point[0]))]+'组合线环的大孔。')  # log[5]
        json7 = PEIXIAN_DANYUAN[str(int(to_point[0]))]
        if int(to_point[0]) <= 4:
            pic_step8= (1080, 340 + 160 * (int(to_point[0])-1))
        elif int(to_point[0]) > 4 and int(to_point[0]) <= 8:
            pic_step8 = (1080, 340 + 160 * (int(to_point[0])-1) + 340)
        elif int(to_point[0]) > 8 and int(to_point[0]) <= 12:
            pic_step8 = (1080, 340 + 160 * (int(to_point[0])-1) + 340 * 2)
    step_list.append(pic_step8)  # [7]
    print('pic_step8:' + str(pic_step8))
    # json[7]
    json_list.append(json7+'-大孔')

    # 6. 再向上进入to_point组合线环#XX的小孔
    if int(to_point[0]) < 12 :
        distance_step_7 = COMBINATION_RING[to_point[0]] - COMBINATION_RING[str(int(to_point[0])+1)]
        if int(to_point[0]) <= 4:
            pic_step9 = (1080, 340 + 160 * (int(to_point[0]) - 1))
        elif int(to_point[0]) > 4 and int(to_point[0]) <= 8:
            pic_step9 = (1080, 340 + 160 * (int(to_point[0]) - 1) + 340)
        elif int(to_point[0]) > 8 and int(to_point[0]) <= 12:
            pic_step9 = (1080, 340 + 160 * (int(to_point[0]) - 1) + 340 * 2)
    elif int(to_point[0]) == 12:
        distance_step_7 = 0
        pic_step9 = (pic_step8[0], pic_step8[1])
    step_list.append(pic_step9)  # [8]
    print('pic_step9:'+str(pic_step9))
    print('3. 再进入' + to_name + '72芯配线单元' + PEIXIAN_DANYUAN[str(int(to_point[0]))] + '组合线环的小孔。')
    # log[9]
    log_list.append('3. 再进入' + to_name + '72芯配线单元' + PEIXIAN_DANYUAN[str(int(to_point[0]))] + '组合线环的小孔。')
    # json[8]
    json_list.append(PEIXIAN_DANYUAN[str(int(to_point[0]))]+'-小孔')

    # 7. 往右进入指定托盘
    distance_step_8 = 34 + 26 * (6 - int(to_point[1])) + 84 + 20.5 * (int(to_point[2])-1)
    print('1. 往右进入'+to_name+'的'+str(to_point[0])+'号72芯配线单元的('+str(to_point[1])+','+str(to_point[2])+')托盘:'+str(distance_step_8))
    # log[10]
    log_list.append('1. 从'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[to_point[0]]+'组合线环的小孔出穿出。')
    # log[11]
    log_list.append('2. 往右进入'+to_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(to_point[0])]+'('+str(to_point[1])+','+str(to_point[2])+')端口。')

    if int(to_point[0]) <= 4:
        pic_step10 = (250, 360 + 160 * (int(to_point[0])-1))
        pic_step12 = (325 + (int(to_point[2]) - 1) * 20, 205 + (int(to_point[0]) - 1) * 160 + (int(to_point[1]) - 1) * 25)
    elif int(to_point[0]) > 4 and int(to_point[0]) <= 8:
        pic_step10 = (250, 360 + 160 * (int(to_point[0]) - 1) + 340)
        pic_step12 = (325 + (int(to_point[2]) - 1) * 20, 205 + (int(to_point[0]) - 1) * 160 + (int(to_point[1]) - 1) * 25 + 335)
    elif int(to_point[0]) > 8 and int(to_point[0]) <= 12:
        pic_step10 = (250, 360 + 160 * (int(to_point[0]) - 1) + 340 * 2)
        pic_step12 = (325 + (int(to_point[2]) - 1) * 20, 205 + (int(to_point[0]) - 1) * 160 + (int(to_point[1]) - 1) * 25 + 335 * 2)
    pic_step11 = (250, pic_step12[1])
    step_list.append(pic_step10)
    step_list.append(pic_step11)
    step_list.append(pic_step12)
    print('pic_step10:'+str(pic_step10))
    print('pic_step11:'+str(pic_step11))
    print('pic_step12:'+str(pic_step12))
    # json[9]
    json_list.append(PEIXIAN_DANYUAN[to_point[0]]+'('+to_point[1]+','+to_point[2]+')')

    used_distance = distance_step_1 + distance_step_2 + distance_step_3 + distance_step_4 + \
                    distance_step_5 + distance_step_6 + distance_step_7 + distance_step_8
    print('总共需要线长：' + str(used_distance))
    cable_list = []
    for cable in CABLE_LENGTH:
        if cable > used_distance:
            cable_list.append(cable)
    cable_list.sort()
    shengyu_xianchang = cable_list[0] - used_distance
    print('剩余线长：' + str(shengyu_xianchang))

    # 调整上下挂纤轮
    index_above = ''
    index_bottom = ''
    if shengyu_xianchang > 456:
        if WHEEL_DISTANCE.index(wheel_above[0]) != 0:
            i = WHEEL_DISTANCE.index(wheel_above[0]) - 1
            while i >= 0:
                if shengyu_xianchang - (WHEEL_DISTANCE[i] - wheel_above[0]) * 2 > 0:
                    index_above = i
                    break
                else:
                    i -= 1
            if index_above != '':
                wheel_above[0] = WHEEL_DISTANCE[index_above]
                print('调整上挂纤轮为：' + str(index_above+1))

            distance_step_4_4 = wheel_above[0] + WHEEL - (BIGLINE2_DISTANCE[from_point[0]]+LINE)
            distance_step_4 = distance_step_4_1 + distance_step_4_2 + distance_step_4_3 + distance_step_4_4
            distance_step_5_1 = wheel_above[0] + WHEEL - WHEEL_DISTANCE[-1]
            distance_step_5 = distance_step_5_1 + distance_step_5_2
            used_distance = distance_step_1 + distance_step_2 + distance_step_3 + distance_step_4 + \
                    distance_step_5 + distance_step_6 + distance_step_7 + distance_step_8
            shengyu_xianchang = cable_list[0] - used_distance
            print('剩余线长2：' + str(shengyu_xianchang))

    if shengyu_xianchang > 456:
        if WHEEL_DISTANCE.index(wheel_bottom[0]) != 0:
            i = WHEEL_DISTANCE.index(wheel_bottom[0]) - 1
            while i >= 0:
                if shengyu_xianchang - (WHEEL_DISTANCE[i] - wheel_bottom[0]) * 2 > 0:
                    index_bottom = i
                    break
                else:
                    i -= 1
            if index_bottom != '':
                wheel_bottom[0] = WHEEL_DISTANCE[index_bottom]
                print('调整下挂纤轮为：' + str(index_bottom+1))

            distance_step_5_2 = wheel_bottom[0] + WHEEL - WHEEL_DISTANCE[-1]
            distance_step_5 = distance_step_5_1 + distance_step_5_2
            used_distance = distance_step_1 + distance_step_2 + distance_step_3 + distance_step_4 + \
                            distance_step_5 + distance_step_6 + distance_step_7 + distance_step_8
            shengyu_xianchang = cable_list[0] - used_distance
            print('剩余线长3：' + str(shengyu_xianchang))
    log_list[4] = '1. 从'+from_name+'72芯配线单元'+PEIXIAN_DANYUAN[str(int(from_point[0])+1)]+'的大孔穿出后，往上经过'+from_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。'
    log_list[5] = '2. 往下到'+from_name+'96芯设备单元'+from_point[0]+'的大线环2。'
    log_list[6] = '1. 从'+from_name+'96芯设备单元'+from_point[0]+'的大线环2出来后，'+'沿水平走线槽经过'+str(shebei_count-1)+'个机架到'+to_name+'96芯设备单元'+from_point[0]+'的大线环2'+\
                    '从大线环2穿出，往上到'+to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_above[0])+1)+'个挂纤轮。再到最下面的挂纤轮。调头向上经过'+\
                    to_name+'侧面第'+str(WHEEL_DISTANCE.index(wheel_bottom[0])+1)+'个挂纤轮。'
    # step_list[5] = (180, 260 + (WHEEL_DISTANCE.index(wheel_above[0]) + 1 - 1) * 215)  # wheel_above
    step_list[5] = (590, 230 + (WHEEL_DISTANCE.index(wheel_above[0])+1-1) * 215)  # wheel_above
    step_list[6] = (590, 230 + (WHEEL_DISTANCE.index(wheel_bottom[0]) + 1 - 1) * 215)  # wheel_bottom
    print('请选择一根长度为：' + str(int(cable_list[0] / 1000)) + '米的网线。')
    log_list.append('请选择一根长度为：' + str(int(cable_list[0] / 1000)) + '米的网线。')  # log[12]
    # json[4]
    json_list[4] = '挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_above[0]) + 1)
    # json_list[5] = '挂纤轮-13'  # json[5]
    json_list[6] = '挂纤轮-' + str(WHEEL_DISTANCE.index(wheel_bottom[0]) + 1)  # json[6]

    pic_step13 = (235,550+(int(from_point[0])-1)*320)
    step_list.append(pic_step13)  # [12]

    print(step_list)
    print(log_list)
    return step_list, log_list, json_list