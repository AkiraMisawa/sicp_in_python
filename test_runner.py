import sys
import unittest


def main(path):
    loader = unittest.TestLoader()
    test = loader.discover(path)
    runner = unittest.TextTestRunner()
    runner.run(test)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: %s path" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])
