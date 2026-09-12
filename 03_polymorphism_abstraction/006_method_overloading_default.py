class Test:
    def total(self,a=None,b=None,c=None):
        values=[x for x in (a,b,c) if x is not None]
        print(sum(values) if len(values)>=2 else "Provide 2 or 3 arguments")
t=Test(); t.total(10,20); t.total(10,20,30); t.total(10)
