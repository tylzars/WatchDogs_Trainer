import pyMeow 

process = pyMeow.open_process("Watch_Dogs.exe")

def update_money(process, money_input): 
    base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3BA2650
    money_offset = pyMeow.pointer_chain_64(process, base_addr, [0x58, 0x10, 0x240, 0x68, 0x10, 0x10, 0x7d4])
    prev_money = pyMeow.r_int(process, money_offset)
    pyMeow.w_int(process, money_offset, money_input)
    new_money = pyMeow.r_int(process, money_offset)
    print(f"From ${prev_money} to ${new_money}!")

def update_skill_points(process, skillpoint_input):
    base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3BA2650
    skill_point_offset = pyMeow.pointer_chain_64(process, base_addr, [0x60, 0x10, 0x240, 0x78, 0x38, 0x8, 0xAA0])
    prev_skillpoint = pyMeow.r_int(process, skill_point_offset)
    pyMeow.w_int(process, skill_point_offset, skillpoint_input)
    new_skillpoint = pyMeow.r_int(process, skill_point_offset)
    print(f"Went from {prev_skillpoint} skillpoints to {new_skillpoint}!")

def update_wanted_level(process, level_input):
    base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3B99A50
    wanted_level_offset = pyMeow.pointer_chain_64(process, base_addr, [0x20, 0x2D0, 0xC0, 0x80, 0x20, 0x8, 0xC])
    prev_wanted_level = pyMeow.r_int(process, wanted_level_offset)
    pyMeow.w_int(process, wanted_level_offset, level_input)
    new_wanted_level = pyMeow.r_int(process, wanted_level_offset)
    print(f"Wanted level went from {prev_wanted_level} to {new_wanted_level}!")



#update_money(process, 456789)
#update_skill_points(process, 5)
#update_wanted_level(process, 0)


# So the data in this struct gets loaded in at a different offsets each time.
# However, the 0x0, 0x40, 0xB0 offsets do not change
# This iterates through the values that change
if False:
    user_current_values =  [5, 4, 14, 6, 6]

    for i in range(0x0, 0x1000, 0x4):
        base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3BBF518
        try:
            for j in range(0x0, 0x400, 0x4):
                test_offset = pyMeow.pointer_chain_64(process, base_addr, [0x0, 0x40, 0xB0, i, 0x0, 0x0, j])
                iterator21 = pyMeow.r_int(process, test_offset)
                if iterator21 in user_current_values:
                    print(f"Found {iterator21} at: {hex(i) + ", " + hex(j)} ")
        except:
            continue

# Use this to try the offsets the previous functions find
# This approach is pretty fuzzy, hoping to get it working better
def update_component(process, component_input, offset1, offset2):
    base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3BBF518
    component_offset = pyMeow.pointer_chain_64(process, base_addr, [0x0, 0x40, 0xB0, offset1, 0x0, 0x0, offset2])
    prev = pyMeow.r_int(process, component_offset)
    pyMeow.w_int(process, component_offset, component_input)
    new = pyMeow.r_int(process, component_offset)
    print(f"{prev} to {new}")

#update_component(process, 6, 0xf0, 0x39c)


# Trying to modify the battery on your phone
# The only thing Cheat Engine detects is the UI element
# Using a debugger, I can see the UI value loaded from a struct in RCX
# I traced out both of these address used in [RCX] and changing either doesn't result in a new value.
# Needed to VEH Debugger to get CE to attached without crash

# Tried searching for Health using the All option in CE
# Got it narrowed down to a lot of floats but nothing changed there
# Should try with a greater diversity of places to jump off??
