import datetime
import os.path
import time
import shutil
from common import char_slot_file, char_slot_backup_directory, installed_char_id_list, base_char_id_list, \
    empty_char_list, get_datetime
from remove_empty_entries import populate_installed_chars

slot_placement_dict = {
    'character_code': 0,
    'costume_index': 1,
    'model_preset': 2,
    'unlock_index': 3,
    'flag_gk2': 4,
    'voice_id_1': 5,
    'voice_id_2': 6,
    'dlc_val_1': 7,
    'dlc_val_2': 8,
}

slot_entry_set = set()
write_slots_list = []
dupe_list = []


class SlotEntry:
    def __init__(self, entry_string):
        values_list = entry_string.split(',')

        self.char_code = values_list[slot_placement_dict['character_code']]

        self.costume_index = int(values_list[slot_placement_dict['costume_index']])
        self.model_preset = int(values_list[slot_placement_dict['model_preset']])
        self.unlock_index = int(values_list[slot_placement_dict['unlock_index']])

        self.flag_gk2 = int(values_list[slot_placement_dict['flag_gk2']])

        self.voice_id_1 = int(values_list[slot_placement_dict['voice_id_1']])
        self.voice_id_2 = int(values_list[slot_placement_dict['voice_id_2']])

        self.dlc_val_1 = int(values_list[slot_placement_dict['dlc_val_1']])
        self.dlc_val_2 = int(values_list[slot_placement_dict['dlc_val_2']])

    def write_string(self):
        return f'[{self.char_code},{self.costume_index},{self.model_preset},{self.unlock_index},{self.flag_gk2},{self.voice_id_1},{self.voice_id_2},{self.dlc_val_1},{self.dlc_val_2}]'

    def __eq__(self, other):
        if isinstance(other, SlotEntry):
            return self.char_code == other.char_code and \
                   self.costume_index == other.costume_index and \
                   self.model_preset == other.model_preset and \
                   self.unlock_index == other.unlock_index

        return False

    def __repr__(self):
        return f'[{self.char_code},{self.costume_index},{self.model_preset},{self.unlock_index},{self.flag_gk2},{self.voice_id_1},{self.voice_id_2},{self.dlc_val_1},{self.dlc_val_2}]'

    def __hash__(self):
        return hash((self.char_code, self.costume_index, self.model_preset, self.unlock_index))


class Slot:
    def __init__(self):
        self.slot_entries = []

    def add_slot_entry(self, new_slot_entry):
        if isinstance(new_slot_entry, SlotEntry):
            self.slot_entries.append(new_slot_entry)

    def write_string(self):
        slot_entry_strings = []
        for slot_entry in self.slot_entries:
            if isinstance(slot_entry, SlotEntry):
                slot_entry_strings.append(slot_entry.write_string())
        return '{' + ''.join(slot_entry_strings) + '}'

    def is_empty(self):
        return len(self.slot_entries) == 0

    def __repr__(self):
        return '{' + f'{self.slot_entries}' + '}'

    def __str__(self):
        return '{' + f'{self.slot_entries}' + '}'


def read_slot_entry(file_reader):
    char_list = []
    while True:
        char = file_reader.read(1)
        if not char:
            print("EOF REACHED, THIS IS BAD")
            break
        if char == ']':
            return SlotEntry(''.join(char_list))
        char_list.append(char)


def read_slot_entries(file_reader, remove_empties):
    current_slot = Slot()
    while True:
        char = file_reader.read(1)
        if not char:
            print("EOF REACHED, THIS IS BAD")
            break
        if char == '}':
            return current_slot
        if char == '[':
            slot_entry = read_slot_entry(file_reader)

            if slot_entry in slot_entry_set:
                dupe_list.append(slot_entry.write_string())
            else:
                if slot_entry.char_code not in base_char_id_list and slot_entry.char_code not in installed_char_id_list:
                    empty_char_list.append(slot_entry)
                    if not remove_empties:
                        slot_entry_set.add(slot_entry)
                        current_slot.add_slot_entry(slot_entry)
                else:
                    slot_entry_set.add(slot_entry)
                    current_slot.add_slot_entry(slot_entry)


def write_new_file():
    if not os.path.exists(char_slot_backup_directory):
        os.makedirs(char_slot_backup_directory)
    shutil.copyfile(char_slot_file, f'{char_slot_backup_directory}\\XV2P_SLOTS_backup_{get_datetime()}.x2s')

    with open(char_slot_file, 'w') as file:
        for slot in write_slots_list:
            if isinstance(slot, Slot):
                file.write(f'{slot.write_string()}')


def remove_duplicates(remove_empties):
    with open(char_slot_file, 'r') as file:
        while True:
            char = file.read(1)

            if not char:
                break
            if char == '{':
                slot = read_slot_entries(file, remove_empties)
                if not slot.is_empty():
                    write_slots_list.append(slot)


def show_results(show_dupes, show_empties, show_slots):
    if show_dupes:
        print(f'Found {len(dupe_list)} duplicates:')
        for dupe in dupe_list:
            print(dupe)

    if show_empties:
        print(f'Found {len(empty_char_list)} empty entries:')
        for empty in empty_char_list:
            print(empty)

    if show_slots:
        print('All Slots: ')
        for slot in write_slots_list:
            print(slot.write_string())


if __name__ == '__main__':
    populate_installed_chars()
    remove_duplicates(True)
    write_new_file()
    show_results(True, True, False)
