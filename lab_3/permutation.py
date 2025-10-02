def print_permutations(string):
    
    def generate_permutations(s, current=""):
        if len(s) == 0:
            print(current)
            return
        
        for i in range(len(s)):
            char = s[i]
            
            remaining = s[:i] + s[i+1:]
            
            generate_permutations(remaining, current + char)
    
    generate_permutations(string)


user_string = input("Enter a string: ")
print(f"All permutations of '{user_string}':")
print_permutations(user_string)