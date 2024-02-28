# CodSoft
new CodSoft internship repository

Calculator Program

    print("Welcome, This is a calculator")
    x = int(input("First number: "))
    y = int(input("Second number: "))
    z = input("Arithmetic operation: ")

    if z == "add":
      print("solution is ", x+y)
    elif z == "subtract":
      print("solution is ", x-y)
    elif z == "multiply":
      print("solution is ", x*y)
    elif z == "divide":
      print("solution is ", x/y)
    else:
      print("error, try again")
 




Password Generator


    import random
    import string

    def createpassword(length):
        character = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(character) for i in range(length))
        return password

    if __name__ == "__main__":
        password_length = int(input("Enter the length of your password: "))
        password = createpassword(password_length)
        print("The Generated Password:", password)





Rock Paper Scissors Program


    import random

    def get_users_input():
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in ['rock', 'paper', 'scissors']:
                return user_choice
            else:
                print("Error. Please enter rock, paper, or scissors.")

    def get_computers_input():
        return random.choice(['rock', 'paper', 'scissors'])

    def find_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose"

    def main():
        user_score = 0
        computer_score = 0
        while True:
            print("\n-- Rock, Paper, Scissors Game --")
            computer_choice = get_computers_input()
            user_choice = get_users_input()

            print("Your choice:", user_choice)
            print("Computers choice:", computer_choice)
            result = find_winner(user_choice, computer_choice)
            print(result)
            if 'win' in result:
                user_score += 1
            elif 'lose' in result:
                computer_score += 1
            print("Score - You: {}, Computer: {}".format(user_score, computer_score))
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break

    if __name__ == "__main__":
    main()
