import timeit

def read_label_txt(filename):
    start_total_time = timeit.default_timer()
    
    labels = {}
    
    with open(filename, "r") as f:
        for line in f:
            if line[0] == "#":
                continue
            else:
                ind = int(line.split()[0])
                label = int(line.split()[1])
                
                if label not in labels.keys():
                    labels[label] = set()
                    labels[label].add(ind)
                else:
                    labels[label].add(ind)
                
    end_total_time = timeit.default_timer() - start_total_time
    print('Time read labels in txt file:', end_total_time)
    
    return labels