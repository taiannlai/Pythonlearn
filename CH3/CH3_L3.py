dist = 384400   #地球到月球的距離
speed = 250     #火箭每分鐘的速度
total_min = dist // speed #需要多少分鐘
total_hours, mins = divmod(total_min, 60)
days, hours = divmod(total_hours, 24)
print("多少天")
print(days)
print("多少小時")
print(hours)
print("多少分鐘")
print(mins)
