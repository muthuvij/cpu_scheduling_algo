def sjf(pid,at,bt):
    print("Gantt Chart :")
    process={}
    gantt=[]
    for i in range(len(pid)):
        process[pid[i]]=[at[i],bt[i]]
    start=0
    while process!={}:
        short_pro=''
        short_job=1000
        for i in process:
            if process[i][0]<=start and process[i][1]<short_job:
                short_job=process[i][1]
                short_pro=i
        if short_pro=='':
            gantt.append('IDLE')
            start+=1
        else:
            for i in range(process[short_pro][1]):
                gantt.append(short_pro)
                start+=1
            del process[short_pro]
    print(gantt)
    tat=[]
    wt=[]
    print("Process\t AT\tBT\tTAT\t WT")
    for i in range(len(pid)):
        l=len(gantt)
        for k in range(l-1,-1,-1):
            if gantt[k]==pid[i]:
                tat.append(k+1-at[i])
                wt.append(tat[i]-bt[i])
                break
    for i in range(len(pid)):
        print(pid[i],"\t",at[i], "\t", bt[i], "\t", tat[i],"\t",wt[i])
    print("Average TAT = ",sum(tat)/len(tat))
    print("Average WT = ",sum(wt)/len(wt))

sjf(['p1','p2','p3','p4','p5'],[3,1,4,0,2],[1,4,2,6,3])
