def solution(commands):
    map_commands = {}
    current_bucket = None
    for command in commands:
        if 'goto' in command:
            current_bucket = command.split()[1]
            if current_bucket not in map_commands:
                map_commands[current_bucket] = []
        else:
            file_name = command.split()[1]
            if file_name not in map_commands[current_bucket]:
                map_commands[current_bucket].append(file_name)
    return sorted(map_commands.items(),key = lambda x : len(x[1]), reverse = 1)[0][0] if map_commands else None
