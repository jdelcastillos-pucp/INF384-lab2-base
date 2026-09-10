1.1 Los cuatro defectos. Para cada uno: qué está mal, en qué archivo y en qué líneas se
manifiesta, y qué consecuencia tiene. Un defecto no es "falta una línea": es qué garantía se
pierde por no tenerla

1. En el .yml el pipeline de validar y publicar artefacto se ejecutan al mismo tiempo.
2. No cuenta con archivos de bloqueo
3. En la linea 32: Analisis de calidad. Se genera un reporte de cobertura en XML (--cov-report=xml), pero no se pasa a SonarCloud en sus argumentos.
4. No se usa un sistema cache para la instalacion de dependencia, relentizando la ejecucion por cada pipeline.
