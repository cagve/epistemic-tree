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
- [ ] Pensar la manera de manejar las query(tipo de estructura de datos)
- [.] Funciones para el parser
	- [ ] Comprueba si la fórmula es sintácticamente correcta
	- [ ] Ordenar el conjunto de subfórmulas por su longitud.
	- [X] Extraer texto del nodo
	- [ ] Extraer tipo de fórmula
	- [X] Extraer el conjunto de subfórmulas
	- [ ] Si la fórmula es monádica, extraer la subfórmula afectada por el operador. Por ejemplo,
```
Ka(p) -----> p
```
	- [ ] Si la fórmula es diádica, extraer las subfórmulas afectadas por el operador. Por ejemplo,
```
p&&q -----> [p,q]
```
- [ ] Gramática tree-sitter
	- [ ] Operadores modales
	- [ ] Paréntesis y reglas de precedencia(Comprobar)
