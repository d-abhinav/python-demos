import random

allTokens = []
soldLocation = 0
players = []


def purchase_tokens():
    t = int(input("How many tokens would you like to buy? (Up to 10) "))
    print("You purchased " + str(t) + ' tokens')
    return t


def welcome_message():
    return input("Welcome to Abhinav's Arcade! Would you like to purchase tokens? yes, or no? ")


def mint_tokens(num_tokens):
    global soldLocation
    st = soldLocation
    end = st + num_tokens
    minted = allTokens[st:end]
    soldLocation = soldLocation + num_tokens
    return minted


def initialize_tokens():
    local_tokens = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
        51, 52, 53, 54, 55, 56, 57, 58, 59, 60
    ]
    # random.shuffle(local_tokens)
    return local_tokens


def pick_winner():
    winning_number = random.choice(allTokens)
    winning_player = None
    for idx, player in enumerate(players):
        print('' + str(idx + 1) + ": " + str(player))
        for token in player:
            if winning_number == token:
                winning_player = idx
                # we are not breaking here so we can print all player tokens
    if winning_player is not None:
        print('The winning number is ' + str(winning_number))
        print('Player ' + str(winning_player + 1) + ' is the winner!')
    else:
        print('The winning number is ' + str(winning_number))
        print("Dealer wins!")


def main():
    global allTokens
    global players
    allTokens = initialize_tokens()
    while soldLocation < 50:
        user_choice = welcome_message()
        if user_choice == "yes":
            tokens = purchase_tokens()
            if 0 < tokens <= 10:
                player_tokens = mint_tokens(tokens)
                players.append(player_tokens)
            else:
                print("invalid selection, select 0-10 tokens only")
    pick_winner()


if __name__ == '__main__':
    main()
