#!/usr/bin/env python3

from enum import Enum, auto
import numpy as np
import json

class IPT(Enum):
    IPT_NONE = 0
    IPT_END = auto()
    IPT_PORT = auto()
    IPT_JOYSTICK_UP = auto()
    IPT_JOYSTICK_DOWN = auto()
    IPT_JOYSTICK_LEFT = auto()
    IPT_JOYSTICK_RIGHT = auto()
    IPT_JOYSTICKRIGHT_UP = auto()
    IPT_JOYSTICKRIGHT_DOWN = auto()
    IPT_JOYSTICKRIGHT_LEFT = auto()
    IPT_JOYSTICKRIGHT_RIGHT = auto()
    IPT_JOYSTICKLEFT_UP = auto()
    IPT_JOYSTICKLEFT_DOWN = auto()
    IPT_JOYSTICKLEFT_LEFT = auto()
    IPT_JOYSTICKLEFT_RIGHT = auto()
    IPT_BUTTON1 = auto()
    IPT_BUTTON2 = auto()
    IPT_BUTTON3 = auto()
    IPT_BUTTON4 = auto()
    IPT_BUTTON5 = auto()
    IPT_BUTTON6 = auto()
    IPT_BUTTON7 = auto()
    IPT_BUTTON8 = auto()
    IPT_BUTTON9 = auto()
    IPT_BUTTON10 = auto()
    IPT_ANALOG_START = auto()
    IPT_PADDLE = auto()
    IPT_PADDLE_V = auto()
    IPT_DIAL = auto()
    IPT_DIAL_V = auto()
    IPT_TRACKBALL_X = auto()
    IPT_TRACKBALL_Y = auto()
    IPT_AD_STICK_X = auto()
    IPT_AD_STICK_Y = auto()
    IPT_AD_STICK_Z = auto()
    IPT_LIGHTGUN_X = auto()
    IPT_LIGHTGUN_Y = auto()
    IPT_PEDAL = auto()
    IPT_PEDAL2 = auto()
    IPT_ANALOG_END = auto()
    IPT_START1 = auto()
    IPT_START2 = auto()
    IPT_START3 = auto()
    IPT_START4 = auto()
    IPT_COIN1 = auto()
    IPT_COIN2 = auto()
    IPT_COIN3 = auto()
    IPT_COIN4 = auto()
    IPT_SERVICE1 = auto()
    IPT_SERVICE2 = auto()
    IPT_SERVICE3 = auto()
    IPT_SERVICE4 = auto()
    IPT_SERVICE = auto()
    IPT_TILT = auto()
    IPT_DIPSWITCH_NAME = auto()
    IPT_DIPSWITCH_SETTING = auto()
    IPT_VBLANK = auto()
    IPT_UNKNOWN = auto()
    IPT_OSD_DESCRIPTION = auto()
    IPT_OSD_1 = auto()
    IPT_OSD_2 = auto()
    IPT_OSD_3 = auto()
    IPT_OSD_4 = auto()
    IPT_EXTENSION = auto()
    IPT_UI_CONFIGURE = auto()
    IPT_UI_ON_SCREEN_DISPLAY = auto()
    IPT_UI_RESET_MACHINE = auto()
    IPT_UI_SHOW_GFX = auto()
    IPT_UI_TOGGLE_CHEAT = auto()
    IPT_UI_UP = auto()
    IPT_UI_DOWN = auto()
    IPT_UI_LEFT = auto()
    IPT_UI_RIGHT = auto()
    IPT_UI_SELECT = auto()
    IPT_UI_CANCEL = auto()
    IPT_UI_TOGGLE_UI = auto()
    IPT_UI_ADD_CHEAT = auto()
    IPT_UI_DELETE_CHEAT = auto()
    IPT_UI_SAVE_CHEAT = auto()
    IPT_UI_WATCH_VALUE = auto()
    IPT_UI_EDIT_CHEAT = auto()
    IPT_START5 = auto()
    IPT_START6 = auto()
    IPT_START7 = auto()
    IPT_START8 = auto()
    IPT_COIN5 = auto()
    IPT_COIN6 = auto()
    IPT_COIN7 = auto()
    IPT_COIN8 = auto()

class Keycode(Enum):
    KEYCODE_A = 0,
    KEYCODE_B = auto()
    KEYCODE_C = auto()
    KEYCODE_D = auto()
    KEYCODE_E = auto()
    KEYCODE_F = auto()
    KEYCODE_G = auto()
    KEYCODE_H = auto()
    KEYCODE_I = auto()
    KEYCODE_J = auto()
    KEYCODE_K = auto()
    KEYCODE_L = auto()
    KEYCODE_M = auto()
    KEYCODE_N = auto()
    KEYCODE_O = auto()
    KEYCODE_P = auto()
    KEYCODE_Q = auto()
    KEYCODE_R = auto()
    KEYCODE_S = auto()
    KEYCODE_T = auto()
    KEYCODE_U = auto()
    KEYCODE_V = auto()
    KEYCODE_W = auto()
    KEYCODE_X = auto()
    KEYCODE_Y = auto()
    KEYCODE_Z = auto()
    KEYCODE_0 = auto()
    KEYCODE_1 = auto()
    KEYCODE_2 = auto()
    KEYCODE_3 = auto()
    KEYCODE_4 = auto()
    KEYCODE_5 = auto()
    KEYCODE_6 = auto()
    KEYCODE_7 = auto()
    KEYCODE_8 = auto()
    KEYCODE_9 = auto()
    KEYCODE_0_PAD = auto()
    KEYCODE_1_PAD = auto()
    KEYCODE_2_PAD = auto()
    KEYCODE_3_PAD = auto()
    KEYCODE_4_PAD = auto()
    KEYCODE_5_PAD = auto()
    KEYCODE_6_PAD = auto()
    KEYCODE_7_PAD = auto()
    KEYCODE_8_PAD = auto()
    KEYCODE_9_PAD = auto()
    KEYCODE_F1 = auto()
    KEYCODE_F2 = auto()
    KEYCODE_F3 = auto()
    KEYCODE_F4 = auto()
    KEYCODE_F5 = auto()
    KEYCODE_F6 = auto()
    KEYCODE_F7 = auto()
    KEYCODE_F8 = auto()
    KEYCODE_F9 = auto()
    KEYCODE_F10 = auto()
    KEYCODE_F11 = auto()
    KEYCODE_F12 = auto()
    KEYCODE_ESC = auto()
    KEYCODE_TILDE = auto()
    KEYCODE_MINUS = auto()
    KEYCODE_EQUALS = auto()
    KEYCODE_BACKSPACE = auto()
    KEYCODE_TAB = auto()
    KEYCODE_OPENBRACE = auto()
    KEYCODE_CLOSEBRACE = auto()
    KEYCODE_ENTER = auto()
    KEYCODE_COLON = auto()
    KEYCODE_QUOTE = auto()
    KEYCODE_BACKSLASH = auto()
    KEYCODE_BACKSLASH2 = auto()
    KEYCODE_COMMA = auto()
    KEYCODE_STOP = auto()
    KEYCODE_SLASH = auto()
    KEYCODE_SPACE = auto()
    KEYCODE_INSERT = auto()
    KEYCODE_DEL = auto()
    KEYCODE_HOME = auto()
    KEYCODE_END = auto()
    KEYCODE_PGUP = auto()
    KEYCODE_PGDN = auto()
    KEYCODE_LEFT = auto()
    KEYCODE_RIGHT = auto()
    KEYCODE_UP = auto()
    KEYCODE_DOWN = auto()
    KEYCODE_SLASH_PAD = auto()
    KEYCODE_ASTERISK = auto()
    KEYCODE_MINUS_PAD = auto()
    KEYCODE_PLUS_PAD = auto()
    KEYCODE_DEL_PAD = auto()
    KEYCODE_ENTER_PAD = auto()
    KEYCODE_PRTSCR = auto()
    KEYCODE_PAUSE = auto()
    KEYCODE_LSHIFT = auto()
    KEYCODE_RSHIFT = auto()
    KEYCODE_LCONTROL = auto()
    KEYCODE_RCONTROL = auto()
    KEYCODE_LALT = auto()
    KEYCODE_RALT = auto()
    KEYCODE_SCRLOCK = auto()
    KEYCODE_NUMLOCK = auto()
    KEYCODE_CAPSLOCK = auto()
    KEYCODE_LWIN = auto()
    KEYCODE_RWIN = auto()
    KEYCODE_MENU = auto()
    JOYCODE_1_LEFT = auto()
    JOYCODE_1_RIGHT = auto()
    JOYCODE_1_UP = auto()
    JOYCODE_1_DOWN = auto()
    JOYCODE_1_BUTTON1 = auto()
    JOYCODE_1_BUTTON2 = auto()
    JOYCODE_1_BUTTON3 = auto()
    JOYCODE_1_BUTTON4 = auto()
    JOYCODE_1_BUTTON5 = auto()
    JOYCODE_1_BUTTON6 = auto()
    JOYCODE_1_BUTTON7 = auto()
    JOYCODE_1_BUTTON8 = auto()
    JOYCODE_1_BUTTON9 = auto()
    JOYCODE_1_BUTTON10 = auto()
    JOYCODE_1_START = auto()
    JOYCODE_1_SELECT = auto()
    JOYCODE_2_LEFT = auto()
    JOYCODE_2_RIGHT = auto()
    JOYCODE_2_UP = auto()
    JOYCODE_2_DOWN = auto()
    JOYCODE_2_BUTTON1 = auto()
    JOYCODE_2_BUTTON2 = auto()
    JOYCODE_2_BUTTON3 = auto()
    JOYCODE_2_BUTTON4 = auto()
    JOYCODE_2_BUTTON5 = auto()
    JOYCODE_2_BUTTON6 = auto()
    JOYCODE_2_BUTTON7 = auto()
    JOYCODE_2_BUTTON8 = auto()
    JOYCODE_2_BUTTON9 = auto()
    JOYCODE_2_BUTTON10 = auto()
    JOYCODE_2_START = auto()
    JOYCODE_2_SELECT = auto()
    JOYCODE_3_LEFT = auto()
    JOYCODE_3_RIGHT = auto()
    JOYCODE_3_UP = auto()
    JOYCODE_3_DOWN = auto()
    JOYCODE_3_BUTTON1 = auto()
    JOYCODE_3_BUTTON2 = auto()
    JOYCODE_3_BUTTON3 = auto()
    JOYCODE_3_BUTTON4 = auto()
    JOYCODE_3_BUTTON5 = auto()
    JOYCODE_3_BUTTON6 = auto()
    JOYCODE_3_BUTTON7 = auto()
    JOYCODE_3_BUTTON8 = auto()
    JOYCODE_3_BUTTON9 = auto()
    JOYCODE_3_BUTTON10 = auto()
    JOYCODE_3_START = auto()
    JOYCODE_3_SELECT = auto()
    JOYCODE_4_LEFT = auto()
    JOYCODE_4_RIGHT = auto()
    JOYCODE_4_UP = auto()
    JOYCODE_4_DOWN = auto()
    JOYCODE_4_BUTTON1 = auto()
    JOYCODE_4_BUTTON2 = auto()
    JOYCODE_4_BUTTON3 = auto()
    JOYCODE_4_BUTTON4 = auto()
    JOYCODE_4_BUTTON5 = auto()
    JOYCODE_4_BUTTON6 = auto()
    JOYCODE_4_BUTTON7 = auto()
    JOYCODE_4_BUTTON8 = auto()
    JOYCODE_4_BUTTON9 = auto()
    JOYCODE_4_BUTTON10 = auto()
    JOYCODE_4_START = auto()
    JOYCODE_4_SELECT = auto()
    JOYCODE_MOUSE_1_BUTTON1 = auto()
    JOYCODE_MOUSE_1_BUTTON2 = auto()
    JOYCODE_MOUSE_1_BUTTON3 = auto()
    JOYCODE_MOUSE_2_BUTTON1 = auto()
    JOYCODE_MOUSE_2_BUTTON2 = auto()
    JOYCODE_MOUSE_2_BUTTON3 = auto()
    JOYCODE_MOUSE_3_BUTTON1 = auto()
    JOYCODE_MOUSE_3_BUTTON2 = auto()
    JOYCODE_MOUSE_3_BUTTON3 = auto()
    JOYCODE_MOUSE_4_BUTTON1 = auto()
    JOYCODE_MOUSE_4_BUTTON2 = auto()
    JOYCODE_MOUSE_4_BUTTON3 = auto()
    JOYCODE_5_LEFT = auto()
    JOYCODE_5_RIGHT = auto()
    JOYCODE_5_UP = auto()
    JOYCODE_5_DOWN = auto()
    JOYCODE_5_BUTTON1 = auto()
    JOYCODE_5_BUTTON2 = auto()
    JOYCODE_5_BUTTON3 = auto()
    JOYCODE_5_BUTTON4 = auto()
    JOYCODE_5_BUTTON5 = auto()
    JOYCODE_5_BUTTON6 = auto()
    JOYCODE_5_BUTTON7 = auto()
    JOYCODE_5_BUTTON8 = auto()
    JOYCODE_5_BUTTON9 = auto()
    JOYCODE_5_BUTTON10 = auto()
    JOYCODE_5_START = auto()
    JOYCODE_5_SELECT = auto()
    JOYCODE_6_LEFT = auto()
    JOYCODE_6_RIGHT = auto()
    JOYCODE_6_UP = auto()
    JOYCODE_6_DOWN = auto()
    JOYCODE_6_BUTTON1 = auto()
    JOYCODE_6_BUTTON2 = auto()
    JOYCODE_6_BUTTON3 = auto()
    JOYCODE_6_BUTTON4 = auto()
    JOYCODE_6_BUTTON5 = auto()
    JOYCODE_6_BUTTON6 = auto()
    JOYCODE_6_BUTTON7 = auto()
    JOYCODE_6_BUTTON8 = auto()
    JOYCODE_6_BUTTON9 = auto()
    JOYCODE_6_BUTTON10 = auto()
    JOYCODE_6_START = auto()
    JOYCODE_6_SELECT = auto()
    JOYCODE_7_LEFT = auto()
    JOYCODE_7_RIGHT = auto()
    JOYCODE_7_UP = auto()
    JOYCODE_7_DOWN = auto()
    JOYCODE_7_BUTTON1 = auto()
    JOYCODE_7_BUTTON2 = auto()
    JOYCODE_7_BUTTON3 = auto()
    JOYCODE_7_BUTTON4 = auto()
    JOYCODE_7_BUTTON5 = auto()
    JOYCODE_7_BUTTON6 = auto()
    JOYCODE_7_BUTTON7 = auto()
    JOYCODE_7_BUTTON8 = auto()
    JOYCODE_7_BUTTON9 = auto()
    JOYCODE_7_BUTTON10 = auto()
    JOYCODE_7_START = auto()
    JOYCODE_7_SELECT = auto()
    JOYCODE_8_LEFT = auto()
    JOYCODE_8_RIGHT = auto()
    JOYCODE_8_UP = auto()
    JOYCODE_8_DOWN = auto()
    JOYCODE_8_BUTTON1 = auto()
    JOYCODE_8_BUTTON2 = auto()
    JOYCODE_8_BUTTON3 = auto()
    JOYCODE_8_BUTTON4 = auto()
    JOYCODE_8_BUTTON5 = auto()
    JOYCODE_8_BUTTON6 = auto()
    JOYCODE_8_BUTTON7 = auto()
    JOYCODE_8_BUTTON8 = auto()
    JOYCODE_8_BUTTON9 = auto()
    JOYCODE_8_BUTTON10 = auto()
    JOYCODE_8_START = auto()
    JOYCODE_8_SELECT = auto()
    JOYCODE_MOUSE_5_BUTTON1 = auto()
    JOYCODE_MOUSE_5_BUTTON2 = auto()
    JOYCODE_MOUSE_5_BUTTON3 = auto()
    JOYCODE_MOUSE_6_BUTTON1 = auto()
    JOYCODE_MOUSE_6_BUTTON2 = auto()
    JOYCODE_MOUSE_6_BUTTON3 = auto()
    JOYCODE_MOUSE_7_BUTTON1 = auto()
    JOYCODE_MOUSE_7_BUTTON2 = auto()
    JOYCODE_MOUSE_7_BUTTON3 = auto()
    JOYCODE_MOUSE_8_BUTTON1 = auto()
    JOYCODE_MOUSE_8_BUTTON2 = auto()
    JOYCODE_MOUSE_8_BUTTON3 = auto()
    JOYCODE_MOUSE_1_BUTTON4 = auto()
    JOYCODE_MOUSE_1_BUTTON5 = auto()
    JOYCODE_MOUSE_1_BUTTON6 = auto()
    JOYCODE_MOUSE_2_BUTTON4 = auto()
    JOYCODE_MOUSE_2_BUTTON5 = auto()
    JOYCODE_MOUSE_2_BUTTON6 = auto()
    JOYCODE_MOUSE_3_BUTTON4 = auto()
    JOYCODE_MOUSE_3_BUTTON5 = auto()
    JOYCODE_MOUSE_3_BUTTON6 = auto()
    JOYCODE_MOUSE_4_BUTTON4 = auto()
    JOYCODE_MOUSE_4_BUTTON5 = auto()
    JOYCODE_MOUSE_4_BUTTON6 = auto()
    JOYCODE_MOUSE_5_BUTTON4 = auto()
    JOYCODE_MOUSE_5_BUTTON5 = auto()
    JOYCODE_MOUSE_5_BUTTON6 = auto()
    JOYCODE_MOUSE_6_BUTTON4 = auto()
    JOYCODE_MOUSE_6_BUTTON5 = auto()
    JOYCODE_MOUSE_6_BUTTON6 = auto()
    JOYCODE_MOUSE_7_BUTTON4 = auto()
    JOYCODE_MOUSE_7_BUTTON5 = auto()
    JOYCODE_MOUSE_7_BUTTON6 = auto()
    JOYCODE_MOUSE_8_BUTTON4 = auto()
    JOYCODE_MOUSE_8_BUTTON5 = auto()
    JOYCODE_MOUSE_8_BUTTON6 = auto()
    JOYCODE_1_LEFT_LEFT = auto()
    JOYCODE_1_LEFT_RIGHT = auto()
    JOYCODE_1_LEFT_UP = auto()
    JOYCODE_1_LEFT_DOWN = auto()
    JOYCODE_2_LEFT_LEFT = auto()
    JOYCODE_2_LEFT_RIGHT = auto()
    JOYCODE_2_LEFT_UP = auto()
    JOYCODE_2_LEFT_DOWN = auto()
    JOYCODE_3_LEFT_LEFT = auto()
    JOYCODE_3_LEFT_RIGHT = auto()
    JOYCODE_3_LEFT_UP = auto()
    JOYCODE_3_LEFT_DOWN = auto()
    JOYCODE_4_LEFT_LEFT = auto()
    JOYCODE_4_LEFT_RIGHT = auto()
    JOYCODE_4_LEFT_UP = auto()
    JOYCODE_4_LEFT_DOWN = auto()
    JOYCODE_5_LEFT_LEFT = auto()
    JOYCODE_5_LEFT_RIGHT = auto()
    JOYCODE_5_LEFT_UP = auto()
    JOYCODE_5_LEFT_DOWN = auto()
    JOYCODE_6_LEFT_LEFT = auto()
    JOYCODE_6_LEFT_RIGHT = auto()
    JOYCODE_6_LEFT_UP = auto()
    JOYCODE_6_LEFT_DOWN = auto()
    JOYCODE_7_LEFT_LEFT = auto()
    JOYCODE_7_LEFT_RIGHT = auto()
    JOYCODE_7_LEFT_UP = auto()
    JOYCODE_7_LEFT_DOWN = auto()
    JOYCODE_8_LEFT_LEFT = auto()
    JOYCODE_8_LEFT_RIGHT = auto()
    JOYCODE_8_LEFT_UP = auto()
    JOYCODE_8_LEFT_DOWN = auto()
    JOYCODE_1_RIGHT_LEFT = auto()
    JOYCODE_1_RIGHT_RIGHT = auto()
    JOYCODE_1_RIGHT_UP = auto()
    JOYCODE_1_RIGHT_DOWN = auto()
    JOYCODE_2_RIGHT_LEFT = auto()
    JOYCODE_2_RIGHT_RIGHT = auto()
    JOYCODE_2_RIGHT_UP = auto()
    JOYCODE_2_RIGHT_DOWN = auto()
    JOYCODE_3_RIGHT_LEFT = auto()
    JOYCODE_3_RIGHT_RIGHT = auto()
    JOYCODE_3_RIGHT_UP = auto()
    JOYCODE_3_RIGHT_DOWN = auto()
    JOYCODE_4_RIGHT_LEFT = auto()
    JOYCODE_4_RIGHT_RIGHT = auto()
    JOYCODE_4_RIGHT_UP = auto()
    JOYCODE_4_RIGHT_DOWN = auto()
    JOYCODE_5_RIGHT_LEFT = auto()
    JOYCODE_5_RIGHT_RIGHT = auto()
    JOYCODE_5_RIGHT_UP = auto()
    JOYCODE_5_RIGHT_DOWN = auto()
    JOYCODE_6_RIGHT_LEFT = auto()
    JOYCODE_6_RIGHT_RIGHT = auto()
    JOYCODE_6_RIGHT_UP = auto()
    JOYCODE_6_RIGHT_DOWN = auto()
    JOYCODE_7_RIGHT_LEFT = auto()
    JOYCODE_7_RIGHT_RIGHT = auto()
    JOYCODE_7_RIGHT_UP = auto()
    JOYCODE_7_RIGHT_DOWN = auto()
    JOYCODE_8_RIGHT_LEFT = auto()
    JOYCODE_8_RIGHT_RIGHT = auto()
    JOYCODE_8_RIGHT_UP = auto()
    JOYCODE_8_RIGHT_DOWN = auto()
    CODE_NONE = 0x8000
    CODE_OTHER = 0x8001
    CODE_DEFAULT = 0x8002
    CODE_PREVIOUS = 0x8003
    CODE_NOT = 0x8004
    CODE_OR = 0x8005

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return {"__enum__": obj.name}

        return json.JSONEncoder.default(self, obj)

def as_enum(s):
    if "__enum__" in s:
        name = s["__enum__"]

        if name.startswith('IPT_'):
            return IPT[name]
        elif name.startswith('KEYCODE_') or name.startswith('JOYCODE_') or name.startswith('CODE_'):
            return Keycode[name]

    return s

def readSequence(f):
    length = np.fromfile(f, '>i2', count=1)[0]

    if length == 0:
        return []

    return [(int((code & 0xF0000000) >> 28), Keycode(code & 0x0FFFFFFF)) for code in np.fromfile(f, '>i4', count=length)]

def writeSequence(seq, f):
    length = len(seq)

    np.array(length).astype('>i2').tofile(f)

    if length > 0:
        seq = [(typeId << 28 | code.value) for typeId, code in seq]
        np.array(seq).astype('>i4').tofile(f)

def readPort(f):
    p = {}

    typeId = np.fromfile(f, '>i4', count=1)[0]

    p['type_lo'] = IPT(typeId & 0xFF)
    p['type_hi'] = int(typeId & 0xFFFFFF00)
    p['mask'] = np.fromfile(f, '>i2', count=1).tolist()[0]
    p['default_value'] = np.fromfile(f, '>i2', count=1).tolist()[0]
    p['sequence'] = readSequence(f)

    return p

def writePort(port, f):
    typeId = port['type_hi'] | port['type_lo'].value
    np.array(typeId).astype('>i4').tofile(f)

    np.array(port['mask']).astype('>i2').tofile(f)
    np.array(port['default_value']).astype('>i2').tofile(f)
    writeSequence(port['sequence'], f)

def readcfg(filename):
    with open(filename, 'r') as f:
        header = np.fromfile(f, 'i1', count=8).tolist() # MAMECFG\x9

        numPorts = np.fromfile(f, '>i4', count=1)[0]

        defaultPorts = []

        for i in range(numPorts):
            defaultPorts.append(readPort(f))

        ports = []

        for i in range(numPorts):
            ports.append(readPort(f))

        # coins
        coins = np.fromfile(f, '>i4', count=8+1).tolist() # 8 coin counters, 1 dispensed tickets

        # mixer
        mixerCfg = np.fromfile(f, 'i1', count=16+16).tolist()

    return {'header': header,
            'current_ports': ports,
            'default_ports': defaultPorts,
            'coins': coins,
            'mixer': mixerCfg}

def writeCfg(filename, cfg):
    with open(filename, 'w') as f:
        np.array(cfg['header']).astype('i1').tofile(f)

        numPorts = len(cfg['default_ports'])
        np.array(numPorts).astype('>i4').tofile(f)
        
        for port in cfg['default_ports']:
            writePort(port, f)

        for port in cfg['current_ports']:
            writePort(port, f)

        np.array(cfg['coins']).astype('>i4').tofile(f)
        np.array(cfg['mixer']).astype('i1').tofile(f)

def portToStr(p):
    if p['type'] & 0x80000000: return 'UNUSED'

    player = (p['type'] & 0xFFFF0000) >> 16
    portType = p['type'] & 0xFF;

    seq = [((e & 0xF0000000) >> 28, e & 0x0FFFFFFF) for e in p['sequence']]

    seq = [(t, (keyCodes[code] if code < 0x8000 else specialKeyCodes[code])) for t, code in seq]

    return 'type: {} (player {}), mask: {:02x}, default: {}, sequence: {}'.format(
            IPT_codes[portType], player + 1, p['mask'], p['default_value'],
            seq)

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--dump', action='store_true', help='Dump the .cfg file in JSON format')
    parser.add_argument('-c', '--create', action='store_true', help='Create the .cfg file from a JSON file')

    parser.add_argument('infile', help='In --dump mode, this is the .cfg file; in --create mode, this is the .json file')
    parser.add_argument('outfile', help='In --dump mode, this is the .json file; in --create mode, this is the .cfg file')

    args = parser.parse_args()

    if args.dump:
        cfg = readcfg(args.infile)

        with open(args.outfile, 'w') as f:
            f.write(json.dumps(cfg, cls=EnumEncoder, indent=2))
    elif args.create:
        with open(args.infile, 'r') as f:
            cfg = json.load(f, object_hook=as_enum)

        writeCfg(args.outfile, cfg)
    else:
        parser.print_help()

