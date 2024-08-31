def common_letters():
    str1 = input("Enter a first string: ")
    str2 = input("Enter a second string: ")
    s1 = set(str1)
    s2 = set(str2)
    
    common = s1 & s2
    return list(common)
print(common_letters())