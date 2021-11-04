class Bibliotheque:
    def __init__(self, Anom, Acatalogue):
        self.nom=Anom
        self.catalogue=Acatalogue 
        
class Livre:
    
    def __init__(self , letitre, Auteur):
        self.titre = letitre
        self.auteur = Auteur    
        
class Personne:
    
    def __init__(self,Anom,Aprenom):
        
        self.nom = Anom
        self.prenom = Aprenom

class Auteur(Personne):
    
    def __init__(self,Anom,Aprenom):
        
        super().__init__(Anom, Aprenom)
        
class Auteur(Personne):
    
    def __init__(self,Anom,Aprenom):
        
        super().__init__(Anom, Aprenom)