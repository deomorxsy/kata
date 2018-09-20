algoritmo "SimulaçãoAprovaçãoReprovação"
// Disciplina   :  [Curso de Algoritmos - Curso em Video]
// Professor   : Gustavo Guanabara
// Função : Permite criar uma simulação de aprovação/recuperação/reprovação de alunos.
// Autor : Lucas da Silva Paixão
// Data : 14/01/2017
// Seção de Declarações
var
   N1, N2, M: Real
inicio
   EscrevaL("---------------------------")
   EscrevaL("  ESCOLA JAVALI CANSADO")
   EscrevaL("---------------------------")
   Escreva("1º Nota: ")
   Leia(N1)
   Escreva("2ª Nota: ")
   Leia(N2)
   M <-(N1+N2)/2
   Escreva("A média do aluno foi ", M:4:2)
   Se(M >= 7) entao
        EscrevaL(" e o aluno está APROVADO.")
   senao
        Se(M >= 5) e (M < 7) entao
             EscrevaL(" e o aluno está em RECUPERAÇÃO.")
        senao
             EscrevaL(" e o aluno está REPROVADO.")
        Fimse
   Fimse
fimalgoritmo