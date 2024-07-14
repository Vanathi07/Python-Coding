text=input("Enter the String: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
newtext = ""
text_len = len(text)
for i in range(text_len):
    if text[i-1]==text[i] and text[i] in vowels:
        newtext = newtext + text[i]+text[i-1]
    elif text[i] not in vowels :
        newtext = newtext + text[i] 
             
print("\nString after removing Vowels: ",newtext)
