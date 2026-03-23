import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as mplAnim
from time import sleep
from urllib.request import urlopen
from scipy.optimize import differential_evolution


   
def calcOrbite(p,t,mEtoile):
    #p est un tableau de 6 éléments:
    #p[0]=a, demi-grand axe, ici en UA
    #p[1]=e, excentricité
    #p[2]=T0, époque du passage au périastre
    #p[3]=i, inclinaison en degrés
    #p[4]=Omega, longitude de la node ascendante, en degrés
    #p[5]=omega, argument du périastre, en degrés
    #t est le temps, ici en années
    #mEtoile=masse de l'étoile, ici en masse solaire
 
    a,e,T0=p[0],p[1],p[2]
    if not isinstance(t,np.ndarray): t=np.array([t])
    
    ####(a) COMPLÉTER LA LIGNE SUIVANTE, qui calcule la période orbitale de la planète
    ####il s'agit de coder l'équation 4 du fichier explicatif, mais pour P plutôt que pour le carré de P
    ####utiliser mEtoile pour le symbole M*
    
    
    
    
    ##############################

    ####(b) COMPLÉTER LA LIGNE SUIVANTE, qui calcule l'anomalie moyenne M selon le temps t
    ####il s'agit de coder l'équation 2 du fichier explicatif.
    #####Attention à la cohérence avec les variables existantes et celle inventée à l'étape précédente
    
    
    
    
    
    ##############################
   
    #on résoud pour l'anomalie excentrique
    M%=(2*np.pi) #mod 2pi pour accord avec calcAnomE
    E=np.empty(t.size)
    for k in range(t.size):
        E[k]=calcAnomE(M[k],p[1])

    #on commence par la position dans le plan orbital
    ####(c) COMPLÉTER LA LIGNE SUIVANTE, qui calcule la distance radiale de la planète au temps t
    ####il s'agit de coder l'équation 6a du fichier explicatif. Attention de ne pas confondre e pour exp
    
    
    
    
    
    ##############################
    
    #l'anomalie vraie
    theta=2*np.arctan2(np.sqrt(1+p[1])*np.sin(E/2),np.sqrt(1-p[1])*np.cos(E/2))

    ####(d) COMPLÉTER LES DEUX LIGNES SUIVANTES, qui calculent les coordonnées cartésiennes x' (variable nommée xx pour la suite)
    ####et y' (variable nommée yy pour la suite) de la planète
    ####il s'agit de coder les équations 7a et 7b du fichier explicatif






    ##############################

    #on transforme au référentiel du ciel (ne pas modifier)
    i,W,w=np.array(p[3:6])*np.pi/180
    x=(np.cos(w)*np.cos(W)-np.cos(i)*np.sin(W)*np.sin(w))*xx -\
      (np.sin(w)*np.cos(W)+np.cos(i)*np.sin(W)*np.cos(w))*yy
    y=(np.cos(w)*np.sin(W)+np.cos(i)*np.cos(W)*np.sin(w))*xx -\
      (np.sin(w)*np.sin(W)-np.cos(i)*np.cos(W)*np.cos(w))*yy
    z=np.sin(i)*np.sin(w)*xx + np.sin(i)*np.cos(w)*yy
    
    return x,y,z


def calcAnomE(M,e,epsilon=1.e-10,iterMax=25):

    # (e) COMPLÉTER la résolution de l'équation de Kepler
    # Déclaration du E initial



    # Vérification



    # Boucle de Newton






    return E



#les codes des animations (ne pas modifier jusqu'à la fin de la fonction anim3())

def anim1():
    global animation

    T0=0.      # époque du passage au périastre
    i=0        # inclinaison, degrés
    Omega=0.   # longitude de la node ascendante, degrés
    omega=0.   # argument du périapse, degrés
    p=[a,e,T0,i,Omega,omega]
    mEtoile=1.
    periode=(p[0]**3/mEtoile)**0.5

    fig=plt.figure(1,figsize=[4,4],dpi=120)
    ax=plt.axes()
    plt.axvline(linestyle=':',color='k')
    plt.axhline(linestyle=':',color='k')
    plt.plot(0,0,'y*',ms=15)

    tt=np.linspace(0,periode,500)
    xxMod,yyMod,zzMod=calcOrbite(p,tt,mEtoile)
    plt.plot(xxMod,yyMod,'r--')

    #pour les animations
    tt=np.linspace(0,max(1,periode),500)
    xxMod,yyMod,zzMod=calcOrbite(p,tt,mEtoile)

    point=plt.Circle((xxMod[0],yyMod[0]),0.04,color='r',zorder=5)
    ax.add_patch(point)

    #orbite réf
    xxRef,yyRef,zzRef=calcOrbite([1,0,0,0,0,0],tt,mEtoile)
    ind=(tt<1).nonzero()[0]
    plt.plot(xxRef[ind],yyRef[ind],'b--')
    pointRef=plt.Circle((xxRef[0],yyRef[0]),0.04,color='b',zorder=5)
    ax.add_patch(pointRef)

    plt.xlabel('Position relative X (UA)')
    plt.ylabel('Position relative Y (AU)')
    plt.axis('equal')
    plt.tight_layout()

    def animIter1(k):
        point.center=(xxMod[k],yyMod[k])
        pointRef.center=(xxRef[k],yyRef[k])

        return (point,)

    animation = mplAnim.FuncAnimation(fig, animIter1, frames=tt.size, interval=15, repeat=False, blit=True)
    plt.show()

def anim2():
    global animation

    a=1.       # demi-grand axe, ici en UA
    T0=0.      # époque du passage au périastre
    p=[a,e,T0,i,Omega,omega]
    mEtoile=1.
    periode=(p[0]**3/mEtoile)**0.5

    tt=np.linspace(0,periode,1000)
    xxMod,yyMod,zzMod=calcOrbite(p,tt,mEtoile)

    fig = plt.figure(figsize=(9,4))
    #partie gauche en 3D
    axW=0.42
    #set H to enable correct aspect ratio
    axH=axW*fig.get_size_inches()[0]/fig.get_size_inches()[1]
    ax=plt.axes([0.05,0.04,axW,axH],projection='3d')

    ax.scatter(0,0,0,marker='*',c='y',s=15)
    #orbite
    ax.plot(xxMod,yyMod,zzMod,c='r')

    #plan du ciel
    xp,yp=np.mgrid[-2:3,-2:3]
    ax.plot_surface(xp,yp,np.zeros_like(xp),alpha=0.2,color='b')
    ax.plot(xxMod,yyMod,0,zdir='z',c='b') #orbite dans plan
    ax.text(1.8,-1.5,0,'Plan du ciel')

    #plan orbital
    ir,w,W=i*np.pi/180,omega*np.pi/180,Omega*np.pi/180
    xpo=(np.cos(w)*np.cos(W)-np.cos(ir)*np.sin(W)*np.sin(w))*xp -\
      (np.sin(w)*np.cos(W)+np.cos(ir)*np.sin(W)*np.cos(w))*yp
    ypo=(np.cos(w)*np.sin(W)+np.cos(ir)*np.cos(W)*np.sin(w))*xp -\
      (np.sin(w)*np.sin(W)-np.cos(ir)*np.cos(W)*np.cos(w))*yp
    zpo=np.sin(ir)*np.sin(w)*xp + np.sin(ir)*np.cos(w)*yp
    ax.plot_surface(xpo,ypo,zpo,alpha=0.2,color='r')
    ax.text(xpo[0,0],ypo[0,0],zpo[0,0],'Plan orbital',ha='center')

    point=ax.scatter(xxMod[0],yyMod[0],zzMod[0],marker='o',color='r',s=15,zorder=10)

    ax.set_xlabel('X (UA)')
    ax.set_ylabel('Y (UA)')
    ax.set_zlabel('Z (UA)')
    ax.set_xlim(-2,2)
    ax.set_ylim(-2,2)
    ax.set_zlim(-2,2)
    #ax.set_aspect('equal')
    ax.view_init(azim=-90.0001, elev=89.9999)

    #partie droite en 2D, vue du ciel
    # ax2 = fig.add_subplot(122)
    ax2=plt.axes([0.6,0.11,0.3,0.77])
    ax2.scatter(0,0,marker='*',c='y',s=15)
    ax2.plot(xxMod,yyMod,c='b')
    point2=plt.Circle((xxMod[0],yyMod[0]),0.04,color='r',zorder=5)
    ax2.add_patch(point2)
    ax2.set_title('Vue du ciel')
    ax2.set_xlim(-2,2)
    ax2.set_ylim(-2,2)
    ax2.set_xlabel('X (UA)')
    ax2.set_ylabel('Y (UA)')
    ax2.set_aspect('equal')

    def animInit2():
        ax.view_init(azim=-90.0001, elev=89.9999)    
        point2.center=(xxMod[0],yyMod[0])
        point._offsets3d=((xxMod[0],),(yyMod[0],),(zzMod[0],))

    def animIter2(k):
        if k==0:
            sleep(3)
        elif k<90:
            ax.view_init(azim=-90-k/2, elev=90-k)
        else:
            ax.view_init(azim=-90-k/2, elev=1)
        point2.center=(xxMod[int(k/180*tt.size)],yyMod[int(k/180*tt.size)])
        point._offsets3d=((xxMod[int(k/180*tt.size)],),(yyMod[int(k/180*tt.size)],),(zzMod[int(k/180*tt.size)],))
        
        return point, point2
        
    animation = mplAnim.FuncAnimation(fig, animIter2, init_func=animInit2,frames=180, interval=100, repeat=False)
    plt.show()


###########Section d'appel des animations####################
    
# ---- animation 1    
e=0.5       # excentricité 0 <= e < 1
a=1.        # demi-grand axe, ici en UA

anim1()



# ---- animation 2
e=0.      # excentricité: 0 <= e < 1
i=0       # inclinaison, degrés: entre 0 et 180
Omega=0.  # longitude du noeud ascendant, degrés: entre 0 et 360
omega=0.   # argument du périastre, degrés: entre 0 et 360

#-----------------------
anim2()
