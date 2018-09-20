algoritmo "semnome"
// Função :
// Autor :
// Data : 12/01/2017
// Seção de Declarações 
var
   ano, nasc, idade: Inteiro
inicio
      Escreva("Em que ano estamos? ")
      Leia(ano)
      Escreva("Em que ano voce nasceu? ")
      Leia(nasc)
      idade <- ano - nasc
      Escreva("Em", ano , " voce terá ", idade , " anos. ")
      Se (idade >= 21) entao
         EscrevaL ("E já terá atingido a maioridade!")
      Fimse
fimalgoritmo
