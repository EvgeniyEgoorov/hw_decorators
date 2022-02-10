import datetime
import os


def decorator(path):
    def wrapper(external):
        def inner(*args, **kwargs):
            _datetime = datetime.datetime.today().strftime(f'date: %d.%m.%Y, time: %H:%M:%S')
            file_name = f'function name: {external.__name__}'
            inputs = f'inputs = {args}, {kwargs}'
            result = external(*args, **kwargs)
            function_details = [_datetime, file_name, inputs, f'result = {result}']
            with open(os.path.join(path, f'{external.__name__}.txt'), 'w', encoding='utf-8') as f:
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


@decorator(os.getcwd())
def summator(x, y):
    return x + y


three = summator(1, 2)
five = summator(2, 3)

res = summator(three, five)

print('result: ', res)
print('result type: ', type(res))


