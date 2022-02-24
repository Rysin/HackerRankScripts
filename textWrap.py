def wrap(string, max_width):
    _string = list(string)
    jj = [_string[i:i+4] for i in range(0, len(_string)+1, max_width)]
    _jj = [''.join(chunk) for chunk in jj]
    return str('\n'.join(_jj))


if __name__ == '__main__':
    string, max_width = 'bscnksbcjscksbcjksbckjdscsbdcbsdkjbcsdjcbsdjkcbsdkjbckjdsbjksd', 11
    result = wrap(string, max_width)
    print(result)
