## ROS Video Car

#### Introducción 🚀

ROS Video Car es un proyecto que controla el funcionamiento de un auto de juguete mediante ROS. El auto posee una placa Raspberry Pi 4 corriendo Ubuntu Server y los nodos ROS correspondientes, a su vez, la electrónica del auto es controlada por una placa Arduino Uno conectada al RPi4 por puerto serie (USB). 

El auto, además, posee una webcam 640x480 USB conectada al RPi4, dándole la capaidad de transmitir video en vivo por medio de OpenCV a la PC.

El master (_roscore_) corre en una PC con Ubuntu. Además controla el movimiento del auto y recibe el stream de video de la webcam del auto.

Por otro lado, La RPi4 está montada sobre el auto, y tiene instalado Ubuntu Server para ARM64, controla el movimiento del auto mediante una placa Arduino Uno conectada al puerto ttyUSB0 de la RPi4.

El auto cuenta con una webcam, con baterías recargables y dura aproximadamente 2 hs.

La PC y la RPi4 se comunican por medio de una red WiFi.

## Estructura del proyecto ✔️

### Package keyboard
* ```keyboard.py``` (host _PC_): inicializa el nodo ```keyboard_node```.
* ```keyboard_node```: nodo que realiza la lectura de las teclas mediante la librería pygame y lo publica en en el tópico ```keyboard_control```.

### Package rosopencv
* ```cam_pub.py``` (host _Raspberry Pi 4_): inicializa el nodo ```cam_pub_py```, el cual publica los cuadros de video en ```video frame```.
* ```cam_sub.py``` (host _PC_): inicializa el nodo ```cam_sub_py```, el cual consume los frames de video de ```video frame``` y los muestra en pantalla.
### Package vcar
* ```publisher_node.py``` (host _RPi4_): inicializa el nodo ```publisher_node```, el cual es un nodo de prueba.
* ```subscriber_node.py``` (host _RPi4_): inicializa el nodo ```subscriber_node```, el cual consume los mensajes de las teclas presionadas de ```keyboard_control``` y los publica en ```cmd_serial``` (en un futuro se prescindirá de este nodo)
* ```ctrl_arduino_node.py``` (host _RPi4_): inicializa el nodo ```ctrl_arduino_node```, el cual consume los mensajes de las teclas presionadas de ```cmd_serial``` y envía los comandos correspondientes por puerto serie a la placa Arduino.

```
    /keyboard
        /src
            /keyboard.py
    /rosopencv
        /src
            /cam_pub.py
            /cam_sub.py
    /vcar
        /src
            /ctrl_arduino_node.py
            /publishe_node.py
            /subscriber_node.py
```

## Ejecutando las pruebas ⚙️

El auto funciona según lo esperado. Sin embargo, se agregarán funcionalidades que mejoren la precisión del movimiento.


## Links ⌨️


## Construido con 🛠️

_Herramientas utilizadas para crear el proyecto_

* [ROS noetic](http://wiki.ros.org/noetic) - Framework para el desarrollo de software para robots.
* [OpenCV](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html) - Librería para Visión por Ordenador.
* [PyGame](https://www.pygame.org/news) - Librería para Python para la creación de videojuegos 

## A futuro📋

* Agregar la electrónica y software necesarios para la odometría.
* Agregar la electrónica necesaria y software para la detección de obstáculos.
* Agregar el software necesario para el reconocimiento de objetos y/o obstáculos mediante la webcam.

## Autor ✒️

**Sebastián Vallespir**
* [GitHub](https://github.com/dsvallespir) 
* [LinkedIn](https://www.linkedin.com/in/sebastian-vallespir/)

