from queue import PriorityQueue
import re


process = []
f = open("input.txt", "r")

count = 0
for i in f:
    if count == 0:
        count = 1
        continue
    s = re.split("[\\s][\\s]*", i)
    process.append((int(s[1]), int(s[0])))

print(process)

pq = PriorityQueue()
pq.put(process[0])
sum_bt = 0
index = 1
waiting_time = []
for i in range(0, len(process)):
    waiting_time.append([0, process[i][1]])
    # print(waiting_time)
# print(waiting_time)
turnaround_time = [0]*len(process)
average_wt = 0
average_tt = 0
sum_wt = 0
while not pq.empty():
    p = pq.get()
    # print(p, sum_bt)
    waiting_time[p[1]][0] += sum_bt-waiting_time[p[1]][1]
    sum_bt += p[0]
    if(index < len(process)):
        pq.put(process[index])
        if(sum_bt > process[index][1]):
            pq.put((sum_bt-process[index][1], p[1]))
            sum_bt = (process[index][1])
        index += 1
    waiting_time[p[1]][1] = sum_bt
    # print(waiting_time)
# print(sum_bt)
print(waiting_time)

for i in range(len(process)):
    turnaround_time[i] = process[i][0]+waiting_time[i][0]
    average_tt += turnaround_time[i]
    average_wt += waiting_time[i][0]
print(turnaround_time)

print("Average waiting time ", average_wt/len(process))
print('Average turnaround time ', average_tt/len(process))

'''
correct output...
(2, 0)
(1, 0)
(3, 1)
(2, 1)
(1, 1)
(4, 3)
(5, 2)
(6, 4)
'''
