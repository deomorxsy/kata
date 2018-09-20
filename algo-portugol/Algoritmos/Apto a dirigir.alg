algoritmo "AptoADigirir"
// Função : Mostra se você está apto a dirigir.
// Autor : Lucas da Silva Paixão
// Data : 13/01/2017
// Seção de Declarações 
var
   X, Y, idade: inteiro
inicio
      EscrevaL("-------------------------")
      EscrevaL("DEPARTAMENTO DE TRÂNSITO ")
      EscrevaL("-------------------------")
      Escreva("Ano Atual (yyyy):")
      Leia(X)
      Escreva("Ano de nascimento (yyyy):")
      Leia(Y)
      EscrevaL("----------STATUS----------")
      idade <- (X - Y)
      EscrevaL("IDADE: ", idade, " ANOS ")
      Se (idade >= 18) entao
      EscrevaL("ESTÁ APTO A TIRAR CARTEIRA")
      senao
      EscrevaL("ESTÁ INAPTO A TIRAR CARTEIRA")
      fimse
      EscrevaL("--------------------------")
fimalgoritmo
