class Test:
    count=0
    def __init__(self): Test.count+=1
    @classmethod
    def number_of_objects(cls): print(cls.count)
objects=[Test() for _ in range(5)]; Test.number_of_objects()
