"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError при
custom_sum.__original_func

Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
print(custom_sum.__doc__)  # 'This function can sum any objects which
have __add___'
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""
from functools import wraps


def save_orig_func(original_func):
    """
    Save original function and its __name__ amd __doc__ attributes
    """
    @wraps(original_func)
    def wrapper(wrapped_func):
        wrapped_func.__name__ = original_func.__name__
        wrapped_func.__doc__ = original_func.__doc__
        wrapped_func.__original_func = original_func
        return wrapped_func
    return wrapper


def print_result(func):
    @save_orig_func(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function."""
        result = func(*args, **kwargs)
        print(result)
        return result

    return wrapper
