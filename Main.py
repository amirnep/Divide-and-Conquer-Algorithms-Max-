#Algorithm Design: Dr. Pira
#Chapter1 Project by Amir Nematpour - 981830281
#Shahid Madani University

import Class as c

arr_num = [] #Array for save numbers

n = int(input("Plaese Enter How Many Numbers Do You Want: "))

for _ in range (n):
    num = int(input("Please Enter number: "))
    arr_num.append(num)

if __name__ == '__main__':
    
    answer = c.find(arr_num)

    print()
    print(c.find.findmax.__doc__)
    print("Maximum is: ",max(answer.findmax())) #Find max
    print()

quit = input("If You Want To Exit Please Press Enter.")
