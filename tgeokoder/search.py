import requests
with open('secret.txt') as f:
    geokoder_api_key = f.read().strip()
from bot_geokoder.models import Filter

query = Filter.objects.values('text')
filters = []
for filter in query:
    for value in filter:
        filters.append(filter[value])
#for value in range(len(filters)):
   # filters.append(filters[value])

#print(type(query),'\n',filters)
list_of_adresses =[]

def get_coord(addres):
    a = requests.get(
        'https://geocode-maps.yandex.ru/1.x/?format=json&apikey={}&geocode={}'.format(geokoder_api_key, addres))
    d = dict(a.json())
    try:
        #dipoint = d['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        results = d['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['results']
        for adres in range(int(results)):
            list_of_adresses.append(d['response']['GeoObjectCollection']['featureMember'][adres]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
            #print(d['response']['GeoObjectCollection']['featureMember'][adres]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])

    except IndexError:
        return [None, None]
    #coord = list(map(float, point))
    for adres in range(len(list_of_adresses)):
        for filter in range(len(filters)):
            if filters[filter] in list_of_adresses[adres]:
                #print(list_of_adresses[adres])
                
                return list_of_adresses[adres]




#get_coord('Красная площадь')
#get_adres('37.621085, 55.753585')