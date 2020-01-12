dist = 384400   #地球到月亮的距離
speed = input("請輸入馬赫數：")    #馬赫速度每小時1225公里
total_hours = dist // int(speed) #計算小時數
days = total_hours // 24    #計算多少天會到
hours = total_hours % 24    #計算最後剩多少小時數
print('總共需要多少天')
print(days)
print('幾小時')
print(hours)