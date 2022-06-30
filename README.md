# pnt_scraper

La Plataforma Nacional de Transparencia incluye buscadores temáticos que compilan información presentada por sujetos obligados. Sin embargo, no existe una opción para descargar masivamente estos datos.

Como la PNT está protegida con Captcha, que no puede ser evadido por Selenium por si solo, en este script se parte de un explorador web abierto donde el usuario ya pasó manualmente este obstáculo y se encuentra en la página de donde se quiere descargar los datos. Este código está implementado específicamente para descargar los datos de Ejercicio del Presupuesto, pero puede ser modificado para otras secciones de los Buscadores Temáticos.

Prerequisitos:
  1) Google Chrome
  2) Python 3 con los siguientes paquetes: selenium, time, csv, bs4, os.


Cómo abrir un navegador Chrome en un puerto local (basado en este árticulo https://learn-automation.com/how-to-execute-selenium-scripts-on-already-opened-browser/):
  1) Descargar ChromeDriver, la herramienta que permite automatizar un navegador abierto. Se puede encontrar en https://chromedriver.chromium.org/. Elige la versión para el Chrome instalado en tu computadora (se puede encontrar la versión en Acerca de Google Chrome, en el menú de la esquina superior derecha). Mover este archivo al directorio desde donde se estará trabajando.
  2) Deshabilitar el firewall. Esto es necesario para que Google Chrome pueda abrirse en un puerto local. Las instrucciones varían de sistema operativo a sistema operativo y pueden encontrarse en Internet.
  3) En el script se utilizará el puerto 9222 (localhost:9222).
  4) Cerrar todas las instancias de Google Chrome abiertas.
  5) Hay diferentes formas de abrir Google Chrome en este puerto. En Linux, en la terminal: google-chrome --remote-debugging-port=9222
  6) Si fue exitoso, debió abrirse una nueva ventana de Chrome y al abrir en otra pestana localhost:9222 debería verse lo mismo que en la pestaña original. 


Instrucciones:
 1) Abrir un navegador Chrome en un puerto local. Entrar a https://plataformadetransparencia.org.mx, resolver el Captcha y navegar a la sección de Ejercicio del Presupuesto (en la barra de abajo, Buscadores Temáticos).
 2) Elegir la informacion que se quiere descargar. Como el Captcha vence en aproximadamente dos horas, se recomienda mantener el número de filas por debajo de 2000. 
 3) El archivo scraper.py descarga cada fila de los elementos mostrados en la página. Como Selenium trabaja sobre lo que se observa en la pantalla, para evitar problemas donde el código no "ve" alguna fila o botón, se recomienda reducir el zoom a 25%. Además, si se quiere correr el código con más de 20 resultados por página, se recomienda utilizar una pantalla grande (en mi caso utilizo una pantalla de 27 pulgadas en posición vertical, y así funciona con 100 resultados por página)
 5) Al correr scraper.py se preguntarán 4 cosas:
    a) El nombre del archivo al que se escribirán los datos (se recomienda añadir la extensión .txt, aunque pareciera que no es necesario). Este archivo si no existe se creará, y si existe se pegarán los datos debajo de los ya existentes. No es necesario crear un archivo diferente cada vez que se corre el script.
    b) La página inicial.
    c) La página final.
    d) El número de resultados por página (para ir contando las observaciones).
 6) NO TOCAR LA COMPUTADORA. Aunque es posible seguir utilizando otras aplicaciones, se recomienda dejar el código correr sin ninguna otra manipulación.  Definitivamente no debe abrirse ninguna otra pestaña o ventana de Chrome mientras el código funciona. Además, configura la computadora para que no se suspenda automáticamente.

Algunas recomendaciones:
  - Puede tomar algún tiempo ajustar la ventana de tal forma que el programa no tenga un error. El error más común es que un objeto no es visible para el programa porque está más abajo o más arriba de la ventana visible y no puede hacerle click, fallando. Si esto sucede, se recomienda alejar el zoom al máximo (25%) y reducir el número de filas por página de tal forma que todo el sitio sea visible sin tener que desplazarse.
  - Otro problema común es que la página no carga a tiempo, haciendo que los objetos no sean visibles y caiga en error. Se recomienda modificar los time.sleep() en el archivo scraper.py para alargar los tiempos de espera.
  - Si el Captcha vence, volver a solucionarlo y moverse a la página donde se quedó y volver a correr el script desde ahí, desplazándose a la página donde cortó el script. Justo por esto se pregunta cual es la página inicial y final, para correr en partes si es necesario. Si el Captcha no funciona aunque se introduzca la solución correcta, cerrar el navegador y volverlo a abrir, a veces detecta que hubo automatización y por eso se niega a aceptar que fue llenado por un humano.

Trabajo futuro:
 - Automatizar los filtros. Esto se planea hacer automatizando la descarga masiva de todos los sujetos obligados disponibles, desde los cuales el usuario podrá guardar un archivo con los sujetos que quiere descargar.
 - Minimizar los errores inesperados. El código es bastante simple y solo introduce tiempos muertos entre instrucciones para esperar a que la página cargue. Sin embargo, es posible introducir tiempos muertos basados hasta que un objeto está disponible.
 - Implementar el código para las demás secciones de los Buscadores Temáticos.

# Probado en Fedora 36, con Google Chrome Version 103.0.5060.53 (Official Build) (64-bit).
