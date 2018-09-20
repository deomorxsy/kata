algoritmo "CalculoIMC"
// Disciplina   :  [Linguagem e Lógica de Programação] 
// Professor   : Gustavo Guanabara 
// Função : Calcular o Índice de Massa Corpórea do indivíduo
// Autor : Lucas da Silva Paixão
// Data : 12/01/2017
// Nota1: Sempre que abrir "Se", feche com "fimse". Vai ajudar na identação
//Declarações: Se, senao, e, entao, fimse
//Utilizado aqui: identação aninhada. Sem a aninhação ficaria como o da
//primeira versão.
var
   M, A, IMC: Real
inicio
      Escreva("Massa (Kg): ")
      Leia(M)
      Escreva("Altura (h): ")
      Leia(A)
      IMC <- (M)/(A^2)
      EscrevaL("IMC: ", IMC:5:2)
      Se (IMC < 17) entao
         EscrevaL("Você está muito abaixo do peso.")
      
      Senao
           Se (IMC >= 17) e (IMC <= 18.5)entao
              EscrevaL("Você está abaixo do peso")
      
           Senao
                Se(IMC >=18.5) e (IMC <=25) entao
                       EscrevaL("Parabéns! Você está no seu peso ideal")
      
                Senao
                     se (IMC >=25) e (IMC <= 30) entao
                        EscrevaL("Você está com obesidade")

                     Senao
                          Se (IMC >= 30) e(IMC <= 35) entao
                             EscrevaL("Você está com Obesidade Severa")
      
                             Senao
                                  Se (IMC >= 35) e (IMC <= 40) entao
                                     EscrevaL("Você está com Obesidade Mórbida")
                                  fimse
                           fimse
                     fimse
                fimse
           fimse
      fimse
      
      EscrevaL("PS: Independente de seu peso, é aconselhável procurar o médico em todos os casos.")
      EscrevaL("Uma bateria de exames sempre deve ser feita de tempos em tempos para que fique")
      Escreva("tudo bem com sua saúde.")

      
fimalgoritmo

