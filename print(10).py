import numpy as np
import pandas as pd
import random
import math
def is_in_the_board(a):
    if a[0]>=1 and a[0]<=9 and a[1]>=1 and a[1]<=18:
        return True
    else:
        return False    
def rand_location():
    location = [random.randint(1,9),random.randint(1,18)]
    while boardGame[location[0],location[1]] == '|':
        location = [random.randint(1,9),random.randint(1,18)]
    return location
def rand_move(location):
    m1 = location[0]
    m2 = location[1]
    move = random.randint(1,4)
    if move == 1:
        m1 += 1
    elif move == 2:
        m1 -= 1
    elif move == 3:
        m2 += 1
    else:
        m2 -= 1
    if boardGame[m1,m2] == '|' and not is_in_the_board([m1,m2]):
        m1 = location[0]
        m2 = location[1]
    return [m1,m2]
def get_score():
    score = point * 10 #- moveeeeee
    return score
def end_game():
    end = False
    if p == s1 or p == s2:
        print("lose")
        end = True
    elif point == 88:
        print("win")
        end = True
    return end
def distance(a,b):
    return math.sqrt(((a[0] - b[0])*(a[0] - b[0])) + ((a[1] - b[1])*(a[1] - b[1])))
def closest_point(a):
    r = 1
    b = [a[0]-r, a[1]-r]
    while r<18:
        for i in range(a[0]-r,a[0]+r):
            for j in {a[1]-r, a[1]+r}:   
                if is_in_the_board([i,j]):
                    if boardGame[i,j]=='1':
                        return r
                if is_in_the_board([j,i]):
                    if boardGame[j,i]=='1':
                        return r
        r += 1
    return 20
def utility(a,b,c):
    distance_importance_factor = 2
    if distance(a,b) == 0 or distance(a,c) == 0:
        return -10000
    utility_a_b_c = 0
    #importance distance of pack_man with souls
    #and souls with each other
    utility_a_b_c -= distance_importance_factor * (distance(b,c) / (distance(a, b) + distance(a, c)))
    #move toward closest point
    utility_a_b_c += 2 * distance_importance_factor * closest_point(a)
    return utility_a_b_c
def max_move(a,b,c,step,point_number):
    aa = [[a[0]+1,a[1]],[a[0]-1,a[1]],[a[0],a[1]],[a[0],a[1]+1],[a[0],a[1]-1]]
    mm = [-10000000,-100000000,-1000000000,-10000000000000,-10000000000000]
    for i in range(0,4):
        if is_in_the_board(aa[i]) and boardGame[aa[i][0],aa[i][1]] != '|':
            if boardGame[aa[i][0],aa[i][1]] == '1':
                mm[i] = min_move1(aa[i],b,c,step,point_number)[0] + poitn_importance
            else:
                mm[i] = min_move1(aa[i],b,c,step,point_number)[0] - poitn_importance                
    max = mm[0]
    move = aa[0]
    for i in range(1,4):
        if max < mm[i]:
            max = mm[i]
            move = aa[i]
    move = [move[0]-a[0],move[1]-a[1]]
    return [max,move]
def min_move1(a,b,c,step,point_number):
    bb = [[b[0]+1,b[1]],[b[0]-1,b[1]],[b[0],b[1]],[b[0],b[1]+1],[b[0],b[1]-1]]
    mm = [10000,10000,10000,10000,10000]
    for i in range(0,4):
        if is_in_the_board(bb[i]):
            mm[i] = min_move2(a,bb[i],c,step,point_number)[0]  
    min = mm[0]
    move = bb[0]
    for i in range(1,4):
        if min > mm[i]:
            min = mm[i]
            move = bb[i]
    return[min,move]
def min_move2(a,b,c,step,point_number):
    if step == 0 :
        return [(utility(a,b,c) + (point_number * poitn_importance)),[0,0]]
    else :
        new_poin_number = point_number
        if boardGame[a[0],a[1]] == '1':
            new_poin_number += 1
        cc = [[c[0]+1,c[1]],[c[0]-1,c[1]],[c[0],c[1]],[c[0],c[1]+1],[c[0],c[1]-1]]
        mm = [10000,10000,10000,10000,10000]
        for i in range(0,4):
            if is_in_the_board(cc[i]):
                mm[i] = max_move(a,b,cc[i],step-1,new_poin_number)[0]  
        min = mm[0]
        move = cc[0]
        for i in range(1,4):
            if min > mm[i]:
                min = mm[i]
                move = cc[i]
        return[min,move]
def pack_man_move():
    return max_move(p,s1,s2,1,0)[1]
def update(p_new_location):
    if boardGame[p_new_location[0],p_new_location[1]] == '1':
        boardGame[p_new_location[0],p_new_location[1]] = '0'
        point += 1
    moveeeeee += 1
    round += 1
        

boardGame = np.array([['|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|'],
                     ['|','1','1','1','1','|','1','1','1','1','1','1','1','1','|','1','1','1','1','|'],
                     ['|','1','|','|','1','|','1','|','|','|','|','|','|','1','|','1','|','|','1','|'],
                     ['|','1','|','1','1','1','1','1','1','1','1','1','1','1','1','1','1','|','1','|'],
                     ['|','1','|','1','|','|','1','|','|','0','0','|','|','1','|','|','1','|','1','|'],
                     ['|','1','1','1','1','1','1','|','0','0','0','0','|','1','1','1','1','1','1','|'],
                     ['|','1','|','1','|','|','1','|','|','|','|','|','|','1','|','|','1','|','1','|'],
                     ['|','1','|','1','1','1','1','1','1','1','1','1','1','1','1','1','1','|','1','|'],
                     ['|','1','|','|','1','|','1','|','|','|','|','|','|','1','|','1','|','|','1','|'],
                     ['|','1','1','1','1','|','1','1','1','1','0','1','1','1','|','1','1','1','1','|'],
                     ['|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|','|']])
p = [10,9]
moveeeeee = 0
point = 0
s1 = rand_location()
s2 = rand_location()
round = 0
poitn_importance = 200
while not end_game() :#and round < 120:
    round += 1
    s1 = rand_move(s1)
    s2 = rand_move(s2)
    p_move = pack_man_move()
    p = [p[0]+p_move[0],p[1]+p_move[1]]
    if boardGame[p[0],p[1]] == '1':
        boardGame[p[0],p[1]] = '0'
        point += 1
    moveeeeee += 1


    print("__________________________________________")
    print("round:",round)
    print("pack-man:",p)
    print(get_score())
    print("s1:",s1)
    print("s2:",s2)