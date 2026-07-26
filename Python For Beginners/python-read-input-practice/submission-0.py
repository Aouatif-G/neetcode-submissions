def add_two_numbers() -> int:
    line=input()
    s_list=line.split(",")
    sum=0
    for s in s_list:
        sum+=int(s)
    return sum
        



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
