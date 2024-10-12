a = input("Enter a Sudoku: ")
chunks = [a[i:i +9] for i in range(0, len(a), 9)]
list = [[int(chunk)] for chunk in chunks]
# Horizontal
for chunk in chunks:
    chunk_sum = 0
    for digit in chunk:
        chunk_sum += int(digit)
    if chunk_sum != 45:
        print("No Sudoku")
        exit()
    else:
        print("Horizontal Sudoku OK")

#Vertical
for i in range(0, 9):
    position_digit_sum = 0
    for chunk in chunks:
        position_digit = int(chunk[i])
        position_digit_sum += position_digit
    if position_digit_sum != 45:
        print("No Sudoku")
        exit()
    else:
        print("Vertical Sudoku OK")
        
        
def is_valid_block(block):
    return sorted(block) == ['1','2', '3', '4', '5', '6', '7', '8', '9' ]
#Sub-square Validation
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        sub_square = [chunks[x][y] for x in range(i, i+3) for y in range(j, j+3)]
        if not is_valid_block(sub_square):
            print('No sudoku')
            exit()
print("sub-square sudoku OK")
        
        
#Good Test: 295743861431865927876192543387459216612387495549216738763524189928671354154938672
#Bad Test: 195743862431865927876192543387459216612387495549216738763524189928671354254938671
