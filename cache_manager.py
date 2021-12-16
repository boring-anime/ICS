import cache_element
import dbHandler
import request


class Cache_manager:

    def __init__(self, request):

        self.request_type =  request.type
        self.key = request.key
        self.value = request.value

    def request_to_cache(self):
        cache = cache_element.Cache()

        if self.request_type == "GET":
            self.respond = cache.get_value(self.key)

            if  self.respond == None:
                database= dbHandler.dbHandler()
                database.createConnection()
                self.respond = database.getData(self.key)

        if self.request_type == "PUT":

            element = cache_element.cache_element(self.key, self.value)


            self.respond = cache.append_element(element)
            database= dbHandler.dbHandler()
            # database.createConnection()
            self.respond = database.putData(self.key, self.value)

        if self.request_type == "DEL":
            self.respond = cache.delete_cache_element(self.key)