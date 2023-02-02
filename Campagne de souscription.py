nbDemandeursacceptés=0
nbDemandeurs=0
Lconditions=["célibataire,","qui à plus de 25 ans,","qui n'as jamais eu d'accident,","de sexe féminin,"]
Lréponses=[0,0,0,0]
nbRéponses=0
Condition=0
while Condition!="N":
    message="Conducteur ",Lconditions[nbRéponses]," tapez 1 si oui, 0 si non, N pour arreter : "
    Condition=input(message)
    if Condition!="N":
        Lréponses[nbRéponses]=int(Condition)
        if nbRéponses==3:
            if Lréponses[1]==1 or (Lréponses[0]==1 and Lréponses[2]==0) or (Lréponses[0]==0 and Lréponses[2]==1) or Lréponses[2]==Lréponses[3]==0:
                print("Souscription validé")
                nbDemandeursacceptés+=1
            else:
                print("Souscription non validé")
            nbRéponses=0
            nbDemandeurs+=1
        else:
            nbRéponses+=1
print(nbDemandeurs, int(nbDemandeursacceptés/nbDemandeurs*100),"%")