const miLista = ["velma","exploradora","jane","john","harry"];

// 1- Cree un bucle for en JS que imprima cada nombre en esta lista
for (let i=0;  i< miLista.length; i++){
    console.log(miLista[i]);
}
//2- Cree un bucle while que recorra la misma lista y también imprima los nombres.
let counter = 0
while (counter<miLista.length){
    console.log(miLista[counter])
    counter++
}
//3- Arrow function que devuelve "Hola mundo"

const saludarMundo = ()=> "Hola mundo"
console.log(saludarMundo())