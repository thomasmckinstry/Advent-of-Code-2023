# python-draft.py

# Advent of Code 2023
# Draft File

numbers_dict = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}

def parseFile(filename):
    with open (filename, "r") as input_file:
        input_string = input_file.read()

    return input_string

input_string = parseFile("day1 - input.txt")
input_arr = input_string.splitlines()

def part1(input_arr):
    sum = 0
    for i in input_arr:
        nums = i.strip("abcdefghijklmnopqrstuvwxyz")
        newnum = nums[0] + nums[-1]
        sum += int(newnum)
    print(sum)

def part2(input_arr):
    sum = 0
    str_nums = list(numbers_dict.keys())
    int_nums = list(numbers_dict.values())

    for i in input_arr:
        print(i, "test string")
        higher_index = -1
        lower_index = -1

        lower_number = ""
        higher_number = ""

        for j in range(9):
            #print("checking", int_nums[j])
            str_index = i.find(str_nums[j])
            int_index = i.find(int_nums[j])
            #print("lower indexes", str_index, int_index)

            current_num = j + 1

            if (str_index >= 0 and int_index >= 0):
                if (str_index < lower_index or lower_index < 0):
                    lower_index = str_index
                    lower_number = str(current_num)
                
                if (int_index < lower_index):
                    lower_index = int_index
                    lower_number = str(current_num)

            elif(str_index >= 0):
                if (str_index < lower_index or lower_index < 0):
                    lower_index = str_index
                    lower_number = str(current_num)
            
            elif (int_index >= 0):
                if (int_index < lower_index or lower_index < 0):
                    lower_index = int_index
                    lower_number = str(current_num)

            #print(lower_number, lower_index)

            str_index = i.rfind(str_nums[j])
            int_index = i.rfind(int_nums[j])
            #print("higher indexes", str_index, int_index)

            if (str_index > int_index and str_index > higher_index):
                higher_index = str_index
                higher_number = str(current_num)
                
            if (str_index < int_index and int_index > higher_index):
                higher_index = int_index
                higher_number = str(current_num) 

            #print("results", lower_number, higher_number)
            
        newnum = lower_number + higher_number
        #print(newnum)
        sum += int(newnum)
        
    print(sum)  

#part1(input_arr)
part2(input_arr)

""" test_input = "two1nine\neightwothree\nabcone2threexyz\nxtwone3four\n4nineeightseven2\nzoneight234\n7pqrstsixteen".splitlines()
part2(test_input)

test_input = "45five7fivegpzhcfbbfiveqhnhhzdqtnltgnkrxz".splitlines()
part2(test_input)

test_input = "eighthree".splitlines()
part2(test_input)

test_input = "sevenine".splitlines()
part2(test_input)

test_input = "eightwothree".splitlines()
part2(test_input)

test_input = "6ninefourgvztqcztk4sevensix1".splitlines()
part2(test_input)

test_input = "2lrlzvdpklf4five8two4".splitlines()
part2(test_input) """