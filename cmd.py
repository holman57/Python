
if __name__ == '__main__':
    N = int(input())
    inputs = [input() for _ in range(N)]
    sequence = []
    while len(inputs) > 0:
        cmd = inputs.pop(0).split(' ')
        if cmd[0] == 'insert':
            sequence.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(sequence)
        elif cmd[0] == 'remove':
            sequence.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            sequence.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            sequence.sort()
        elif cmd[0] == 'pop':
            sequence.pop()
        elif cmd[0] == 'reverse':
            sequence.reverse()
        
            