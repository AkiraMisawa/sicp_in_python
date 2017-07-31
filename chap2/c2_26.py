from utility import cons, list, append, print_list

if __name__ == '__main__':
    x = list(1, 2, 3)
    y = list(4, 5, 6)

    print_list(append(x, y))
    print_list(cons(x, y))
    print_list(list(x, y))
