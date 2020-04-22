file = open("file.txt")

#lines = file.readlines() #print the content in an array list
#print(lines)

#all_content = file.read() #print all the content in a file archive
#print(all_content)

#new_file = open("books_already_read", "w") #replace the archive in a new one
new_file = open("books_already_read", "a") #open the archive and inserting the pointer in the end of the file

new_file.write("- Recursive - Blake Crouch\n") #write in the archive
new_file.write("- The Institute - Stephen King\n")

new_file.close() #close the archive, this is very important to avoid conflicts