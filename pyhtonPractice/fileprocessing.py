file_path = r"C:\Users\Zafar\Devlopment Workspace\Development Python\pyhtonPractice\example.txt"
print(file_path)
with open(file_path, "r") as fil:
    print(fil.readline())