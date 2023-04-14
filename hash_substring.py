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
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p_len = hash(pattern)
    t_len = hash(text[:len(pattern)])
    occurrences = []

    for i in range (len(text) - len(pattern) + 1):
        if p_len == hash(text[i:i+len(pattern)]) and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
        if i < len(text) - len(pattern):
            t_len = hash(text[i+1:i+len(pattern)+1]) + hash(text[i]) - hash(text[i+len(pattern)])
 
    return occurrences 


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

