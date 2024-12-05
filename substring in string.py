def strStr(haystack, needle):
        needle_length = len(needle)
        for i in range(len(haystack) - needle_length+1):
            print(i)
            print(haystack[i:needle_length+i])
            if haystack[i:needle_length] == needle:
                print(haystack[i:needle_length])
                return i
        return -1

print(strStr("hello", 'll'))
print(strStr("hsadhashh", 'ash'))