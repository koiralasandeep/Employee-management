# 6-1. Files
Files are permanent storage for data  
The data is available even after the program stops running

## a. Types of files

### Text files
A text file contains data that has been encoded as text  
Even if the file contains numbers, those numbers are stored in the file as a series of characters.  
Such files may be opened and viewed in a text editor such as Notepad. 

### Binary files
A binary file contains data that has not been converted to text  
The data that is stored in a binary file is intended only for a program to read, like Word or Excel  
Contents of a binary file cannot be viewed with a text editor.

<details>
  <summary>
    💡 Note:
  </summary>
  For the scope of Chapters 6, 7, 8 we will be working with text files
</details>


## b. File Access Methods
### Sequential access 
Data is accessed from the beginning of the file to the end of the file  
If you want to read a piece of data that is stored at the very end of the file, you have to read all of the data that comes before it  
Similar to the way cassette tape players work

### Direct access or random access 
You can jump directly to any piece of data in the file without reading the data that comes before it  
Similar to the way a CD player or an MP3 player works

💡 For this class, we will use sequential access files.


## c. File Processing Steps
1. Open file
2. Read from or write to file
3. Close file - if we don't close the file,  any new data will not be written to the file