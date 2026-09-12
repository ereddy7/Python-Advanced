class Test:
    def total(self,a=None,b=None,c=None):
        vals=[x for x in (a,b,c) if x is not None]; print(sum(vals) if len(vals)>=2 else "Provide 2 or 3")
t=Test(); t.total(10,20); t.total(10,20,30); t.total(10)
