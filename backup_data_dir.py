import logging
import os
import shutil

from common import data_directory, mod_data_directory, get_datetime, game_directory, setup_logger

logger = setup_logger()


def zip_data(src, zip_dir):
    if not os.path.exists(zip_dir):
        os.makedirs(zip_dir)
    backslash_char = "\\"
    zip_file_path = os.path.join(zip_dir, f'{src.split(backslash_char).pop()}_backup_{get_datetime()}')
    shutil.make_archive(zip_file_path, format='zip', root_dir=src, logger=logger)


if __name__ == '__main__':
    zip_data(data_directory, os.path.join(game_directory, 'data_backups'))
    zip_data(mod_data_directory, os.path.join(game_directory, 'data_backups'))
