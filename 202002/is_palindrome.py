symbols = set([',', '.', '-', '/', '\\', ';'])

def trim(text):
    trim_text = ''
    for i in range(0, len(text)):
        if text[i:i+1] not in symbols:
            trim_text += text[i:i+1]
    
    print(trim_text)
    return trim_text

def reverse(text):
    return text[::-1]
    
def is_palindrome(text):
    return text == reverse(text)
    


something = input("Enter text: ")
if is_palindrome(trim(something)):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")