Algoritmo "MédiaEnem"
// Disciplina   :  [Linguagem e Lógica de Programação] 
// Professor   : Gustavo Guanabara 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Lucas da Silva Paixão
// Data atual  : 18/01/2017
Var
N, H, L, M, Media1, R:Real

Inicio
      EscrevaL("Simulação de média do ENEM")
      Escreva("Natureza: ")
      Leia(N)
      Escreva("Humanas: ")
      Leia(H)
      Escreva("Linguagens: ")
      Leia(L)
      Escreva("Matemática: ")
      Leia(M)
      Media1 <- (N + H + L + M)/4
      Escreva("Redação: ")
      Leia(R)
      EscrevaL("Sua média no ENEM é ", (Media1 + R)/2, ".")
      



Fimalgoritmo