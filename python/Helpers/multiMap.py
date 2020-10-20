# multiMap(3, [0, 20, 40, 60, 80, 100], [0, 15, 43, 53, 75, 100], 100)

def multiMap(val, _in, _out, size):
    if (val <= _in[0]):
        return _out[0]

    if len(_in) > (size - 1) and val >= _in[size - 1]:
        return _out[int(size) - 1]

    # search right interval
    pos = 1  # _in[0] allready tested
    while val > _in[pos]:
        pos += 1

    # this will handle all exact "points" in the _in array
    if val == _in[pos]:
        return _out[pos]

    # interpolate in the right segment for the rest
    return (val - _in[pos - 1]) * (_out[pos] - _out[pos - 1]) / (_in[pos] - _in[pos - 1]) + _out[pos - 1]
