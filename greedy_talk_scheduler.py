from sorting_algorithms import *

class Talk:
    def __init__(self, startTime, stopTime):
        self.start = startTime
        self.stop = stopTime
        self.duration = stopTime - startTime

def schedule(talks):
    sortedTalks = insertion_sort(talks, rule=lambda x,y: x.stop <= y.stop)
    scheduled = []
    for talk in talks:
        if not conflicts(scheduled, talk):
            scheduled.append(talk)
    return scheduled

def conflicts(talks, talk):
    for t in talks:
        if t.start >= talk.start and t.start < talk.stop:
            return True
        if t.stop <= talk.stop and t.stop > talk.start:
            return True
    return False
