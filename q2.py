#!/usr/bin/env python
# coding: utf-8

# In[8]:


################################################################################################################################
# DEFINIR LA FONCTION PERMETTANT DE CALCULER UN POLYNOME
################################################################################################################################

def Polynome_calcul(num) :
    f = num**3 - 1.5 * num**2 - (num+1) * num + (num+1)
    return f
################################################################################################################################
# DEFINIR LA FONCTION PERMETTANT GERER LES EXCEPTIONS ET COMUNIQUER AVEC L'UTILISATEUR
################################################################################################################################
def polynome() :



    while True : # tant que les champs ci-dessours sont vraix, je continue à executer mes input

            try :
                # Transformer les input en valeur numérique
                num = float(input('Entrez une valeur numéque : '))             



# DEFINIR UNE BORNE TROP GRANDE POUR LA CALCULE DE LE POLYNOME

                borne_sup = 6 # définir la taille de la borne supérieur
                if len(str(num)) > borne_sup : #Transformer les nombres en caractère puis en compter le nombre

                    print(f'Le nombre {num} est supérieur on nombre de caractère autorisé de {borne_sup} entrez une nouvelle valeur')




                
# DEFINIR UNE BORNE TROP PETITE POUR LA CALCULE DE LE POLYNOME 

                borne_inf = 2 # définir la taille de la borne inférieur
                if len(str(num)) < 2 : #Transformer les nombres en caractère puis en compter le nombre

                    print(f'Le nombre {num} est supérieur on nombre de caractère autorisé de {borne_inf} entrez une nouvelle valeur')
                    




# VERIFIER SI L'UTILISATEUR N'A ENTRE AUCUNE VALEUR (Ne fonctionne pas surement à cause du ValueError déjà présent plus bas)
                
                if not num : #Si le premier input est vide,     
                    raise ValueError('Vous n\'avait pas entré de première valeur') #je génère une erreur à afficher à l'utilisateur
            

                
    

# TRANSFORMER LES NOMBRES COMPLEXES EN REEL (ne fonctionne pas à cause du input)
                #chercher si "num" est un complex
                if num ==  complex :
                    #si "num" est un complexe, le transformer en real
                    num = abs(num)
                    
                    
# TRANSFORMER LA VALEUR SI EST EGALE A UNE CHAINE DE CARACTERE (ne sert pas)
                elif num == str :  # Si a ou b est une chaine de caractère, je le transforme un float
                    num = float(num)

                    
                    
#RETOURNER LA VALEUR ABSOLUE D'UN NOMBRE NEGATIF
                elif num < 0 :
                    a = abs(num)
            
                
            except ValueError: #Si l'utilisateur entre une chaine de caractère, le message suivant va lui être retourné
                pass   
                print('Veillez Entrer une valeur numérique est non texctuelle')

            else : #Si aucune des précedentes conditions ne sont remplis, je retourne ma fonction parmettant de calculer le polynome

                return Polynome_calcul(num)


# In[9]:


polynome()


# In[ ]:




