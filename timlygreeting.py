import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
timestamph=int(time.strftime('%H'))
print(timestamph)
timestampm=int(time.strftime('%M'))
print(timestampm)
timestamps=int(time.strftime('%S'))
print(timestamps)
if(5<=timestamph<12 ):
    print("Good Morning 🌅")
          
elif(12<=timestamph<17):

  print("Good Afternoon ☀️")
elif(17<=timestamph<21):
   
    print("Good Evening 🌇")
 
else:
 print("Good Night 🌙")