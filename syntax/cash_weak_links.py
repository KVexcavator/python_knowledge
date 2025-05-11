# Обычный кэш хранит сильные ссылки, не давая объектам удаляться. Проблему решает WeakValueDictionary.

import weakref 
 
class Cache: 
    def init(self): 
        self._data = weakref.WeakValueDictionary() 
 
    def get(self, key): 
        return self._data.get(key) 
 
    def set(self, key, value): 
        self._data[key] = value 
 
# Объекты в кэше удаляются, когда на них нет других ссылок 