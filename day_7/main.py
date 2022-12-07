from dataclasses import dataclass
from typing import List

active_ls_read = False

TOTAL_MEMORY = 70000000
DESIRED_MEMORY = 30000000
valid_dir_sizes = []
valid_dir_sizes_for_deletion = []


class DirectoryObject:
    def __init__(self, name):
        self.name = name
        self.parent_dir = None
        self.child_dirs = []
        self.files = []

    def set_parent_dir(self, parent_dir):
        self.parent_dir = parent_dir

    def append_child_dir(self, child_dir):
        self.child_dirs.append(child_dir)

    def append_file(self, file_in_file):
        self.files.append(file_in_file)

    def get_parent_dir(self):
        return self.parent_dir

    def get_child_dir(self):
        return self.child_dirs

    def get_child_dir_names(self):
        return [child.name for child in self.child_dirs]

    def get_child_with_matching_name(self, seach_name: str):
        for child in self.child_dirs:
            if child.name == seach_name:
                return child


@dataclass
class File:
    name: str
    size: int


def get_command_blocks():
    global active_ls_read
    command_list = []
    current_ls_stack = []
    with open('input.csv', 'r') as input_file:
        for line in input_file:
            if line.startswith('$') and active_ls_read:
                command_list.append(current_ls_stack.copy())
                current_ls_stack.clear()
                active_ls_read = False
            if line.startswith('$ cd'):
                command_list.append(line.strip())
            if line.startswith('$ ls'):
                current_ls_stack.append(line.strip())
                active_ls_read = True
            if not line.startswith('$'):
                current_ls_stack.append(line.strip())
    return command_list


def perform_cd(command_line: str, current_dir: DirectoryObject):
    _, _, target_dir = command_line.split(' ')
    if target_dir == '..':
        return current_dir.get_parent_dir()
    else:
        if target_dir in current_dir.get_child_dir_names():
            return current_dir.get_child_with_matching_name(target_dir)
        else:
            new_dir = DirectoryObject(target_dir)
            new_dir.set_parent_dir(current_dir)
            current_dir.append_child_dir(new_dir)
            return new_dir


def perform_ls(list_entries: List[str], current_dir: DirectoryObject):
    for entry in list_entries:
        if not entry.startswith('$'):
            if not entry.startswith('dir'):
                file_size, filename = entry.split(' ')
                current_dir.append_file(File(filename, int(file_size)))
    return current_dir


def get_root_dir(dir_state: DirectoryObject):
    iter_dir = dir_state
    while iter_dir.name != '/':
        iter_dir = iter_dir.get_parent_dir()
    return iter_dir


def check_dir_sizes(root_dir: DirectoryObject):
    global valid_dir_sizes
    dir_size = 0
    for file in root_dir.files:
        dir_size += file.size
    for child in root_dir.child_dirs:
        dir_size += check_dir_sizes(child)
    if dir_size < 100000:
        valid_dir_sizes.append(dir_size)
    return dir_size


def get_dir_size(input_dir: DirectoryObject):
    dir_size = 0
    for file in input_dir.files:
        dir_size += file.size
    for child in input_dir.child_dirs:
        dir_size += check_dir_sizes(child)
    return dir_size


def check_dir_for_deletion(input_dir: DirectoryObject, target_space: int):
    global valid_dir_sizes_for_deletion
    dir_size = get_dir_size(input_dir)
    if dir_size > target_space:
        valid_dir_sizes_for_deletion.append(dir_size)
        for child in input_dir.get_child_dir():
            check_dir_for_deletion(child, target_space)


if __name__ == '__main__':
    current_dir_state = DirectoryObject('default')
    for command in get_command_blocks():
        if isinstance(command, str):
            current_dir_state = perform_cd(command, current_dir_state)
        if isinstance(command, list):
            perform_ls(command, current_dir_state)

    root_dir = get_root_dir(current_dir_state)
    check_dir_sizes(root_dir)
    print(f'sum of all valid directories: {sum(valid_dir_sizes)}')

    unused_space = TOTAL_MEMORY - get_dir_size(root_dir)
    target_space_for_deletion = DESIRED_MEMORY - unused_space
    check_dir_for_deletion(root_dir, target_space_for_deletion)
    candidate_size_to_delete = min(valid_dir_sizes_for_deletion)
    print(f'Candidate to delete has the size: {candidate_size_to_delete}')
