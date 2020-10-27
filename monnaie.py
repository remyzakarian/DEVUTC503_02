class Monnaie:
    def __init__(self,valeur,devise):
        Monnaie.verifierinit(valeur,devise)
        self.valeur = float(valeur)
        self.devise = str(devise)
        
    
    def verifierinit(valeur,devise):
        val = str(valeur).isnumeric()
        dev = str(devise).isalpha()
        if val==False:
            raise Exception("valeur ne doit pas etre alphabetique")
        if dev==False:
            raise Exception("devise ne doit pas etre numerique")
    
    def ajouter(self,obj):
        if self.__class__.__name__ == obj.__class__.__name__:
            if obj.devise != self.devise:
                raise TypeError("devises sont diferentes")
            else: 
                self.valeur += obj.valeur
        else :
            raise TypeError("you are not adding money")
    
    def retrancher(self,obj):
        if self.__class__.__name__ == obj.__class__.__name__:
            if obj.devise != self.devise:
                raise TypeError("devises sont diferentes")
            else: 
                self.valeur -= obj.valeur
        else :
            raise TypeError("you are not substracting money")

if __name__ = "__main__":
    m1 = Monnaie(5,"euro")
    m2 = Monnaie(7,"euro")
    m1.ajouter(m2)
    assert m1.valeur == 12
    m1 = Monnaie(5,"euro")
    m2 = Monnaie(7,"euro")
    m1.retrancher(m2)
    assert m1.valeur == -2

