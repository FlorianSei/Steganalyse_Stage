import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
from random import random

#os.chdir("C:/Users/fseignat/Desktop/stega Seignat/code_images/ALASKA/Cover")

img=mpimg.imread('C:/Users/fseignat/Desktop/stega Seignat/code_images/ALASKA/Cover/00002.jpg')



#start_time = time.time()


def modif_image(img,clef,seuil):
    """
    

    Parameters
    ----------
    img : image à modifier
    clef : profondeur de bit 
    seuil : représente le taux d'insertion. Si tirage>seuil, le bit est modifié (va de 0 à 7)

    Returns
    -------
    image modifié

    """
    #Tatouage sur la partie bleue
    #plan = np.zeros(img.shape[0:2], dtype="uint8")
    plan = img[:,:,2]
    
    #Tableau qui va déterminer les pixels à changer
    marque =  np.ones(np.shape(plan),dtype="uint8")*(2**clef)*(np.random.random(size=np.shape(plan))>seuil)
    
    #insertion de la marque
    plan_marque= np.bitwise_xor(plan,marque)
 
    
    img2=np.copy(img)
    
    img2[:,:,2]=plan_marque
    return(img2)
    


#print("--- %s seconds ---" % (time.time() - start_time))
