def fcfs(pid,at,bt):
    print("Gantt Chart :")
    dpid=[]
    dat=[]
    dbt=[]
    for i in range(len(pid)):
        dpid.append(pid[i])
        dat.append(at[i])
        dbt.append(bt[i])
    l=len(pid)
    gantt=[]
    s=0
    for i in range(l):
        ind=at.index(min(at))
        if min(at)>s:
            for m in range(s,min(at)):
                gantt.append("IDLE")
        for j in range(s,s+bt[ind]):
            gantt.append(pid[ind])
        s+=bt[ind]
        pid.pop(ind)
        at.pop(ind)
        bt.pop(ind)
    print(gantt)
    tat=[]
    wt=[]
    print("Process\t AT\tBT\tTAT\tWT")
    for i in range(len(dpid)):
        l=len(gantt)
        for k in range(l-1,-1,-1):
            if gantt[k]==dpid[i]:
                tat.append(k+1-dat[i])
                wt.append(tat[i]-dbt[i])
                break
    for i in range(len(dpid)):
        print(dpid[i],"\t",dat[i],"\t",dbt[i],"\t",tat[i],"\t",wt[i])
    print("Average TAT = ",sum(tat)/len(tat))
    print("Average WT = ",sum(wt)/len(wt))

fcfs(['p1','p2','p3','p4','p5'],[4,6,0,6,5],[5,4,3,2,4])
