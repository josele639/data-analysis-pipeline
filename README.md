# data-analysis-pipeline

El proyecto esta basado en un Dataframe de todas las peliculas que se estrenaron en 2010.
La tabla principal contiene el ID de Imbd, el título y el genero de la pelicula.
Utilizando la API y el ID de cada pelicula he podido obtener el presupuesto, la recaudacion y el voto medio de algunas de las peliculas.

La limpieza esta hecha teniendo 2 consideraciones, en la primera tabla guardo solo aquellas peliculas de las que tengo voto medio, en la segunda tabla solo aquellas de las que tengo recaudacion y presupuesto.

Gracias a estos datos he obtenido el ROI de cada pelicula, el retorno de la inversión, es decir, cuantas unidades obtengo de beneficio por cada unidad invertida.

Para ejecutar el programa hay que escribir python main.py en la terminal y seguir las instrucciones que se imprimen por consola.

¡Espero que te guste, te enseñe de cine y te ayude a elegir la pelicula que ver esta noche!