# Cristian Armando Larios Bravo
# Haciendo y probando codigos chidos

'''
Problema 1
Analice el efecto de los calores específicos variables en la eficiencia del ciclo de Otto ideal
usando aire como fluido de trabajo. Al inicio del proceso de compresión el aire está a 100 kPa y
300 K. Determine el porcentaje de error al usar calor específico constante a la temperatura
ambiente para las siguientes combinaciones de relaciones de compresión y temperaturas
máximas: r= 6, 8, 10, 12, y Tmax=1000, 1500, 2000, 2500 K.
Realice una gráfica del error contra r y contra Tmax.
'''

import math as m
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Funciones

if __name__ == "__main__":
    # Con cv constante
    r = 6
    t3 = 1000
    # Caso 1-4 cv constante
    for i in range(1,4):
        print(f"Caso {i} cv constante")
        t1 = 300
        p1 = 100
        R = 0.287
        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"t3 = {t3}")

        v1 = (R * t1) / p1
        t2 =  m.pow(r,(1.4-1))* t1
        qin = 0.718*(t3-t2)
        p2  = p1*(t2/t1)
        p3 = p2*(t3/t2)*r
        t4 =  t3 / m.pow(r,(1.4-1))
        p4 = p3 * (t4/t3) * 1/r
        qr = -0.718*(t1-t4)
        wneto = qin - qr
        n = wneto/qin
        pme = wneto / (v1*(1-(1/r)))
        eff = 1 - ((t4-t1) /(t3-t2))
        

        print(f"v1 = {v1}")
        print(f"t2 = {t2}")
        print(f"qin = {qin}")
        print(f"p2 = {p2}")
        print(f"p3 = {p3}")
        print(f"t4 = {t4}")
        print(f"p4 = {p4}")
        print(f"qr = {qr}")
        print(f"wneto = {wneto}")
        print(f"n = {n}")
        print(f"pme = {pme}")
        print(f"eficiencia termica = {eff*100}%\n")

        t3 +=500
    t3 = 2250
    for i in range(0,1):
        print(f"Caso {i+4} cv constante")
        t1 = 300
        p1 = 100
        R = 0.287
        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"t3 = {t3}")

        v1 = (R * t1) / p1
        t2 =  m.pow(r,(1.4-1))* t1
        qin = 0.718*(t3-t2)
        p2  = p1*(t2/t1)
        p3 = p2*(t3/t2)*r
        t4 =  t3 / m.pow(r,(1.4-1))
        p4 = p3 * (t4/t3) * 1/r
        qr = -0.718*(t1-t4)
        wneto = qin - qr
        n = wneto/qin
        pme = wneto / (v1*(1-(1/r)))
        eff = 1 - ((t4-t1) /(t3-t2))
        

        print(f"v1 = {v1}")
        print(f"t2 = {t2}")
        print(f"qin = {qin}")
        print(f"p2 = {p2}")
        print(f"p3 = {p3}")
        print(f"t4 = {t4}")
        print(f"p4 = {p4}")
        print(f"qr = {qr}")
        print(f"wneto = {wneto}")
        print(f"n = {n}")
        print(f"pme = {pme}")
        print(f"eficiencia termica = {eff*100}%\n")

    r = 8
    t3 = 1000
    # Caso 5-8 cv constante
    for i in range(1,4):
            print(f"Caso {i+4} cv constante")
            t1 = 300
            p1 = 100
            R = 0.287
            print("\nDatos de entrada")
            print(f"p1 = {p1}")
            print(f"t1 = {t1}")
            print(f"r = {r}")
            print(f"t3 = {t3}")

            v1 = (R * t1) / p1
            t2 =  m.pow(r,(1.4-1))* t1
            qin = 0.718*(t3-t2)
            p2  = p1*(t2/t1)
            p3 = p2*(t3/t2)*r
            t4 =  t3 / m.pow(r,(1.4-1))
            p4 = p3 * (t4/t3) * 1/r
            qr = -0.718*(t1-t4)
            wneto = qin - qr
            n = wneto/qin
            pme = wneto / (v1*(1-(1/r)))
            eff = 1 - ((t4-t1) /(t3-t2))

            print(f"v1 = {v1}")
            print(f"t2 = {t2}")
            print(f"qin = {qin}")
            print(f"p2 = {p2}")
            print(f"p3 = {p3}")
            print(f"t4 = {t4}")
            print(f"p4 = {p4}")
            print(f"qr = {qr}")
            print(f"wneto = {wneto}")
            print(f"n = {n}")
            print(f"pme = {pme}\n")
            print(f"eficiencia termica = {eff*100}%\n")

            t3 +=500
    t = 2250
    for i in range(0,1):
        print("Caso 8 cv constante")
        t1 = 300
        p1 = 100
        R = 0.287
        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"t3 = {t3}")

        v1 = (R * t1) / p1
        t2 =  m.pow(r,(1.4-1))* t1
        qin = 0.718*(t3-t2)
        p2  = p1*(t2/t1)
        p3 = p2*(t3/t2)*r
        t4 =  t3 / m.pow(r,(1.4-1))
        p4 = p3 * (t4/t3) * 1/r
        qr = -0.718*(t1-t4)
        wneto = qin - qr
        n = wneto/qin
        pme = wneto / (v1*(1-(1/r)))
        eff = 1 - ((t4-t1) /(t3-t2))
        

        print(f"v1 = {v1}")
        print(f"t2 = {t2}")
        print(f"qin = {qin}")
        print(f"p2 = {p2}")
        print(f"p3 = {p3}")
        print(f"t4 = {t4}")
        print(f"p4 = {p4}")
        print(f"qr = {qr}")
        print(f"wneto = {wneto}")
        print(f"n = {n}")
        print(f"pme = {pme}")
        print(f"eficiencia termica = {eff*100}%\n")
    r = 10
    t3 = 1000
    # Caso 9-12 cv constante
    for i in range(1,4):
            print(f"Caso {i+8} cv constante")
            t1 = 300
            p1 = 100
            R = 0.287
            print("\nDatos de entrada")
            print(f"p1 = {p1}")
            print(f"t1 = {t1}")
            print(f"r = {r}")
            print(f"t3 = {t3}")

            v1 = (R * t1) / p1
            t2 =  m.pow(r,(1.4-1))* t1
            qin = 0.718*(t3-t2)
            p2  = p1*(t2/t1)
            p3 = p2*(t3/t2)*r
            t4 =  t3 / m.pow(r,(1.4-1))
            p4 = p3 * (t4/t3) * 1/r
            qr = -0.718*(t1-t4)
            wneto = qin - qr
            n = wneto/qin
            pme = wneto / (v1*(1-(1/r)))
            eff = 1 - ((t4-t1) /(t3-t2))

            print(f"v1 = {v1}")
            print(f"t2 = {t2}")
            print(f"qin = {qin}")
            print(f"p2 = {p2}")
            print(f"p3 = {p3}")
            print(f"t4 = {t4}")
            print(f"p4 = {p4}")
            print(f"qr = {qr}")
            print(f"wneto = {wneto}")
            print(f"n = {n}")
            print(f"pme = {pme}")
            print(f"eficiencia termica = {eff*100}%\n")

            t3 +=500
    t3 = 2250
    for i in range(0,1):
        print("Caso 12 cv constante")
        t1 = 300
        p1 = 100
        R = 0.287
        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"t3 = {t3}")

        v1 = (R * t1) / p1
        t2 =  m.pow(r,(1.4-1))* t1
        qin = 0.718*(t3-t2)
        p2  = p1*(t2/t1)
        p3 = p2*(t3/t2)*r
        t4 =  t3 / m.pow(r,(1.4-1))
        p4 = p3 * (t4/t3) * 1/r
        qr = -0.718*(t1-t4)
        wneto = qin - qr
        n = wneto/qin
        pme = wneto / (v1*(1-(1/r)))
        eff = 1 - ((t4-t1) /(t3-t2))
        

        print(f"v1 = {v1}")
        print(f"t2 = {t2}")
        print(f"qin = {qin}")
        print(f"p2 = {p2}")
        print(f"p3 = {p3}")
        print(f"t4 = {t4}")
        print(f"p4 = {p4}")
        print(f"qr = {qr}")
        print(f"wneto = {wneto}")
        print(f"n = {n}")
        print(f"pme = {pme}")
        print(f"eficiencia termica = {eff*100}%\n")
    r = 12
    t3 = 1000
    # Caso 13-16 cv constante
    for i in range(1,4):
            print(f"Caso {i+12} cv constante")
            t1 = 300
            p1 = 100
            R = 0.287
            print("\nDatos de entrada")
            print(f"p1 = {p1}")
            print(f"t1 = {t1}")
            print(f"r = {r}")
            print(f"t3 = {t3}")

            v1 = (R * t1) / p1
            t2 =  m.pow(r,(1.4-1))* t1
            qin = 0.718*(t3-t2)
            p2  = p1*(t2/t1)
            p3 = p2*(t3/t2)*r
            t4 =  t3 / m.pow(r,(1.4-1))
            p4 = p3 * (t4/t3) * 1/r
            qr = -0.718*(t1-t4)
            wneto = qin - qr
            n = wneto/qin
            pme = wneto / (v1*(1-(1/r)))
            eff = 1 - ((t4-t1) /(t3-t2))

            print(f"v1 = {v1}")
            print(f"t2 = {t2}")
            print(f"qin = {qin}")
            print(f"p2 = {p2}")
            print(f"p3 = {p3}")
            print(f"t4 = {t4}")
            print(f"p4 = {p4}")
            print(f"qr = {qr}")
            print(f"wneto = {wneto}")
            print(f"n = {n}")
            print(f"pme = {pme}")
            print(f"eficiencia termica = {eff*100}%\n")

            t3 +=500
    t3=2250
    for i in range(0,1):
        print("Caso 16 cv constante")
        t1 = 300
        p1 = 100
        R = 0.287
        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"t3 = {t3}")

        v1 = (R * t1) / p1
        t2 =  m.pow(r,(1.4-1))* t1
        qin = 0.718*(t3-t2)
        p2  = p1*(t2/t1)
        p3 = p2*(t3/t2)*r
        t4 =  t3 / m.pow(r,(1.4-1))
        p4 = p3 * (t4/t3) * 1/r
        qr = -0.718*(t1-t4)
        wneto = qin - qr
        n = wneto/qin
        pme = wneto / (v1*(1-(1/r)))
        eff = 1 - ((t4-t1) /(t3-t2))
        

        print(f"v1 = {v1}")
        print(f"t2 = {t2}")
        print(f"qin = {qin}")
        print(f"p2 = {p2}")
        print(f"p3 = {p3}")
        print(f"t4 = {t4}")
        print(f"p4 = {p4}")
        print(f"qr = {qr}")
        print(f"wneto = {wneto}")
        print(f"n = {n}")
        print(f"pme = {pme}")
        print(f"eficiencia termica = {eff*100}%\n")
    
    
    # Con cv variable

    # Datos de la tabla de propiedades de gas ideal del aire
    datos = pd.read_excel('Ciclo Otto 2\gas_ideal_propiedades.xlsx', header=0)
    t = datos['T']      # Temperatura
    h = datos['h']      #
    Pr = datos['Pr']    #
    u = datos['u']      #
    vr = datos['vr']    #
    s = datos['s']      #

    # Caso 1-4 cv variable
    r = 6
    for i in range(1,4):

        print(f"Caso {i} cv variable")
        p1 = 100
        t1 = 300
        t3 = 1000
        rc = 2
        R = 0.287

        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"rc = {rc}")
        print(f"t3 = {t3}")

        ''' Proceso 1-2 '''
        # Estado 1
        print("\nEstado 1")
        # Calcular Pr1, h1, Vr1
        for i in range(0,121,1):
            if round(t1) >= t[120]:     # Por si llega al limite de temperatura de la tabla
                pr1 = Pr[120]
                u1 = u[120]
                vr1 = vr[120]
                break

            if round(t1) >= t[i] and round(t1) < t[i+1]:
                pr1 = Pr[i]
                u1 = u[i]
                vr1 = vr[i]
                break
        
        print(f'Pr1 = {pr1}')
        print(f'u1 = {u1}')
        print(f'Vr1 = {vr1}')

        # Estado 2
        print("\nEstado 2")
        # Calculamos Vr2
        # v = vr1/vr2   =>  vr2 = vr1/r
        # r = vr1 / vr2
        vr2 = vr1 / r
        # Calculamos Pr2
        print(f"Vr2 = {vr2}")
        for i in range(0,121,1):
            if vr2 <= vr[i] and vr2 > vr[i+1]:
                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                # y = y0 + ((y1-y0) / (x1-x0)) * (x - x0)
                t2 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                h2 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                pr2 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                break

        print(f"t2 = {t2}")
        print(f"h2 = {h2}")
        print(f"Pr2 = {pr2}")
        # Dado que es una presion icentropica
        # p2 = p1 * (pr2/pr1)
        p2 = p1 * (pr2 / pr1)
        print(f"p2 = {p2}")

        ''' Proceso 2-3 '''
        print("\nEstado 3")
        # Estado 3      p3 = p2
        p3 = p2
        print(f"p3 = {p3}")
        # rc = v3/v2
        # Por la ec. de los gases ideales:
        # (p2*v2) / T2 = (p3*v3) / t3 => t3 = t2(p3/p2)(v3/v2)

        for i in range(0,120,1):
            if t3 >= t[i] and t3 < t[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                pr3 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                vr3 = vraux2_arriba + ( (vraux1_abajo - vraux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                h3 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)

                
                break

        print(f"h3 = {h3}")
        print(f"Pr3 = {pr3}")
        print(f"Vr3 = {vr3}")

        ''' Proceso 3-4 '''
        # Estado 4
        print("\nEstado 4")
        # vr4/vr4 = v4/v3
        # vr4 = vr3(r/rc)

        vr4 = vr3 * (r / rc)
        print(f"Vr4 = {vr4}")

        for i in range(0,120,1):
            if vr4 <= vr[i] and vr4 > vr[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                uaux1_abajo = u[i]
                uaux2_arriba = u[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                t4 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                pr4 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                u4 = uaux2_arriba + ( (uaux1_abajo - uaux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)

                
                break
        
        print(f"t4 = {t4}")
        print(f"Pr4 = {pr4}")
        print(f"u4 = {u4}")

        # p4 = p3(pr4 / pr3)
        p4 = p3 * (pr4 / pr3)
        print(f"p4 = {p4}")
        # t3 = La temperatura despues del proceso de adicion de calor
        print(f"\n\n######  TEMPERATURA DESPUES DEL PROCESO DE ADICION DE CALOR = {t3}  ######")

        """ 
        a) Temperatura Maxima
        Comparar todas las temperaturas
        """
        lista_temperaturas = [t1, t2, t3, t4]
        temp_mayor = 0
        nums = 4

        for i in range(nums):
            num = lista_temperaturas[i]
            if num > temp_mayor:
                temp_mayor = num



        """ 
        b) Presión Maxima
        Comparar todas las presiones
        """
        if h2 > h3:
            pMayor = h2
        else:
            pMayor = h3

        '''
        c) Eficiencia energetica
        nDiesel = Wnet / qsum  
        · qsum = h3 - h2
        · qcad = u1 - u4
        '''
        qsum = h3 -h2
        qcad = u1 - u4
        wneto = qsum + qcad
        nDiesel = wneto / qsum
        print(f"qsum = {qsum}")
        print(f"qcad = {qcad}")
        print(f"Wneto = {wneto}")

        
        """ 
        d) Presion media efectiva
        pme = wneto / (v1-v2)
        v1 = (R*T) / P
        R = constante universal (0.287)
        v2 = (R * T2) / P2
        """

        v1 = (R * t1) / p1
        v2 = (R * t2) / p2
        v3 = v2
        v4 = v1
        pme = wneto / (v1-v2)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v3 = {v3}")
        print(f"v4 = {v4}")
        
        

        print("\n\n~~~~~~~~~~~~~~~~ RESULTADOS ~~~~~~~~~~~~~~~~")
        print(f"a) Temperatura máxima = {temp_mayor}ºK")
        print(f"b) Presion Máxima = {pMayor}kJ/kg")
        print(f"c) Eficiencia Térmica: nDiesel = {nDiesel}")
        print(f"d) Presión Media Efectiva: PME = {pme}kPa\n")
    
        t3+=500

    for i in range(4,5):

        print(f"Caso {i} cv variable")
        p1 = 100
        t1 = 300
        t3 = 2250
        rc = 2
        R = 0.287

        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"rc = {rc}")
        print(f"t3 = {t3}")

        ''' Proceso 1-2 '''
        # Estado 1
        print("\nEstado 1")
        # Calcular Pr1, h1, Vr1
        for i in range(0,120,1):
            if round(t1) >= t[i] and round(t1) < t[i+1]:
                pr1 = Pr[i]
                u1 = u[i]
                vr1 = vr[i]
                break
        
        print(f'Pr1 = {pr1}')
        print(f'u1 = {u1}')
        print(f'Vr1 = {vr1}')

        # Estado 2
        print("\nEstado 2")
        # Calculamos Vr2
        # v = vr1/vr2   =>  vr2 = vr1/r
        # r = vr1 / vr2
        vr2 = vr1 / r
        # Calculamos Pr2
        print(f"Vr2 = {vr2}")
        for i in range(0,121,1):
            if vr2 <= vr[i] and vr2 > vr[i+1]:
                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                # y = y0 + ((y1-y0) / (x1-x0)) * (x - x0)
                t2 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                h2 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                pr2 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                break

        print(f"t2 = {t2}")
        print(f"h2 = {h2}")
        print(f"Pr2 = {pr2}")
        # Dado que es una presion icentropica
        # p2 = p1 * (pr2/pr1)
        p2 = p1 * (pr2 / pr1)
        print(f"p2 = {p2}")

        ''' Proceso 2-3 '''
        print("\nEstado 3")
        # Estado 3      p3 = p2
        p3 = p2
        print(f"p3 = {p3}")
        # rc = v3/v2
        # Por la ec. de los gases ideales:
        # (p2*v2) / T2 = (p3*v3) / t3 => t3 = t2(p3/p2)(v3/v2)

        for i in range(0, 120, 1):
            if t3 >= t[i] and t3 < t[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                pr3 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                vr3 = vraux2_arriba + ( (vraux1_abajo - vraux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                h3 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)

                
                break

        print(f"h3 = {h3}")
        print(f"Pr3 = {pr3}")
        print(f"Vr3 = {vr3}")

        ''' Proceso 3-4 '''
        # Estado 4
        print("\nEstado 4")
        # vr4/vr4 = v4/v3
        # vr4 = vr3(r/rc)

        vr4 = vr3 * (r / rc)
        print(f"Vr4 = {vr4}")

        for i in range(0, 120, 1):
            if vr4 <= vr[i] and vr4 > vr[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                uaux1_abajo = u[i]
                uaux2_arriba = u[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                t4 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                pr4 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                u4 = uaux2_arriba + ( (uaux1_abajo - uaux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)

                
                break
        
        print(f"t4 = {t4}")
        print(f"Pr4 = {pr4}")
        print(f"u4 = {u4}")

        # p4 = p3(pr4 / pr3)
        p4 = p3 * (pr4 / pr3)
        print(f"p4 = {p4}")
        # t3 = La temperatura despues del proceso de adicion de calor
        print(f"\n\n######  TEMPERATURA DESPUES DEL PROCESO DE ADICION DE CALOR = {t3}  ######")

        """ 
        a) Temperatura Maxima
        Comparar todas las temperaturas
        """
        lista_temperaturas = [t1, t2, t3, t4]
        temp_mayor = 0
        nums = 4

        for i in range(nums):
            num = lista_temperaturas[i]
            if num > temp_mayor:
                temp_mayor = num



        """ 
        b) Presión Maxima
        Comparar todas las presiones
        """
        if h2 > h3:
            pMayor = h2
        else:
            pMayor = h3

        '''
        c) Eficiencia energetica
        nDiesel = Wnet / qsum  
        · qsum = h3 - h2
        · qcad = u1 - u4
        '''
        qsum = h3 -h2
        qcad = u1 - u4
        wneto = qsum + qcad
        nDiesel = wneto / qsum
        print(f"qsum = {qsum}")
        print(f"qcad = {qcad}")
        print(f"Wneto = {wneto}")

        
        """ 
        d) Presion media efectiva
        pme = wneto / (v1-v2)
        v1 = (R*T) / P
        R = constante universal (0.287)
        v2 = (R * T2) / P2
        """

        v1 = (R * t1) / p1
        v2 = (R * t2) / p2
        v3 = v2
        v4 = v1
        pme = wneto / (v1-v2)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v3 = {v3}")
        print(f"v4 = {v4}")
        
        

        print("\n\n~~~~~~~~~~~~~~~~ RESULTADOS ~~~~~~~~~~~~~~~~")
        print(f"a) Temperatura máxima = {temp_mayor}ºK")
        print(f"b) Presion Máxima = {pMayor}kJ/kg")
        print(f"c) Eficiencia Térmica: nDiesel = {nDiesel}")
        print(f"d) Presión Media Efectiva: PME = {pme}kPa\n")

    # Caso 5-8 cv variable
    r = 8
    for i in range(5,8):

        print(f"Caso {i} cv variable")
        p1 = 100
        t1 = 300
        t3 = 1000
        rc = 2
        R = 0.287

        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"rc = {rc}")
        print(f"t3 = {t3}")

        ''' Proceso 1-2 '''
        # Estado 1
        print("\nEstado 1")
        # Calcular Pr1, h1, Vr1
        for i in range(0,121,1):
            if round(t1) >= t[120]:     # Por si llega al limite de temperatura de la tabla
                pr1 = Pr[120]
                u1 = u[120]
                vr1 = vr[120]
                break

            if round(t1) >= t[i] and round(t1) < t[i+1]:
                pr1 = Pr[i]
                u1 = u[i]
                vr1 = vr[i]
                break
        
        print(f'Pr1 = {pr1}')
        print(f'u1 = {u1}')
        print(f'Vr1 = {vr1}')

        # Estado 2
        print("\nEstado 2")
        # Calculamos Vr2
        # v = vr1/vr2   =>  vr2 = vr1/r
        # r = vr1 / vr2
        vr2 = vr1 / r
        # Calculamos Pr2
        print(f"Vr2 = {vr2}")
        for i in range(0,121,1):
            if vr2 <= vr[i] and vr2 > vr[i+1]:
                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                # y = y0 + ((y1-y0) / (x1-x0)) * (x - x0)
                t2 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                h2 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                pr2 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                break

        print(f"t2 = {t2}")
        print(f"h2 = {h2}")
        print(f"Pr2 = {pr2}")
        # Dado que es una presion icentropica
        # p2 = p1 * (pr2/pr1)
        p2 = p1 * (pr2 / pr1)
        print(f"p2 = {p2}")

        ''' Proceso 2-3 '''
        print("\nEstado 3")
        # Estado 3      p3 = p2
        p3 = p2
        print(f"p3 = {p3}")
        # rc = v3/v2
        # Por la ec. de los gases ideales:
        # (p2*v2) / T2 = (p3*v3) / t3 => t3 = t2(p3/p2)(v3/v2)

        for i in range(0,120,1):
            if t3 >= t[i] and t3 < t[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                pr3 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                vr3 = vraux2_arriba + ( (vraux1_abajo - vraux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                h3 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)

                
                break

        print(f"h3 = {h3}")
        print(f"Pr3 = {pr3}")
        print(f"Vr3 = {vr3}")

        ''' Proceso 3-4 '''
        # Estado 4
        print("\nEstado 4")
        # vr4/vr4 = v4/v3
        # vr4 = vr3(r/rc)

        vr4 = vr3 * (r / rc)
        print(f"Vr4 = {vr4}")

        for i in range(0,120,1):
            if vr4 <= vr[i] and vr4 > vr[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                uaux1_abajo = u[i]
                uaux2_arriba = u[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                t4 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                pr4 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                u4 = uaux2_arriba + ( (uaux1_abajo - uaux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)

                
                break
        
        print(f"t4 = {t4}")
        print(f"Pr4 = {pr4}")
        print(f"u4 = {u4}")

        # p4 = p3(pr4 / pr3)
        p4 = p3 * (pr4 / pr3)
        print(f"p4 = {p4}")
        # t3 = La temperatura despues del proceso de adicion de calor
        print(f"\n\n######  TEMPERATURA DESPUES DEL PROCESO DE ADICION DE CALOR = {t3}  ######")

        """ 
        a) Temperatura Maxima
        Comparar todas las temperaturas
        """
        lista_temperaturas = [t1, t2, t3, t4]
        temp_mayor = 0
        nums = 4

        for i in range(nums):
            num = lista_temperaturas[i]
            if num > temp_mayor:
                temp_mayor = num



        """ 
        b) Presión Maxima
        Comparar todas las presiones
        """
        if h2 > h3:
            pMayor = h2
        else:
            pMayor = h3

        '''
        c) Eficiencia energetica
        nDiesel = Wnet / qsum  
        · qsum = h3 - h2
        · qcad = u1 - u4
        '''
        qsum = h3 -h2
        qcad = u1 - u4
        wneto = qsum + qcad
        nDiesel = wneto / qsum
        print(f"qsum = {qsum}")
        print(f"qcad = {qcad}")
        print(f"Wneto = {wneto}")

        
        """ 
        d) Presion media efectiva
        pme = wneto / (v1-v2)
        v1 = (R*T) / P
        R = constante universal (0.287)
        v2 = (R * T2) / P2
        """

        v1 = (R * t1) / p1
        v2 = (R * t2) / p2
        v3 = v2
        v4 = v1
        pme = wneto / (v1-v2)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v3 = {v3}")
        print(f"v4 = {v4}")
        
        

        print("\n\n~~~~~~~~~~~~~~~~ RESULTADOS ~~~~~~~~~~~~~~~~")
        print(f"a) Temperatura máxima = {temp_mayor}ºK")
        print(f"b) Presion Máxima = {pMayor}kJ/kg")
        print(f"c) Eficiencia Térmica: nDiesel = {nDiesel}")
        print(f"d) Presión Media Efectiva: PME = {pme}kPa\n")
    
        t3+=500
    
    for i in range(8,9):

        print(f"Caso {i} cv variable")
        p1 = 100
        t1 = 300
        t3 = 2250
        rc = 2
        R = 0.287

        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"rc = {rc}")
        print(f"t3 = {t3}")

        ''' Proceso 1-2 '''
        # Estado 1
        print("\nEstado 1")
        # Calcular Pr1, h1, Vr1
        for i in range(0,121,1):
            if round(t1) >= t[120]:     # Por si llega al limite de temperatura de la tabla
                pr1 = Pr[120]
                u1 = u[120]
                vr1 = vr[120]
                break

            if round(t1) >= t[i] and round(t1) < t[i+1]:
                pr1 = Pr[i]
                u1 = u[i]
                vr1 = vr[i]
                break
        
        print(f'Pr1 = {pr1}')
        print(f'u1 = {u1}')
        print(f'Vr1 = {vr1}')

        # Estado 2
        print("\nEstado 2")
        # Calculamos Vr2
        # v = vr1/vr2   =>  vr2 = vr1/r
        # r = vr1 / vr2
        vr2 = vr1 / r
        # Calculamos Pr2
        print(f"Vr2 = {vr2}")
        for i in range(0,121,1):
            if vr2 <= vr[i] and vr2 > vr[i+1]:
                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                # y = y0 + ((y1-y0) / (x1-x0)) * (x - x0)
                t2 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                h2 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                pr2 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                break

        print(f"t2 = {t2}")
        print(f"h2 = {h2}")
        print(f"Pr2 = {pr2}")
        # Dado que es una presion icentropica
        # p2 = p1 * (pr2/pr1)
        p2 = p1 * (pr2 / pr1)
        print(f"p2 = {p2}")

        ''' Proceso 2-3 '''
        print("\nEstado 3")
        # Estado 3      p3 = p2
        p3 = p2
        print(f"p3 = {p3}")
        # rc = v3/v2
        # Por la ec. de los gases ideales:
        # (p2*v2) / T2 = (p3*v3) / t3 => t3 = t2(p3/p2)(v3/v2)

        for i in range(0,120,1):
            if t3 >= t[i] and t3 < t[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                pr3 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                vr3 = vraux2_arriba + ( (vraux1_abajo - vraux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                h3 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)

                
                break

        print(f"h3 = {h3}")
        print(f"Pr3 = {pr3}")
        print(f"Vr3 = {vr3}")

        ''' Proceso 3-4 '''
        # Estado 4
        print("\nEstado 4")
        # vr4/vr4 = v4/v3
        # vr4 = vr3(r/rc)

        vr4 = vr3 * (r / rc)
        print(f"Vr4 = {vr4}")

        for i in range(0,120,1):
            if vr4 <= vr[i] and vr4 > vr[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                uaux1_abajo = u[i]
                uaux2_arriba = u[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                t4 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                pr4 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                u4 = uaux2_arriba + ( (uaux1_abajo - uaux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)

                
                break
        
        print(f"t4 = {t4}")
        print(f"Pr4 = {pr4}")
        print(f"u4 = {u4}")

        # p4 = p3(pr4 / pr3)
        p4 = p3 * (pr4 / pr3)
        print(f"p4 = {p4}")
        # t3 = La temperatura despues del proceso de adicion de calor
        print(f"\n\n######  TEMPERATURA DESPUES DEL PROCESO DE ADICION DE CALOR = {t3}  ######")

        """ 
        a) Temperatura Maxima
        Comparar todas las temperaturas
        """
        lista_temperaturas = [t1, t2, t3, t4]
        temp_mayor = 0
        nums = 4

        for i in range(nums):
            num = lista_temperaturas[i]
            if num > temp_mayor:
                temp_mayor = num



        """ 
        b) Presión Maxima
        Comparar todas las presiones
        """
        if h2 > h3:
            pMayor = h2
        else:
            pMayor = h3

        '''
        c) Eficiencia energetica
        nDiesel = Wnet / qsum  
        · qsum = h3 - h2
        · qcad = u1 - u4
        '''
        qsum = h3 -h2
        qcad = u1 - u4
        wneto = qsum + qcad
        nDiesel = wneto / qsum
        print(f"qsum = {qsum}")
        print(f"qcad = {qcad}")
        print(f"Wneto = {wneto}")

        
        """ 
        d) Presion media efectiva
        pme = wneto / (v1-v2)
        v1 = (R*T) / P
        R = constante universal (0.287)
        v2 = (R * T2) / P2
        """

        v1 = (R * t1) / p1
        v2 = (R * t2) / p2
        v3 = v2
        v4 = v1
        pme = wneto / (v1-v2)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v3 = {v3}")
        print(f"v4 = {v4}")
        
        

        print("\n\n~~~~~~~~~~~~~~~~ RESULTADOS ~~~~~~~~~~~~~~~~")
        print(f"a) Temperatura máxima = {temp_mayor}ºK")
        print(f"b) Presion Máxima = {pMayor}kJ/kg")
        print(f"c) Eficiencia Térmica: nDiesel = {nDiesel}")
        print(f"d) Presión Media Efectiva: PME = {pme}kPa\n")

    # Caso 9-12 cv variable
    r = 10
    for i in range(9,12):

        print(f"Caso {i} cv variable")
        p1 = 100
        t1 = 300
        t3 = 1000
        rc = 2
        R = 0.287

        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"rc = {rc}")
        print(f"t3 = {t3}")

        ''' Proceso 1-2 '''
        # Estado 1
        print("\nEstado 1")
        # Calcular Pr1, h1, Vr1
        for i in range(0,121,1):
            if round(t1) >= t[120]:     # Por si llega al limite de temperatura de la tabla
                pr1 = Pr[120]
                u1 = u[120]
                vr1 = vr[120]
                break

            if round(t1) >= t[i] and round(t1) < t[i+1]:
                pr1 = Pr[i]
                u1 = u[i]
                vr1 = vr[i]
                break
        
        print(f'Pr1 = {pr1}')
        print(f'u1 = {u1}')
        print(f'Vr1 = {vr1}')

        # Estado 2
        print("\nEstado 2")
        # Calculamos Vr2
        # v = vr1/vr2   =>  vr2 = vr1/r
        # r = vr1 / vr2
        vr2 = vr1 / r
        # Calculamos Pr2
        print(f"Vr2 = {vr2}")
        for i in range(0,121,1):
            if vr2 <= vr[i] and vr2 > vr[i+1]:
                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                # y = y0 + ((y1-y0) / (x1-x0)) * (x - x0)
                t2 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                h2 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                pr2 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                break

        print(f"t2 = {t2}")
        print(f"h2 = {h2}")
        print(f"Pr2 = {pr2}")
        # Dado que es una presion icentropica
        # p2 = p1 * (pr2/pr1)
        p2 = p1 * (pr2 / pr1)
        print(f"p2 = {p2}")

        ''' Proceso 2-3 '''
        print("\nEstado 3")
        # Estado 3      p3 = p2
        p3 = p2
        print(f"p3 = {p3}")
        # rc = v3/v2
        # Por la ec. de los gases ideales:
        # (p2*v2) / T2 = (p3*v3) / t3 => t3 = t2(p3/p2)(v3/v2)

        for i in range(0,120,1):
            if t3 >= t[i] and t3 < t[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                pr3 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                vr3 = vraux2_arriba + ( (vraux1_abajo - vraux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                h3 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)

                
                break

        print(f"h3 = {h3}")
        print(f"Pr3 = {pr3}")
        print(f"Vr3 = {vr3}")

        ''' Proceso 3-4 '''
        # Estado 4
        print("\nEstado 4")
        # vr4/vr4 = v4/v3
        # vr4 = vr3(r/rc)

        vr4 = vr3 * (r / rc)
        print(f"Vr4 = {vr4}")

        for i in range(0,120,1):
            if vr4 <= vr[i] and vr4 > vr[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                uaux1_abajo = u[i]
                uaux2_arriba = u[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                t4 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                pr4 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                u4 = uaux2_arriba + ( (uaux1_abajo - uaux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)

                
                break
        
        print(f"t4 = {t4}")
        print(f"Pr4 = {pr4}")
        print(f"u4 = {u4}")

        # p4 = p3(pr4 / pr3)
        p4 = p3 * (pr4 / pr3)
        print(f"p4 = {p4}")
        # t3 = La temperatura despues del proceso de adicion de calor
        print(f"\n\n######  TEMPERATURA DESPUES DEL PROCESO DE ADICION DE CALOR = {t3}  ######")

        """ 
        a) Temperatura Maxima
        Comparar todas las temperaturas
        """
        lista_temperaturas = [t1, t2, t3, t4]
        temp_mayor = 0
        nums = 4

        for i in range(nums):
            num = lista_temperaturas[i]
            if num > temp_mayor:
                temp_mayor = num



        """ 
        b) Presión Maxima
        Comparar todas las presiones
        """
        if h2 > h3:
            pMayor = h2
        else:
            pMayor = h3

        '''
        c) Eficiencia energetica
        nDiesel = Wnet / qsum  
        · qsum = h3 - h2
        · qcad = u1 - u4
        '''
        qsum = h3 -h2
        qcad = u1 - u4
        wneto = qsum + qcad
        nDiesel = wneto / qsum
        print(f"qsum = {qsum}")
        print(f"qcad = {qcad}")
        print(f"Wneto = {wneto}")

        
        """ 
        d) Presion media efectiva
        pme = wneto / (v1-v2)
        v1 = (R*T) / P
        R = constante universal (0.287)
        v2 = (R * T2) / P2
        """

        v1 = (R * t1) / p1
        v2 = (R * t2) / p2
        v3 = v2
        v4 = v1
        pme = wneto / (v1-v2)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v3 = {v3}")
        print(f"v4 = {v4}")
        
        

        print("\n\n~~~~~~~~~~~~~~~~ RESULTADOS ~~~~~~~~~~~~~~~~")
        print(f"a) Temperatura máxima = {temp_mayor}ºK")
        print(f"b) Presion Máxima = {pMayor}kJ/kg")
        print(f"c) Eficiencia Térmica: nDiesel = {nDiesel}")
        print(f"d) Presión Media Efectiva: PME = {pme}kPa\n")
    
        t3+=500

    for i in range(12,13):

        print(f"Caso {i} cv variable")
        p1 = 100
        t1 = 300
        t3 = 2250
        rc = 2
        R = 0.287

        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"rc = {rc}")
        print(f"t3 = {t3}")

        ''' Proceso 1-2 '''
        # Estado 1
        print("\nEstado 1")
        # Calcular Pr1, h1, Vr1
        for i in range(0,121,1):
            if round(t1) >= t[120]:     # Por si llega al limite de temperatura de la tabla
                pr1 = Pr[120]
                u1 = u[120]
                vr1 = vr[120]
                break

            if round(t1) >= t[i] and round(t1) < t[i+1]:
                pr1 = Pr[i]
                u1 = u[i]
                vr1 = vr[i]
                break
        
        print(f'Pr1 = {pr1}')
        print(f'u1 = {u1}')
        print(f'Vr1 = {vr1}')

        # Estado 2
        print("\nEstado 2")
        # Calculamos Vr2
        # v = vr1/vr2   =>  vr2 = vr1/r
        # r = vr1 / vr2
        vr2 = vr1 / r
        # Calculamos Pr2
        print(f"Vr2 = {vr2}")
        for i in range(0,121,1):
            if vr2 <= vr[i] and vr2 > vr[i+1]:
                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                # y = y0 + ((y1-y0) / (x1-x0)) * (x - x0)
                t2 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                h2 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                pr2 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                break

        print(f"t2 = {t2}")
        print(f"h2 = {h2}")
        print(f"Pr2 = {pr2}")
        # Dado que es una presion icentropica
        # p2 = p1 * (pr2/pr1)
        p2 = p1 * (pr2 / pr1)
        print(f"p2 = {p2}")

        ''' Proceso 2-3 '''
        print("\nEstado 3")
        # Estado 3      p3 = p2
        p3 = p2
        print(f"p3 = {p3}")
        # rc = v3/v2
        # Por la ec. de los gases ideales:
        # (p2*v2) / T2 = (p3*v3) / t3 => t3 = t2(p3/p2)(v3/v2)

        for i in range(0,120,1):
            if t3 >= t[i] and t3 < t[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                pr3 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                vr3 = vraux2_arriba + ( (vraux1_abajo - vraux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                h3 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)

                
                break

        print(f"h3 = {h3}")
        print(f"Pr3 = {pr3}")
        print(f"Vr3 = {vr3}")

        ''' Proceso 3-4 '''
        # Estado 4
        print("\nEstado 4")
        # vr4/vr4 = v4/v3
        # vr4 = vr3(r/rc)

        vr4 = vr3 * (r / rc)
        print(f"Vr4 = {vr4}")

        for i in range(0,120,1):
            if vr4 <= vr[i] and vr4 > vr[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                uaux1_abajo = u[i]
                uaux2_arriba = u[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                t4 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                pr4 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                u4 = uaux2_arriba + ( (uaux1_abajo - uaux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)

                
                break
        
        print(f"t4 = {t4}")
        print(f"Pr4 = {pr4}")
        print(f"u4 = {u4}")

        # p4 = p3(pr4 / pr3)
        p4 = p3 * (pr4 / pr3)
        print(f"p4 = {p4}")
        # t3 = La temperatura despues del proceso de adicion de calor
        print(f"\n\n######  TEMPERATURA DESPUES DEL PROCESO DE ADICION DE CALOR = {t3}  ######")

        """ 
        a) Temperatura Maxima
        Comparar todas las temperaturas
        """
        lista_temperaturas = [t1, t2, t3, t4]
        temp_mayor = 0
        nums = 4

        for i in range(nums):
            num = lista_temperaturas[i]
            if num > temp_mayor:
                temp_mayor = num



        """ 
        b) Presión Maxima
        Comparar todas las presiones
        """
        if h2 > h3:
            pMayor = h2
        else:
            pMayor = h3

        '''
        c) Eficiencia energetica
        nDiesel = Wnet / qsum  
        · qsum = h3 - h2
        · qcad = u1 - u4
        '''
        qsum = h3 -h2
        qcad = u1 - u4
        wneto = qsum + qcad
        nDiesel = wneto / qsum
        print(f"qsum = {qsum}")
        print(f"qcad = {qcad}")
        print(f"Wneto = {wneto}")

        
        """ 
        d) Presion media efectiva
        pme = wneto / (v1-v2)
        v1 = (R*T) / P
        R = constante universal (0.287)
        v2 = (R * T2) / P2
        """

        v1 = (R * t1) / p1
        v2 = (R * t2) / p2
        v3 = v2
        v4 = v1
        pme = wneto / (v1-v2)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v3 = {v3}")
        print(f"v4 = {v4}")
        
        

        print("\n\n~~~~~~~~~~~~~~~~ RESULTADOS ~~~~~~~~~~~~~~~~")
        print(f"a) Temperatura máxima = {temp_mayor}ºK")
        print(f"b) Presion Máxima = {pMayor}kJ/kg")
        print(f"c) Eficiencia Térmica: nDiesel = {nDiesel}")
        print(f"d) Presión Media Efectiva: PME = {pme}kPa\n")

    # Caso 13-16 cv variable
    r = 12
    for i in range(13,16):

        print(f"Caso {i} cv variable")
        p1 = 100
        t1 = 300
        t3 = 2250
        rc = 2
        R = 0.287

        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"rc = {rc}")
        print(f"t3 = {t3}")

        ''' Proceso 1-2 '''
        # Estado 1
        print("\nEstado 1")
        # Calcular Pr1, h1, Vr1
        for i in range(0,121,1):
            if round(t1) >= t[120]:     # Por si llega al limite de temperatura de la tabla
                pr1 = Pr[120]
                u1 = u[120]
                vr1 = vr[120]
                break

            if round(t1) >= t[i] and round(t1) < t[i+1]:
                pr1 = Pr[i]
                u1 = u[i]
                vr1 = vr[i]
                break
        
        print(f'Pr1 = {pr1}')
        print(f'u1 = {u1}')
        print(f'Vr1 = {vr1}')

        # Estado 2
        print("\nEstado 2")
        # Calculamos Vr2
        # v = vr1/vr2   =>  vr2 = vr1/r
        # r = vr1 / vr2
        vr2 = vr1 / r
        # Calculamos Pr2
        print(f"Vr2 = {vr2}")
        for i in range(0,121,1):
            if vr2 <= vr[i] and vr2 > vr[i+1]:
                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                # y = y0 + ((y1-y0) / (x1-x0)) * (x - x0)
                t2 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                h2 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                pr2 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                break

        print(f"t2 = {t2}")
        print(f"h2 = {h2}")
        print(f"Pr2 = {pr2}")
        # Dado que es una presion icentropica
        # p2 = p1 * (pr2/pr1)
        p2 = p1 * (pr2 / pr1)
        print(f"p2 = {p2}")

        ''' Proceso 2-3 '''
        print("\nEstado 3")
        # Estado 3      p3 = p2
        p3 = p2
        print(f"p3 = {p3}")
        # rc = v3/v2
        # Por la ec. de los gases ideales:
        # (p2*v2) / T2 = (p3*v3) / t3 => t3 = t2(p3/p2)(v3/v2)

        for i in range(0,120,1):
            if t3 >= t[i] and t3 < t[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                pr3 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                vr3 = vraux2_arriba + ( (vraux1_abajo - vraux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                h3 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)

                
                break

        print(f"h3 = {h3}")
        print(f"Pr3 = {pr3}")
        print(f"Vr3 = {vr3}")

        ''' Proceso 3-4 '''
        # Estado 4
        print("\nEstado 4")
        # vr4/vr4 = v4/v3
        # vr4 = vr3(r/rc)

        vr4 = vr3 * (r / rc)
        print(f"Vr4 = {vr4}")

        for i in range(0,120,1):
            if vr4 <= vr[i] and vr4 > vr[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                uaux1_abajo = u[i]
                uaux2_arriba = u[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                t4 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                pr4 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                u4 = uaux2_arriba + ( (uaux1_abajo - uaux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)

                
                break
        
        print(f"t4 = {t4}")
        print(f"Pr4 = {pr4}")
        print(f"u4 = {u4}")

        # p4 = p3(pr4 / pr3)
        p4 = p3 * (pr4 / pr3)
        print(f"p4 = {p4}")
        # t3 = La temperatura despues del proceso de adicion de calor
        print(f"\n\n######  TEMPERATURA DESPUES DEL PROCESO DE ADICION DE CALOR = {t3}  ######")

        """ 
        a) Temperatura Maxima
        Comparar todas las temperaturas
        """
        lista_temperaturas = [t1, t2, t3, t4]
        temp_mayor = 0
        nums = 4

        for i in range(nums):
            num = lista_temperaturas[i]
            if num > temp_mayor:
                temp_mayor = num



        """ 
        b) Presión Maxima
        Comparar todas las presiones
        """
        if h2 > h3:
            pMayor = h2
        else:
            pMayor = h3

        '''
        c) Eficiencia energetica
        nDiesel = Wnet / qsum  
        · qsum = h3 - h2
        · qcad = u1 - u4
        '''
        qsum = h3 -h2
        qcad = u1 - u4
        wneto = qsum + qcad
        nDiesel = wneto / qsum
        print(f"qsum = {qsum}")
        print(f"qcad = {qcad}")
        print(f"Wneto = {wneto}")

        
        """ 
        d) Presion media efectiva
        pme = wneto / (v1-v2)
        v1 = (R*T) / P
        R = constante universal (0.287)
        v2 = (R * T2) / P2
        """

        v1 = (R * t1) / p1
        v2 = (R * t2) / p2
        v3 = v2
        v4 = v1
        pme = wneto / (v1-v2)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v3 = {v3}")
        print(f"v4 = {v4}")
        
        

        print("\n\n~~~~~~~~~~~~~~~~ RESULTADOS ~~~~~~~~~~~~~~~~")
        print(f"a) Temperatura máxima = {temp_mayor}ºK")
        print(f"b) Presion Máxima = {pMayor}kJ/kg")
        print(f"c) Eficiencia Térmica: nDiesel = {nDiesel}")
        print(f"d) Presión Media Efectiva: PME = {pme}kPa\n")

    for i in range(16,17):

        print(f"Caso {i} cv variable")
        p1 = 100
        t1 = 300
        t3 = 2250
        rc = 2
        R = 0.287

        print("\nDatos de entrada")
        print(f"p1 = {p1}")
        print(f"t1 = {t1}")
        print(f"r = {r}")
        print(f"rc = {rc}")
        print(f"t3 = {t3}")

        ''' Proceso 1-2 '''
        # Estado 1
        print("\nEstado 1")
        # Calcular Pr1, h1, Vr1
        for i in range(0,121,1):
            if round(t1) >= t[120]:     # Por si llega al limite de temperatura de la tabla
                pr1 = Pr[120]
                u1 = u[120]
                vr1 = vr[120]
                break

            if round(t1) >= t[i] and round(t1) < t[i+1]:
                pr1 = Pr[i]
                u1 = u[i]
                vr1 = vr[i]
                break
        
        print(f'Pr1 = {pr1}')
        print(f'u1 = {u1}')
        print(f'Vr1 = {vr1}')

        # Estado 2
        print("\nEstado 2")
        # Calculamos Vr2
        # v = vr1/vr2   =>  vr2 = vr1/r
        # r = vr1 / vr2
        vr2 = vr1 / r
        # Calculamos Pr2
        print(f"Vr2 = {vr2}")
        for i in range(0,121,1):
            if vr2 <= vr[i] and vr2 > vr[i+1]:
                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                # y = y0 + ((y1-y0) / (x1-x0)) * (x - x0)
                t2 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                h2 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                pr2 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr2 - vraux2_arriba)
                break

        print(f"t2 = {t2}")
        print(f"h2 = {h2}")
        print(f"Pr2 = {pr2}")
        # Dado que es una presion icentropica
        # p2 = p1 * (pr2/pr1)
        p2 = p1 * (pr2 / pr1)
        print(f"p2 = {p2}")

        ''' Proceso 2-3 '''
        print("\nEstado 3")
        # Estado 3      p3 = p2
        p3 = p2
        print(f"p3 = {p3}")
        # rc = v3/v2
        # Por la ec. de los gases ideales:
        # (p2*v2) / T2 = (p3*v3) / t3 => t3 = t2(p3/p2)(v3/v2)

        for i in range(0,120,1):
            if t3 >= t[i] and t3 < t[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                haux1_abajo = h[i]
                haux2_arriba = h[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                pr3 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                vr3 = vraux2_arriba + ( (vraux1_abajo - vraux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)
                h3 = haux2_arriba + ( (haux1_abajo - haux2_arriba) / (taux1_abajo - taux2_arriba) ) * (t3 - taux2_arriba)

                
                break

        print(f"h3 = {h3}")
        print(f"Pr3 = {pr3}")
        print(f"Vr3 = {vr3}")

        ''' Proceso 3-4 '''
        # Estado 4
        print("\nEstado 4")
        # vr4/vr4 = v4/v3
        # vr4 = vr3(r/rc)

        vr4 = vr3 * (r / rc)
        print(f"Vr4 = {vr4}")

        for i in range(0,120,1):
            if vr4 <= vr[i] and vr4 > vr[i+1]:
                praux1_abajo = Pr[i]
                praux2_arriba = Pr[i+1]

                uaux1_abajo = u[i]
                uaux2_arriba = u[i+1]

                vraux1_abajo = vr[i]
                vraux2_arriba = vr[i+1]

                taux1_abajo = t[i]
                taux2_arriba = t[i+1]

                t4 = taux2_arriba + ( (taux1_abajo - taux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                pr4 = praux2_arriba + ( (praux1_abajo - praux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)
                u4 = uaux2_arriba + ( (uaux1_abajo - uaux2_arriba) / (vraux1_abajo - vraux2_arriba) ) * (vr4 - vraux2_arriba)

                
                break
        
        print(f"t4 = {t4}")
        print(f"Pr4 = {pr4}")
        print(f"u4 = {u4}")

        # p4 = p3(pr4 / pr3)
        p4 = p3 * (pr4 / pr3)
        print(f"p4 = {p4}")
        # t3 = La temperatura despues del proceso de adicion de calor
        print(f"\n\n######  TEMPERATURA DESPUES DEL PROCESO DE ADICION DE CALOR = {t3}  ######")

        """ 
        a) Temperatura Maxima
        Comparar todas las temperaturas
        """
        lista_temperaturas = [t1, t2, t3, t4]
        temp_mayor = 0
        nums = 4

        for i in range(nums):
            num = lista_temperaturas[i]
            if num > temp_mayor:
                temp_mayor = num



        """ 
        b) Presión Maxima
        Comparar todas las presiones
        """
        if h2 > h3:
            pMayor = h2
        else:
            pMayor = h3

        '''
        c) Eficiencia energetica
        nDiesel = Wnet / qsum  
        · qsum = h3 - h2
        · qcad = u1 - u4
        '''
        qsum = h3 -h2
        qcad = u1 - u4
        wneto = qsum + qcad
        nDiesel = wneto / qsum
        print(f"qsum = {qsum}")
        print(f"qcad = {qcad}")
        print(f"Wneto = {wneto}")

        
        """ 
        d) Presion media efectiva
        pme = wneto / (v1-v2)
        v1 = (R*T) / P
        R = constante universal (0.287)
        v2 = (R * T2) / P2
        """

        v1 = (R * t1) / p1
        v2 = (R * t2) / p2
        v3 = v2
        v4 = v1
        pme = wneto / (v1-v2)
        print(f"v1 = {v1}")
        print(f"v2 = {v2}")
        print(f"v3 = {v3}")
        print(f"v4 = {v4}")
        
        

        print("\n\n~~~~~~~~~~~~~~~~ RESULTADOS ~~~~~~~~~~~~~~~~")
        print(f"a) Temperatura máxima = {temp_mayor}ºK")
        print(f"b) Presion Máxima = {pMayor}kJ/kg")
        print(f"c) Eficiencia Térmica: nDiesel = {nDiesel}")
        print(f"d) Presión Media Efectiva: PME = {pme}kPa\n")

    # Grafica
    x, y = np.loadtxt('Ciclo Otto 2\puntos.txt', skiprows=1, usecols=[0,1], unpack= True)
    x1,y1 = np.loadtxt('Ciclo Otto 2\puntos2.txt', skiprows=1, usecols=[0,1], unpack= True)
    plt.plot(x,y)
    plt.plot(x1,y1)
    plt.title('Grafica del error contra r y contra Tmax')
    plt.ylabel('Error relativo')
    plt.xlabel('r')
    plt.show()