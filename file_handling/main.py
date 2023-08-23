# demofile.txt 파일 읽기 
f = open("file_handling\demofile.txt", "r")
print(f.read()) 

# 오류가 났던 이유 : 현재 작업 디렉토리가 C:\Users\OWNER\Documents\day24 
# 이렇게 되어있었기 때문에 앞에 file_handling 추가해주어야 한다.

# 작업 디렉토리 확인 : 현재 작업 디렉토리를 확인하는 코드 
import os 
print(os.getcwd())

# read(숫자)로 반환된 문자수를 지정할 수 있음
f = open("file_handling/demofile.txt", "r")
print(f.read(5)) # Hello

# readline() 메소드를 통해, 파일의 한 줄만을 반환
f = open("file_handling/demofile.txt", "r")
print(f.readline()) # Hello! Welcome to demofile.txt

# 파일 처리가 끝난 뒤, 반드시 close() 메소드를 사용
f = open("file_handling/demofile.txt", "r")
f.close() # Hello! Welcome to demofile.txt

# 파일 끝에 덧붙이기 (append)
f = open("file_handling/demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

# 덧붙여진 파일을 다시 읽고, 결과 확인
f = open("file_handling/demofile.txt", "r")
print(f.read())
# Hello Welcome to demofile.txt
# This is for testing purposes.
# Good Luck! Now the file has more content!

# 파일 생성하고 쓰기 (write)
f = open("file_handling/demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# 쓰여진 파일을 읽고, 결과 확인
f = open("file_handling/demofile3.txt", "r")
print(f.read()) # Woops! I have deleted the content!



