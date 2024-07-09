print("Please provide AI some data to learn...")
print("The current data length is 0, 100 symbols left")
data = ''
while len(data) < 100:
    user_input = input('Print a random string containing 0 or 1:\n\n')
    data += ''.join([c for c in user_input if c in '01'])
    print(f'Current data length is {len(data)}, {100 - len(data)} symbols left'
          if len(data) < 100
          else f'\nFinal data string:\n{data}\n')


binary_sequences = {f'{key_1}{key_2}{key_3}': {'0': 0, '1': 0} for key_1 in '01' for key_2 in '01' for key_3 in '01'}
temp = data[:3]
for i in data[3:]:
    binary_sequences[temp][i] += 1
    temp = temp[1:] + i

print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""")


balance = 1000
while balance > 0:
    user = input("\nPrint a random string containing 0 or 1:\n\n")
    while (len([c for c in user if c in '01']) < 4) and user != 'enough':
        user = input("\nPrint a random string containing 0 or 1:\n\n")
    if user == 'enough':
        break
    temp = user[:3]
    prediction = ''
    for i in user[3:]:
        prediction += '0' if binary_sequences[temp]['0'] > binary_sequences[temp]['1'] else '1'
        temp = temp[1:] + i

    print('predictions:\n' + prediction + '\n')

    correct_guesses = [c == d for c, d in zip(user[3:], prediction)].count(True)
    print(f"Computer guessed {correct_guesses} out of {len(user[3:])} symbols right"
          f"({round(correct_guesses / len(user[3:]) * 100, 2)} %)")
    balance = balance - (correct_guesses - (len(user[3:]) - correct_guesses))
    print(f"Your balance is now ${balance}")

print("Game over!")
