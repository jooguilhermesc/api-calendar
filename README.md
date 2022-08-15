# API Calendário com Feriados

A presente API supre uma necessidade bem específica para quem precisa trabalhar com datas úteis do calendário da Febraban.

Os dados retornados pela API são simples

```
"Date": Data no formato timezone;
"Day": Dia da semana de domingo a sábado, onde domingo é 0 e segue até sábado ser representado pelo 6
"Week": Representa qual semana do ano aquela data pertende variando de 1 a 52;
"Month": Número do mês de Janeiro a Dezembro;
"Quarter": Trimestre do ano;
"Year": Ano;
"Year_half": Semestre do ano;
"workday": Define se é um dia útil (1) ou não (0).
```

Essa API foi desenvolvida para ser utilizada no PowerBI, então pode ser consumida tranquilamente como um Web Básico e assim gerar dimensão calendário já com os feriados de maneira descomplicada.
