# Diagnostico

Documento de resolución para la parte 1 del laboratorio 2.

## 1.1 Los cuatro defectos
1. Publicación sin validación previa: pipeline.yml, línea 43.

No hay nada que impida publicar antes de validar. La parte validar necesitaría un 
    needs: validar
antes de poder iniciar su proceso (de hecho publicar suele ser más rápido)

2. No hay nombre de artefacto ni versión del mismo, pipeline.yml, vlinea 66. 

Las publicaciones no aplican versionado a los artefactos que suben, lo que dificulta el seguimiento. 

3. Análisis de calidad inseguro después de pruebas: pipeline.yml linea 32. 

Si por alguna razón el paso de Ejecutar pruebas falla y da 0, como no hay nada más Github Actions cancela los demás pasos, de modo que el paso Análisis de Calidad que involcura el análisis de SonarCloud nunca se ejecuta. 

4. Tanto validar como publicar hacen ambas la instalación de dependencias: pipeline.yml, lineas 24 y 55.

Como no funcionan como pasos que siguen uno del otro, entonces ambos instalan dependencias innecesariamente y puede que no lleguen a crear el mismo artefacto. 

## 1.2 El defecto que explica la duración. 
Diría que el defecto 4, ya que se hacen descargas e instalaciones en ambos pasos (validar y publicar), lo que hace que ambos jobs repitan un paso y se añada tiempo, por ejemplo en los números medidos, es aproximadamente 1m 4s, entre los cuales el validar-> Análisis de calidad es lo que suele tomar más tiempo.

## 1.3 El vínculo con su caso


## 1.4 La métrica DORA
Las alcanzables sin despliegue son: 
- Tiempo de entrega del cambio
- Porcentaje de fallas en el cambio. 

Lo que se espera mover es el tiempo de entrega del cambio, ya que los errores afectan los tiempos principalmente. 

## 1.5 El proxy
La duración del workflow en Actions. 