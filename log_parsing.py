def AskForFileName():
    file_name = input("Enter your input file name: \n")
    return file_name

def ReadFileContents(file_name):
    open_file = open(file_name, 'r')
    all_file_contents = open_file.readlines()
    open_file.close()
    return all_file_contents

def BuildCrashList(all_file_contents):
    crash_list = []
    for line in all_file_contents:
        if ('crash' or 'Crash') in line:
            crash_list.append(line)
    return crash_list

def WriteNewFile(crash_list):
    new_file = open('crash.txt', 'w')
    for line in crash_list:
        new_file.write(line)
    new_file.close()

if __name__ == "__main__":
    file_name = 'crash.log'
    all_file_contents = ReadFileContents(file_name)
    crash_list = BuildCrashList(all_file_contents)
    new_file = WriteNewFile(crash_list)
