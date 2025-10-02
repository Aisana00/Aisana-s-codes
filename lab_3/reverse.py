def reverse_words(sentence):
    
    
    words = sentence.split()
    
   
    reversed_words = words[::-1]
    
    
    return ' '.join(reversed_words)

user_input = input("Enter a sentence: ")
reversed_sentence = reverse_words(user_input)
print(f"Reversed: {reversed_sentence}")