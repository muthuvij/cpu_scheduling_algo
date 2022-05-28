def rorb(pid,at,bt,tq):
    print("Gantt Chart :")
    process={}
    gantt=[]
    for i in range(len(pid)):
        process[pid[i]]=[at[i],bt[i],0]
    start=0
    check=0
    while process!={}:
        curr_job=''
        for i in process:
            if process[i][0]<=start and process[i][2]==0:
                curr_job=i
                break
        if curr_job=='':
            if check==1:
                gantt.append('IDLE')
                start+=1
            elif check==0:
                for i in process:
                    process[i]=[process[i][0],process[i][1],0]
                check=1
        else:
            if(process[curr_job][1]<=tq):
                for i in range(process[curr_job][1]):
                    gantt.append(curr_job)
                    start+=1
                del process[curr_job]
            else:
                for i in range(tq):
                    gantt.append(curr_job)
                    start+=1
                process[curr_job]=[process[curr_job][0],process[curr_job][1]-tq,1]
            check=0
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
    print("Time Quantum =",tq)
    print("Average TAT = ",sum(tat)/len(tat))
    print("Average WT = ",sum(wt)/len(wt))

rorb(['p1','p2','p3','p4','p5'],[0,11,12,3,14],[5,3,1,2,3],2)
