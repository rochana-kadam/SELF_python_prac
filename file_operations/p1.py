
#* 1. Create a file named student.txt and write your name into it.

# with open ("student.txt","x") as f:
#     f.write("hello, i'm Rochana")

#* 2. Read and display the contents of student.txt.
# with open ("student.txt","r") as f:
#     print(f.read())

# * 3. Append your course name to student.txt without deleting the existing content.
# with open ("student.txt","a") as f:
#     f.write(" \n i'm studing mca.")

# * 4. Read only the first line of a file.
# with open("student.txt","r") as f:
#     first_line=f.readline()
#     print(first_line)

# * Count the number of characters in a text file.
# with open ("student.txt","r") as f:
#     content=f.read()
#     print(len(content))

# * Create a file named `college.txt` and write your college name, course name, and semester on three separate lines.
# with open ("college.txt","x") as f:
#     f.write("College name: Mes IMCC \nCourse name: MCA \nSemester: ")

# * Read `college.txt` and count how many lines it contains.
# with open ("college.txt", "r") as f:
#     lines=f.readlines()
#     print(len(lines))

# * Create a file named `story.txt` with a few sentences. Write a program to count the total number of words in it.
# with open ("story.txt", "r") as f:
#     content=f.read()
#     words=content.split()
#     print(len(words))

# * Read `story.txt` and check whether the word `Python` exists in the file. Print an appropriate message.
# with open ("story.txt", "r") as f:
#     content=f.read()
#     words=content.split()
#     if "python" in words:
#         print("word found")
#     else:
#         print("word not found")

# * Copy all the contents of `story.txt` into a new file named `backup.txt`.
# with open ("story.txt", "r") as f:
#     content=f.read()
# with open("backup.txt", "x") as f:
#     f.write(content)


# * Read a text file and count the total number of vowels (a, e, i, o, u) in its contents.
# with open ("college.txt","r") as f:
#     content=f.read()
#     cnt=0
#     for i in content:
#         if i.lower() in "aeiou":
#             cnt+=1
#     print(cnt)


# * Ask the user to enter three sentences and append all three to `journal.txt`, each on a separate line.
# s1=input("enter sentence 1: ")
# s2=input("enter sentence 2: ")
# s3=input("enter sentence 3: ")
# with open ("journal.txt", "a") as f:
#     f.write(f"{s1}\n{s2}\n{s3}")

# * Read a file and print each line with its line number, starting from 1.
# with open ("story.txt", "r") as f:
#     lines=f.readlines()
#     for i in range (len(lines)):
#         print(f"{i}. {lines[i]}")

# * Read a file, replace every occurrence of `bad` with `good`, and save the updated content back to the file.
# with open ("sample.txt","r+") as f:
#     content=f.read()
#     content=content.replace("bad", "good")
#     f.write(content)   #! doubt why won't the write function overwrite the content here

