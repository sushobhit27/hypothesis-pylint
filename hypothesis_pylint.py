import string
from hypothesis import strategies as st


EXCEPTIONS = ['OSError',
              'ArithmeticError',]

NUMERIC_EXCEPTIONS = ['ArithmeticError',
                      'OverflowError',
                      'FloatingPointError',
                      'ZeroDivisionError']

OPERATORS = ['+',
             '-',
             '*',
             '/',
             '%']


def operator():
    return st.sampled_from(OPERATORS)


def import_from():
    renamed_package = st.text(alphabet=string.ascii_lowercase, min_size=1, max_size=10).example()
    original_package = st.text(alphabet=string.ascii_lowercase, min_size=1, max_size=10).example()
    package_path = '.'.join(st.lists(elements=st.text(alphabet=string.ascii_lowercase, min_size=1, max_size=10)).example())
    return 'from ' + package_path + ' import ' + original_package + ' as ' + renamed_package


def arithmetic_assign_exp():
    op = '='
    operand = st.text(alphabet=string.ascii_lowercase, min_size=1, max_size=10).example()
    value = st.text(alphabet=string.digits, min_size=1, max_size=5).example()
    return operand + ' = ' + value


def except_handler():
    exceptions = tuple(st.sets(st.sampled_from(NUMERIC_EXCEPTIONS)).example())
    if not exceptions:
        exceptions = ''
    return 'except ' + str(exceptions) + ':'


if __name__ == '__main__':
    print(except_handler())
    print(arithmetic_assign_exp())
    print(import_from())