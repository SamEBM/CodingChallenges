# Perform a basic string compression using the counts of repteated characters. 
# Assume the string has only uppercase and lower letters (a-z,A-Z).
# Example:
# Input: "aabcccccaaa"
# Output: "a2b1c5a3"
# If the compressed string is not smaller than the original, return the original string

# Time Complexity: O(n)
# If using concatetation instead of append the time complexity increases to O(p + k^2)
# Where p = the size of the origina string and k = number of char sequences (4 in the example)

def compress(original):
    compressedCounts = []
    count = 0
    current = original[0]

    for i in range(len(original)):
        if original[i] == current:
            count += 1
        else:
            compressedCounts.append(current + str(count))
            # Faster than 
            # compressed += (current + str(count))
            count = 1
            current = original[i]

    compressedCounts.append(current + str(count))
    compressed = ''.join(compressedCounts)

    if len(compressed) >= len(original):
        return original

    return compressed

if __name__ == '__main__':
    while True:
        original = input('Enter a string you want to compress or type "stop" to exit: ')
        original = original.strip()
        if original == 'stop':
            break
        else:
            print("Original string: " + original)
            print("Compressed string: " + compress(original))