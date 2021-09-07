# Python Program that make special code from lines of file
file = open('books.txt', 'r') # opening the file in read only mode

Lines = file.readlines() # reading the lines of the file

count = 0

# Strips the newline character
for line in Lines:
    word = line.strip()
    print(f"{word} -> {word[0]}{len(word)}")
    count += 1
