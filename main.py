import datetime
import os


def decorator(path):
    def wrapper(external):
        def inner(*args, **kwargs):
            _datetime = datetime.datetime.today().strftime(f'date: %d.%m.%Y, time: %H:%M:%S')
            file_name = f'function name: {external.__name__}'
            inputs = f'inputs = {args}, {kwargs}'
            result = f'result = {external(*args, **kwargs)}'
            function_details = [_datetime, file_name, inputs, result]
            with open(os.path.join(path, f'{external.__name__}.txt'), 'a', encoding='utf-8') as f:
                data = '\n'.join(str(item) for item in function_details)
                f.write(data + '\n')
            return result
        return inner
    return wrapper


@decorator(os.getcwd())
def foo(a, b):
    return a / b


@decorator(os.getcwd())
def foo2(a, b):
    return a * b


foo(5, 6)
foo2(a=10, b=33)
