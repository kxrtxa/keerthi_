def count_and_display_4lettter_words():
    file_handle = open("Para.txt", "r")
   # var letter_words=0
    line=""
    while line==file_handle.read():
         print(line)
    file_handle.close()

def main():
    count_and_display_4lettter_words()

if __name__ == "__main__":
    main()

