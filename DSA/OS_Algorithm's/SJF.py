from queue import PriorityQueue
import heapq
import re


'''
s = "my name is nitendra kumar"
print('-'.join(s.split(" ")))
'''


class p:
    def __init__(self, at, bt):
        self.arrival_time = at
        self.burst_time = bt


process = []
f = open("input.txt", "r")
count = 0
for i in f:
    if count == 0:
        count = 1
        continue
    s = re.split("[\\s][\\s]*", i)
    process.append((int(s[0]), int(s[1])))


# for i in process:
    # print(i.arrival_time, "   ", i.burst_time)

waiting_time = [0]*len(process)
turnaround_time = [0]*len(process)

# print(waiting_time)
# print(turnaround_time)

pq = PriorityQueue()

pq.put((process[0][1], process[0][0]))
index = 1
sum_bt = 0
# print(pq.qsize())
while not pq.empty():
    p = pq.get()
    # print(pq.qsize(), " ", p.arrival_time, "  ", p.burst_time)
    waiting_time[p[1]] = sum_bt - p[1]
    turnaround_time[p[1]] = waiting_time[p[1]]+p[0]
    # print(" *** ", waiting_time[p[1]])

    sum_bt += p[0]
    if(index < len(process)):
        for i in range(index, len(process)):
            if(process[i][0] <= sum_bt):
                # print(process[i].arrival_time, " ***  ", process[i].burst_time)
                pq.put((process[i][1], process[i][0]))
            else:
                index = i
                break
            if(i == len(process)-1):
                index = i+5

    # print(pq.qsize())
print(waiting_time)
print(turnaround_time)
average_wt = 0
average_tt = 0
for i in range(len(waiting_time)):
    average_wt += waiting_time[i]
    average_tt += turnaround_time[i]


print("Average waiting time ", average_wt/len(waiting_time))
print("Average turnaround time ", average_tt/len(turnaround_time))

'''
q = PriorityQueue()

q.put((1, 'A'))
q.put((3, 'B'))
q.put((2, 'C'))
q.put((2, 'B'))


for i in range(q.qsize()):
    w = q.get()
    print(w[0], "   ", w[1])

'''
