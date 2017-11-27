class MyList(object):
    def __init__(self):
        self.container = []
    def __repr__(self):
        return str(self.container)
    def add(self, element):
        try:
            self.container.append(element)
        except NameError as e:
            raise(e)

    def remove(self, element):
        self.container.remove(element)
    def sort(self):
        self.container.sort()
    def __getitem__(self, index):
        return self.container[index]



ml = MyList()
ml.add(1)
ml.add(2)
ml.add(3)
ml.add(0)
ml.remove(3)
ml.sort()
print ml
print ml[1]
ml.add(asdf  )
