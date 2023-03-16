# answer = int(input("What is 4 * 7? "))
# if answer == 28:
#     print("Correct!")
# else:
#     print("Incorrect!")
# 
# hour = int(input("Enter the hour: "))
# minute = int(input("Enter the minute: "))
# amorpm = (input("am or pm? "))
# 
# if amorpm == "am" and hour == 12:
#     hour -= 12
# if amorpm == "pm" and hour != 12:
#     hour += 12
# if minute < 10:
#     print(hour,":0",minute,sep="")
# else:
#     print(hour,":",minute,sep="")
#     
# day = input("What day is the event? ")
# timestart = int(input("What time does it start? "))
# timeend = int(input("What time does it end? "))
# 
# if day == "Monday" or day == "Wednesday" or day == "Friday" and timestart <= 12 and timeend >= 1:
#     print("Your event overlaps!")
# else:
#     print("your event doesn't overlap!")
#     
a = bool(int(input("Enter a: ")))
b = bool(int(input("Enter b: ")))
print(a)
print(b)
if a == True:
    if b == True:
        xor = 0
    else:
        xor = 1
if a == False:
    if b == False:
        xor = 0
    else:
        xor = 1


print("a XOR b is", bool(xor))
    