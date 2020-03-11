boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

def pairs_list(list1, list2):
    if len(list1) != len(list2):
        print("К сожалению один список короче другого, следовательно, кто-то останется без пары")
        return 0
    else:
        ideal_pairs = zip(list1, list2)
        print("Идеальные пары:")
        for pair in ideal_pairs:
            print(pair[0], "и", pair[1])

pairs_list(sorted(boys),sorted(girls))
