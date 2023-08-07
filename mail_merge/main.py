#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("starting_letter.txt", mode="w") as file: # Write Mode
    file.write(f"invited_names.txt")

# 각 라인의 목록 객체의 항목인 목록으로 파일의 모든 라인을 반환
f = open("demofile.txt", "r")
print(f.readlines())

# replace() method
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x) 

# 문자열의 시작과 끝에서 공백 제거 strip() method
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite") 

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        
