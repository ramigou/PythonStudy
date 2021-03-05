rating = open('rating.txt', 'r')
rating_dict = {}
for line in rating.readlines():
    name = line.split()[0]
    score = int(line.split()[1].rstrip('\n'))
    rating_dict[name] = score

print(rating_dict)