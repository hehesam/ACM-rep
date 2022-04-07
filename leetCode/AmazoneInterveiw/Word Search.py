

def path_finder(board, curr, word, word_index, visited):
    if word_index == len(word):
        return True
    x,y = curr
    if 0<=x<len(board) and 0<=y<len(board[x]) and curr not in visited:
        if board[x][y] == word[word_index]:
            tmp = board[x][y]
            visited.add(curr)
            down = path_finder(board, (x+1,y), word, word_index+1,visited)
            up = path_finder(board, (x-1,y), word, word_index+1,visited)
            right = path_finder(board, (x,y+1), word, word_index+1,visited)
            left = path_finder(board, (x,y-1), word, word_index+1,visited)
            return down or up or left or right
        else:
            return False
    return False


def find_word(board, word):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                visited = set()
                if path_finder(board, (i,j), word, 0, visited):
                    return True
    return False







board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"

print(find_word(board, word))