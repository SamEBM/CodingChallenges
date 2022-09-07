# Check if all caracters within a string are different
# Time complexity: O(n) where n is the lenght of the string
# Space complexity: O(c) where c is the caracter set, O(1) simplified 

def areUnique(str):
    if len(str) > 128:
        return False

    chars = [False] * 128
    for i in range(len(str)):
        character = str[i]
        if chars[ord(character)]:
            return False
        chars[ord(character)] = True
    return True

if __name__ == "__main__":
    str = input("Enter a string to check if all characters are different: ")
    if areUnique(str):
        print("All characters in the string are different")
    else:
        print("There is at least one repeated character in the string")