import datetime
import logging
import time

char_dir = 'A:\\SteamLibrary\\steamapps\\common\\DB Xenoverse 2\\data\chara'
game_directory = 'A:\\SteamLibrary\\steamapps\\common\\DB Xenoverse 2'
data_directory = 'A:\\SteamLibrary\\steamapps\\common\\DB Xenoverse 2\\data'
char_slot_file = 'A:\\SteamLibrary\\steamapps\\common\\DB Xenoverse 2\\data\\XV2P_SLOTS.x2s'
char_slot_backup_directory = 'A:\\SteamLibrary\\steamapps\\common\\DB Xenoverse 2\\data\\slot_backups'
base_char_id_list = ['GOK', 'BDK', 'GK4', 'GOD', 'GKG', 'GTG', 'GHS', 'GHM', 'GHL', 'PIC', 'KLL', 'YMC', 'TSH', 'RAD',
                     'SBM', 'NAP', 'VGT', 'VG4', 'GRD', 'BAT', 'RCM', 'JES', 'GNY', 'FRZ', 'FR4', 'FR5', 'TRX', 'TRS',
                     'G17', 'S17', 'G18', 'CL3', 'CL4', 'CLJ', 'VDL', 'BUL', 'BUM', 'BUS', 'GTX', 'VTO', 'BRL', 'BLS',
                     'PAN', 'GIL', 'OSV', 'OSB', 'OBB', 'SD3', 'SD4', 'SD1', 'GGT', 'STN', 'DMG', 'DM2', 'SIN', 'TOK',
                     'BUZ', 'APL', 'RSB', 'GHP', 'MIR', 'TOW', 'WIS', 'HST', 'JCO', 'POD', 'FRG', 'STD', 'OSN', 'CL1',
                     'TKT', 'TK3', 'ROK', 'GGK', 'GVG', 'GFR', 'G16', 'COL', 'CO2', 'GHF', 'TLS', 'JNB', 'FOF', 'TG1',
                     'TG2', 'TG3', 'TG4', 'TG5', 'NP1', 'NP2', 'NP3', 'NP4', 'HUM', 'HUF', 'SYM', 'SYF', 'NMC', 'FRI',
                     'MAM', 'MAF', 'MAP', 'TE0', 'TE1', 'EL0', 'TWP', 'TWT', 'THJ', 'THG', 'THC', 'THK', 'GG1', 'SLG',
                     'ZBN', 'DDR', 'NIL', 'MRN', 'HIT', 'DND', 'SCR', 'BLM', 'JNG', 'GKB', 'TRF', 'FRS', 'CAB', 'HIK',
                     'VDS', 'CMP', 'ZMS', 'GBR', 'BJK', 'VTB', 'ZMG', 'ZMD', 'BUU', 'DBR', 'G13', 'TPO', 'R17', 'JRN',
                     'FUU', 'GKS', 'KFL', 'SB2', 'TM0', 'TM1', 'NI0', 'NI1', 'NI2', 'BLF', 'FOK', 'FOD', 'FOV', 'CL2',
                     'URN', 'RSV', 'CPY', 'OWN', 'LPA', 'AVB', 'AVC', 'MST', 'PTN', 'XEN', 'XEG']
installed_char_id_list = []
empty_char_list = []


def get_datetime():
    timestamp = time.time()
    return datetime.datetime.fromtimestamp(timestamp).strftime('%m_%d_%H_%M')

def setup_logger():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.debug('This message should appear on the console')
    logging.info('So should this')
    logging.warning('And this, too')
    return logging.getLogger()