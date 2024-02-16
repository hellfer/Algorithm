def solution(my_string, is_prefix):
    prefix_length = len(is_prefix)
    if my_string[-prefix_length:] == is_prefix:
        return 1
    else:
        return 0
