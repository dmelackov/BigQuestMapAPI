import requests
from PIL import Image
import pygame
from io import BytesIO


class API:
    def __init__(self):
        self.geoCoderUrl = "http://geocode-maps.yandex.ru/1.x/"
        self.staticMapUrl = "http://static-maps.yandex.ru/1.x/"
        self.organizationUrl = "https://search-maps.yandex.ru/v1/"

        self.geoCoderApikey = "40d1649f-0493-4b70-98ba-98533de7710b"
        self.organizationApikey = ""

        self.format = "json"

    def loadMap(self, YandexMap):
        params = {}
        if len(YandexMap.markers) != 0:
            params['pt'] = '~'.join(list(map(lambda x: x.toString(), YandexMap.markers)))
        params['ll'] = YandexMap.position.toString()
        params['z'] = YandexMap.size
        params['l'] = YandexMap.layer
        return self.requestStaticMap(params)

    def requestGeocoder(self, params: dict):
        localParams = params
        localParams['apikey'] = self.geoCoderApikey
        localParams['format'] = self.format
        response = self.defaultResponse(self.staticMapUrl, localParams)
        return response.json()

    def requestOrganization(self, params: dict):
        localParams = params
        localParams['apikey'] = self.organizationApikey
        localParams["lang"] = "ru_RU"
        response = self.defaultResponse(self.staticMapUrl, localParams)
        return response.json()

    def requestStaticMap(self, params: dict):
        localParams = params
        localParams['size'] = "600,450"
        response = self.defaultResponse(self.staticMapUrl, localParams)
        image = Image.open(BytesIO(response.content)).convert("RGB")
        mode = image.mode
        size = image.size
        data = image.tobytes()
        pyImage = pygame.image.fromstring(data, size, mode)
        return pyImage

    def defaultResponse(self, apiServer, params: dict):
        response = requests.get(apiServer, params=params)
        #print(params)
        if not response:
            print(response.content)
            return
        return response


class GeocoderMapObject:
    def __init__(self, response):
        self.response = response

    def getPostion(self):
        pass

    def getSize(self):
        pass

    def getAddress(self):
        pass

    def getIndex(self):
        pass


ApiClassObject = API()
