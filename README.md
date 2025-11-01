# Arboles_Complementarios

Autores: 

Sebastian Clavijo Tocasuchyl
Nicolas Caucali Junco


Objetivo:

Podar dos árboles para encontrar sus versiones complementarias con mayor número de hojas


Lenguaje de desarrollo:

Python


Porcentaje de IA usada:


60%. Fue de gran ayuda para manejar la impresión y la ejecución de las funciones implementadas, además de algunos detalles en la lógica de cuáles y cómo implementar ciertas estructuras. Sin embargo, la IA por sí sola no podía encontrar la forma de hacerlo, incluso cometiendo errores una vez ya le había guiado en la forma en que yo lo quería hacer


¿Cómo se desarrolló?

La manera en que lo pensamos el día de clase fue buscar todas las posibles secuencias de hojas que se generaban con cada posible poda para ambos árboles y luego compararlas para buscar las que fueran iguales, de estas se buscaba la mayor y esa era la respuesta final del programa.

Mi primer boceto era comparar todas las secuencias del árbol B con el árbol A sin modificar, luego se hacía una poda en el árbol A y volvía a comparar con todas las posibles secuencias del árbol B y proseguir con la siguiente poda. Pero esto era muy costoso, por lo que la IA me ayudó con la idea de usar los conjuntos implementados en Python (con los que ya tengo experiencia) ya que estos me permiten de forma eficiente comparar todas las posibles secuencias de forma rápida. 

Un problema que tuve fue que los set de Python sólo pueden almacenar objetos inmutables y las listas se pueden modificar, por lo que tuve que usar tuplas para las secuencias de hojas.

Un compañero en clase dio la idea de podar las hojas que estaban en un árbol pero que no se encontraban en un nodo del otro árbol, esto es un descarte que mejora en muchas situaciones la complejidad del algoritmo, puesto que evita revisar hojas que no tienen posibilidad de ser parte las hojas de un árbol complementario (Esto se hace al principio del código).


Estructuras usadas:

Árbol binario (Clase nodo)

Valor (el entero del nodo) y dos punteros, izquierdo y derecho, que apuntan a otro objeto Nodo o a None.

set 

Esta es la estructura para la eficiencia del algoritmo. Se usa de dos maneras:
Para guardar todos los valores que existen en un árbol y comprobar si un valor existe. También para crear un set de tuplas para poder encontrar qué secuencias tienen en común con la intersección.

tuple 

Se usó para representar una secuencia de hojas individuales. Se prefirió tuple en lugar de list por una razón, los set de Python sólo pueden almacenar objetos inmutables, las tuplas son inmutables y el perfecto reemplazo de las listas.

list 

Al final se toma la dupla ganadora de la intersección y la convierte en una lista antes de devolverla, ya que es un formato fácil de manejar.


Recomendaciones: 

Correr el código en Colab 

Si se quiere probar algún árbol específico, se pueden modificar los de los ejemplos

La impresión de los árboles es de arriba a abajo, como de izquierda a derecha. 



