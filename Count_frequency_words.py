def freq_words():
    str_input = input("Enter a string: ")
    li = str_input.split()
    d = {}
    
    for i in li:
        if i not in d:
            d[i] = 0
        d[i] = d[i] + 1
    
    print(d)

freq_words()
