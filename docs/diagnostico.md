1.1 Los cuatro defectos. Para cada uno: qué está mal, en qué archivo y en qué líneas se manifiesta, y qué consecuencia tiene. Un defecto no es "falta una línea": es qué garantía se pierde por no tenerla.

Defecto 1: La instalación usa `pip install -r requirements.txt`, y ese archivo declara versiones abiertas como `requests>=2.31` la cual no es una version fijada. Aunque existe `requirements.lock` en el repositorio, el workflow nunca lo usa.
Archivo 1: `.github/workflows/pipeline.yml`, pasos "Instalar dependencias" (es igual en el job `validar` y en `publicar`).
Consecuencia 1: Se pierde reproducibilidad porque dos ejecuciones del mismo commit pueden instalar versiones distintas de las dependencias transitivas, así que si funcionó en una corrida no garantiza que funcione en la siguiente.

Defecto 2: No hay ningún mecanismo de caché para las dependencias. Cada corrida vuelve a descargar e instalar todo desde cero.
Archivo 2: `.github/workflows/pipeline.yml`, pasos "Preparar Python" (ambos jobs)
Consecuencia 2: Se pierde velocidad de feedback: cada ejecución paga el costo completo de descarga/instalación, inflando la duración del pipeline sin necesidad.

Defecto 3: El job `publicar` no depende del job `validar`, y el paso de análisis de SonarCloud no verifica el resultado del quality gate.
Archivo 3: `.github/workflows/pipeline.yml`, job `publicar` y paso "Analisis de calidad" del job `validar` | 
Consecuencia 3: Se pierde la garantía de calidad: aunque el análisis de SonarCloud falle o el código no cumpla el quality gate, el job `publicar` corre de todas formas porque no espera a `validar` ni revisa su resultado.

Defecto 3: El artefacto se publica siempre con el nombre fijo `paquete` sin versión, y la condición `if` no restringe la rama, por lo que cualquier push a cualquier rama dispara la publicación. | 
Archivo 3: `.github/workflows/pipeline.yml`, job `publicar`: la condición `if:` y el paso "Publicar el paquete" (`name: paquete`)
Consecuencia 3: Se pierde trazabilidad y control: no se puede saber qué versión del código corresponde a qué artefacto descargado, y se pueden publicar artefactos desde ramas de feature sin pasar por `main` ni por revisión.

1.2 El defecto que explica la duración. De los cuatro, cuál explica el tiempo que registraron en docs/linea-base.md. Sustenten con el número que midieron.

El defecto 2 (ausencia de caché) es el que explica el tiempo registrado en `docs/linea-base.md`, donde mis tres ejecuciones dieron **1m 4s, 1m 3s y 1m 6s** que son prácticamente el mismo tiempo en las tres corridas. Eso es justamente la firma de un pipeline sin caché: si hubiera caché de dependencias, la segunda y tercera corrida deberían ser notablemente más rápidas que la primera que llena la caché. Como no bajó, se sostiene que cada corrida reinstala todo desde cero.

1.3 El vínculo con su caso. Cuál de los cuatro defectos ataca la restricción del caso transversal de su grupo. Citen un dato del value stream map que levantaron en la Sesión 1.

Para el Caso 3, Seguros Pacífico Sur, el defecto vinculado es que el pipeline no se detenga si falla el análisis de calidad. La restricción del caso no es una espera visible sino retrabajo constante por defectos no atrapados a tiempo, sustentado en que el rendimiento acumulado de calidad es de apenas 11% y que 76 de 94 historias fueron devueltas al menos una vez. Un quality gate que no bloquea nada reproduce ese mismo patrón.

1.4 La métrica DORA. Qué métrica DORA esperan mover con la intervención y por qué. Solo dos son alcanzables sin despliegue: identifiquen cuáles y elijan una.

Sin llegar a desplegar a producción, las únicas dos métricas DORA que se puede mover con esta intervención son el tiempo de entrega del cambio y el porcentaje de fallas en el cambio; la frecuencia de despliegue y el tiempo de restauración del servicio requieren un despliegue real. Elijo el tiempo de entrega del cambio porque la corrección del defecto de caché tiene un efecto medible y directo sobre la duración del pipeline.

1.5 El proxy. Qué número concreto van a medir para sustentar que la métrica se movió. Decláralo antes de intervenir. Hagan commit de este archivo antes de tocar el workflow. La marca de tiempo del commit es parte de la evidencia.

El número concreto que se va a medir es la duración total del job validar en GitHub Actions. La línea base es un promedio de aproximadamente 1 minuto 4 segundos sobre las tres ejecuciones registradas antes de intervenir el workflow. Ese valor queda declarado como punto de comparación antes de aplicar la corrección del defecto de caché.
