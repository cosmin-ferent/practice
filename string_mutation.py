def mutate_string(string, position, character):
    l_string = list(string)
    l_string[position] = character
    string = ''.join(l_string)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
