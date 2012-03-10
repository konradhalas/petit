import types

class Petit(type):

    def __new__(cls, cls_name, cls_parents, cls_attr): 
        cls.cls_attr = cls_attr
        for parent in cls_parents:
            cls.fix_names(parent.__dict__)
        cls.fix_names(cls_attr)
        return type.__new__(cls, cls_name, cls_parents, cls_attr)

    @classmethod
    def fix_names(cls, cls_attr):
        for attr in cls_attr.copy():
            if isinstance(cls_attr[attr], types.FunctionType):
                if cls.is_bad_function_name(attr):
                    cls.cls_attr[cls.create_good_function_name(attr)] = cls_attr[attr]

    @classmethod
    def is_bad_function_name(cls, function_name):
        return function_name.lower() != function_name and '_' not in function_name 

    @classmethod
    def create_good_function_name(cls, function_name):
        new_function_name = function_name[0].lower() 
        for char in function_name[1:]:
            if char.isupper():
                new_function_name += '_'
                char = char.lower()
            new_function_name += char
        return new_function_name

