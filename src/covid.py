import urequests
from machine import Pin
import ujson
from led import Led
from button import Button


led_red = Led(21)
led_yellow = Led(22)
led_green = Led(19)
button_left = Button(23)
button_right = Button(18)

def getData():
    location = 'portugal'
    data1 = '2020-07-03T00:00:00Z'
    data2 = '2020-07-04T00:00:00Z'
    data3 = '2020-07-05T00:00:00Z'
    url = 'https://api.covid19api.com/total/country/{0}?from={1}&to={2}'.format(location, data1, data2)
    url2 = 'https://api.covid19api.com/total/country/{0}?from={1}&to={2}'.format(location, data2, data3)
    dados_passado = urequests.get(url).json()
    dados_atual = urequests.get(url2).json()
    return dados_passado, dados_atual

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

first = button_left.state()
second = button_right.state()

while True:
    novosmortos_passado, novosmortos_atual = mortos()
    novosinfetados_passado, novosinfetados_atual = infetados()

    first = button_left.state()
    second = button_right.state()

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
    print('Pressione longamente o botão esquerdo para saber se o novo numero de infetados é superior ao do dia anterior, e o botão direito para as mortes.')
    print('Nas ultimas horas, registaram-se mais',novosmortos_atual, 'mortes e mais', novosinfetados_atual,'infetados.')
    print(getData()[1])
    #print('Atualmente registam-se',,'casos ativos e um total de',,'recuperados')
#print(getData)
#print('Do you think that the number of infected people increased? Press the right button for yes, and the left button for no')

