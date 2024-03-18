var frutas = ['pera', 'melancia', 'manga'];

//usamos o push para adicionar mais elementos no vetor
frutas.push('morango', 'pitaya'); 

//outras formas de adcionar elementos a um vetor
frutas[frutas.length] = 'banana';

//splice
frutas.splice(6,0,'jabuticaba');
console.log(frutas)