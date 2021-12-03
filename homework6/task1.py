"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
from functools import wraps


def instances_counter(cls):
    """Adds a class methods get_created_instances and
    reset_instances_counter."""
    cls.inst_counter = 0

    @wraps(cls)
    def init_with_inst_counter(*args, **kwargs):
        """Increment counter on initialization of new instances."""
        cls.inst_counter += 1

    def get_created_instances(*args):
        """Get number of created instances."""
        return cls.inst_counter

    def reset_instances_counter(*args):
        """Get number of created instances and reset the counter."""
        num_instances = cls.inst_counter
        cls.inst_counter = 0
        return num_instances

    cls.__init__ = init_with_inst_counter
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls
