import random
import sys


CONTINUE=0
FINISH=1
ERROR=2

def great_and_good(answers):
    
    
    #入力受付
    in_num=input()

    great_count=0
    good_count=0
    numbers=[]
    error=0
    
    

    if is_notint(in_num):
        print("半角数字を入力してください", end="\n")
        error=1
    else:
        numbers= list(in_num)
    if len(numbers)!=len(answers):
       print("桁数が違います", end="\n")
       error=1
    else:
        numbers=[int(i) for i in numbers]
    if check_duplicate(numbers):
        print("同じ数字が入っています", end="\n")
        error=1
    
    if error==0:
        for index, num in enumerate(numbers):
            if num==answers[index]:
                great_count=great_count+1
            elif num in answers:
                good_count=good_count+1
            
        print("great:", great_count)
        print("good :", good_count, end="\n\n")
        if great_count==3:
            print("正解です！！")
            return FINISH
        else:
            
            return CONTINUE
    else:
        
        return ERROR

def is_notint(string):
    try:
        int(string)
    except ValueError:
        return True
    else:
        return False

def check_duplicate(in_list):
    cp_list=in_list.copy()
    for i in range(len(cp_list)):
        poped=cp_list.pop()
        flag=(poped in cp_list)
        if flag:
            return True
    return False



def generate_answer():
    answers= [random.randint(0, 9) for i in range(0, 3)]
    while check_duplicate(answers):
        answers= [random.randint(0, 9) for i in range(0, 3)]
    
    return answers

#答えの生成
answers=generate_answer()

def playgame(answers):
    playlimit=10
    games_count=1

    while (games_count!=playlimit+1):
        print("Great&Good を開始します。")
        print("{} 回目のチャレンジ".format(games_count))
        print(("3桁の数字を入力してください："))
        flag=great_and_good(answers)

        if flag==FINISH:
            break
        elif flag==ERROR:
            continue
        else:
            games_count=games_count+1
    else:
        answer=int("".join(map(str, answers)))
        print("残念、違います。")
        print("答えは{}でした。".format(answer))


playgame(answers)