from itertools import zip_longest

def mergeAlternately(word1, word2):
    merged = ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
    return merged

def main():
    print(mergeAlternately('cat', 'pussy'))

if __name__ == '__main__':
    main()
