def priwp(pid,at,bt,pri):
    print("Gantt Chart :")
    process={}
    gantt=[]
    for i in range(len(pid)):
        process[pid[i]]=[at[i],bt[i],pri[i]]
    start=0
    while process!={}:
        high_pri_job=''
        high_pri=-1000
        for i in process:
            if process[i][0]<=start and process[i][2]>high_pri:
                high_pri_job=i
                high_pri=process[i][2]
        if high_pri_job=='':
            gantt.append('IDLE')
            start+=1
        else:
            gantt.append(high_pri_job)
            process[high_pri_job]=[process[high_pri_job][0],process[high_pri_job][1]-1,process[high_pri_job][2]]
            start+=1
            if process[high_pri_job][1]==0:
                del process[high_pri_job]
    print(gantt)
    tat=[]
    wt=[]
    print("Process\t AT\tBT\tPriority TAT\t WT")
    for i in range(len(pid)):
        l=len(gantt)
        for k in range(l-1,-1,-1):
            if gantt[k]==pid[i]:
                tat.append(k+1-at[i])
                wt.append(tat[i]-bt[i])
                break
    for i in range(len(pid)):
        print(pid[i],"\t",at[i], "\t", bt[i], "\t",pri[i], "\t", tat[i],"\t",wt[i])
    print("Average TAT = ",sum(tat)/len(tat))
    print("Average WT = ",sum(wt)/len(wt))

priwp(['p1','p2','p3','p4','p5'],[0,1,2,3,4,5],[4,3,1,5,2],[2,3,4,5,5])
