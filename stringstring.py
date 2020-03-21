from ascii_letters import ascii_letters


def stringstring(string):
    base = ''
    for i in range(6):
        for j in string:
            base += ascii_letters[i][j]
        base += '\n'
    string = string.replace(' ', '')

    result = ''
    counter = 0
    for i in base:
        if i == '~':
            result += string[counter]
            counter += 1
            if counter == len(string):
                counter = 0
        else:
            result += i

    return result


if __name__ == "__main__":
    print(stringstring('Hello World!'))
    print(stringstring("This is StringString"))
