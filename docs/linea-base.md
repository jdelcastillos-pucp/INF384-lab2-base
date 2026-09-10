# Linea base de ejecucion

Ejecutar el workflow tres veces desde la pestana Actions, con **Run workflow**,
sin modificar ningun archivo del repositorio. Registrar aqui los resultados.

| Ejecucion | Duracion | URL |
|---|---|---|
| 1 | 56 s|https://github.com/vitayien/INF384-lab2-20200909/actions/runs/34529468719 |
| 2 | 59 s|https://github.com/vitayien/INF384-lab2-20200909/actions/runs/34530211048 |
| 3 | 1min 2s|https://github.com/vitayien/INF384-lab2-20200909/actions/runs/34530404812 |

## Declaracion de uso de IA generativa

Indicar si se utilizaron herramientas de IA generativa para completar este
trabajo previo, cuales, y con que proposito. Adjuntar los prompts utilizados.

1.2. El defecto que que explica porque el tiempo es mayor por cada ejecución es la instalacion de dependencias del proyecto cada vez que se corre un workflow
1.3. Los dos jobs de validación y publicación se ejecutan paralelamente, por lo que si el codigo se encuentra con errores, el proyecto aun así se publicará.
1.4. Porcentaje de fallas en el cambio y tiempo de entrega del cambio. Se espera mover el tiempo de entrega del cambio.
1.5. Se espera medir la duración de la ejecución para sustentar que la metrica se movio.
