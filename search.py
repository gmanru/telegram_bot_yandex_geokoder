import requests
with open('secret.txt') as f:
    geokoder_api_key = f.read().strip()


filters = ['Орловская область','Москва']
list_of_adresses =[]

def get_coord(addres):
    a = requests.get(
        'https://geocode-maps.yandex.ru/1.x/?format=json&apikey={}&geocode={}'.format(geokoder_api_key, addres))
    d = dict(a.json())
    try:
        point = d['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')
        results = d['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['results']
        for adres in range(int(results)):
            list_of_adresses.append(d['response']['GeoObjectCollection']['featureMember'][adres]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
            #print(d['response']['GeoObjectCollection']['featureMember'][adres]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])

    except IndexError:
        return [None, None]
    coord = list(map(float, point))
    for adres in range(len(list_of_adresses)):
        for filter in range(len(filters)):
            if filters[filter] in list_of_adresses[adres]:
                print(list_of_adresses[adres],results)
        #print(filters[filter])
        #print(list_of_adresses)
    #coord.reverse()
    #print(coord)
    return list_of_adresses


def get_adres(coord:str):
    #print('entered')
    a = requests.get(
        'https://geocode-maps.yandex.ru/1.x/?format=json&apikey={}&geocode={}'.format('42e25768-2695-41ce-bc97-a25cf4bf21fd', coord))
    d = dict(a.json())
    #print(d)
    try:
        results = d['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['results']
        for adres in range(len(results)):
            #list_of_adresses.append(d['response']['GeoObjectCollection']['featureMember'][adres]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
            print(d['response']['GeoObjectCollection']['featureMember'][adres]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
    except IndexError:
        return [None, None]
    #coord = list(map(float, point))
    #coord.reverse()
    #for filter in range(len(filters)):
    if filters in list_of_adresses:
        print(adres,results)

    return adres

get_coord('Красная площадь')
#get_adres('37.621085, 55.753585')