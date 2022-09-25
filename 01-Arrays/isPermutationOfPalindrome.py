# Given a string, check if it is a permutation of a palindrome
# Hint: A permutation of a palindrome can have no more than 1 character 
# that has an odd count, every other caracter must have an even count.

# Time Complexity: O(n)
# Space Complexity: O(c), where c is the character set

def isPermutationOfPalindrome(str):
    phrase = str.lower()
    dict = {}
    foundOdd = False

    for i in range(len(phrase)):
        if phrase[i] in dict:
            dict[phrase[i]] += 1
        elif phrase[i].isalpha():
            dict[phrase[i]] = 1
    
    for j in dict.keys():
        if dict[j] % 2 == 1:
            if foundOdd:
                return False
            else:
                foundOdd = True
    
    return True

if __name__ == "__main__":
    keepGoing = True

    while keepGoing:
        str = input("Enter a string to check if it is a permutation of a palindrome or write 'stop' to exit: ")
        if str == "stop":
            keepGoing = False
            break
        print("Is a permutation of a palindrome? ", isPermutationOfPalindrome(str))