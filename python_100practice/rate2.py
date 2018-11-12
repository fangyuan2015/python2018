#!/usr/bin/env python
#coding=utf-8
#企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

while True:
    profit = input("请输入当月利润:\n")
    if profit <= 100000:
        reward = profit * 0.1
        
        print "you profit is %d ,and reward is %d" %(profit,reward)
    
    elif 200000 > profit > 100000:
        reward = (profit - 100000) * 0.1 + 100000 * 0.075
        print "you profit is %d ,and reward is %d" %(profit,reward)
    elif 200000 <= profit < 400000:
        reward = (profit - 200000) * 0.05
        print "you profit is %d ,and reward is %d" %(profit,reward)
    elif 400000 <= profit < 600000:
        reward = (profit - 400000) * 0.03
        print "you profit is %d ,and reward is %d" %(profit,reward)
    elif 60000 <= profit <= 1000000:
        reward = (profit - 600000) * 0.015
        print "you profit is %d ,and reward is %d" %(profit,reward)
    elif profit > 1000000:
        reward = (profit - 1000000) * 0.01
        print "you profit is %d ,and reward is %d" %(profit,reward)
    else:
        print "please input new"

    
    
    
        
