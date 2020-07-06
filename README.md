# Introdução
Neste projeto foi desenvolvido o uso de uma API, usando os resultados fornecidos por esta para acender/apagar os LEDs. A API usada foi a do COVID-19, que nos devolve o número de casos ativos, o número de mortes e o de recuperados, entre duas datas à nossa escolha, correspondentes a um país, também à nossa escolha. 
# Desenvolvimento
**API usada**: [COVID-19 - All Documentation](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest)

Neste projeto, foi usada a By Country.


Para esta API são fornecidos os seguintes parâmetros: duas datas e a localização (país em específico). 
```python
url = https://api.covid19api.com/total/country/{0}?from={1}&to={2}.format(location,data1,data2)
dados= urequests.get(url).json()
```
Os dados desta API são recolhidos com a função getData().

De forma a conseguir efetuar-se uma comparação do novo número de infetados e de mortos, é necessário fornecer três datas - o dia 3 é o dia atual, o dia 2 é o dia antes desse e o dia 3 é o dia anterior a este - de forma a que se consigam obter o número de casos ativos e de mortes tanto do dia 1 para o dia 2, como do dia 2 para o dia 3. Caso a primeira seja inferior à segunda, o LED vermelho irá acender-se. Se for igual, o LED amarelo acender-se-á, e, por fim, caso seja superior, o LED verde será o acendido.
Carregando no botão esquerdo, obtém-se esta comparação para o número novo de infetados e carregando no botão direito, obtém-se a comparação para o número novo de mortes.

O número de novos infetados é dado pela função infetados() e o número de novas mortes é dado pela função mortos(). Estas funcionam da mesma maneira_ através de um ciclo for, percorrem os dados obtidos e realiza-se um append para uma lista vazia dos valores desejados, quando estes são encontrados, neste caso "Confirmed" e "Deaths". Por exemplo, para as mortes dos dois dias anteriores tem-se que:
 ``` python
    mortes_passado = []
    for value in getData()[0]:
        mortes_passado.append(value["Deaths"])
```
Depois, é realizada a subtração entre o último e o primeiro valor desta lista, de forma a conseguir-se obter o valor desejado.


No final, é dado um print quantitativo do número novo de infetados e de mortos do dia 2 para o dia 3, ou seja do dia passado para o dia atual.
## Output
Para um dia1 = 2020/07/03, dia2 = 2020/07/04 e dia3 = 2020/07/05, e sendo a nossa localização Portugal, obtém-se o seguinte output:

>Press (until the led goes on) the left button to know if the number of infected is superior/inferior/equal to the one on the prior days, or the right button, for the deaths.

>Nas ultimas horas, registaram-se mais 9 mortes e mais 328 infetados.

>No dia anterior, tinham-se registado mais 7 mortes e mais 413 infetados. (esta linha é opcional, é apenas para verificação da cor dos LEDs)

>{'Lat': '0', 'Active': 13192, 'City': '', 'Province': '', 'Deaths': 1605, 'Recovered': 28772, 'Confirmed': 43569, 'CityCode': '', 'Lon': '0', 'Country': 'Portugal', 'CountryCode': '', 'Date': '2020-07-04T00:00:00Z'}

Pelo que, pressionando o botão direito temos que o LED verde aceso, e, pressionando o botão esquerdo, temos o LED vermelho aceso.

# Conclusão
O código corre e faz o pedido, contudo é ligeiramente lento em apresentar os resultados, devido ao facto de estarmos a usar ciclos for para percorrer os dados da API e a juntá-los a uma lista. Daí o botão ter de ser pressionado longamente, para conseguir estar em "síncrono" com o momento em que os resultados são lançados.
