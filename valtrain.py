import random, os
os.system('color')

red = '\033[91m'
blue = '\033[96m'
green = '\033[92m'



def get_card_value(card):
    """returns value of a card """
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        return 11 # adjusted to 1 if needs be later
    else:
        return int(card)

def adjust_ace(hand, total_value):
    """adjusts ace logic"""
    num_aces = hand.count("A")
    while total_value > 21 and num_aces:
        total_value -= 10
        num_aces -= 1
    return total_value

def get_card():
    """generates a random card along with its value"""
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    card = random.choice(cards)
    value = get_card_value(card)
    return card, value

def generate_hand():
    """random card of 2-4 hands and calculates the total value"""
    hand = []
    total_value = 0

    for _ in range(random.randint(2, 4)):
        card, value = get_card()
        hand.append(card)
        total_value += value

    total_value = adjust_ace(hand, total_value)
    return hand, total_value

def play_blackjack_trainer():
    hand, total_value = generate_hand()
    print(f"{blue}━" * 30)
    print(f"{blue}Hand:\033[0m", " ".join(hand))

    while True:
        user_input = input(f"{blue}Calculate the total value: \033[0m")
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print(f"{red}Invalid input. Please enter an integer value.\033[0m")

    if user_input == total_value:
        print(f"{green}Correct!\033[0m")
    else:
        print(f"{red}Wrong. The correct total value is {total_value}.\033[0m")


def main():
    print(f"{blue}Welcome!\033[0m")
    while True:
        play_blackjack_trainer()

if __name__ == "__main__":
    main()
