import matplotlib.pyplot as plt
import numpy as np
import os 
from scipy import special



def sigma_chap(WR,beta):
    """
    

    Parameters
    ----------
    WR : coefficients issus de la décomposition en ondelettes
    beta : paramètre de la GGD
    Returns
    -------
    Estimateur de alpha, second paramètre de la GDD (Formule p5 du document WaveStat.pdf)

    """
    if beta=="Pas de solution":
        estim_sigma='Pas de solution'
    else:
        L=len(WR)      #Comme l'image est un carré, la longueur et la largeur sont identiques    
        som=np.sum(np.abs(WR)**beta)
        estim_sigma=(beta/(L**2)*som)**(1/beta)
    return(estim_sigma)


def log_mat(WR):
    """
    

    Parameters
    ----------
    WR : coefficients d'ondeletettes'

    Returns
    -------
    Permet de renvoyer le log des coefficients en mettant des 1 à la place de -inf (utile pour les calculs suivants)

    """
    (long,lar)=np.shape(WR)
    Y=np.ones((long,lar))                #comme on fait log|xi|*xi, si xi=0, je mets les termes de log|xi| pour éviter d'avoir l'infini
    L=np.where(WR!=0,WR,Y)
    return np.log(L)
    
    

def g(WR,beta_k):
    """
    Fonction que l'on doit annuler par la méthode de Newton (Formule p5 du 
    document WaveStat.pdf et algorithme en appendice )'

    Parameters
    ----------
    WR : coefficients issus de la décomposition en ondelettes
    beta_k : paramètre à estimer 

    Returns
    -------
    Valeur de la fonction à annuler en beta_k

    """
    (long,lar)=np.shape(WR)
    som=np.sum(np.abs(WR)**beta_k)                  #correspond à la somme des |xi|**beta
    mat_log=log_mat(np.abs(WR))                              
    som_log=np.sum((mat_log*np.abs(WR)**beta_k))    #correspond à la somme des |xi|**beta*log|xi|
    val=1+special.polygamma(0,1/beta_k)/beta_k-som_log/som+np.log(beta_k/(long*lar)*som)/beta_k
    return val



def g_prime(WR,beta_k):
    """
       Dérivé de la fonction à annuler (Formule p5 du 
    document WaveStat.pdf et algorithme en appendice )'

    Parameters
    ----------
    WR : coefficients issus de la décomposition en ondelettes
    beta_k : paramètre à estimer 

    Returns
    -------
    Valeur de la dérivée de la fonction à annuler en beta_k

    """
    (long,lar)=np.shape(WR)
    mat_log=log_mat(np.abs(WR))  
    som=np.sum(np.abs(WR)**beta_k)                               #correspond à la somme des |xi|**beta
    som_log=np.sum(mat_log*np.abs(WR)**beta_k)      #correspond à la somme des |xi|**bet
    som_log_car=np.sum((mat_log**2*np.abs(WR)**beta_k))            #correspond à la somme des |xi|**beta*log|xi|**2
    #on décompose ensuite les termes de la dérivée 
    val1=-special.polygamma(0,1/beta_k)/(beta_k**2)-special.polygamma(1,1/beta_k)/(beta_k**3)+1/(beta_k**2)   
    val2=-som_log_car/som+som_log**2/som**2
    val3=som_log/(beta_k*som)-np.log(beta_k/(long*lar)*som)/beta_k**2
    val=val1+val2+val3
    return val


def Fm(beta):
    """
    

    Parameters
    ----------
    beta : paramètre à estimer

    Returns
    -------
    renvoie Fm(beta)  (défini à la fin du papier Wave Stat)

    """
    
    num=special.gamma(2/beta) 
    den=np.sqrt(special.gamma(1/beta)*special.gamma(3/beta))
    return num/den


def Fm_prime(beta):
    """
    

    Parameters
    ----------
    beta : paramètre à estimer 

    Returns
    -------
    dérivé de Fm en beta

    """
    u=special.gamma(2/beta)
    v=np.sqrt(special.gamma(1/beta)*special.gamma(3/beta))
    u_prime=-2/beta**2*special.polygamma(0,2/beta)*special.gamma(2/beta)
    num_v_prime=-1/beta**2*(special.polygamma(0,1/beta)*special.gamma(1/beta)*special.gamma(3/beta)+3*special.gamma(1/beta)*special.polygamma(0,3/beta)*special.gamma(3/beta))
    den_v_prime=2*v
    v_prime=num_v_prime/den_v_prime
    val=(u_prime*v-v_prime*u)/v**2
    return val

def val_dep_beta(WR):
    """
    

    Parameters
    ----------
    WR : coefficients d'ondelettes

    Returns
    -------
    renvoie une "bonne" valeur pour initialiser le beta_0  (calcul par Newton)

    """
    (long,lar)=np.shape(WR)
    m1=np.sum(np.abs(WR))
    WR_car=WR*WR
    m2=np.sum(WR_car)
    m1=m1/(long*lar)
    m2=m2/(long*lar)
    beta_k=0.5             #valeur de départ (arbitraire)
    beta_k_1=beta_k-(Fm(beta_k)-m1/np.sqrt(m2))/Fm_prime(beta_k)
    while np.abs(beta_k-beta_k_1)>10**(-4) and beta_k_1>0:
        beta_k=beta_k_1
        beta_k_1=beta_k-(Fm(beta_k)-m1/np.sqrt(m2))/Fm_prime(beta_k)
    return(beta_k)


def beta_chap(WR,val_dep,eps):
    """
    

    Parameters
    ----------
    WR : coefficients issus de la décomposition en ondelettes
    val_dep : valeur de départ pour trouver le zéro de la fonction (1 a l'air d'être une valeur proche de la solution)
    eps : précision de l'approximation
    
    Returns
    -------
    valeur qui annule la fonction g avec la précision eps
    """
    
    i=0
    N=10
    beta_k=val_dep                                  #valeur actuelle
    beta_k_1=beta_k-g(WR,beta_k)/g_prime(WR,beta_k)       #valeur suivante
    while np.abs(beta_k-beta_k_1)>eps and i<N and beta_k_1>0:
        beta_k=beta_k_1
        beta_k_1=beta_k-g(WR,beta_k)/g_prime(WR,beta_k)
        i+=1
    if i==N:
        beta_k="Pas de solution"
    return beta_k