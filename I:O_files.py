#     ********* READING FILES ***********
# -------------------------------------------
#       Without Context Manager
# f = open('_file.txt', 'r')
# prt(f.mode)
# f.close()   in
#---------------------------------------------  
    #   With Context Manager
# with open('_file.txt', 'r') as f:
    # ------------------------------
    #          Reading files

    # f_contents=f.read()
    # print(f_contents, end="")
    # --------------------------------
    #       You can also loops 

    # for i in f:
    #     print(i, end="") 
    # ---------------------------------
    #         Reading "Chunks" of files

    # f_contents=f.read(100)
    # print(f_contents, end="")

    # **This code ^ prints the first hundred letters or individual elements of the code
    # **to print the next chunk of code, you must ennter the code again

    # f_contents=f.read(100)
    # print(f_contents, end="")

    # **Then to print the next code you keep on typing the next code
    # ---------------------------------
    #        Using While loops to write "chunks" of code

    # size_of_chunks=10
    # f_contents=f.read(size_of_chunks)
    # while len(f_contents)>0:
    #     print(f_contents, end="")
    #     f_contents=f.read(size_of_chunks)
    # ---------------------------------
    #       Using Seek
    # size_of_chunks=10

    # f_contents=f.read(size_of_chunks)
    # print(f_contents, end="")

    # f_contents=f.read(size_of_chunks)
    # print(f_contents, end="")

    # # **This gives you the first twenty elements in the file
    # # **through you chahnge where you want to begin the print process form

    # f.seek(60)
    # f_contents=f.read(size_of_chunks)
    # print(f_contents)
    # ----------------------------------
# _________________________________________________________________________________
#      **********  Writing Files  **************
# ----------------------------------------------
#       To write a new string in file
# Have the file open in write mode
# with open("_file_writemode.txt","w") as f:
#     f.write("hello")
# The write function deletes everything and writes the string into this file
# -----------------------------------------------
#           To write from a file

# with open("_file.txt","r") as rf:
#     f_contents=rf.read()
# with open("_file_writemode.txt", "w") as wf:
#     wf.write(f_contents)
#------------------------------------------------
#           To write chunks of code

# with open("_file.txt", "r") as rf:
#     with open('_file_writemode.txt', "w")as wf:
#         size_of_chunks=20
#         f_contents=rf.read(size_of_chunks)
#         wf.write(f_contents)
# -------------------------------------------------
#           While loop while writing files

# with open("_file.txt","r")as rf:
#     with open("_file_writemode.txt", "w")as wf:
#         f_contents=rf.read()
#         while len(f_contents)>0:
#             wf.write(f_contents)
#             f_contents=rf.read()
        
        

    