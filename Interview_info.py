input = "My name is Utkarsh Panwar"
output = "yM Panwar eman Utkarsh si"

input =  input.split()   #['My', 'name', 'is', 'Utkarsh', 'Panwar']
output = ""
j = len(input) -1
for i in range(len(input)-1):
    # print(i,j)
    first_word = input[i][::-1]
    last_word = input[j]
    output += " " +first_word
    if i==j:
        break
    output+= " " +last_word
    j -=1
    
    # print(word)
print(output)



