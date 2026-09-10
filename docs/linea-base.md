# Linea base de ejecucion

Ejecutar el workflow tres veces desde la pestana Actions, con **Run workflow**,
sin modificar ningun archivo del repositorio. Registrar aqui los resultados.

| Ejecucion | Duracion | URL |
|---|---|---|
| 1 | 1m 1s | https://github.com/Setziret/INF384-lab2-20171857/actions/runs/34509658203 |
| 2 | 1m 4s | https://github.com/Setziret/INF384-lab2-20171857/actions/runs/34510273436 |
| 3 | 1m 4s | https://github.com/Setziret/INF384-lab2-20171857/actions/runs/34510538593 |

## Declaracion de uso de IA generativa

Indicar si se utilizaron herramientas de IA generativa para completar este
trabajo previo, cuales, y con que proposito. Adjuntar los prompts utilizados.

Se utilizó Claude (Anthropic) en el modo chat, como herramienta de consulta y soporte técnico durante la ejecución del bloque C de este trabajo previo. El uso se limitó a las siguientes situaciones:

    1. Diagnóstico del error exit code 3 del sonar-scanner-cli durante la ejecución del workflow 
        Ayudó a interpretar el log de ejecución de GitHub Actions e identificar que el error *Organization key 'schira-pucp' does not exist* se debía a que la variable SONAR_ORG del repositorio contenía el nombre visible de la organización en SonarCloud en lugar de su Key real (setziret), tras un cambio de nombre de la organización.

    2. Aclaración conceptual sobre el uso de ${{ secrets.* }} vs ${{ vars.* }} en GitHub Actions, y sobre la diferencia entre el Organization name y el Organization key en SonarCloud.

Todas las configuraciones y la serie de pasos de todos los bloques fueron realizadas por mí (Sebastian Chira aka Setziret). Claude no generó código, no modificó el archivo pipeline.yml ni el README.md, y no ejecutó ninguna acción dentro de las plataformas del laboratorio. Se limitó el uso a explicación de errores y mensajes de error.

A continuación declaro los prompts utilizados. Cabe resaltar que cuando uso las "/* */" se refiere a comentarios que hago ahora mismo mientras escribo estas líneas y no fueron mandados a Claude. Esto principalmente por el paso de archivos o logs largos. 


### Prompt 1
Usaré este chat para el apoyo del desarrollo de un laboratorio. Ayudame en lo que puedas. 
Este laboratorio es uno de Temas Avanzados en Ingeniería de Software. Se usarán Github, Github Actions, Vercel, SonarCloud y demás. Recién crearé mi cuenta de SonarCloud. Tu labor es principalmente de apoyo y de asegurarme que los pasos que sigo son correctos, así como de ofrecerme explicaciones si algunas cosas no me salen, pero yo seré quien haga esto principalmente. Quiero decirte también que en el curso usamos las métricas DORA y probablemente se pidan en el lab. 

La guía es la siguiente: /* Le pase el texto del bloque C para que tuviera contexto. */
El pipeline.yml es este: /* le pasé el pipeline, no lo pongo porque sería muy largo. */
Y el README.md asociado es este: /* igual le pasé el REAMDE.md */
También declarar que trabajaré en Codespaces para evitar problemas de instalacion y ahorrar tiempo. 

Mi primera duda es que no logro tener ejecuciones exitosas y creo que hice todo el bloque C bien, mis resultados son: 
C.1 — Repositorio del grupo
    Fork creado como INF384-lab2-20171857
    Nombre creado.
    No se cambió la visibilidad
    Activación de workflow hecha.

C.2 — Cuenta y organización en SonarCloud.
    Cuenta creada, importada de Github
    Creación de cuenta free creada
    Proyecto importado

C.3 — Desactivar el análisis automático
    Desactivado

C.4 — Token y secreto
    Token generado:
    SONAR_TOKEN: --------
    SONAR_ORG: schira-pucp
    SONAR_PROJECT_KEY: -------
    (los token los tengo pero obvio no los comparto). 

El fallo siempre es:
Action failed: The process '/opt/hostedtoolcache/sonar-scanner-cli/8.1.0-build.6389/linux-x64/bin/sonar-scanner' failed with exit code 3

Por que se da?

### Prompt 2
Ok, me sale eto
/* Aquí pasé 2 cosas:
    1. El log de error completo que daba el pipeline. Para comprobación de que se hizo así adjunto que empezaba con: Run SonarSource/sonarqube-scan-action@v8
Installing Sonar Scanner CLI 8.1.0.6389 for linux-x64...
Downloading from: https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-8.1.0.6389-linux-x64.zip
Downloading signature from: https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-8.1.0.6389-linux-x64.zip.asc
Importing SonarSource public key from hkps://keyserver.ubuntu.com...
/usr/bin/gpg --homedir /home/runner/work/_temp/gpg-ecd6b29e --batch --keyserver hkps://keyserver.ubuntu.com --recv-keys 679F1EE92B19609DE816FDE81DB198F93525EC1A
gpg: keybox '/home/runner/work/_temp/gpg-ecd6b29e/pubring.kbx' created
gpg: /home/runner/work/_temp/gpg-ecd6b29e/trustdb.gpg: trustdb created
gpg: key 1DB198F93525EC1A: public key "SonarSource S.A. <infra@sonarsource.com>" imported
...
...
17:35:00.214 INFO  Create analysis
17:35:00.856 ERROR Organization key 'schira-pucp' does not exist.
17:35:01.184 INFO  EXECUTION FAILURE
17:35:01.185 INFO  Total time: 15.195s
Error: Action failed: The process '/opt/hostedtoolcache/sonar-scanner-cli/8.1.0-build.6389/linux-x64/bin/sonar-scanner' failed with exit code 3

    2. Una imagen de las pestaña Organizations de SonarCloud donde estaban el Organization Name, Key, etc (la fila)
*/

Veo que dice que schira-pucp no existe, 

Puede ser porque antes la organización tenia otro nombre, pero se la cambie por facilidad. Que puedo hacer  en ese caso? 


