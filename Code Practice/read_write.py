with open('test.txt','r') as read:
    content = read.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)