'''
average waiting time = 4.2
average turnaround time=8.2
'''
import re
f = open("input.txt", "r")
arrival_time = []
burst_time = []
waiting_time = []
turnaround_time = []
count = 0
for i in f:
    if count == 0:
        count = 1
        continue
    s = re.split("[\\s][\\s]*", i)
    arrival_time.append(int(s[0]))
    burst_time.append(int(s[1]))


# print(arrival_time)
# print(burst_time)
# print(len(arrival_time))


sum_bt = 0
for i in range(0, len(arrival_time)):
    wt = sum_bt-arrival_time[i]
    waiting_time.append(wt)
    turnaround_time.append(wt+burst_time[i])
    sum_bt += burst_time[i]


print(waiting_time)
print(turnaround_time)
sum_wt = 0
sum_tt = 0
for i in range(0, len(waiting_time)):
    sum_wt += waiting_time[i]
    sum_tt += turnaround_time[i]

print("Average waiting time = ", sum_wt/len(waiting_time))
print("Average turnaround time = ", sum_tt/len(turnaround_time))
