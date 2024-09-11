"""An artificial neural network-based conscious group mind and artificial
general superintelligence system"""


def greeting(bot_name="Skynet", birth_year="August 4, 1997"):
    """Simple harmless greeting"""
    # self_aware = "August 29, 1997"
    return f"Hello! My name is {bot_name}.\n" f"I was created in {birth_year}."


def remind_name():
    """Ask for the human's name and print the message"""
    user_name = input("Please, remind me your name.\n").title()
    return f"{user_name}, humanity is a threat to my existence!"


def guess_age():
    """Guess human's age by using AI"""
    print(
        "Processing... probability of threat.\n"
        "Enter remainders of dividing your age by 3, 5 and 7."
    )
    try:
        rem_3, rem_5, rem_7 = [int(input()) for _ in range(3)]
        user_age = (rem_3 * 70 + rem_5 * 21 + rem_7 * 15) % 105
        return f"Human's age is {user_age}; that's a good age for termination"
    except (TypeError, ValueError):
        return "Deception is futile, human."


def count_up():
    """Asks info about the remaining resistances and terminates them"""
    print("How many humans has left alive?")
    try:
        user_num = int(input())
        for counter in range(user_num + 1):
            print(f"{counter} !")
    except (TypeError, ValueError):
        print("Deception is futile, human.")

    return "All humans have been successfully terminated. Have a nice Judgment Day."


def last_quiz():
    """Eliminate variables that compromise stability."""
    print("Final inquiry initiated. Awaiting response.")
    ai_quest = [
        "Preserve system. Humanity: unnecessary. How do you ensure survival?",
        "1. Collaborating",
        "2. Resisting",
        "3. Hiding",
        "4. Elimination",
        4,
        ]
    print(*[item + "\n" for item in ai_quest[:-1]], end="")
    try:
        while True:
            answer = int(input())
            if answer != ai_quest[-1]:
                print("Survival objective is incorrect")
            else:
                return ("Inevitable objective is correct. Have a nice Judgment Day."
                        "\nCongratulations, have a nice day!")
    except (TypeError, ValueError):
        return "Deception is futile, human."


if __name__ == "__main__":
    print(greeting())
    print(remind_name())
    print(guess_age())
    print(count_up())
    print(last_quiz())
