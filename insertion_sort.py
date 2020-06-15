
# Insertion Sort
'''
Code with bells and whistles
def displayList(arr):
  surround_arr = ["--" for num in arr]
  surround_arr = "-----" + '--'.join(surround_arr)
  arr = [str(num) for num in arr]
  array = "| " + ' | '.join(arr) + " |"
  print(surround_arr)
  print(array)
  print(surround_arr)

cards = [6, 8, 5, 4, 3]
displayList(cards) #Aesthetics
hit_key = input()
for new_card_pos in range(1, len(cards)):
  key_card = cards[new_card_pos]
  print("Key card = ",key_card) #Aesthetics
  comparing_pointer = new_card_pos - 1
  while comparing_pointer >= 0 and key_card < cards[comparing_pointer]:
    cards[comparing_pointer+1] = cards[comparing_pointer]
    cards[comparing_pointer] = " " #Aesthetics
    comparing_pointer = comparing_pointer - 1
    displayList(cards) #Aesthetics
  cards[comparing_pointer+1] = key_card
  displayList(cards) #Aesthetics
  hit_key = input() #Aesthetics
'''

cards = [6, 8, 5, 4, 3]
for new_card_pos in range(1, len(cards)):
  key_card = cards[new_card_pos]
  comparing_pointer = new_card_pos - 1
  while comparing_pointer >= 0 and key_card < cards[comparing_pointer]:
    cards[comparing_pointer+1] = cards[comparing_pointer]
    comparing_pointer = comparing_pointer - 1
  cards[comparing_pointer+1] = key_card

  # Worst case O(n^2) [8,6,5,4,3]
  # Best case O(n) [3,4,5,6,8]
