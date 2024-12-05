def lengthOfLongestSubstring( s: str) -> int:
        str_len = {}
        result = ''
        for chr in s:
            if chr in result:
                return len(result)
            else:
                result += chr

print(lengthOfLongestSubstring("pwwkew"))