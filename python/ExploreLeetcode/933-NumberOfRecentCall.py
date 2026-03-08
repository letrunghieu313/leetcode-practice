from collections import deque

class RecentCounter(object):
    def __init__(self):
        self.times = deque()
        
    def ping(self, t):
        self.times.append(t)
        while self.times and self.times[0] < t - 3000:
            self.times.popleft()
        return len(self.times)
        
        
if __name__ == "__main__":
    obj = RecentCounter()
    test = [0, 1, 100, 3001, 3002, 6000]
    for x in test:
        result = obj.ping(x)
    print(result)
        
        
# Document of this is in the notebook(Ipad) 
# this problem use the queue to remove the one that outside of range. 

responseTimes = [100, 200, 150,300]

count = 2 
Ave =  150 + 150 = 300 / 2 =  150 yes

i = 3 => 300


