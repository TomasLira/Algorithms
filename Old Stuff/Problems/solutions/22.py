from sys import maxsize

def gas_station(gas,cost):
        net_list = [i - j for i,j in zip(gas,cost)]
        if sum(net_list) < 0:
            return -1
        max_counter = -maxsize
        start_idx = -1
        counter = 0
        for idx,num in reversed(list(enumerate(net_list))):
            counter  += num
            if max_counter < counter:
                start_idx = idx
                max_counter = counter
        return start_idx