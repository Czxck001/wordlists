grouppath = 'note/groups.md'
lines = []
for line in open(grouppath):
    if line.strip():
        tokens = line.strip().split(':')
        lines.append('### {}'.format(tokens[0]))
        lines.append(''.join(tokens[1:]).strip())
    else:
        lines.append('')

with open('test.md', 'w') as f:
    f.write('\n'.join(lines))
