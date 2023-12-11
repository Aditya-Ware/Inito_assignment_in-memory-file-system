# Inito_assignment_in-memory-file-system







This is a in menory - file system implemented in Python. It provides file/directory management operations such as navigating directories, listing contents, searching for patterns in files, displaying file contents, creating, moving, copying, and removing files and directories. And all requirements.

## Usage
## Launch the program
```
python main.py
```

1. **Change Directory (cd):**
   ```
   cd [directory_path]
   ```
   Change the current working directory. If no path is provided, it will change to the home directory.

2. **List Items (ls):**
   ```
   ls [directory_path]
   ```
   List items in the specified directory. If no path is provided, it lists items in the current directory.

3. **Search Pattern in File (grep):**
   ```
   grep "pattern" file
   ```
   Search for a specified pattern in a file.

4. **Display File Content (cat):**
   ```
   cat file
   ```
   Display the content of a specified file.

5. **Create Empty File (touch):**
   ```
   touch file
   ```
   Create an empty file with the specified name.

6. **Edit File (echo):**
   ```
   echo "text" file
   ```
   Write the specified text to the specified file.

7. **Move File/Directory (mv):**
   ```
   mv source destination
   ```
   Move a file or directory from the source path to the destination path.

8. **Copy File/Directory (cp):**
   ```
   cp source destination
   ```
   Copy a file or directory from the source path to the destination path.

9. **Remove File/Directory (rm):**
   ```
   rm file/directory
   ```
   Remove the specified file or directory.

10. **Create Directory (mkdir):**
   ```
   mkdir directory
   ```
   Create a new directory with the specified name.

11. **Exit the File Manager:**
   ```
   exit
   ```
   Exit the command-line file manager.

## Notes

- This file manager supports both absolute and relative paths.
- Use double quotes for patterns with spaces in the grep command.
- Be cautious when using the remove (rm) command, as it permanently deletes files and directories.

## Examples

- Change to a directory:
  ```
  $ cd Documents
  ```

- List items in the current directory:
  ```
  $ ls
  ```

- Search for a pattern in a file:
  ```
  $ grep "keyword" example.txt
  ```

- Display the content of a file:
  ```
  $ cat example.txt
  ```

- Create an empty file:
  ```
  $ touch newfile.txt
  ```

- Move a file:
  ```
  $ mv oldfile.txt /path/to/newlocation/
  ```

- Copy a file:
  ```
  $ cp existingfile.txt /path/to/destination/
  ```

- Remove a file or directory:
  ```
  $ rm unwantedfile.txt
  ```

- Create a new directory:
  ```
  $ mkdir new_directory
  ```

- Exit the file manager:
  ```
  $ exit
  ```
