from datetime import datetime

class cache_element:

    def __init__(self, key, value=None):
      self.key = key
      self.value = value
      self.timestamp = datetime.now()

class Cache:

    def __init__(self):
        self.array = []

    def append_element(self, cache_element):
        self.array.append(cache_element)

    def get_value(self, key):

        for element in self.array:
            if element.key == key:
                print("value = " + str(element.value))
                return element.value

            else:
                continue

        return None

    def delete_cache_element(self, key):
        for element in self.array:
            if element.key == key:
                self.array.remove(element)
            


# p1 = cache_element("John", 36)
# p2 = cache_element("sh", "test")
# p3 = cache_element("Rit", "test")

# Cache =  Cache()
# Cache.append_element(p1)
# Cache.append_element(p2)
# Cache.append_element(p3)
# Cache.get_value("Rit")
# Cache.delete_cache_element("Rit")
# Cache.get_value("Rit")
# element = Cache.get_element()
# print(element.key)
# for element in Cache.array:
#     print("key = " + element.key)