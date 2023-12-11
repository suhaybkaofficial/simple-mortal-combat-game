import random

def display_health(player1, player2):
    print(f"{player1['name']} HP: {'H' * (player1['health'] // 2)}")
    print(f"{player2['name']} HP: {'H' * (player2['health'] // 2)}")

def attack(player, opponent):
    magnitude = int(input(f"{player['name']} Attacks!! Choose your attack magnitude between 1 and 50: "))

    if 1 <= magnitude <= 50:
        success_chance = random.randint(1, 100)
        if success_chance <= (50 - magnitude):
            print(f"Ooopsy! {player['name']} missed the attack!")
        else:
            damage = random.randint(1, magnitude)
            print(f"{player['name']} hits {damage} damage!!!")
            opponent['health'] -= damage
    else:
        print("The attack magnitude must be between 1 and 50. Try again.")
        attack(player, opponent)

def main():
    print("MEDIPOL KOMBAT\n")
    
    player1 = {'name': input("First Hero\nPlease enter your hero's name: "), 'health': 100}
    player2 = {'name': input("Second Hero\nPlease enter your hero's name: "), 'health': 100}

    while player1['name'] == player2['name']:
        print(f"{player1['name']} is taken, please choose another name!")
        player2['name'] = input("Second Hero\nPlease enter your hero's name: ")

    starting_player = random.choice([player1, player2])
    print(f"\nCoin toss result: {starting_player['name']} starts first!")
    
    while player1['health'] > 0 and player2['health'] > 0:
        display_health(player1, player2)
        
        if starting_player == player1:
            attack(player1, player2)
        else:
            attack(player2, player1)

        starting_player = player1 if starting_player == player2 else player2

    print(f"\n{player1['name']}\n{player2['name']}\nHP:\n{starting_player['name']} Wins")

    play_again = input("Do you want to play another round? (Yes or No): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing! See you again!")

if __name__ == "__main__":
    main()
