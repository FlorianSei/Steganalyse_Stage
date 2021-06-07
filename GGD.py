import numpy as np
import math
import numpy.random as npr
import matplotlib.pyplot as plt


def PDF_GGD(x,sigma,beta):
    """
    Calcule la daensité de probabilité de la loi gaussienne généralisée

    """
    f=beta/(2*sigma*math.gamma(1/beta))*np.exp(-(np.abs(x)/sigma)**beta)
    return f
    


def densite_GGD(N,sigma,beta):
    """
    

    Parameters
    ----------
    N : nombre de données conservées via Monte-Carlo
    sigma,beta : paramètre de la GGD

    Returns
    -------
    renvoie la densité de la GDD

    """
    c=0
    L=[]
    while c<N:
        x=-100+200*npr.random(1)     #je considère que f(x)=0 pour |x|>300
        y=npr.random(1)
        if PDF_GGD(x, sigma, beta)>y:
            c+=1
            L.append(float(x))
    plt.hist(L,bins='auto',density=True,alpha=0.9,color='green')
    return L


#L=densite_GGD(30000,1,8)
