============= 1.1============================
-PRIMER DEFECTO:
-¿Qué está mal? -> Duplicidad de código, 
-Archivo -> pipeline.yml
-Línea -> Para el paso "Descargar el codigo" (linea 14 y 47), "Preparar Python" (linea 20 y 50) e "Instalar dependencias" (linea 24 y 55)

-SEGUNDO DEFECTO:
-¿Qué está mal? -> Falta de caché en las dependencias de Python
-Archivo -> pipeline.yml
-Línea -> En ninguna de las dos ejecuciones se usa 'pip'. (linea 20 y 51)


-TERCER DEFECTO:
-¿Qué está mal? -> Falta de dependencia explícita entre los trabajos (needs)
Defecto: Los jobs validar y publicar se ejecutan en paralelo. El job publicar no tiene la propiedad needs: validar.
-Archivo -> pipeline.yml
-Línea -> "validar" y "publicar" se ejecutan en paralelo. Para que tenga sentido, debería haber un "needs" relacionado a "validar".

-CUARTO DEFECTO:
-¿Qué está mal? -> Falta de comillas en versión de Python
-Archivo -> pipeline.yml
-Línea -> (linea 22 y 53)

============= 1.2============================
En este caso el defecto relacionado con el tiempo registrado en la línea base esta directamente relacionado al PRIMER
DEFECTO. Porque se esta consumiendo tiempo repitiendo código.
Por ejemplo en mi linea base los tiempos finales de las 3 ejecuciones fueron: 1m 6s, 1m 29s y 54s

============= 1.3============================
En este caso relacionado al VSM se ve afecta la eficiencia del flujo debido a la "demora" adicional del pipeline por el 
código duplicado
============= 1.4============================
La métrica que se movería tras "arreglar" el código del pipeline sería: "Lead time para cambios" puesto que reduciríamos el tiempo
que demora en ejecutarse el pipeline,

============= 1.5============================
Vamos a medir el tiempo de ejecución del pipeline (basicamente lo que hemos registrado en el trabajo previo del laboratorio)



