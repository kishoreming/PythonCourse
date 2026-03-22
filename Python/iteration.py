class Count:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 3:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

obj = Count()
sum=0
for i in obj:
    sum=sum+i
    print(sum);