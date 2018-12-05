algoritmo "ViagemDisney"
// Disciplina   :  [Linguagem e Lógica de Programação] 
// Professor   : Gustavo Guanabara 
// Função :  Nivelamento de dinheiro para viagem para a Disney
// Autor : deomorxsy
// Data : 12/01/2017
// Seção de Declarações 
var
    cash : Real
inicio
      EscrevaL("Vamos começar o programa de nivelamento de dinheiro para viagens.")
      Escreva("Quanto dinheiro você tem?")
      Leia(cash)
      Se(cash >= 10000) entao
              EscrevaL("Analisamos o seu dinheiro e...")
              EscrevaL("PARABÉNS! Comece a fazer as malas ainda hoje para sua viagem!")
      Senao
              EscrevaL("Infelizmente você não tem o dinheiro básico para se manter na Disney, ainda.")
              EscrevaL("Mas não desanime! Continue trabalhando duro e suas férias chegarão!")
      fimse

fimalgoritmo
