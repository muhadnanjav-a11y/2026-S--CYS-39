# import Adnan
import os
# if __name__ == "__main__":
#     Adnan.welcome()

# def main():
#     print("This is the main function of the program.")
#     print("You can add more code here to perform various tasks.")
# main()


with open("file1.txt", "w") as file:
    file.write("This is elon musk\n")
    file.write("You and I\n")

with open("file1.txt", "r") as file:
    code = file.read()
    print(code)

# os.mkdir("folder")
if os.path.exists("folder"):
    for i in range(5):
        file_name = f"file_{i}.txt"
        file_path = os.path.join("folder", file_name)
        with open(file_path, "w") as file:
            file.write(f"This is {file_name}\n")


files = os.listdir("folder")
print("Files in 'folder':")
for file in files:
    print(file)
        
os.remove("file1.txt")

print(os.getcwd())
os.chdir("folder")
print(os.getcwd())

if not os.path.exists("subfolder"):
    os.mkdir("subfolder")
