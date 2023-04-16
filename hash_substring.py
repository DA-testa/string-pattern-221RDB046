# python3

def read_input():

    text = input()
    if text[0]=="I":
        pattern = input().rstrip()
        text = input().rstrip()
    elif text[0]=="F":
        file_name = "tests/06"
        with open(file_name, 'r') as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()

    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    pattern_hash = hash(pattern)
    occurrences = []

    for i in range (len(text) - len(pattern) + 1):
        if pattern_hash == hash(text[i:i+len(pattern)]) and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
