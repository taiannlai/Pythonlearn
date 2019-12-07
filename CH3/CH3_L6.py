dist = 384400   #地球到月亮的距離
speed = 1225    #馬赫速度每小時1225公里
total_hours, total_mins = divmod(dist, speed)
mins, second = divmod(total_mins, 60)
days, hours = divmod(total_hours, 24)
print('總共需要多少天')
print(days)
print('幾小時')
print(hours)
print('幾分鐘')
print(mins)
print('幾秒鐘')
print(second)