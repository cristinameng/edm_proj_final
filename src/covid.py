from machine import Pin
import urequests
import ujson

led_red = Pin(21, Pin.OUT)
led_yellow = Pin(22, Pin.OUT)
led_green = Pin(19, Pin.OUT)
button_left = Pin(23, Pin.IN, Pin.PULL_UP)
button_right = Pin(18, Pin.IN, Pin.PULL_UP)


def getData():
    location = 'portugal'
    data1 = '2020-07-03T00:00:00Z'
    data2 = '2020-07-04T00:00:00Z'
    data3 = '2020-07-05T00:00:00Z'

    #Datas de teste (numero de mortos é igual)
    #data1 = '2020-06-25T00:00:00Z'
    #data2 = '2020-06-26T00:00:00Z'
    #data3 = '2020-06-27T00:00:00Z'

    url = 'https://api.covid19api.com/total/country/{0}?from={1}&to={2}'.format(location, data1, data2)
    url2 = 'https://api.covid19api.com/total/country/{0}?from={1}&to={2}'.format(location, data2, data3)
    dados_passado = urequests.get(url).json()
    dados_atual = urequests.get(url2).json()
    dados_output = dados_atual[1]
    return dados_passado, dados_atual,dados_output

def infetados():
    infetados_passado = []
    infetados_novo = []

    for value in getData()[0]:
        infetados_passado.append(value["Confirmed"])
    for value in getData()[1]:
        infetados_novo.append(value["Confirmed"])
    
    novosinfetados_atual = infetados_novo[1] - infetados_novo[0]
    novosinfetados_passado = infetados_passado[1] - infetados_passado[0]

    return novosinfetados_passado, novosinfetados_atual

def mortos():
    mortes_passado = []
    mortes_novo = []

    for value in getData()[0]:
        mortes_passado.append(value["Deaths"])
    for value in getData()[1]:
        mortes_novo.append(value["Deaths"])
    
    novosmortos_atual = mortes_novo[1] - mortes_novo[0]
    novosmortos_passado = mortes_passado[1] - mortes_passado[0]
    
    return novosmortos_passado, novosmortos_atual

while True:
    novosmortos_passado, novosmortos_atual = mortos()
    novosinfetados_passado, novosinfetados_atual = infetados()

    first = button_left.value()
    second = button_right.value()

    if first and not second: #novos infetados
        led_red.off()
        led_green.off()
        led_yellow.off()

        if novosinfetados_atual > novosinfetados_passado:
            led_red.on()
        elif novosinfetados_atual < novosinfetados_passado:
            led_green.on()
        elif novosinfetados_atual == novosinfetados_passado:
            led_yellow.on()
    
    if second and not first: #novas mortes
        led_red.off()
        led_green.off()
        led_yellow.off()

        if novosmortos_atual > novosmortos_passado:
            led_red.on()
        elif novosmortos_atual < novosmortos_passado:
            led_green.on()
        elif novosmortos_atual == novosmortos_passado:
            led_yellow.on()
    print('Press (until the led goes on) the left button to know if the number of infected is superior/inferior/equal to the one on the prior days, or the right button, for the deaths')
    print('Nas ultimas horas, registaram-se mais',novosmortos_atual, 'mortes e mais', novosinfetados_atual,'infetados.')
    #print('No dia anterior, tinham-se registado mais',novosmortos_passado, 'mortes e mais', novosinfetados_passado,'infetados.')
    print(getData()[2]) #Dados do dia atual