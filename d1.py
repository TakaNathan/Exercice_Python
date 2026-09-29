import math
#fonction tempsVoyage qui calcule le temps en fonction de la distance te de la vitesse
#(float,float)->float
def tempsVoyage(distance,vitesse) :
    temps_en_heures = distance/vitesse
    temps_en_minutes = (temps_en_heures*60)
    return temps_en_minutes

#fonction qui calcule la note finale en fonction des 5 notes fournies en tenant compte des ponderations
#(float,float,float,float,float)->float
def noteFinale(note_labos,note_devoirs,note_quiz,note_e_partiel,note_e_final) :
    note_finale = (note_labos*10/100) +(note_devoirs*25/100) + (note_quiz*5/100) +(note_e_partiel*20/100)+(note_e_final*40/100)
    return note_finale

#fonction qui va recuperer les 5 parametres d'entree et retourner une phrase
#(str,str,str,str,int)->str
def bibformat(auteur,titre,ville,maisonEdition,annee) :
    annee = str(annee)#pour pouvoir concatener le int avec + comme un string
    n = auteur+" ("+annee+"). "+titre+". "+ville+": "+maisonEdition
    return n


"""fonction qui va demander et recuperer les donnees entrees par l'utilisateur
et afficher une phrase en se servant de la foonction bibformat()"""
#()->()
def bibformatPrint() :
    auteur = input("Entrer le nom de l'auteur: ")
    titre = input("Entrer le titre de l'oeuvre: ")
    ville = input("Entrer la ville d'edition: ")
    maisonEdition = input("Entrer la maison d'edition: ")
    annee = input("Entrer l'annee d'edition: ")
    print(bibformat(auteur,titre,ville,maisonEdition,annee))

#bibformatPrint()


"""fonction qui resoud l'equation 10^4y = x+3 en fonction de y
suivant la valeur de x en se servant de la fonction log10 de math"""
#(float)->float
def logFun(x) :
    y = (math.log10(x+3))/4 #log10 renvoie le logarithme en base 10 d'un nombre
    return y


#fonction qui permet de dire si une annee est bissextile ou pas
#(int)->(bool)
def anneeBis(an) :
    resultat1 = not bool(an%4) #an divisible par 4 signifie bool(a%4)=false et resultat sera true
    #si an n'est pas divisible par 4 resultat sera false 
    resultat2 = not (not bool(an%100) and bool(an%400))
    resultat = resultat1 and resultat2
    return resultat

print (anneeBis(2016))
print (anneeBis(2022))
print(anneeBis(1904))
print(anneeBis(1928))
print(anneeBis(1950))
print(anneeBis(1990))
print(anneeBis(1932))

