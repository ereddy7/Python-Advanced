class Test:
    count=0
    def __init__(self): Test.count+=1
    @classmethod
    def objects(cls): print(cls.count)
t1=Test(); t2=Test(); Test.objects(); t3=Test(); Test.objects()
