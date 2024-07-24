import time


def print_with_delay(text, delay=2):
    print(text)
    time.sleep(delay)


def go_north(points):
    print_with_delay(
        "You have reached a huge tree. You need to choose another direction."
    )
    points -= 1  # Decrease points by one
    print_with_delay(f"Your current points: {points}")
    return points


def go_east(points):
    print_with_delay(
        "You have arrived at a stream. Looks like you are on the right path!"
    )
    print_with_delay("Congratulations, you have successfully escaped the forest!")
    points += 2  # Increase points by two
    print_with_delay(f"Your current points: {points}")
    return points


def go_south(points):
    print_with_delay(
        "You encountered an angry gorilla. You need to escape to another direction."
    )
    points -= 1  # Decrease points by one
    print_with_delay(f"Your current points: {points}")
    return points


def go_west(points):
    print_with_delay("You have reached a swamp. This doesn't seem to be the right way.")
    points -= 1  # Decrease points by one
    print_with_delay(f"Your current points: {points}")
    return points


def climb_tree(points):
    print_with_delay("You decided to climb the huge tree for a better view...")
    points += 1  # Increase points by one
    print_with_delay(f"Your current points: {points}")
    return points


def explore_cave(points):
    print_with_delay("You found an entrance to a dark cave. Do you want to explore it?")
    choice = (
        input("Type 'yes' if you want to enter, 'no' if you don't: ").strip().lower()
    )
    if choice == "yes":
        print_with_delay("You entered the cave and encountered a strange monster!")
        points -= 2  # Decrease points by two
        print_with_delay(f"Your current points: {points}")
    else:
        print_with_delay(
            "You decided not to explore the cave and continued your journey."
        )
        print_with_delay(f"Your current points: {points}")
    return points


def find_treasure(points):
    print_with_delay(
        "You found a treasure buried in the soil! Just as you expected, you gained 5 additional points."
    )
    points += 5  # Increase points by five
    print_with_delay(f"Your current points: {points}")
    return points


def undo_last_move(points):
    print_with_delay("Undoing to the previous step.")
    print_with_delay(f"Your current points: {points}")
    return points


def choose_path(points):
    print("\n1. Go north (decrease points by one)")
    print("2. Go east (increase points by two)")
    print("3. Go south (decrease points by one)")
    print("4. Go west (decrease points by one)")
    print("5. Climb the tree (increase points by one)")
    print("6. Explore the cave (may decrease points by two)")
    print("7. Find treasure (increase points by five)")
    print("8. Undo last move")

    choice = input("Choose the direction number you want to go to: ")

    if choice == "1":
        return go_north(points)
    elif choice == "2":
        return go_east(points)
    elif choice == "3":
        return go_south(points)
    elif choice == "4":
        return go_west(points)
    elif choice == "5":
        return climb_tree(points)
    elif choice == "6":
        return explore_cave(points)
    elif choice == "7":
        return find_treasure(points)
    elif choice == "8":
        return undo_last_move(points)
    else:
        print("\nPlease choose a valid number (1, 2, 3, 4, 5, 6, 7, or 8)")
        return choose_path(points)


def forest_escape_game():
    print(
        "You are stuck in the forest. You must make some right decisions to safely escape."
    )
    print("Choose the option that seems appropriate:")

    print("\n1. Direction towards the dense forest")
    print("2. Direction towards the valley")
    print("3. Direction towards the deserted road")

    first_choice = input("Choose the first direction number: ")
    points = 0

    if first_choice == "1":
        print("\nYou are walking on a path in the dense forest...")
        points = choose_path(points)
    elif first_choice == "2":
        print("\nYou are following the path of the valley...")
        points = choose_path(points)
    elif first_choice == "3":
        print("\nYou are walking the deserted road...")
        points = choose_path(points)
    else:
        print("\nPlease choose a valid number (1, 2, or 3)")
        forest_escape_game()

    # Check win or lose condition
    if points >= 3:
        print(
            "\nCongratulations! You won the game! You managed to escape from the forest with points:",
            points,
        )
    else:
        print(
            "\nUnfortunately, you failed to escape from the forest. Final points:",
            points,
        )


def play_forest_escape_game():
    while True:
        forest_escape_game()
        print("\nDo you want to play again?")
        play_again = (
            input("Type 'yes' if you want to play again, or 'no' if you don't: ")
            .strip()
            .lower()
        )
        if play_again != "yes":
            print("\nThank you for playing the game!")
            break
        print("\nLet's start again!")


# Start the game
play_forest_escape_game()
