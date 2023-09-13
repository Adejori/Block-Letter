# Oluwatobi Adejori
# I am a mechanical engineer who loves coding

first_initial = [[' ', 'O', 'O', 'O', ' '], ['O', ' ', ' ', ' ', 'O'], ['O', ' ', ' ', ' ', 'O'], ['O', ' ', ' ', ' ', 'O'], ['O', ' ', ' ', ' ', 'O'], ['O', ' ', ' ', ' ', 'O'], [' ', 'O', 'O', 'O', ' ']]

second_initial = [[' ', ' ', 'A', ' ', ' '], [' ', 'A', ' ', 'A', ' '], ['A', ' ', ' ', ' ', 'A'], ['A', 'A', 'A', 'A', 'A'], ['A', ' ', ' ', ' ', 'A'], ['A', ' ', ' ', ' ', 'A'], ['A', ' ', ' ', ' ', 'A']]

block_length = len(first_initial)
for i in range(block_length):
  _line = "".join(first_initial[i]) + " " + "".join(second_initial[i])
  print(_line)

