def AskForFileName():
    '''
    Functionthat will ask the user to input the name of the file to open.
    :return: file_name
    '''

    file_name = input('Enter the name of the input file: \n')
    return file_name

def ReadFileContents(file_name):
    '''
    Function that will read all the lines from the file and return this list.
    :param file_name:
    :return: all_file_contents
    '''

    open_file = open(file_name, 'r')
    all_file_contents = open_file.readlines()
    open_file.close()

    return all_file_contents

def BuildHeadList(all_file_contents):
    '''
    This function will loop over the variable populated in ReadFileContents and append to another list called HeadList
    the header information from the file. There are the lines from the top of the file to the lines that start with the
    word ATOM
    :param all_file_contents:
    :return: head_list
    '''

    head_list = []
    for line in all_file_contents:
        if not line.startswith('ATOM'):
            head_list.append(line)
        if line.startswith('ATOM'):
            break

    return head_list

def BuildAtomList(all_file_contents):
    '''
    This function will loop over the variable populated in ReadFileContents and append to another list called atom_list
    all the lines that begin with ATOM and only these lines.
    :param all_file_contents:
    :return: atom_list
    '''

    atom_list = []
    for line in all_file_contents:
        if line.startswith('ATOM'):
            atom_list.append(line)

    return atom_list

def BuildTailList(all_file_contents):
    '''
    This function will loop over the variable populated in ReadFileContents and append to another list call tail_list
    all the lines that are below those that begin with ATOM (the lines left over).
    :param all_file_contents:
    :return: tail_list
    '''

    tail_list = []
    after_atom = False
    for line in all_file_contents:
        if not line.startswith('ATOM') and after_atom == False:
            continue
        elif line.startswith('ATOM'):
            after_atom = True
            continue
        elif not line.startswith('ATOM') and after_atom == True:
            tail_list.append(line)

    return tail_list

def WriteOutputFile(head_list, atom_list, tail_list):
    '''
    This function will take the 3 lists and will write 3 lists to an output file called output.txt.
    :param head_list:
    :param atom_list:
    :param tail_list:
    :return:
    '''

    output_file = open('output.txt', 'w')

    for line in head_list:
        output_file.write(line)
    for line in atom_list:
        output_file.write(line)
    for line in tail_list:
        output_file.write(line)

    output_file.close()


if __name__ == '__main__':
    all_file_contents = ReadFileContents('1JKB.pdb')
    print(type(all_file_contents))

    head_list = BuildHeadList(all_file_contents)
    print(type(all_file_contents))

    atom_list = BuildAtomList(all_file_contents)
    print(type(all_file_contents))

    tail_list = BuildTailList(all_file_contents)
    print(type(all_file_contents))