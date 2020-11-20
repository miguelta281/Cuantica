import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as ct

def Energia (n:int,a:float,m:float = ct.m_e)->list:

    """ Calcula la energía para una partícula confinada en un pozo cuantico infinito
    Parametros:
        n [int] -> Número de estados 
        a [float] -> Ancho del pozo [m]
        m [float] -> Masa de la partícula confinada [kg]
    Return:
        E [list] -> Energías para cada uno de los niveles de energia respectivamente [eV]
    """
    num_estados = [x for x in range(1,n)]
    energias = []
    for i in range(0,len(num_estados)):
        energias.append((num_estados[i] **2  * np.pi ** 2  *  ct.hbar ** 2 )/( 2* m * a ** 2) * 6.24e18 )
 
    return energias

def FuncionDeOnda (n:int,a:float,num = 100)->list:
    """
    Calcula las funciones de onda, para cada uno de los estados de energía
    Parametros:
        n [int] -> Número de estados 
        a [float] -> Ancho del pozo  [m]
        num [int] -> Número de puntos en el ancho del pozo con los cuales se va a construir la función de onda
    Return:
        x [list] -> Puntos en el rango del ancho del pozo con  los cuales se construyo la función de onda
        FuncionesDeOnda [list] -> Funciones de onda para cada nivel de energía 
    """
    num_estados = [x for x in range(1,n)]
    x = np.linspace(0,a,num)
    fun = []

    for i in range(0,len(num_estados)):
        fun.append((2 / a) * np.sin((num_estados[i] * np.pi) * (x/a)))
    
    return x, fun
    
def Visualizacion (n:int,a:float,m:float = ct.m_e,num = 100)->list:
    """ Calcula la energía para una partícula confinada en un pozo cuantico infinito
    Parametros:
        n [int] -> Número de estados 
        a [float] -> Ancho del pozo [m]
        m [float] -> Masa de la partícula confinada  [kg]
        num [int] -> Número de puntos en el ancho del pozo con los cuales se va a construir la función de onda
    Return:
        x [list] -> Puntos en el rango del ancho del pozo con  los cuales se construyo la función de onda
        E [list] -> Energías para cada uno de los niveles de energia respectivamente [eV]
        FuncionesDeOnda [list] -> Funciones de onda para cada nivel de energía    
    """
    if a > 1e-5 and a < 1:
        k = int(str(a)[-1])
    else:
        k = int(str(a)[0])


    Eng = Energia(n,a,m)
    x , FunOnda = FuncionDeOnda(n,a,num)
    num_estados = [x for x in range(1,n)]
    escalar = 10 ** (np.floor(np.log10(a))-1)
    b = list(np.diff(Eng) * k * escalar) 
    b.append(b[-1]) 

    plt.figure(figsize=(8,8))
    plt.xlabel('Tamaño del pozo [m]',fontsize =16)
    plt.ylabel('Energía [eV]',fontsize =16)
    plt.plot(x,[Eng[0] for x in range(0, len(x))], ls = '--', color = 'k', label = 'Energias')
    plt.plot(x,FunOnda[0] * b[0] + Eng[0], color = 'b' , label = 'Función de onda')
    for i in range(1,len(num_estados)):
            plt.plot(x,[Eng[i] for x in range(0, len(x))], color = 'k',ls = '--')
            plt.plot(x,FunOnda[i] * b[i] + Eng[i], color = 'b' )
    plt.legend(loc='upper right', fontsize =16 )
    plt.show()
    return  x, Eng, FunOnda    
    

