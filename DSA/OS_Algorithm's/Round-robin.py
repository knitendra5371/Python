from queue import PriorityQueue
from collections import deque
import re

process = []
time_process = []

f = open("input.txt", "r")

count = 0
for i in f:
    if count == 0:
        count = 1
        continue
    s = re.split("[\\s][\\s]*", i)
    process.append([int(s[1]), int(s[0]), int(s[0])])
    time_process.append([int(s[1]), int(s[0])])

# print(process)

quantum = 2
q = []
q.append(process[0])
waiting_time = []

for item in process:
    waiting_time.append([0, item[1]])

# print(waiting_time)

sum_bt = 0
index = 1
for item in q:
    waiting_time[item[2]][0] += (sum_bt-item[1])
    sum_bt += (quantum if item[0] >= quantum else item[0])
    # print("*", item)
    if(index < len(process)):
        for i in range(index, len(process)):
            if(sum_bt >= process[index][2]):
                q.append(process[index])
                index += 1
            else:
                break
    if(item[0]-quantum > 0):
        item[0] = item[0]-quantum
        item[1] = sum_bt
        q.append(item)


# print(sum_bt)
print(waiting_time)
# print(time_process)
# print(process)
turnaround_time = []
average_wt = 0
average_tt = 0
for i in process:
    turnaround_time.append([waiting_time[i[2]][0]+time_process[i[2]][0], i[2]])
    average_wt += waiting_time[i[2]][0]
    average_tt += turnaround_time[i[2]][0]

print(turnaround_time)
print("Average waiting time ", average_wt/len(process))
print("Average turnaround time ", average_tt/len(process))


'''
Average waiting time  7.2
Average turnaround time  11.2

'''
