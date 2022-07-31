import numpy as np
import random


def manual_lotto_method(my_num):
    my_num = sorted(my_num)
    lotto_count = 0
    while(True):
        lotto_num = []
        while(True):
            if len(lotto_num) == 7 :
                break
            rand_num = random.randint(1,46)        
            if not rand_num in lotto_num :
                lotto_num.append(rand_num)

        lotto_num = sorted(lotto_num)
        print('mynum : {} lotto_num : {}'.format(my_num, lotto_num))
        lotto_count += 1
        if my_num == lotto_num :
            print("congradulate, number : ", lotto_count)
            print("you spended {} won".format(lotto_count * 1000))
            break
        else :
            print("next time : ", lotto_count)
        

def auto_lotto_method(lotto_week_count):
    seed_num = random.randint(1,1000)
    random.seed(seed_num)
    lotto_range = [1,46]
    lotto_count = 0
    while(True):
        my_nums = []
        for i in range(lotto_week_count) :
            my_num = []
            while(True):
                if len(my_num) == 7 :
                    my_num = sorted(my_num)
                    my_nums.append(my_num)
                    break
                rand_num = random.randint(lotto_range[0],lotto_range[1])
                if not rand_num in my_num :
                    my_num.append(rand_num)                    
        
        lotto_num = []
        while(True):
            if len(lotto_num) == 7 :
                break
            rand_num = random.randint(lotto_range[0],lotto_range[1])        
            if not rand_num in lotto_num :
                lotto_num.append(rand_num)

        lotto_num = sorted(lotto_num)
        lotto_count += 1
        for i in range(lotto_week_count):
            if my_nums[i] == lotto_num :
                print("congradulate, won number : ", lotto_count)
                print('seed : {}, my numbers : {}, lotto number : {}'.format(seed_num, my_nums,lotto_num))
                print("you spended {} won".format(lotto_count * 1000 * lotto_week_count))
                return lotto_count
        #print("you spended {} won".format(lotto_count * 1000 * lotto_week_count))

if __name__ == "__main__" :
    my_num = [1,2,3,4,5,6,7]
    lotto_spend_money = []
    for i in range(100) :
        spend_money = auto_lotto_method(5)
        print('{} try : spend money : {}'.format(i,spend_money))
        lotto_spend_money.append(spend_money)
    print('mean spend money : ', np.mean(lotto_spend_money))
    #manual_lotto_method(my_num)