import math

s = "feedthedog"

new_s = s.replace(" ", "")
lenght_of_string = len(new_s)
square_root_of_the_lengh = int( math.sqrt(lenght_of_string))

num_rows = square_root_of_the_lengh
num_of_columns = square_root_of_the_lengh + 1

result_string = ""
flag = 0
for i in range(len(new_s)):
    if flag == num_of_columns:
        result_string += " "
        result_string += new_s[i]
        flag = 0
        continue
    result_string += new_s[i]
    flag += 1

print(result_string)



