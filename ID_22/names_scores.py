name_array = []
name_file = open('namesscores.txt','r')
for read in name_file:
    #print(name)
    read = read.replace('"', "") # remove the quotation marks
    read = read.split(',') # split the big string by commas
    name_array = read

print(name_array)
name_array.sort()

name_index = 1 # start at 1
total = 0 # initi

for name in name_array:
    #print(name)
    sum_char = 0
    for c in name:
        #print(c)
        if c == 'A':
            sum_char += 1
        elif c == 'B':
            sum_char += 2
        elif c == 'C':
            sum_char += 3
        elif c == 'D':
            sum_char += 4
        elif c == 'E':
            sum_char += 5
        elif c == 'F':
            sum_char += 6
        elif c == 'G':
            sum_char += 7
        elif c == 'H':
            sum_char += 8
        elif c == 'I':
            sum_char += 9
        elif c == 'J':
            sum_char += 10
        elif c == 'K':
            sum_char += 11
        elif c == 'L':
            sum_char += 12
        elif c == 'M':
            sum_char += 13
        elif c == 'N':
            sum_char += 14
        elif c == 'O':
            sum_char += 15
        elif c == 'P':
            sum_char += 16
        elif c == 'Q':
            sum_char += 17
        elif c == 'R':
            sum_char += 18
        elif c == 'S':
            sum_char += 19
        elif c == 'T':
            sum_char += 20
        elif c == 'U':
            sum_char += 21
        elif c == 'V':
            sum_char += 22
        elif c == 'W':
            sum_char += 23
        elif c == 'X':
            sum_char += 24
        elif c == 'Y':
            sum_char += 25
        elif c == 'Z':
            sum_char += 26

    #print(sum_char)
    name_score = name_index * sum_char
    #print(name_score)
    name_index += 1
    print(name_index)
    total += name_score

print(total)