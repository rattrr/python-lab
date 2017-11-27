class MyList(object):
    def __init__(self):
        self.container = []
    def __repr__(self):
        return str(self.container)
    def add(self, element):
        self.container.append(element)
    def remove(self, element):
        try:
            self.container.remove(element)
        except ValueError as e:
            raise e
    def sort(self):
        self.container.sort()
    def __getitem__(self, index):
        to_return = None
        try:
            to_return = self.container[index]
        except IndexError as e:
            raise e
        return to_return



ml = MyList()
ml.add(1)
ml.add(2)
ml.add(3)
ml.add(0)
ml.remove(3)
ml.sort()
print ml[1]
print ml
