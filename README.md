# Epistemic tree (DEV BRANCH)
## Índice
* [Introducción](#introducción)
* [Lenguaje(provisional)](#lenguaje(provisional))
* [Brainstorming](#brainstorming)
* [TODO](#todo)

## Introducción
Proyecto en desarrollo para trabajo fin de máster.

## Lenguaje(provisional)
| Símbolo | Fórmula      | Ejemplo |
|---------|--------------|---------|
| &&      | Conjunción   | p&&q    |
| ||      | Disyunción   | p||q    |
| =>      | Implicación  | p=>q    |
| <>      | Equivalencia | p<>q    |
| Ka      | Conocimiento | Kap     |
| Ma      | Dual         | Map     |

El conjunto de átomos se define como [p-z] y el conjunto de átomos a1,a2,...,an.

## Brainstorming
* Símbolos de los operadores: Si hay interfaz gráfica, puede ser interesante que las fórmulas sean escritas en latex(?)
* (IMP) Parser como clase: La idea es construir una clase que reciba la fórmula como atributo. Las funciones se definen como métodos de dicha clase.

## TODO list
- [ ] Arbol
	- [ ] Crear la función buscar parent
	- [ ] Ahora mismo, las ramas se extraen a partir del, sería convienente que se extrajeran a partir de la fórmula
	- [ ] [IMPORTANTE] Hay algunas funciones recursivas, no sé como devolver un único valor, por eso ahora mismo requieren de una lista que las rellena.
- [ ] Simplificar la gramática y extraer info con querys
- [X] Pensar la manera de manejar las query(tipo de estructura de datos)
- [X] [IMP] Problema con los paréntesis externos. Lo ideal sería omitirlos en caso de que fueran exteriores. Se puede hacer tanto
		desde la gramática como desde el programa.
- [ ] Funciones para el parser
	- [ ] Manego de errores 
	- [X] Extraer el agente de la fórmula modal
	- [X] Comprueba si la fórmula es sintácticamente correcta(CUIDADO CON LOS PARÉNTESIS)
	- [X] Ordenar el conjunto de subfórmulas por su longitud.
	- [X] Extraer texto del nodo
	- [X] Extraer tipo de fórmula
	- [X] Función de longitud
	- [X] Extraer el conjunto de subfórmulas
	- [X] Si la fórmula es monádica, extraer la subfórmula afectada por el operador. 
	- [X] Si la fórmula es diádica, extraer las subfórmulas afectadas por el operador. 
- [X] Gramática tree-sitter
	- [X] Operadores modales
	- [X] Paréntesis y reglas de precedencia(Comprobar)
