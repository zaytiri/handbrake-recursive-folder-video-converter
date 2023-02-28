def split_string(string, separator, stop_character, include_separator=False):
    """
    Splits a given string into a list using a separator except when a sub-string is between a specific stop character.
    :param include_separator: boolean to specify if the separator character must be included in the list or not
    :param string: string to be split
    :param separator: separator to split the string
    :param stop_character: split does not happen between two of these characters
    :return: a list containing the string but separated between specified separator
    """
    list_of_params = []
    param = ''

    is_between = False
    for character in string:
        if is_between:
            if character == stop_character:
                is_between = False
                if not include_separator:
                    continue
        else:
            if character == stop_character:
                is_between = True
                if not include_separator:
                    continue

            if character == separator:
                list_of_params.append(param)
                param = ''
                continue

        param += character

    list_of_params.append(param)

    return list_of_params
