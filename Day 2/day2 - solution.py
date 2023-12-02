# python-draft.py

# Advent of Code 2023
# Draft File

# Puts the whole input into a single string
def parseFile(filename):
    with open (filename, "r") as input_file:
        input_string = input_file.read()

    return input_string

input_string = parseFile("day2 - input.txt")
input_arr = input_string.splitlines() # Divides the input into an array

def part1(input_arr):
    sum = 0
    blocks_dict = {"red" : 12, "green" : 13, "blue" : 14} #Blocks in the bag

    for i in input_arr:

        new_i = i.replace(":", ";")
        nums_arr = new_i[4:].split(";") #Removes the Game prefix, splits the input into Game Number, Game Results
        game_num = nums_arr[0]

        valid_game = True

        for j in range(len(nums_arr)):
            nums_arr[j] = nums_arr[j].split(",") #Splits the Game Results into arrays (Num Color)

        for k in range(1, len(nums_arr)): #Iterate through each entry (First is game number)
            for entry in nums_arr[k]: #Iterate through the game array

                space_index = entry.rfind(" ") + 1 #The divider between the number and color

                picked_num = int(entry[1:space_index])
                blocks_num = blocks_dict[entry[space_index: len(entry)]]

                if (picked_num > blocks_num): #Checks blocks claimed against number of blocks
                    valid_game = False

        if (valid_game):
            sum += int(game_num)


        #print("DEBUG", nums_arr)
    print(sum)

def part2(input_arr):
    sum = 0

    for i in input_arr:

        blocks_dict = {"red" : 0, "green" : 0, "blue" : 0} #Reset the block count each game

        new_i = i.replace(":", ";")
        nums_arr = new_i[4:].split(";") #Same as part 1
        game_num = nums_arr[0]

        for j in range(len(nums_arr)):
            nums_arr[j] = nums_arr[j].split(",") #Same as part 1

        for k in range(1, len(nums_arr)):
            for entry in nums_arr[k]:
                space_index = entry.rfind(" ") + 1
                picked_num = int(entry[1:space_index])
                blocks_num = blocks_dict[entry[space_index: len(entry)]]

                if (picked_num > blocks_num):
                    blocks_dict[entry[space_index: len(entry)]] = picked_num #Set number of blocks if picked is greater than recorded

        blocks_power = (blocks_dict["red"] * blocks_dict["blue"] * blocks_dict["green"])
        sum += blocks_power
        #print("DEBUG", sum)
    print(sum)
                    

part1(input_arr)

part2(input_arr)

#test_input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
#part1(test_input.splitlines())

#test_input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\nGame 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\nGame 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\nGame 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\nGame 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
#part2(test_input.splitlines())