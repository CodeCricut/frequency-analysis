letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def freq_analysis(string):
    i = 0
    freq = []
    while i < len(letters):
        freq.append(0)
        i += 1
    i = 0
    while i < len(letters):
        j = 0
        tempString = string
        while j < len(string):
            if letters[i] in tempString:
                letIndex = tempString.index(letters[i]) + 1
                tempString = tempString[letIndex: ]
                freq[i] += 1
            j += 1
        i += 1
    i = 0
    while i < len(letters):
        freq[i] = freq[i] / float(len(string))
        i += 1
    return(freq)

print(freq_analysis("abcd"))

