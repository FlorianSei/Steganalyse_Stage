import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import csv
import os

from test_wave import decomposition_image, concatene
from GGD import densite_GGD
from estimation_parametres import sigma_chap, beta_chap,g_prime,val_dep_beta
from fingerprinting import modif_image


import time

os.chdir("C:/Users/fseignat/Desktop/stega Seignat/code_images/ALASKA")
start_time = time.time()



## Récupération des images
def recup_image(num,BD):
    '''

    Parameters
    ----------
    num : numéro de l'image à traiter
    BD : base de données (de type Cover ou JMiPOD)

    Returns
    -------
    renvoie l'image 

    '''
    L=['0']*5
    S=list(str(num/10**4))
    S=np.delete(S,1)
    for i in range(len(S)):
        L[i]=S[i]
    s=''.join(L)
    che=BD+"/"+str(s)+'.jpg'
    if os.path.exists(che):
        img=mpimg.imread(che)
    else:
        img=False                       #le chemin n'existe pas (vient du fait que la Base a des "trous", 00006.jpg n'existe pas par exemple)
    return img


def selection_images(N):
    """
    

    Parameters
    ----------
    N : nombre d'images à récupérer

    Returns
    -------
    renvoie une liste de N nombres représentant les images à sélectionner

    """
    L=[]
    i=0
    while i<N:
        s=np.random.randint(1,80006)            #80005 images dans Alaska sans compter les "trous"
        if type(recup_image(s))!=bool:
            i+=1
            L.append(s)
    return L

    #Image naturelle (Cover)

#img=mpimg.imread('00001.jpg')
#img=recup_image(16)


    #Image stégo "à la main"
clef=0
#seuil=0
#img=modif_image(img,clef,seuil)
#plt.imshow(img)




#Coeffcients d'ondelettes en fonction du nombre d'échelles, de l'échelle et du plan
nb_echelle=3
#nb_plan=3
#echelle=3
#plan=1
#WR=concatene(img,nb_echelle,echelle)




#Estimation paramètres
# val_dep=val_dep_beta(WR)
# beta_estim=beta_chap(WR,val_dep,10**(-4))
# sigma_estim=sigma_chap(WR,beta_estim)

# print(' val_dep=',val_dep, '\n',' beta_estim = ',beta_estim ,'\n','sigma_estim = ',sigma_estim)
# print("--- %s seconds ---" % (time.time() - start_time))



##Rassemblement des informations dans des tableaux


# nb_images=21
# Seuil=np.arange(0,1,0.1)

# with open('data_COVER.csv','a',newline='') as fichiercsv:
#       writer=csv.writer(fichiercsv)
#       writer.writerow(['Nom', 'Echelle', 'Plan', 'Beta_Chapeau','Sigma_chapeau'])
#       writer.writerow('\n')
#       for j in range(0,nb_images):
#           img=recup_image(j)
#           print("j=",j)
#           if type(img)!=bool:                                #image existe(cela renvoie bien un tableau)
#                 #for s in Seuil:
#                     #s=round(s,1)
#                     #img=modif_image(img,clef,s)
#                     for k in range(0,nb_plan):
#                         for i in range(0,nb_echelle):
#                             WR=decomposition_image(img,nb_echelle,i+1,k+1)
#                             val_dep=val_dep_beta(WR)
#                             beta_estim=beta_chap(WR,val_dep,10**(-4))
#                             sigma_estim=sigma_chap(WR,beta_estim)
#                             writer.writerow([str(j)+'.jpg', str(i+1), str(k+1),str(beta_estim),str(sigma_estim)])
#                         writer.writerow('\n')
#           writer.writerow('\n')
#           writer.writerow('\n')



##Moyenne pour une image
Seuil=np.arange(0,1,0.1)
#S=selection_images(10)
S=[53548, 921, 20948, 61358, 10483, 29149, 2727, 41508, 26273, 49717]


# with open('Stego_2bits.csv','a',newline='') as fichiercsv:
#       writer=csv.writer(fichiercsv)
#       writer.writerow(['Image','Echelle','Seuil', 'Beta_Chapeau','Sigma_chapeau'])
#       writer.writerow('\n')
#       z=0
#       for c in S:
#         print("c=",c)
#         img=recup_image(c,"Cover")
#         for i in range(0,nb_echelle):
#             for s in Seuil:
#                 z+=1
#                 print(z)
#                 s=round(s,1)
#                 for l in range(100):
#                           B=[]
#                           S=[]
#                           img_mod=modif_image(img,0,s)
#                           img_mod=modif_image(img_mod,1,s)
#                           WR=concatene(img_mod,nb_echelle,i+1)
#                           val_dep=val_dep_beta(WR)
                      
#                           beta_estim=beta_chap(WR,val_dep,10**(-4))
#                           B.append(beta_estim)
#                           sigma_estim=sigma_chap(WR,beta_estim)
#                           S.append(sigma_estim)
#                 bet=np.mean(B)
#                 sig=np.mean(S)
#                 writer.writerow([str(c),str(i+1),str(s),str(bet),str(sig)])
#         writer.writerow('\n')


# with open('Stego_3bits.csv','a',newline='') as fichiercsv:
#       writer=csv.writer(fichiercsv)
#       writer.writerow(['Image','Echelle','Seuil', 'Beta_Chapeau','Sigma_chapeau'])
#       writer.writerow('\n')
#       z=0
#       for c in S:
#         print("c=",c)
#         img=recup_image(c,"Cover")
#         for i in range(0,nb_echelle):
#             for s in Seuil:
#                 z+=1
#                 print(z)
#                 s=round(s,1)
#                 for l in range(100):
#                           B=[]
#                           S=[]
#                           img_mod=modif_image(img,0,s)
#                           img_mod=modif_image(img_mod,1,s)
#                           img_mod=modif_image(img_mod,2,s)
#                           WR=concatene(img_mod,nb_echelle,i+1)
#                           val_dep=val_dep_beta(WR)
                      
#                           beta_estim=beta_chap(WR,val_dep,10**(-4))
#                           B.append(beta_estim)
#                           sigma_estim=sigma_chap(WR,beta_estim)
#                           S.append(sigma_estim)
#                 bet=np.mean(B)
#                 sig=np.mean(S)
#                 writer.writerow([str(c),str(i+1),str(s),str(bet),str(sig)])
#         writer.writerow('\n')





# print("--- %s seconds ---" % (time.time() - start_time))



#Tracé des différents paramètres 
# Cov=open('COVER.csv','r')
# r_cov = csv.reader(Cov, delimiter=',')
# liste_cov = list(r_cov)
# Cov.close()


# file=open('Stego_1bit.csv','r')
# r = csv.reader(file, delimiter=',')
# liste = list(r)
# file.close()

    #Séléction pour chaque image
# IM1=liste[1:32]
# Cov1=liste_cov[2:5]

# IM2=liste[32:63]
# Cov2=liste_cov[6:9]

# IM3=liste[63:94]
# Cov3=liste_cov[10:13]

# IM4=liste[94:125]
# Cov4=liste_cov[14:17]

# IM5=liste[125:156]
# Cov5=liste_cov[18:21]

# IM6=liste[156:187]
# Cov6=liste_cov[22:25]

# IM7=liste[187:218]
# Cov7=liste_cov[26:29]

# IM8=liste[218:249]
# Cov8=liste_cov[30:33]

# IM9=liste[249:280]
# Cov9=liste_cov[34:37]

# IM10=liste[280:311]
# Cov10=liste_cov[38:41]


    #Tracer les graphes
    
def evolution_parametre_insertion(Cov,IM,echelle):
    """
    

    Parameters
    ----------
    Cov: paramètre de l'image cover
    IM : prend une liste représentant les coefficients pour une image retouchée
    echelle : echelle à étudier

    Returns
    -------
    renvoie 3 graphiques (car 3 échelles) représentant l'évolution des paramètres en fonction du seuil ainsi que la valeur théorique

    """
    Selec_modif=np.array(IM[(echelle-1)*10+1:echelle*10+1])           #données de l'image modifiée
    Selec_Cov=np.array(Cov[echelle-1])
    Seuil=np.arange(0,1,0.1)
    #Selection paramètres
    Sigma_modif=list(map(float,Selec_modif[:,4]))       #permet le conversion en float
    Beta_modif=list(map(float,Selec_modif[:,3]))
    Sigma_Cover=np.ones(len(Seuil))*float(Selec_Cov[3])
    Beta_Cover=np.ones(len(Seuil))*float(Selec_Cov[2])
    
    
    #Tracé
    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    p1,=ax1.plot(Seuil,Sigma_modif, 'b:o',label="Sigma modifié")
    p2,=ax1.plot(Seuil, Sigma_Cover, 'b',label="Sigma Cover")
    plt.legend()
    
    p3,=ax2.plot(Seuil,Beta_modif, 'y:o',label='Beta modifié')
    p4,=ax2.plot(Seuil,Beta_Cover, 'y',label='Beta_Cover')

    ax1.set_xlabel('Seuil',fontsize=10)
    ax1.set_ylabel('Sigma', color='black',fontsize=10)
    ax2.set_ylabel('Beta', color='black',fontsize=10)
    
    nom=Selec_Cov[0]

    plt.title("Image "+str(nom)+" à l'échelle " +str(echelle),fontsize=10)
    ax1.legend(handles=[p1, p2, p3,p4],fontsize=7)
    plt.show()
    return()



#for echelle in [1,2,3]:
#   evolution_parametre_insertion(Cov10,IM10,echelle)


#Vérification de la loi GGd pour les coefficients d'ondelettes

# img=recup_image(2)
# WR=decomposition_image(img,nb_echelle,1,1)
# (img_mod,nb_bit)=modif_image(img,clef,0.2)
# WR_mod=decomposition_image(img_mod,nb_echelle,1,1)

#plt.figure()
#densite_GGD(10000,sigma_estim,beta_estim)
#plt.hist(np.reshape(WR,WR.shape[0]*WR.shape[1]), bins='auto',color='red',density=True, alpha=0.3, rwidth=0.85)
#plt.hist(np.reshape(WR_mod,WR_mod.shape[0]*WR_mod.shape[1]), bins='auto',color='green',density=True, alpha=0.7, rwidth=0.85)
# plt.title("clef=4, seuil=0.2")

