rules = {}
updates = []

halfway = False

with open('5_input.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        if not line.strip():
            halfway = True
            continue
        
        if not halfway:
            key, value = int(line.split('|')[0]), int(line.split('|')[1])
            if not rules.__contains__(key):
                rules[key] = [value]
            else:
                rules[key].append(value)
        else:
            updates.append(list(map(int, line.split(','))))

count = 0

for update in updates:
    def innerLoop():
        for idx, num in enumerate(update):
            if idx == 0:
                continue # skip the first one, all the rules will always be true
            if num in rules:
                rule = rules[num]
                existing = update[:idx-1]

                if not set(existing).isdisjoint(set(rule)):
                    return 0
        
        return update[int((len(update)-1)/2)]
    
    count += innerLoop()

print(count)