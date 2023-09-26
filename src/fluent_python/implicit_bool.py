class MySequence:
    def __init__(self, n):
        self.n = n
        self._x = list(range(n))
    
    def __len__(self):
        print("Len called")
        return self.n
    
    def __getitem__(self, i):
        return self._x[i]
    

s = MySequence(10)
if s:
    print(s[2:4])
    print(True)