
let a = document.getElementById('exibe_resultado');
let b = 7;
let c = 8;

if(b >= 7 && b == 7){
   a.innerHTML= "bol";
   a.innerHTML= "light";
}
/*Quando é necessário verificar mais de uma condição, em que cada uma delas precisará ser verdadeira, utilizamos os caracteres “&&”.

Na prática, as instruções 1 e 2 só serão executadas caso as condições 1 e 2 sejam verdadeiras. Vamos a outro exemplo: */
if(b >=7 || b == 7){
    a.innerHTML= "square";
}
/*Repare que, nesse código, os caracteres “&&” foram substituídos por “||”. Esses últimos são utilizados quando uma ou outra condição precisa ser verdadeira para que as instruções condicionais sejam executadas. */

//E o que acontece se quisermos verificar mais condições?

//Nesse caso, podemos fazer isso tanto para a forma em que todas precisam ser verdadeiras, separadas por “&&”, quanto para a forma em que apenas uma deve ser verdadeira, separadas por “||”. Além disso, é possível combinar os dois casos na mesma verificação. Veja o exemplo:
if ( (b >= 7 && b == 7) || b === 7){
    a.innerHTML= "triangle"
}

//Como verificar se uma condição é falsa (ou não verdadeira)?
if(!b <7){
    a.innerHTML= "tome"
}

/* O sinal “!” é utilizado para negar a condição. As instruções 1 e 2 serão executadas caso a condição 1 não seja verdadeira.

Agora vamos praticar um pouco. Nos três emuladores de código a seguir, apresentamos as estruturas de decisão vistas até aqui. No primeiro emulador, temos o uso da estrutura de decisão if de maneira simples, contendo apenas uma única condição:” */

//ELSE

let a1 = document.getElementById('exibe_resultado_else')

if(b < 7 ){
    a1.innerHTML= "b e maior que 7"
}else{
    a1.innerHTML= "b nao  e maior que 7"
}

/*Perceba que o "else" (senão) acompanha o "if" (se). Logo, SE as condições forem verdadeiras, faça isto. SENÃO, faça aquilo.

É importante mencionar que no último fragmento foi utilizado, de modo proposital, português-estruturado nas condições e instruções. Isso porque, mais adiante, você mesmo codificará esse "if/else" em JavaScript.*/