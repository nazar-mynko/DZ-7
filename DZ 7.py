class Counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        def money(max_degree, number):
            i=0
            for _ in range(max_degree):
                yield number**i
                i+=1
        res = money(15, 2)
        print(res)
        for _ in res:
            print(_)
        if self.i > self.max_number:
            raise StopIteration
        return self.i
count = Counter(5)
for hell in count:
    print(hell)
