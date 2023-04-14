from strplus.cases import to_pascal, to_camel

class Str(str):
    def __new__(cls, wrapped_str):
        if not isinstance(wrapped_str, str):
            raise TypeError("wrapped_str must be a string")
        return super().__new__(cls, wrapped_str)

    def __getattr__(self, attr):
        return super().__getattribute__(attr)

    def __getitem__(self, key):
        if isinstance(key, int):
            item = super().__getitem__(key)
            if isinstance(item, str):
                return Str(item)
            return item
        elif isinstance(key, slice):
            return Str(super().__getitem__(key))
        else:
            raise TypeError("indices must be integers")
    def pascal(self):
        return Str(to_pascal(self))
    def camel(self):
        return Str(to_camel(self))
