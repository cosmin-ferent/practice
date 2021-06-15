
def split_and_join(line):
    split_text = line.split(" ")
    join_text = "-".join(split_text)
    return join_text


line = input('Your text: ')
result = split_and_join(line)
print(result)
