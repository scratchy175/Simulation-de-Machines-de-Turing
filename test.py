import itertools

stuff = [0,1,'_','#']*3

for subset in itertools.combinations(stuff, 3):
    print(subset)