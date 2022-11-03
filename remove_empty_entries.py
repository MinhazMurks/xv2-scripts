import os

from common import char_dir, installed_char_id_list, base_char_id_list


def populate_installed_chars():
    installed_char_id_list.extend(os.listdir(char_dir))


if __name__ == '__main__':
    populate_installed_chars()
