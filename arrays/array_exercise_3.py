max_num = int(input("Enter max number: "))

odd_numbers = list(filter(lambda x: x%2 ==1 , range(1,max_num)))
print(odd_numbers)