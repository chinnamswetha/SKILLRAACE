def flames_relationship(name1, name2):
    
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    
    total_letters = len(set(name1 + name2))
    
    
    flames_sequence = ['Friendship', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    
    
    remaining_letters = []
    for letter in name1:
        if letter in name2:
            name2 = name2.replace(letter, "", 1)
        else:
            remaining_letters.append(letter)
    
    for letter in name2:
        remaining_letters.append(letter)
    
    
    relationship_index = (total_letters % len(flames_sequence)) - 1
    relationship = flames_sequence[relationship_index]
    
    return relationship


name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
relationship = flames_relationship(name1, name2)
print(f"The relationship between {name1} and {name2} is: {relationship}")