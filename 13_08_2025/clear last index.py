def clear_last_bit(value,index):
    mask = ~0
    mask = mask<< index
    res = value | mask
    print(res) 