lineCount = 1

while lineCount <= 5:
    ch = '1'
    charCount = 0
    while charCount < 11:
        print(ch, end='')
        ch = '0' if ch == '1' else '1'
        charCount += 1
    print()
    lineCount += 1