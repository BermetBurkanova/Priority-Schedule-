def scheduling_al():
    prc = int(input("Enter the number of processes: "))
    a=[]
    ave_wt = 0
    ave_tat = 0
    for i in range(prc):
        b = []
        print("Enter the name of ",i+1 , "process")
        name = input()
        arrival = int(input("Enter the arrival time: "))
        burst = int(input("Enter the burst time: "))
        priority = int(input("Enter the priority time: "))
        b.append(name)
        b.append(arrival)
        b.append(burst)
        b.append(priority)
        a.append(b)
    print(a)


    for i in range(len(a)):
        if a[i-1][-1]>a[i][-1]:
            (a[i-1],a[i])=(a[i], a[i-1])
        print (a)
    print("Pname \t Arrival Time \t Execution \t Priority \t Waiting time \t TAT\n")
    for i in range (len(a)):
        if i-1<0:
            waiting = 0
        elif a[i-1][1]-a[i][1]>0:
            waiting = a[i-1][1]-a[i][1]+ a[i-1][2]+waiting
        else:
            waiting = waiting + a[i-1][2]
        ave_wt = + waiting
        turnaround = waiting + a[i][2]
        ave_tat = +turnaround
        print(str(a[i][0])+"\t"+" "+str(a[i][1])+"\t"+"\t"+str(a[i][2])+ "\t \t"+str(a[i][3])+"\t \t \t"+str(waiting)+"\t"+str(turnaround)+"\n")
    ave_wt= ave_wt/prc
    ave_tat= ave_tat/prc
    print("Average waiting time is:" + str(ave_wt))
    print("Average turnaround time is:" + str(ave_tat))
def scheduling_al():
    prc = int(input("Enter the number of processes: "))
    a=[]
    ave_wt = 0
    ave_tat = 0
    for i in range(prc):
        b = []
        print("Enter the name of ",i+1 , "process")
        name = input()
        arrival = int(input("Enter the arrival time: "))
        burst = int(input("Enter the burst time: "))
        priority = int(input("Enter the priority time: "))
        b.append(name)
        b.append(arrival)
        b.append(burst)
        b.append(priority)
        a.append(b)
    print(a)


    for i in range(len(a)):
        if a[i-1][-1]>a[i][-1]:
            (a[i-1],a[i])=(a[i], a[i-1])
        print (a)
    print("Pname \t Arrival Time \t Execution \t Priority \t Waiting time \t TAT\n")
    for i in range (len(a)):
        if i-1<0:
            waiting = 0
        elif a[i-1][1]-a[i][1]>0:
            waiting = a[i-1][1]-a[i][1]+ a[i-1][2]+waiting
        else:
            waiting = waiting + a[i-1][2]
        ave_wt = + waiting
        turnaround = waiting + a[i][2]
        ave_tat = +turnaround
        print(str(a[i][0])+"\t"+" "+str(a[i][1])+"\t"+"\t"+str(a[i][2])+ "\t \t"+str(a[i][3])+"\t \t \t"+str(waiting)+"\t"+str(turnaround)+"\n")
    ave_wt= ave_wt/prc
    ave_tat= ave_tat/prc
    print("Average waiting time is:" + str(ave_wt))
    print("Average turnaround time is:" + str(ave_tat))
