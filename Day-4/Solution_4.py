import re

WORD = "XMAS"
WORD_2 = "MAS"

def get_data() -> list:
    with open(file="./Day-4/Puzzle_Input.txt", mode="r") as pi:
        return [line.strip() for line in pi.readlines()]



def part_one(word_search, word) -> int:
    found_words = 0

    def check_letters(board, word, row, col, index, 
                      forwards=False, backwards=False, up=False, down=False, left_diagonal_up=False, right_diagonal_up=False,
                      left_diagonal_down=False, right_diagonal_down=False) -> int:
        if index > len(word) - 1:
            return True
        if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1 or board[row][col] != word[index]:
            return False
        
        found_words = []

        if forwards:
            found_words.append(check_letters(board=board, word=word, row=row, col=col+1, index=index+1, forwards=True))
        if backwards:
            found_words.append(check_letters(board=board, word=word, row=row, col=col-1, index=index+1, backwards=True))
        if up:
            found_words.append(check_letters(board=board, word=word, row=row-1, col=col, index=index+1, up=True))
        if down:
            found_words.append(check_letters(board=board, word=word, row=row+1, col=col, index=index+1, down=True))
        if left_diagonal_up:
            found_words.append(check_letters(board=board, word=word, row=row-1, col=col-1, index=index+1, left_diagonal_up=True))
        if right_diagonal_up:
            found_words.append(check_letters(board=board, word=word, row=row-1, col=col+1, index=index+1, right_diagonal_up=True))
        if left_diagonal_down:
            found_words.append(check_letters(board=board, word=word, row=row+1, col=col-1, index=index+1, left_diagonal_down=True))
        if right_diagonal_down:
            found_words.append(check_letters(board=board, word=word, row=row+1, col=col+1, index=index+1, right_diagonal_down=True))
        
        return sum(found_words)

    rows = len(word_search)
    cols = len(word_search[0])

    for row in range(rows):
        for col in range(cols):
            if word_search[row][col] == word[0]:
                found_words += check_letters(board=word_search, word=word, row=row, col=col, index=0, 
                                             forwards=True, backwards=True, up=True, down=True, left_diagonal_up=True, right_diagonal_up=True,
                                             left_diagonal_down=True, right_diagonal_down=True
                                             )
    
    return found_words


def part_two(board, word):
    found_words = 0

    rows = len(board) - 1
    cols = len(board[0]) - 1
    
    for r in range(1, rows):
        for c in range(1, cols):
            if board[r][c] == "A":
                if board[r-1][c-1] + board[r+1][c+1] in ["MS", "SM"] and board[r-1][c+1] + board[r+1][c-1] in ["MS", "SM"]:
                    found_words += 1

    return found_words

    

if __name__ == "__main__":
    word_search = get_data()
    print(part_one(word_search=word_search, word=WORD))
    print(part_two(board=word_search, word=WORD_2))
