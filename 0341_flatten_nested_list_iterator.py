from collections import deque

class NestedIterator:
    def __init__(self, nestedList):
        def flatten(nestedList):
            result = []
            for i in nestedList:
                if isinstance(i, int):
                    result.append(i)
                else:
                    result.extend(flatten(i))
            return result

        self.n = deque(flatten(nestedList))

    def next(self):
        return self.n.popleft()

    def hasNext(self):
        return len(self.n) > 0

nestedList = [[1,1],2,[1,1]]
i, v = NestedIterator(nestedList), []
while i.hasNext(): v.append(i.next())
print(v)