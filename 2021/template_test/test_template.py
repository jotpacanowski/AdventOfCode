import runpy
import pathlib
from sys import path


def template_test():
    print('asdf')


def test_args(argv):
    p = pathlib.Path(__file__).parent.joinpath('./test.py').as_posix()
    runpy.run_path(p, run_name='asdf', init_globals={'do_the_test': argv})


if __name__ == '__main__':
    test_args([None, 'ex', '1'])
    test_args([None, 'ex', '2'])
    try:
        test_args([None, 'ex', '3'])
        print(' --> error')
    except KeyError:
        ...
    try:
        test_args(['', ''])
        print('file found (???)')
    except FileNotFoundError:
        ...

    print('\n\nAll tests passed')
