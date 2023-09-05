class MyNumbers:
    def __init__(self, start, stop):
        self.start = start 
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

def main():
    my_list = MyNumbers(10, 50)
    
    my_iter = iter(my_list)
    
    try:
        while True:
            element = next(my_iter)
            print(element)
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
