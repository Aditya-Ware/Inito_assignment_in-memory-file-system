import os
import re
import shutil
def main():
    while True:
        try:
            print(os.getcwd())
            command = input('$ ')
            execute(command)
        except Exception as e:
            print(' error', e)


def execute(command):
    commands = command.split()

    #to change directory
    if commands[0] == 'cd':
        try:
            if len(commands) > 1:
                os.chdir(commands[1])
            else:
                os.chdir(os.path.expanduser('~'))
        except FileNotFoundError:
            print('Directory not found')

    #to list items in directory
    elif commands[0] == 'ls':
        if len(commands) > 1:
            try:
                os.listdir(commands[1])
            except FileNotFoundError:
                print('Directory not found')
        else:
            print(os.listdir())

    #searches pattern        
    elif commands[0] == 'grep':
        if len(commands) > 2:
            try:
                with open(commands[2], 'r') as file:
                    print('\n'.join(line for line in file if re.search(commands[1], line)))
            except FileNotFoundError:
                print('File not found')
        else:
            print('Usage: grep "pattern" file')

    #to display file content        
    elif commands[0] == 'cat':
        if len(commands) > 1:
            try:
                with open(commands[1], 'r') as file:
                    print(file.read())
            except FileNotFoundError:
                print('File not found')
        else:
            print('Usage: cat file')

    # to create empty file
    elif commands[0] == 'touch':
        if len(commands) > 1:
            try:
                open(commands[1], 'a').close()
            except Exception as e:
                print('An error occurred:', e)
        else:
            print('Usage: touch file')

    #to edit a file
    elif commands[0] == 'echo':
        if len(commands) > 2:
            try:
                with open(commands[2], 'w') as file:
                    file.write(' '.join(commands[3:]))
            except Exception as e:
                print('An error occurred:', e)
        else:
            print('Usage: echo "text" file')

    #to move file /directory to any location
    elif commands[0] == 'mv':
        if len(commands) > 2:
            try:
                shutil.move(commands[1], commands[2])
            except Exception as e:
                print('An error occurred:', e)
        else:
            print('Usage: mv file1 file2')

    # to copy file/directory to any location
    elif commands[0] == 'cp':
        if len(commands) > 2:
            try:
                shutil.copy(commands[1], commands[2])
            except Exception as e:
                print('An error occurred:', e)
        else:
            print('Usage: cp file1 file2')

    # to remove file/ directory
    elif commands[0] == 'rm':
        if len(commands) > 1:
            try:
                if os.path.isdir(commands[1]):
                    shutil.rmtree(commands[1])
                else:
                    os.remove(commands[1])
            except Exception as e:
                print('An error occurred:', e)
        else:
            print('Usage: rm file/directory')

    #to create a directory
    elif commands[0] == 'mkdir':
        if len(commands) > 1:
            try:
                os.mkdir(commands[1])
            except Exception as e:
                print('An error occurred:', e)
        else:
            print('Usage: mkdir directory')
    elif commands[0] == 'exit':
        exit()
    else:
        print('Unknown command:', commands[0])
        
if __name__ == '__main__':
    main()
