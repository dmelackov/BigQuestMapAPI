import requests
from PIL import Image
import pygame
from io import BytesIO
from app.objects.vectorUtils import Vector


class API:
    def __init__(self):
        self.geoCoderUrl = "http://geocode-maps.yandex.ru/1.x/"
        self.staticMapUrl = "http://static-maps.yandex.ru/1.x/"
        self.organizationUrl = "https://search-maps.yandex.ru/v1/"

        self.geoCoderApikey = "40d1649f-0493-4b70-98ba-98533de7710b"
        self.organizationApikey = "ebbc19e0-2f51-41bc-bb0a-4b882df65a8e"

        self.format = "json"

    def loadMap(self, YandexMap):
        localparams = {}
        if len(YandexMap.markers) != 0:
            localparams['pt'] = '~'.join(list(map(lambda x: x.toString(), YandexMap.markers)))
        localparams['ll'] = YandexMap.position.toString()
        localparams['z'] = YandexMap.size
        localparams['l'] = YandexMap.layer
        return self.requestStaticMap(localparams)

    def findAddressGeocoder(self, address):
        params = {'geocode': address}
        return GeocoderMapObject(self.requestGeocoder(params))

    def requestGeocoder(self, params: dict):
        localParams = params
        localParams['apikey'] = self.geoCoderApikey
        localParams['format'] = self.format
        response = self.defaultResponse(self.geoCoderUrl, localParams)
        return response.json()

    def requestOrganization(self, address, params={}):
        localParams = params
        localParams["text"] = address
        localParams["apikey"] = self.organizationApikey
        localParams["lang"] = "ru_RU"
        localParams["type"] = "biz"
        localParams["spn"] = "1,1"
        response = self.defaultResponse(self.organizationUrl, localParams)
        return OrganisationObject(response.json())

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
        if not response:
            print(response.content)
            return
        return response


class GeocoderMapObject:
    def __init__(self, response):
        self.response = response

    def getPostion(self):
        toponym = self.response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
        return Vector(float(toponym_longitude), float(toponym_lattitude))

    def getSize(self):
        toponym = self.response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        xstart, ystart = map(float, toponym["boundedBy"]["Envelope"]["upperCorner"].split())
        xstop, ystop = map(float, toponym["boundedBy"]["Envelope"]["lowerCorner"].split())
        longitude_size, lattitude_size = [xstart - xstop, ystart - ystop]
        z = 0
        while longitude_size < 360 / 2 ** z and z <= 17:
            z += 1
        while lattitude_size < 360 / 2 ** z and z <= 17:
            z += 1
        return z - 1

    def getAddress(self):
        toponym = self.response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        return toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["formatted"]

    def getIndex(self):
        toponym = self.response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        try:
            return toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
        except KeyError:
            return 'Отсутствует'


class OrganisationObject:
    def __init__(self, response):
        self.response = response
        if len(self.response["features"]) == 0:
            return None
        self.geocode = ApiClassObject.findAddressGeocoder(self.getAddress())

    def getAddress(self):
        if len(self.response["features"]) == 0:
            return None
        toponym = self.response["features"][0]["properties"]["CompanyMetaData"]
        return toponym["address"]

    def getIndex(self):
        if len(self.response["features"]) == 0:
            return None
        return self.geocode.getIndex()

    def getPostion(self):
        if len(self.response["features"]) == 0:
            return None
        toponym = self.response["features"][0]
        coords = toponym['geometry']['coordinates']
        toponym_longitude, toponym_lattitude = coords
        return Vector(float(toponym_longitude), float(toponym_lattitude))

    def getName(self):
        if len(self.response["features"]) == 0:
            return None
        toponym = self.response["features"][0]["properties"]["CompanyMetaData"]
        return toponym['name']


ApiClassObject = API()
