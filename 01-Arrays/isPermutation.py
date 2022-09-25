# Given two strings, write a method to decide if one is a permutation of the other
# Permutation: Two string with the same name and characters in different order

# Time complexity: O(2n) == O(n)
# Space complexity: O(n)

def isPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    dict = {}

    for i in range(len(str1)):
        if str1[i] in dict:
            dict[str1[i]] =+ 1
        else:
            dict[str1[i]] = 1
    
    for j in range(len(str2)):
        if str2[j] in dict:
            if dict[str2[j]] == 0:
                print(dict)
                return False
            else:
                dict[str2[j]] -= 1
    
    print(dict)
    return True


if __name__ == "__main__": 
    # str1 = input("Enter first string: ")
    # str2 = input("Enter second string: ")
    str1 = "samuel "
    str2 = "asumle"
    str3 = "ssamuel"
    print(isPermutation(str1, str2))