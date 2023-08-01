# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt") as file:
#     file.write("New text.") # is UnsupportedOperations: not writable (Error) => 파일을 읽기 전용 모드로 열었기 때문

# with open("my_file.txt", mode="r") as file: # 읽기 모드

with open("my_file.txt", mode="w") as file: # 쓰기 모드
    file.write("New text.") # 이전 텍스트가 모두 삭제되고 이 텍스트로 대체됨 

# 파일에 있는 모든 것을 삭제하기 않고 추가하고 싶다면 "a"
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# 새로운 파일 만들기 (Create new_file.txt)
with open("new_file.txt", mode="w") as file:
    file.write("New text.")
