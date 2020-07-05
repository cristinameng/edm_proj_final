# Introdução
Neste projeto foi desenvolvido o uso de uma API, usando os resultados fornecidos por esta para acender/apagar os LEDs. A API usada foi a do COVID-19, que nos devolve o número de casos ativos, o número de mortes e o de recuperados, entre duas datas à nossa escolha, correspondentes a um país, também à nossa escolha. 
# Desenvolvimento
**API usada**: https://api.covid19api.com/total/country/{0}?from={1}&to={2}

Ao pedirmos a data fornecida por este url, esta vem em json. De forma a conseguir controlar os LEDs, é necessário conseguir convertê-la, de forma a conseguir ser lida pela ESP32.

São fornecidas três datas: comparar-se-á o número de casos ativos e também de mortes tanto do dia 1 para o dia 2, como do dia 2 para o dia 3. Caso a primeira seja inferior à segunda, o LED vermelho irá acender-se. Se for igual, o LED amarelo acender-se-á, e, por fim, caso seja superior, o LED verde será o acendido. 

Carregando no botão esquerdo, obtém-se esta comparação para o número novo de infetados e carregando no botão direito, obtém-se a comparação para o número novo de mortes.
No final, é dado um print quantitativo do número novo de infetados e de mortos do dia 2 para o dia 3, ou seja do dia passado para o dia atual.
# Output
