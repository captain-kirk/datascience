def read_fasta(filename):
    """Returns a dictionary associating labels with DNA."""
    result = {}
    with open(filename, 'rt') as f:
        dna = ''
        label = ''
        for line in f:
            if line.startswith('>'):
                if label != '':
                    result[label] = dna
                label = line[1:-1]
                dna = ''
            else:
                dna += line[:-1]
        result[label] = dna
        return result

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and all(data[0][i:i+j] in x for x in data):
                    substr = data[0][i:i+j]
    return substr


def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


def findsub():
    data = read_fasta("dnasub.txt")
    sequences = []
    #findprint(data)
    for key in data:
    	sequences.append(data[key])
     
#    print(sequences)
    
    longsub = long_substr(sequences)
    print(longsub)