
def set_converted_bytes_with_label(size_in_bytes):
    kilobyte = 1024
    megabyte = kilobyte * kilobyte
    gigabyte = megabyte * kilobyte

    if kilobyte < size_in_bytes < megabyte:
        converted_size = size_in_bytes / kilobyte
        label = 'KB'
    elif megabyte < size_in_bytes < gigabyte:
        converted_size = size_in_bytes / megabyte
        label = 'MB'
    elif size_in_bytes >= gigabyte:
        converted_size = size_in_bytes / gigabyte
        label = 'GB'
    else:
        converted_size = size_in_bytes
        label = 'B'

    return {'size': converted_size, 'label': label}
