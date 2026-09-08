# Mi Hackpad

**9-Key Mechanical Macropad**

Mi Hackpad es un macropad mecánico de 9 teclas diseñado y desarrollado como un proyecto personal de electrónica, programación y diseño de PCB.

El proyecto está basado en una **Seeed XIAO RP2040** y utiliza **9 switches mecánicos Cherry MX**, junto con un LED RGB direccionable **SK6812MINI**.

El objetivo principal del proyecto es crear un dispositivo pequeño y totalmente personalizable que permita ejecutar diferentes teclas, atajos y macros desde un conjunto compacto de botones.

El Hackpad está pensado principalmente como un proyecto experimental relacionado con **Stardance**, además de servir como una forma de aprender sobre diseño de circuitos, PCB, microcontroladores y firmware para teclados.

## Características

* 9 teclas mecánicas.
* Distribución física de 3 × 3 teclas.
* Switches Cherry MX.
* Microcontrolador Seeed XIAO RP2040.
* LED RGB direccionable SK6812MINI.
* PCB diseñada en KiCad.
* Firmware basado en KMK + CircuitPython.
* Teclas y macros totalmente configurables.
* Diseño compacto.
* Posibilidad de personalizar las funciones de cada tecla.

## Hardware

### Microcontrolador

El Hackpad utiliza una **Seeed XIAO RP2040** como microcontrolador.

La XIAO RP2040 está basada en el microcontrolador **Raspberry Pi RP2040**, que se encarga de leer el estado de los switches y enviar las acciones correspondientes al ordenador mediante USB.

La PCB del proyecto contiene las conexiones necesarias para que el microcontrolador pueda interactuar con los switches y el sistema de iluminación.

> La XIAO RP2040 no aparece como un footprint propio dentro del archivo `.kicad_pcb` proporcionado, por lo que su montaje físico final puede realizarse externamente a la PCB.

## Switches

El Hackpad utiliza:

**9 × Cherry MX**

Los nueve switches están organizados en una matriz física de:

```text
[ 1 ] [ 2 ] [ 3 ]

[ 4 ] [ 5 ] [ 6 ]

[ 7 ] [ 8 ] [ 9 ]
```

Cada switch funciona como una entrada que puede ser detectada por el microcontrolador.

Las posiciones de los switches están separadas aproximadamente **15,09 mm**, formando una distribución compacta de 3 × 3.

## Asignación de GPIO

Según el diseño actual de la PCB, las nueve teclas están conectadas a los siguientes GPIO del RP2040:

| Tecla | GPIO   |
| ----- | ------ |
| Key 1 | GPIO2  |
| Key 2 | GPIO27 |
| Key 3 | GPIO7  |
| Key 4 | GPIO1  |
| Key 5 | GPIO3  |
| Key 6 | GPIO4  |
| Key 7 | GPIO29 |
| Key 8 | GPIO6  |
| Key 9 | GPIO28 |

Estos GPIO deben coincidir con la configuración utilizada posteriormente en el firmware.

## Iluminación RGB

El proyecto incorpora un:

**1 × SK6812MINI**

El SK6812MINI es un LED RGB direccionable que permite controlar el color y brillo mediante una señal digital.

La PCB proporciona las conexiones necesarias para:

* Alimentación de +5 V.
* GND.
* Entrada de datos del LED.

La iluminación está pensada para añadir un indicador visual al Hackpad y puede ser controlada desde el firmware KMK.

## PCB

La PCB fue diseñada utilizando **KiCad**.

El diseño contiene los footprints de:

* 9 switches Cherry MX.
* 1 LED SK6812MINI.
* Conexiones de alimentación.
* Conexiones de señal para los switches.
* Conexiones necesarias para el microcontrolador.

La disposición de los switches forma una cuadrícula de 3 × 3.

### Distribución

```text
┌─────────┬─────────┬─────────┐
│  KEY 1  │  KEY 2  │  KEY 3  │
├─────────┼─────────┼─────────┤
│  KEY 4  │  KEY 5  │  KEY 6  │
├─────────┼─────────┼─────────┤
│  KEY 7  │  KEY 8  │  KEY 9  │
└─────────┴─────────┴─────────┘
```

El diseño todavía se encuentra en desarrollo, por lo que pueden existir cambios en la PCB antes de fabricar la versión final.

## Firmware

El Hackpad utiliza **KMK Firmware**, un firmware para teclados mecánicos basado en CircuitPython.

KMK permite definir el comportamiento de cada tecla mediante Python.

Esto significa que las funciones de las teclas pueden modificarse sin tener que rediseñar la PCB.

Por ejemplo, una tecla puede configurarse para:

* Escribir una letra.
* Ejecutar una combinación de teclas.
* Controlar el volumen.
* Silenciar el audio.
* Ejecutar una macro.
* Ejecutar otras acciones compatibles con KMK.

## Configuración actual

El firmware inicial del proyecto contiene funciones como:

```text
A
B
C
Windows + D
Macro de texto
Mute
Volumen +
Volumen -
```

Esta configuración es provisional y será actualizada para utilizar las nueve teclas presentes en la PCB.

## Funcionamiento

El funcionamiento básico del Hackpad es:

```text
       SWITCH
          │
          ▼
    ┌─────────────┐
    │ XIAO RP2040 │
    └──────┬──────┘
           │
           ▼
     KMK / CircuitPython
           │
           ▼
        USB / PC
```

Cuando se presiona una tecla, el RP2040 detecta el cambio eléctrico producido por el switch.

El firmware KMK interpreta esa entrada y ejecuta la función asignada.

Por ejemplo:

```text
Presionar Key 7
       ↓
GPIO29 detecta la pulsación
       ↓
KMK identifica Key 7
       ↓
Ejecuta la función configurada
       ↓
El ordenador recibe la acción
```

El LED SK6812MINI funciona de forma independiente como dispositivo de iluminación controlado mediante una señal digital.

## Software utilizado

### KiCad

Utilizado para diseñar la PCB y definir los componentes y conexiones del hardware.

### CircuitPython

Entorno utilizado por la XIAO RP2040 para ejecutar el firmware.

### KMK Firmware

Firmware utilizado para definir el comportamiento del teclado, las teclas, macros y funciones adicionales.

### Python

El firmware del Hackpad se configura mediante código Python compatible con CircuitPython y KMK.

## Estructura del proyecto

Una estructura posible para el repositorio es:

```text
custom-lightpad/
│
├── README.md
│
├── hardware/
│   ├── panclin.kicad_pro
│   ├── panclin.kicad_sch
│   └── panclin.kicad_pcb
│
└── firmware/
    └── code.py
```

## Objetivos del proyecto

El proyecto busca combinar aprendizaje y desarrollo práctico.

Los principales objetivos son:

1. Aprender diseño de PCB con KiCad.
2. Comprender circuitos electrónicos básicos.
3. Aprender a trabajar con el RP2040.
4. Utilizar switches mecánicos en un dispositivo real.
5. Aprender CircuitPython.
6. Aprender a utilizar KMK Firmware.
7. Crear un dispositivo USB personalizado.
8. Experimentar con iluminación RGB.
9. Crear un Hackpad funcional relacionado con Stardance.

## Próximas mejoras

Entre las mejoras previstas se encuentran:

* Corregir el firmware para utilizar las 9 teclas.
* Completar y verificar el esquemático.
* Revisar todas las conexiones eléctricas.
* Finalizar el diseño de la PCB.
* Definir el contorno final de la PCB.
* Fabricar una primera versión.
* Probar cada switch individualmente.
* Probar el LED RGB.
* Crear macros específicas para Stardance.
* Diseñar una carcasa.
* Mejorar la iluminación RGB.
* Documentar el montaje final.

## Estado del proyecto

**En desarrollo**

La PCB ya cuenta con el diseño físico de los nueve switches y el LED SK6812MINI.

El firmware todavía necesita ser actualizado para coincidir completamente con las nueve entradas definidas en el hardware.

## Autor

**Nacho**

Proyecto:

**Mi Hackpad — Stardance**

Repositorio:

`custom-lightpad`

## Tecnologías

* KiCad
* Seeed XIAO RP2040
* Raspberry Pi RP2040
* Cherry MX
* SK6812MINI
* CircuitPython
* KMK Firmware
* Python
