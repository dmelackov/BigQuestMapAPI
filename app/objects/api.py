from app.objects.map import Map


class API:
    def __init__(self):
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
