# examples
demo
import pdb

a = [1, 2, 3, 4, 5]

# for num in a:
#     print(num)


class Iterable(object):
    def __init__(self):
        self.container = []

    def __iter__(self):
        return Iterator(self.container)

    def add_nums(self, num_temp):
        self.container.append(num_temp)


class Iterator(object):
    def __init__(self, container):
        self.container = container
        self.count = 0

    def __next__(self):
        if self.count < len(self.container):
            result = self.container[self.count]
            self.count += 1
            return result
        else:
            raise StopIteration


pdb.set_trace()
a1 = Iterable()
a1.add_nums(2)
a1.add_nums(4)
for num in a1:
    print(num)

