def main():
    main_counter = True
    while main_counter:
        row_number_counter = True
        while row_number_counter:
            row_number = int(input("row number:"))
            if row_number < 4 or row_number > 8:
                row_number_counter = True
                print("please write a valid row number")
            else:
                row_number_counter = False
        input_loop = False
        player1 = input("player 1:")#x   they are the players
        player2 = input("player 2:")#y
        #player1_count = 0
        #player2_count = 0
        list_of_ABC = ["A", "B", "C", "D", "E", "F", "G", "H"]  # we use this one to help us make the table
        print("   ", end=" ")
        for i in range(row_number):
            print(f"{list_of_ABC[i]:<3}", end=" ")
        print()
        print("  ", end="")
        print("----" * row_number, end="")
        print("-")
        real_list = [[" "] * row_number for y in range(row_number)]
        for a in range(1, row_number + 1):
            if a == 1:
                for b in range(0, row_number):
                    real_list[0][b] = f"| {player2} "

            if a == row_number:
                for y in range(0, row_number):
                    real_list[-1][y] = f"| {player1} "

            elif a != 1 and a != row_number:
                for c in range(0, row_number):
                    real_list[a - 1][c] = "|   "

            print(f"{a} ", end="")
            for f in range(row_number):
                print(real_list[a - 1][f], end="")
            print("|", end="")
            print(f" {a}")
            print("  ", end="")
            print("----" * row_number, end="")
            print("-")

        print("   ", end=" ")
        for i in range(row_number):
            print(f"{list_of_ABC[i]:<3}", end=" ")
        print()

        counter_for_player = 0
        end_counter = True
        old_real_list = []
        counter_2 = 0

        while end_counter:      # after we made the first table now we can start to play
            player1_count = 0     # end counter and the others help us quit or keep going
            player2_count = 0       # if there is a mistaken input they will take the input again
            removed_stone = " "
            counter_for_player += 1
            counter_if_there_is_block = True
            while counter_if_there_is_block:

                if counter_for_player % 2 == 1:
                    position_for_now_and_later = input(
                        f"{player1}, please enter the position of your own stone you want to move and the target position:")
                    opponents_stone = player2
                elif counter_for_player % 2 == 0:
                    position_for_now_and_later = input(
                        f"{player2}, please enter the position of your own stone you want to move and the target position:")
                    opponents_stone = player1

                take_first_place = position_for_now_and_later[0:2]
                take_last_place = position_for_now_and_later[3:]
                take_first_place = take_first_place.upper()
                take_last_place = take_last_place.upper()

                if position_for_now_and_later[0].isnumeric() == False or position_for_now_and_later[3].isnumeric() == False:
                    print("firts put the number than a character in alphabet like 4C . now try again")
                    counter_if_there_is_block = True
                else:

                    if int(take_first_place[0]) > row_number:
                        print("please enter a valid start")
                        counter_if_there_is_block = True

                    else:
                        if real_list[int(take_first_place[0])-1][list_of_ABC.index(take_first_place[1])] == "|   " or real_list[int(take_first_place[0])-1][list_of_ABC.index(take_first_place[1])] == f"| {opponents_stone} ":
                            print("your current location is wrong")
                            counter_if_there_is_block = True

                        else:

                            if take_first_place[1] == take_last_place[1] and take_first_place[0] != take_last_place[0]:
                                if int(take_first_place[0]) > int(take_last_place[0]):
                                    for b in range(int(take_last_place[0]), int(take_first_place[0])):
                                        if real_list[b-1][list_of_ABC.index(take_first_place[1])] != "|   ":
                                            counter_if_there_is_block = True
                                            print("The way that you want to go is blocked.Try again!")
                                            break
                                        else:
                                            counter_if_there_is_block = False
                                elif int(take_first_place[0]) < int(take_last_place[0]):
                                    for c in range(int(take_first_place[0]), int(take_last_place[0])):
                                        if real_list[c][list_of_ABC.index(take_first_place[1])] != "|   ":
                                            counter_if_there_is_block = True
                                            print("The way that you want to go is blocked.Try again!")
                                            break
                                        else:
                                            counter_if_there_is_block = False
                            if take_first_place[1] != take_last_place[1] and take_first_place[0] == take_last_place[0]:
                                if list_of_ABC.index(take_first_place[1]) < list_of_ABC.index(take_last_place[1]):
                                    for d in range(int(list_of_ABC.index(take_first_place[1]))+1, int(list_of_ABC.index(take_last_place[1]))+1):
                                        if real_list[int(take_first_place[0])-1][d] != "|   ":
                                            counter_if_there_is_block = True
                                            print("The way that you want to go is blocked.Try again!")
                                            break
                                        else:
                                            counter_if_there_is_block = False
                                elif list_of_ABC.index(take_first_place[1]) > list_of_ABC.index(take_last_place[1]):
                                    for s in range(int(list_of_ABC.index(take_last_place[1])), int(list_of_ABC.index(take_first_place[1]))):
                                        if real_list[int(take_first_place[0])-1][s] != "|   ":
                                            counter_if_there_is_block = True
                                            print("The way that you want to go is blocked.Try again!")
                                            break
                                        else:
                                            counter_if_there_is_block = False


            counter_2 +=1
            list_of_ABC = ["A", "B", "C", "D", "E", "F", "G", "H"]
            print("   ", end=" ")
            for i in range(row_number):
                print(f"{list_of_ABC[i]:<3}", end=" ")
            print()
            print("  ", end="")
            print("----" * row_number, end="")
            print("-")
            real_list = [[" "] * row_number for y in range(row_number)]
            for a in range(1, row_number + 1):

                if a == 1:
                    for b in range(0, row_number):
                        real_list[0][b] = f"| {player2} "

                if a == row_number:
                    for y in range(0, row_number):
                        real_list[-1][y] = f"| {player1} "

                elif a != 1 and a != row_number:
                    for c in range(0, row_number):
                        real_list[a - 1][c] = "|   "
            if counter_2 > 1:
                real_list = old_real_list
            for a in range(1, row_number + 1):
                if counter_for_player % 2 == 1: # this is for the first player after that there is also one for the second player
                    if a == int(take_first_place[0]):
                        first_index = list_of_ABC.index(take_first_place[1])
                        real_list[a - 1][first_index] = "|   "
                    if a == int(take_last_place[0]):
                        second_index = list_of_ABC.index(take_last_place[1])
                        real_list[a - 1][second_index] = f"| {player1} "
                    if take_first_place[1] != take_last_place[1] and take_first_place[0] == take_last_place[0]: # this line looks for the horizontal moves
                        # they look for the ones that are not in corners
                        if int(take_last_place[0])-3 >= 0:
                            if real_list[int(take_last_place[0])-2][list_of_ABC.index(take_last_place[1])] == f"| {player2} " and real_list[int(take_last_place[0])-3][list_of_ABC.index(take_last_place[1])] == f"| {player1} ":
                                real_list[int(take_last_place[0]) - 2][list_of_ABC.index(take_last_place[1])] = "|   "
                                removed_stone = f"{int(take_last_place[0])-1}"+f"{take_last_place[1]}"
                        if int(take_last_place[0])+1 < row_number:
                            if real_list[int(take_last_place[0])][list_of_ABC.index(take_last_place[1])] == f"| {player2} " and real_list[int(take_last_place[0])+1][list_of_ABC.index(take_last_place[1])] == f"| {player1} ":
                                real_list[int(take_last_place[0])][list_of_ABC.index(take_last_place[1])] = "|   "
                                removed_stone = f"{int(take_last_place[0])+1}"+f"{take_last_place[1]}"
                        if list_of_ABC.index(take_last_place[1])+2 < row_number:
                            if real_list[int(take_last_place[0])-1][list_of_ABC.index(take_last_place[1])+1] == f"| {player2} " and real_list[int(take_last_place[0])-1][list_of_ABC.index(take_last_place[1])+2] == f"| {player1} ":
                                real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) + 1] = "|   "
                                removed_stone = f"{take_last_place[0]}"+f"{list_of_ABC[list_of_ABC.index(take_last_place[1])+1]}"
                        if list_of_ABC.index(take_last_place[1])-2 >= 0:
                            if real_list[int(take_last_place[0])-1][list_of_ABC.index(take_last_place[1])-1] == f"| {player2} " and real_list[int(take_last_place[0])-1][list_of_ABC.index(take_last_place[1])-2] == f"| {player1} ":
                                real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) - 1] = "|   "
                                removed_stone = f"{take_last_place[0]}"+f"{list_of_ABC[list_of_ABC.index(take_last_place[1])-1]}"

                        # those are looking for the corners
                        if real_list[0][0] == f"| {player2} " and real_list[0][1] == f"| {player1} "  and int(take_last_place[0]) == 2 and list_of_ABC.index(take_last_place[1]) == 0:
                            real_list[0][0] = "|   "
                            removed_stone = "1A"
                        if real_list[0][0] == f"| {player2} " and real_list[1][0] == f"| {player1} "  and int(take_last_place[0]) == 1 and list_of_ABC.index(take_last_place[1]) == 1:
                            real_list[0][0] = "|   "
                            removed_stone = "1A"

                        if real_list[0][-1] == f"| {player2} " and real_list[0][-2] ==  f"| {player1} "  and int(take_last_place[0]) == 2 and list_of_ABC.index(take_last_place[1]) == row_number-1:
                            real_list[0][-1] = "|   "
                            removed_stone = "1" + f"{list_of_ABC[row_number - 1]}"
                        if real_list[0][-1] == f"| {player2} " and real_list[1][-1] == f"| {player1} "  and int(take_last_place[0]) == 1 and list_of_ABC.index(take_last_place[1]) == row_number-2:
                            real_list[0][-1] = "|   "
                            removed_stone ="1"+f"{list_of_ABC[row_number-1]}"

                        if real_list[-1][0] == f"| {player2} " and real_list[-2][0] == f"| {player1} "  and int(take_last_place[0]) == row_number and list_of_ABC.index(take_last_place[1]) == 1:
                            real_list[-1][0] = "|   "
                            removed_stone = f"{row_number}" + "A"
                        if real_list[-1][0] == f"| {player2} " and real_list[-1][1] == f"| {player1} "  and int(take_last_place[0]) == row_number-1 and list_of_ABC.index(take_last_place[1]) == 0:
                            real_list[-1][0] = "|   "
                            removed_stone = f"{row_number}"+"A"

                        if real_list[-1][-1] == f"| {player2} " and real_list[-2][-1] == f"| {player1} "  and int(take_last_place[0]) == row_number and list_of_ABC.index(take_last_place[1]) == row_number-2:
                            real_list[-1][-1] = "|   "
                            removed_stone = f"{row_number}"+f"{list_of_ABC[row_number-1]}"
                        if real_list[-1][-1] == f"| {player2} " and real_list[-1][-2]== f"| {player1} "  and int(take_last_place[0]) == row_number-1 and list_of_ABC.index(take_last_place[1]) == row_number-1:
                            real_list[-1][-1] = "|   "
                            removed_stone = f"{row_number}"+f"{list_of_ABC[row_number-1]}"
                    if take_first_place[1] == take_last_place[1] and take_first_place[0] != take_last_place[0]:  # this line looks for the vertical moves
                        if list_of_ABC.index(take_last_place[1])-2 >= 0:  # vertical moves ( not a corner)
                            if real_list[int(take_last_place[0])-1][list_of_ABC.index(take_last_place[1])-1] == f"| {player2} " and real_list[int(take_last_place[0])-1][list_of_ABC.index(take_last_place[1])-2] == f"| {player1} ":
                                real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) - 1] = "|   "
                                removed_stone = f"{int(take_last_place[0])}"+f"{list_of_ABC[list_of_ABC.index(take_last_place[1])-1]}"
                        if list_of_ABC.index(take_last_place[1])+2 < row_number:
                            if real_list[int(take_last_place[0])-1][list_of_ABC.index(take_last_place[1])+1] == f"| {player2} " and real_list[int(take_last_place[0])-1][list_of_ABC.index(take_last_place[1])+2] ==  f"| {player1} ":
                                real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) + 1] = "|   "
                                removed_stone = f"{int(take_last_place[0])}"+f"{list_of_ABC[list_of_ABC.index(take_last_place[1])+1]}"
                        if int(take_last_place[0]) - 3 >= 0:
                            if real_list[int(take_last_place[0])-2][list_of_ABC.index(take_last_place[1])] == f"| {player2} " and real_list[int(take_last_place[0])-3][list_of_ABC.index(take_last_place[1])] == f"| {player1} ":
                                real_list[int(take_last_place[0]) - 2][list_of_ABC.index(take_last_place[1])] = "|   "
                                removed_stone = f"{int(take_last_place[0])-1}"+f"{list_of_ABC[list_of_ABC.index(take_last_place[1])]}"
                        if int(take_last_place[0])+1 < row_number:
                            if real_list[int(take_last_place[0])][list_of_ABC.index(take_last_place[1])] == f"| {player2} " and real_list[int(take_last_place[0])+1][list_of_ABC.index(take_last_place[1])] ==  f"| {player1} ":
                                real_list[int(take_last_place[0])][list_of_ABC.index(take_last_place[1])] = "|   "
                                removed_stone = f"{int(take_last_place[0])+1}"+f"{list_of_ABC[list_of_ABC.index(take_last_place[1])]}"
                        # corner lines for vertical moves
                        if real_list[0][0] == f"| {player2} " and real_list[0][1] == f"| {player1} " and int(
                                take_last_place[0]) == 2 and list_of_ABC.index(take_last_place[1]) == 0:
                            real_list[0][0] = "|   "
                            removed_stone = "1A"
                        if real_list[0][0] == f"| {player2} " and real_list[1][0] == f"| {player1} " and int(
                                take_last_place[0]) == 1 and list_of_ABC.index(take_last_place[1]) == 1:
                            real_list[0][0] = "|   "
                            removed_stone = "1A"

                        if real_list[0][-1] == f"| {player2} " and real_list[0][-2] == f"| {player1} " and int(
                                take_last_place[0]) == 2 and list_of_ABC.index(take_last_place[1]) == row_number - 1:
                            real_list[0][-1] = "|   "
                            removed_stone = "1" + f"{list_of_ABC[row_number - 1]}"
                        if real_list[0][-1] == f"| {player2} " and real_list[1][-1] == f"| {player1} " and int(
                                take_last_place[0]) == 1 and list_of_ABC.index(take_last_place[1]) == row_number - 2:
                            real_list[0][-1] = "|   "
                            removed_stone = "1" + f"{list_of_ABC[row_number - 1]}"

                        if real_list[-1][0] == f"| {player2} " and real_list[-2][0] == f"| {player1} " and int(
                                take_last_place[0]) == row_number and list_of_ABC.index(take_last_place[1]) == 1:
                            real_list[-1][0] = "|   "
                            removed_stone = f"{row_number}" + "A"
                        if real_list[-1][0] == f"| {player2} " and real_list[-1][1] == f"| {player1} " and int(
                                take_last_place[0]) == row_number - 1 and list_of_ABC.index(take_last_place[1]) == 0:
                            real_list[-1][0] = "|   "
                            removed_stone = f"{row_number}" + "A"

                        if real_list[-1][-1] == f"| {player2} " and real_list[-2][-1] == f"| {player1} " and int(
                                take_last_place[0]) == row_number and list_of_ABC.index(take_last_place[1]) == row_number - 2:
                            real_list[-1][-1] = "|   "
                            removed_stone = f"{row_number}" + f"{list_of_ABC[row_number - 1]}"
                        if real_list[-1][-1] == f"| {player2} " and real_list[-1][-2] == f"| {player1} " and int(
                                take_last_place[0]) == row_number - 1 and list_of_ABC.index(
                                take_last_place[1]) == row_number - 1:
                            real_list[-1][-1] = "|   "
                            removed_stone = f"{row_number}" + f"{list_of_ABC[row_number - 1]}"


                # and this is the same one for the second player
                elif counter_for_player % 2 == 0:
                    if a == int(take_first_place[0]):
                        first_index = list_of_ABC.index(take_first_place[1])
                        real_list[a - 1][first_index] = "|   "
                    if a == int(take_last_place[0]):
                        second_index = list_of_ABC.index(take_last_place[1])
                        real_list[a - 1][second_index] = f"| {player1} "
                    if a == int(take_first_place[0]):
                        first_index = list_of_ABC.index(take_first_place[1])
                        real_list[a - 1][first_index] = "|   "
                    if a == int(take_last_place[0]):
                        second_index = list_of_ABC.index(take_last_place[1])
                        real_list[a - 1][second_index] = f"| {player2} "
                    if take_first_place[1] != take_last_place[1] and take_first_place[0] == take_last_place[0]:
                        if int(take_last_place[0]) - 3 >= 0:
                            if real_list[int(take_last_place[0]) - 2][list_of_ABC.index(take_last_place[1])] == f"| {player1} " and real_list[int(take_last_place[0]) - 3][list_of_ABC.index(take_last_place[1])] == f"| {player2} ":
                                real_list[int(take_last_place[0]) - 2][list_of_ABC.index(take_last_place[1])] = "|   "
                                removed_stone = f"{int(take_last_place[0]) - 1}" + f"{take_last_place[1]}"
                        if int(take_last_place[0]) + 1 < row_number:
                            if real_list[int(take_last_place[0])][list_of_ABC.index(take_last_place[1])] == f"| {player1} " and real_list[int(take_last_place[0]) + 1][list_of_ABC.index(take_last_place[1])] == f"| {player2} ":
                                real_list[int(take_last_place[0])][list_of_ABC.index(take_last_place[1])] = "|   "
                                removed_stone = f"{int(take_last_place[0]) + 1}" + f"{take_last_place[1]}"
                        if list_of_ABC.index(take_last_place[1]) + 2 < row_number:
                            if real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) + 1] == f"| {player1} " and real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) + 2] == f"| {player2} ":
                                real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) + 1] = "|   "
                                removed_stone = f"{take_last_place[0]}" + f"{list_of_ABC[list_of_ABC.index(take_last_place[1]) + 1]}"
                        if list_of_ABC.index(take_last_place[1]) - 2 >= 0:
                            if real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) - 1] == f"| {player1} " and real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) - 2] == f"| {player2} ":
                                real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) - 1] = "|   "
                                removed_stone = f"{take_last_place[0]}" + f"{list_of_ABC[list_of_ABC.index(take_last_place[1]) - 1]}"

                        if real_list[0][0] == f"| {player1} " and real_list[0][1] == f"| {player2} " and int(take_last_place[0]) == 2 and list_of_ABC.index(take_last_place[1]) == 0:
                            real_list[0][0] = "|   "
                            removed_stone = "1A"
                        if real_list[0][0] == f"| {player1} " and real_list[1][0] == f"| {player2} " and int(take_last_place[0]) == 1 and list_of_ABC.index(take_last_place[1]) == 1:
                            real_list[0][0] = "|   "
                            removed_stone = "1A"

                        if real_list[0][-1] == f"| {player1} " and real_list[0][-2] == f"| {player2} " and int(take_last_place[0]) == 2 and list_of_ABC.index(take_last_place[1]) == row_number - 1:
                            real_list[0][-1] = "|   "
                            removed_stone = "1" + f"{list_of_ABC[row_number - 1]}"
                        if real_list[0][-1] == f"| {player1} " and real_list[1][-1] == f"| {player2} " and int(take_last_place[0]) == 1 and list_of_ABC.index(take_last_place[1]) == row_number - 2:
                            real_list[0][-1] = "|   "
                            removed_stone = "1" + f"{list_of_ABC[row_number - 1]}"

                        if real_list[-1][0] == f"| {player1} " and real_list[-2][0] == f"| {player2} " and int(take_last_place[0]) == row_number and list_of_ABC.index(take_last_place[1]) == 1:
                            real_list[-1][0] = "|   "
                            removed_stone = f"{row_number}" + "A"
                        if real_list[-1][0] == f"| {player1} " and real_list[-1][1] == f"| {player2} " and int(take_last_place[0]) == row_number - 1 and list_of_ABC.index(take_last_place[1]) == 0:
                            real_list[-1][0] = "|   "
                            removed_stone = f"{row_number}" + "A"

                        if real_list[-1][-1] == f"| {player1} " and real_list[-2][-1] == f"| {player2} " and int(take_last_place[0]) == row_number and list_of_ABC.index(take_last_place[1]) == row_number - 2:
                            real_list[-1][-1] = "|   "
                            removed_stone = f"{row_number}" + f"{list_of_ABC[row_number - 1]}"
                        if real_list[-1][-1] == f"| {player1} " and real_list[-1][-2] == f"| {player2} " and int(take_last_place[0]) == row_number - 1 and list_of_ABC.index(take_last_place[1]) == row_number - 1:
                            real_list[-1][-1] = "|   "
                            removed_stone = f"{row_number}" + f"{list_of_ABC[row_number - 1]}"
                    if take_first_place[1] == take_last_place[1] and take_first_place[0] != take_last_place[0]:
                        if list_of_ABC.index(take_last_place[1]) - 2 >= 0:
                            if real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) - 1] == f"| {player1} " and real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) - 2] == f"| {player2} ":
                                real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) - 1] = "|   "
                                removed_stone = f"{int(take_last_place[0])}" + f"{list_of_ABC[list_of_ABC.index(take_last_place[1]) - 1]}"
                        if list_of_ABC.index(take_last_place[1]) + 2 < row_number:
                            if real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) + 1] == f"| {player1} " and real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) + 2] == f"| {player2} ":
                                real_list[int(take_last_place[0]) - 1][list_of_ABC.index(take_last_place[1]) + 1] = "|   "
                                removed_stone = f"{int(take_last_place[0])}" + f"{list_of_ABC[list_of_ABC.index(take_last_place[1]) + 1]}"
                        if int(take_last_place[0]) - 3 >= 0:
                            if real_list[int(take_last_place[0]) - 2][list_of_ABC.index(take_last_place[1])] == f"| {player1} " and real_list[int(take_last_place[0]) - 3][list_of_ABC.index(take_last_place[1])] == f"| {player2} ":
                                real_list[int(take_last_place[0]) - 2][list_of_ABC.index(take_last_place[1])] = "|   "
                                removed_stone = f"{int(take_last_place[0]) - 1}" + f"{list_of_ABC[list_of_ABC.index(take_last_place[1])]}"
                        if int(take_last_place[0]) + 1 < row_number:
                            if real_list[int(take_last_place[0])][list_of_ABC.index(take_last_place[1])] == f"| {player1} " and real_list[int(take_last_place[0]) + 1][list_of_ABC.index(take_last_place[1])] == f"| {player2} ":
                                real_list[int(take_last_place[0])][list_of_ABC.index(take_last_place[1])] = "|   "
                                removed_stone = f"{int(take_last_place[0]) + 1}" + f"{list_of_ABC[list_of_ABC.index(take_last_place[1])]}"

                        if real_list[0][0] == f"| {player1} " and real_list[0][1] == f"| {player2} " and int(take_last_place[0]) == 2 and list_of_ABC.index(take_last_place[1]) == 0:
                            real_list[0][0] = "|   "
                            removed_stone = "1A"
                        if real_list[0][0] == f"| {player1} " and real_list[1][0] == f"| {player2} " and int(take_last_place[0]) == 1 and list_of_ABC.index(take_last_place[1]) == 1:
                            real_list[0][0] = "|   "
                            removed_stone = "1A"

                        if real_list[0][-1] == f"| {player1} " and real_list[0][-2] == f"| {player2} " and int(take_last_place[0]) == 2 and list_of_ABC.index(take_last_place[1]) == row_number - 1:
                            real_list[0][-1] = "|   "
                            removed_stone = "1" + f"{list_of_ABC[row_number - 1]}"
                        if real_list[0][-1] == f"| {player1} " and real_list[1][-1] == f"| {player2} " and int(take_last_place[0]) == 1 and list_of_ABC.index(take_last_place[1]) == row_number - 2:
                            real_list[0][-1] = "|   "
                            removed_stone = "1" + f"{list_of_ABC[row_number - 1]}"

                        if real_list[-1][0] == f"| {player1} " and real_list[-2][0] == f"| {player2} " and int(take_last_place[0]) == row_number and list_of_ABC.index(take_last_place[1]) == 1:
                            real_list[-1][0] = "|   "
                            removed_stone = f"{row_number}" + "A"
                        if real_list[-1][0] == f"| {player1} " and real_list[-1][1] == f"| {player2} " and int(take_last_place[0]) == row_number - 1 and list_of_ABC.index(take_last_place[1]) == 0:
                            real_list[-1][0] = "|   "
                            removed_stone = f"{row_number}" + "A"

                        if real_list[-1][-1] == f"| {player1} " and real_list[-2][-1] == f"| {player2} " and int(take_last_place[0]) == row_number and list_of_ABC.index(take_last_place[1]) == row_number - 2:
                            real_list[-1][-1] = "|   "
                            removed_stone = f"{row_number}" + f"{list_of_ABC[row_number - 1]}"
                        if real_list[-1][-1] == f"| {player1} " and real_list[-1][-2] == f"| {player2} " and int(take_last_place[0]) == row_number - 1 and list_of_ABC.index(take_last_place[1]) == row_number - 1:
                            real_list[-1][-1] = "|   "
                            removed_stone = f"{row_number}" + f"{list_of_ABC[row_number - 1]}"

                print(f"{a} ", end="")
                for f in range(row_number):
                    print(real_list[a - 1][f], end="")
                print("|", end="")
                print(f" {a}")
                print("  ", end="")
                print("----" * row_number, end="")
                print("-")

            print("   ", end=" ")
            for i in range(row_number):
                print(f"{list_of_ABC[i]:<3}", end=" ")
            print()
            old_real_list = real_list
            if removed_stone != " ":
                print(f"the stone at position {removed_stone} is locked and removed")
            for z in range(row_number):
                for v in range(row_number):
                    if real_list[z][v] == f"| {player1} ":
                        player1_count += 1
                    if real_list[z][v] ==  f"| {player2} ":
                        player2_count +=1
            if player2_count < 2:
                print(f"{player1} has won the game")
                input_loop = True

            elif player1_count < 2:
                print(f"{player2} has won the game")
                input_loop = True
            # after the if lines we just check for who won and who lost
            # than we ask if they want to play again
            while input_loop :
                look_to_end_counter = input("do you want to play again y/Y for yes and n/N for no:")
                if look_to_end_counter == "y" or look_to_end_counter == "Y":
                    end_counter = False
                    input_loop = False
                    main_counter = True
                elif look_to_end_counter == "n" or look_to_end_counter == "N":
                    end_counter = False
                    input_loop = False
                    main_counter = False
                else:
                    print("incorrect data try again")
                    input_loop = True
main()
