from analysis import genero_roi_vote
from analysis import max_10_pelis
from analysis import max_10_roi
from analysis import graf_roi_imagen
from analysis import save_show_pdf

def main():
    print("""Muy buenas, elige uno de los siguientes géneros y te dare información sobre el :)
Comedy         
Action         
Drama          
Adventure      
Crime          
Biography      
Horror         
Documentary     
Animation       
Romance         
War         
Fantasy         
Mystery         
Musical       
Thriller
    """)
    genero = input("¿De que género quieres tener información?:")
    try:
        genero_roi_vote(genero)
        pre1 = input("¿Quieres una lista de las mejores peliculas del género? Responde S/N:")
        if pre1 == "S":
            max_10_pelis(genero)
        pre2 = input("¿Quieres una lista de las peliculas más rentables del género? Responde S/N:")
        if pre2 == "S":
            max_10_roi(genero)
        pre3 = input("¿Quieres un gráfico de los géneros más rentables? Responde S/N:")
        if pre3 == "S":
            graf_roi_imagen()
        pre4 = input("¿Quieres guardarlo en un PDF y verlo? Responde S/N:")
        if pre4 == "S":
            save_show_pdf()
        print("¡Muchas gracias!")
        
    except:
        print("Ese género no esta en la lista")

if __name__=="__main__":
    main()