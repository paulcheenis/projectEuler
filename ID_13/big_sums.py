input_file = open("input.txt", "r")
split_ten_array = []
big_array = []


for i in input_file:
    #print(i)
    split_10 = i[-11:]
    big_array.append(int(i))
    #print(split_10)
    split_ten_array.append(int(split_10))

#print(split_ten_array)

#sum = 0

#for j in split_ten_array:
    #sum = sum + j

big_sum = 0

for k in big_array:
    big_sum = big_sum + k

print(big_sum)