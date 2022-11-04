hour, minute = map(int, input().split())
seconds = int(input())

minute = minute+seconds
if(minute>=60):
    remain = minute%60
    extrahour = minute//60
    minute = remain
    hour = hour+extrahour
    if(hour>23):
        hour = hour-24;
        
print(hour, minute)