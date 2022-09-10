#Fonction qui a pour argument une date donnée

from this import d


def deterJour() :
        
    #Création de dictionnaires pour les différentes données : mois,jour, siècle
    dict_valeur_mois = {"01" : 0, "02" : 3, "03" : 3, "04" : 6, "05" : 1, "06" : 4, "07" : 6, "08" : 2, "09" : 5, "10" : 0, "11" : 3, "12" : 5}
    dict_valeur_jour = {0:"Dimanche", 1:"Lundi", 2:"Mardi", 3:"Mercredi", 4:"Jeudi", 5:"Vendredi", 6:"Samedi"}
    dict_valeur_siecle = {"16":6, "17":4, "18":2, "19":0, "20":6, "21":4}
    
    date = input("Veuillez renseigner une date sous ce format (DD/MM/YYYY) : ")
   
    #Attention pour date[:2], l'élement correspondant à l'indice 2 n'est pas compris
    #valeur_mois[date[3:5]] pour récupérer la valeur associée à la clé
    stock =  int(date[-2:]) +(int(date[-2:])//4) + int(date[:2])+dict_valeur_mois[date[3:5]]
    

    #test pour savoir si une année est bissextile ou non :
    if (int(date[-4:])%4 == 0 and int(date[-4:])%100 !=0 or int(date[-4:])%400 ==0) :
        #Test pour savoir si le mois est Janvier ou Février dans le cadre où l'année est bissextile
        if date[3:5]=="01" or date[3:5]=="02" :
            stock = stock - 1
        stock += dict_valeur_siecle[date[-4:-2]]
        stock %= 7
        print("Le", date, "est un", dict_valeur_jour[stock], "et l'année est bissextile.")

    else : 
        stock += dict_valeur_siecle[date[-4:-2]]
        stock %=7
        print("Le", date, "est un", dict_valeur_jour[stock], " et l'année n'est pas bissextile.")
        

deterJour()