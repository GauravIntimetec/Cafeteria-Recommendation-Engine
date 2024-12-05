def is_valid(S):
    stack = []
    mapping = {"(":")","{":"}", "[":"]" }

    for character in S:
        if character in mapping.values():
            if not stack or stack.pop() in mapping:  #last character in stack
                continue
            else:
                return False

        if character in mapping.keys():
            stack.append(character)
    return len(stack) == 0

print(is_valid("{(()))}"))