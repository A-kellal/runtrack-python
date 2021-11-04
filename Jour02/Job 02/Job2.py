class Personne:
    
    def __init__(self,Anom,Aprenom):
        
        self.nom = Anom
        self.prenom = Aprenom

class Auteur(Personne):
    
    def __init__(self,Anom,Aprenom):
        self.oeuvres=[]
#        self.nom = Anom
#        self.prenom = Aprenom
        super().__init__(Anom, Aprenom)
    
    def listerOeuvre(self):
        for livre in self.oeuvres: # ajouter le nouveau livre a l'oeuvre de l'auteur
            livre.printe()
        
    def ecrireUnLivre(self, titre):
        livre = Livre(titre, self)
        self.oeuvres.append(livre)
        
class Livre:
    
    def __init__(self , letitre, Auteur):
        self.titre = letitre
        self.auteur = Auteur
    def printe(self):
        return(print(self.titre,self.auteur))  

P1 = Livre("rahim","Test")
P1.printe()
#P1.ecrireUnLivre("LORD")
#P1.listerOeuvre()