# Drawing an english ruler
def draw_line(tick_len, tick_label=''):
    line = '-' * tick_len

    if tick_label:
        line += ' ' + tick_label

    print(line)


def draw_interval(center_len):
    if center_len > 0:
        current_center_len = center_len - 1

        draw_interval(current_center_len)
        draw_line(center_len)
        draw_interval(current_center_len)


def draw_ruler(num_inches, major_len):
    draw_line(major_len, '0')

    for i in range(1, num_inches + 1):
        draw_interval(major_len - 1)
        draw_line(major_len, str(i))


if __name__ == "__main__":
    print(draw_ruler(2, 4))
