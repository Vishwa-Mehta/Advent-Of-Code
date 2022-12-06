import sys

def get_buffer() -> str:
    buff = ""
    for _ in sys.stdin:
        _ = _.strip()
        buff += _
    return buff

def get_marker_pos(buff:str, window_len:int) -> int:

    window = buff[:window_len]
    marker_pos = 0
    distinct_chars = 0
    curr_window_char = 0
    old_marker_pos = 0

    while curr_window_char < window_len:
        if distinct_chars < window_len:
            if window.count(window[curr_window_char]) > 1:
                marker_pos = old_marker_pos + window.index(window[curr_window_char]) + 1
                window = buff[marker_pos:marker_pos+window_len]
                distinct_chars = 0
                curr_window_char = 0
                old_marker_pos = marker_pos
            else:
                distinct_chars += 1
                marker_pos += 1
                curr_window_char += 1

    return marker_pos

buff = get_buffer()

# part 1
win_len = 4
print(get_marker_pos(buff, win_len))

# part 2
win_len = 14
print(get_marker_pos(buff, win_len))
