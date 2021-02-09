from app.objects.map import Map


class API:
    def __init__(self):
        self.geoCoderUrl = ""
        self.staticMapUrl = ""
        self.organizationUrl = ""

        self.geoCoderApikey = ""
        self.organizationApikey = ""

        self.format = "json"

    def loadMap(self):
        pass

    def requestGeocoder(self, params):
        pass

    def requestOrganization(self, params):
        pass

    def requestStaticMap(self, params):
        pass


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

