Algoritmo "semnome"
// Disciplina   :  [Linguagem e Lógica de Programação] 
// Professor   : Gustavo Guanabara 
// Descrição   : Contar até determinado número, utilizando uma razão pré
// determinada.
// Autor(a)    : Lucas da Silva Paixão
// Data atual  : 01/02/2017
Var
   Contador, N, Razao:Inteiro
Inicio
   Contador <- 0
   EscrevaL("Quer contar até quanto?")
   Leia(N)
   EscrevaL("Quer contar de quanto em quanto?")
   Leia(razao)
   Enquanto (Contador <= N) faca
     EscrevaL(Contador)
     Contador <- Contador + razao
   FimEnquanto
   
   //No bloco acima, lê-se: Enquanto o Contador for menor ou igual a N,
   //Escreva o Contador(Que nesse ponto ainda era 0 graças à atribuição da
   //linha 10). Atribuindo uma soma entre o Contador(0) e a VARIÁVEL razao,
   //Temos que o LOOPING começa e volta para Enquanto. O EscrevaL vai agora
   //Escrever o "Contador + razao", e o Laço de Repetição não se encerrará
   //até que Contador seja menor ou igual a N.
Fimalgoritmo