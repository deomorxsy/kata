#!/usr/bin/R
#30/01/2021

#setwd("~/Documentos/coding/projetos/rscripts/bib-packrat")
#packrat::on("~/Documentos/coding/projetos/rscripts/bib-packrat")

# Exercise 1: Vectors and Functions
#https://www.r-exercises.com/2019/08/12/vectors-and-functions

#1.1
rivstats <- c(length(rivers), sum(rivers), mean(rivers), median(rivers), var(rivers),
                sd(rivers), min(rivers), max(rivers))
rivstats

#1.2
#Média truncada: valor da porcentagem * número total de amostras.
#O valor do produto é retirado dos extremos da amostra.
#A) 0.25 * 8 = 2.0 || mean(1, 2, 3, 6) = 3.
trunmed <- mean(c(-100, 0, 1, 2, 3, 6, 50, 73), trim=0.25)
#B)
trunrivers <- mean(rivers, trim=(10/length(rivers)))
