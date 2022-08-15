# API Calendário com Feriados

A presente API supre uma necessidade bem específica para quem precisa trabalhar com datas úteis do calendário da Febraban.

```
Link: https://apicalendarholidays.herokuapp.com/
```

## Passando parâmetros para a API (atualização - 15/08/2022)

*Agora é possível gerar um calendário de acordo com a necessidade do range de datas, basta passar o intervalo de datas no formato yyyy-mm-aa, como especificado abaixo.*

Se nenhum parâmetro for passado, a API retornará um calendário de datas entre 2010-01-01 e a data atual.

### Exemplo 1 passando as duas datas: 

```
https://apicalendarholidays.herokuapp.com/?dt_start=2022-01-30&dt_end=2022-03-02
```

### Exemplo 2 passando a data de início (dt_end padrão = a data atual): 

```
https://apicalendarholidays.herokuapp.com/?dt_start=2022-01-30
```

### Exemplo 3 passando a data de fim (dt_start padrão = 2010-01-01): 

```
https://apicalendarholidays.herokuapp.com/?dt_end=2022-03-02
```


## Dados retornados pela API:

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

Essa API foi desenvolvida para ser utilizada no PowerBI, então pode ser consumida tranquilamente como um Web Básico e assim gerar uma dimensão calendário já com os feriados de maneira descomplicada.
