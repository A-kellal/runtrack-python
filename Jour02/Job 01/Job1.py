#exmple class

class Person:                                # constructeur
    def __init__(self, Fprenom, Fnom):
        self.prenom =Fprenom
        self.nom = Fnom
        
    def sepresenter(self):
        return(print(self.prenom," ", self.nom))
        
    def set_nom(self, Fnom ):
        self.nom= Fnom
            
    def get_nom(self):
        return self.nom
    
    
        
# Héritage

class auteur(Person):
    def __init__(self,Aprenom,Anom):
        
        self.prenom = Aprenom
        self.nom = Anom
        super().__init__(Aprenom,Anom) # les parametres qu on vas donné a la class mére
    #super donne acces au constructeur
        def set_nom(self, Anom ):
            self.nom= Anom
            
        def get_nom(self):
            return self.nom
        

P1 = Person("leo", "messi") #☺extentier
#P1.sepresenter()      
P1.set_nom ("pascale")
P1.sepresenter()      

 




      