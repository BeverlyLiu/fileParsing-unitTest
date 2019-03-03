import file_parsing_module as fpm

def Diff2Files(file_1, file_2):
    '''
    This function will open both files reading in all lines into 2 separate variables and compare the 2 to determine
    if the files are different.
    :param file_1:
    :param file2:
    :return:
    '''

    open_file = open(file_1)
    file_1_contents = open_file.readlines()
    open_file.close()

    open_file = open(file_2)
    file_2_contents = open_file.readlines()
    open_file.close()

    diff_list = []

    for index, line in enumerate(file_1_contents):
        if file_1_contents[index] != file_2_contents[index]:
            diff_list.append(line)

    print("The number of difference between the 2 files: ", len(diff_list))


def Run():
    file_name = fpm.AskForFileName()
    all_file_contents = fpm.ReadFileContents(file_name)
    head_list = fpm.BuildHeadList(all_file_contents)
    atom_list = fpm.BuildAtomList(all_file_contents)
    tail_list = fpm.BuildTailList(all_file_contents)
    fpm.WriteOutputFile(head_list,atom_list,tail_list)
    Diff2Files('1JKB.pdb', 'output.txt')


if __name__ == '__main__':
    Run()