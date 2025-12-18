#Using a queue, write a program that manages a queue of files to print.

import queue

# creates a queue of files to print
files_to_print = queue.Queue()

while True:
   print('1. Add file to print')
   print('2. Print file')
   print('0. Quit')
   menu = input('Select an option: ')

   
   if menu == '1':
      file_name = input('Enter file name to print: ')
      # add new file to the end of the queue 
      files_to_print.put(file_name)

   elif menu == '2':
      if not files_to_print.empty():
         current_file = files_to_print.get()
         print(f'File {current_file} is currently being printed. Please wait!')
      else:
         print("The print queue is empty!")

   elif menu == '0':
      break