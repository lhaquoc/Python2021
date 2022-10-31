import time


def anagram_solution_1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True
    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            a_list[pos2] = None
        else:
            still_ok = False
        pos1 = pos1 + 1
    return still_ok


def anagram_solution_2(s1, s2):
    a_list = list(s1)
    b_list = list(s2)

    a_list.sort()
    b_list.sort()

    pos = 0
    matches = True
    while pos < len(a_list) and matches:
        if a_list[pos] == b_list[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches


def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i
    end = time.time()
    return the_sum, end - start


def main():
    for i in range(5):
        print("Sum of %d required %10.7f seconds" % sum_of_n_2(1000000))


if __name__ == '__main__':
    main()
