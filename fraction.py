class Fraction:
    def __init__(self,numerateur,denominateur):
        self.numerateur = numerateur
        self.denominateur = denominateur
    
    def __mult__(self,obj):
        self.numerateur = self.numerateur * obj.numerateur
        self.denominateur = self.denominateur * obj.denominateur
    
    def __add__(self,obj):
        if self.denominateur == obj.denominateur:
            self.numerateur = self.numerateur + obj.numerateur
        elif self.denominateur != obj.denominateur:
            denominateurcommun = self.denominateur * obj.denominateur
            self.numerateur = self.numerateur * obj.denominateur
            secondnumerateur = obj.numerateur * self.denominateur
            self.denominateur = denominateurcommun
            seconddenominateur = denominateurcommun
            self.numerateur = self.numerateur + secondnumerateur

    def simplifier(self):
        numresfinal = 1
        denumresfinal = 1
        numres = self.decompose(self.numerateur)
        denumres = self.decompose(self.denominateur)
        for i in numres:
            if i in denumres:
                numres.remove(i)
                denumres.remove(i)
        print(numres)
        print(denumres)
        
        for i in numres:
            if numres == []:
                self.numerateur=1
            else:
                numresfinal = numresfinal * i
        
        for i in denumres:
            if denumres == []:
                self.denominateur=1
            else:
                denumresfinal = denumresfinal * i
        print(numresfinal)
        print(denumresfinal)
        self.numerateur = numresfinal
        self.denominateur = denumresfinal    

    def decompose(self, n):
        res=[]
        i=2
        while n>1: 
            while n%i==0: 
                res += [i]
                n=n/i
            i=i+1
        return res