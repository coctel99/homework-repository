from functools import wraps


class KeyValueStorage:
    def __init__(self, path_to_file: str):
        try:
            with open(path_to_file) as fi:
                for line in fi:
                    # TODO: check for value error
                    key, value = line.strip().split("=")
                    if getattr(self, key, None) is None:
                        setattr(self, key, value)
        except FileNotFoundError:
            print(f"File {path_to_file} not found")
        except ValueError as val_err:
            print(f"Cannot assign {val_err.args} attribute")

    def __getitem__(self, item):
        return getattr(self, item)


class B:
    pass


if __name__ == '__main__':
    a = KeyValueStorage("test.txt")
    print(a.__dict__)
    b = B()
    pass

