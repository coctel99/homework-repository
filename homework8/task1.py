from functools import wraps


def make_key_value_storage(cls):
    """
    Make key-value storage from specified class
    :param cls: Class to alter
    :return: Altered class
    """
    original_init = cls.__init__

    @wraps(cls)
    def new_init(self, path_to_file, *args, **kwargs):
        """
        Give instance attributes from file
        :param self: Instance of a class
        :param path_to_file: Path to the file with keys and values
        :param args: Original __init__ *args
        :param kwargs: Original __init__ **kwargs
        """
        original_init(self, *args, **kwargs)
        try:
            with open(path_to_file) as fi:
                for line in fi:
                    key, value = line.strip().split("=")
                    if key.count(" ") > 0:
                        raise ValueError(key)
                    if getattr(self, key, None) is None:
                        setattr(self, key, value)
        except FileNotFoundError:
            print(f"File {path_to_file} not found")
        except ValueError as val_err:
            print(f"Cannot assign '{val_err}' attribute")

    def get_item(self, item):
        """Get a value with the key"""
        return getattr(self, item)

    cls.__init__ = new_init
    cls.__getitem__ = get_item
    return cls
