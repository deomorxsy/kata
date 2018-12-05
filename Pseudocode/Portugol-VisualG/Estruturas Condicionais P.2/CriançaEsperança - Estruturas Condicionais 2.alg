Algoritmo "CriançaEsperança"
// Disciplina   :  [Linguagem e Lógica de Programação] 
// Professor   : Gustavo Guanabara 
// Descrição   : Exercício com as estruturas ESCOLHA e CASO. Alternativa à
// Se e Senão.
// Autor(a)    : deomorxsy
// Data atual  : 16/01/2017
Var
   N, Valor:Real

Inicio
      EscrevaL("----------------------")
      EscrevaL("   CRIANÇA ESPERANÇA  ")
      EscrevaL("----------------------")
      EscrevaL("Muito obrigado por ajudar")
      EscrevaL("Digite [1] para doar R$10")
      EscrevaL("Digite [2] para doar R$25")
      EscrevaL("Digite [3] para doar R$50")
      EscrevaL("Digite [4] para doar outros valores")
      EscrevaL("Digite [5] para cancelar")
      Leia(N)
      Escolha N
              Caso 1
                   Valor <- 10
              Caso 2
                   Valor <- 25
              Caso 3
                   Valor <- 50
              Caso 4
                    Escreva("Qual o valor da doação? R$")
                    Leia(Valor)
              Caso 5
                   Valor <- 0
      FimEscolha
      EscrevaL("----------------------")
      Escreval("SUA DOAÇÃO FOI DE R$", Valor)
      EscrevaL("----------------------")

Fimalgoritmo