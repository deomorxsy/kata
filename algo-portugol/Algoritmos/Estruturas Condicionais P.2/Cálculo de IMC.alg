algoritmo "CalculoIMC"
// Disciplina   :  [Linguagem e Lógica de Programação] 
// Professor   : Gustavo Guanabara 
// Função :
// Autor :
// Data : 12/01/2017
// Seção de Declarações 
var
   M, A, IMC: Real
inicio
      Escreva("Massa (Kg): ")
      Leia(M)
      Escreva("Altura (h): ")
      Leia(A)
      IMC <- (kg)/(A^2)
      EscrevaL("IMC: ", IMC:5:2)
      Se (IMC < 17) entao
         EscrevaL("Você está muito abaixo do peso.")
      
      Senao (IMC >= 17) e (IMC <= 18.5),entao
         EscrevaL("Você está abaixo do peso")
      
      Senao (IMC >=18.5) e (IMC <=25) entao
         EscrevaL("Parabéns! Você está no seu peso ideal")
      
      Senao (IMC >=25) e (IMC <= 30) entao
         EscrevaL("Você está com obesidade")

      Senao (IMC >= 30) e(IMC <= 35) entao
         EscrevaL("Você está com obesidade Severa")
      
      Senao (IMC >= 35) e (IMC <= 40) entao
         EscrevaL("Você está com obseidade mórbida")
      fimse
      
      EscrevaL("PS: Independente de seu peso, é aconselhável procurar o médico em todos os casos.")
      EscrevaL("Uma bateria de exames sempre deve ser feita de tempos em tempos para que fique")
      Escreva("tudo bem com sua saúde.")

      
fimalgoritmo

