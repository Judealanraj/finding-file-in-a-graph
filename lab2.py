#here we are using deapth first search to ensure searching indeapth as much as possible
# before going to beside nodes..



def read_input(file_path):                          #read a file with given style of file writing and put them into tre structure.
    tree = {}
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                node, children = line.split(':')
                node = node.strip()
                children = [child.strip() for child in children.split(',')] if children.strip() else []
                tree[node] = children
    return tree

def dfs(tree, start_node, target_file, path=None):      #depth first searching algorithm
    if path is None:
        path = []

    path.append(start_node)

    if start_node == target_file:
        return path

    for child in tree.get(start_node, []):
        if child not in path:  # Avoid cycles
            result = dfs(tree, child, target_file, path)
            if result:  # If found, return the path
                return result

    path.pop()  # Remove the node if not found in this path
    return None

def find_file_path(file_path, target_file):         #function for find correct path of matching file
    tree = read_input(file_path)
    start_node = 'root'
    path = dfs(tree, start_node, target_file)
    return path if path else []


input_file = 'C:\\Users\\alan\\Desktop\\input.txt'             # here we must use our input file path
target_file = 'file2'
path_to_file = find_file_path(input_file, target_file)
print(path_to_file)
