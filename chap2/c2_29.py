import utility


def make_mobile(left, right):
    return utility.list(left, right)


def make_branch(length, structure):
    return utility.list(length, structure)


def left_branch(mobile):
    return utility.car(mobile)


def right_branch(mobile):
    return utility.car(utility.cdr(mobile))


def branch_length(branch):
    return utility.car(branch)


def branch_structure(branch):
    return utility.car(utility.cdr(branch))


def total_weight(mobile):
    return 0


def main():
    print("Hello")


if __name__ == '__main__':
    main()
