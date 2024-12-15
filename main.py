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


update_money(process, 456789)
update_skill_points(process, 5)
update_wanted_level(process, 0)


# Not working code (thought it worked at one point...)
def update_electronic_components(process, component_input):
    if component_input > 20:
        print("too many components")
        return
    
    base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3BCA870
    electronic_component_offset = pyMeow.pointer_chain_64(process, base_addr, [0x0, 0x6E8, 0xB0, 0x1A0, 0x0, 0x0, 0xC])
    prev_money = pyMeow.r_int(process, electronic_component_offset)
    pyMeow.w_int(process, electronic_component_offset, component_input)
    new_money = pyMeow.r_int(process, electronic_component_offset)
    print(f"Had {prev_money} electric components to {new_money} eletric components.")

def update_system_keys(process, component_input):
    if component_input > 8:
        print("too many components")
        return
    
    base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3BBF518
    electronic_component_offset = pyMeow.pointer_chain_64(process, base_addr, [0x0, 0x40, 0xB0, 0x1D0, 0x0, 0x0, 0xC])
    prev_money = pyMeow.r_int(process, electronic_component_offset)
    pyMeow.w_int(process, electronic_component_offset, component_input)
    new_money = pyMeow.r_int(process, electronic_component_offset)
    print(f"Had {prev_money} code components to {new_money} code components.")

def update_chemical_components(process, component_input):
    if component_input > 6:
        print("too many components")
        return
    
    base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3BBF518
    electronic_component_offset = pyMeow.pointer_chain_64(process, base_addr, [0x0, 0x40, 0xB0, 0xC8, 0x0, 0x0, 0xC])
    prev_money = pyMeow.r_int(process, electronic_component_offset)
    pyMeow.w_int(process, electronic_component_offset, component_input)
    new_money = pyMeow.r_int(process, electronic_component_offset)
    print(f"Had {prev_money} explosive components to {new_money} explosive components.")

def update_unstable_chemical_components(process, component_input):
    if component_input > 6:
        print("too many components")
        return
    
    ### This is not accurate, need to do in cheat engine
    base_addr = pyMeow.get_module(process, "Disrupt_b64.dll")['base'] + 0x3BBFA00
    electronic_component_offset = pyMeow.pointer_chain_64(process, base_addr, [0x0, 0x148, 0x48, 0x88, 0x0, 0x0, 0xD8C])
    prev_money = pyMeow.r_int(process, electronic_component_offset)
    pyMeow.w_int(process, electronic_component_offset, component_input)
    new_money = pyMeow.r_int(process, electronic_component_offset)
    print(f"Had {prev_money} explosive2 components to {new_money} explosive2 components.")

#update_electronic_components(process, 13) # Broken
#update_system_keys(process, 8) # Broken
#update_chemical_components(process, 6) # Broken
#update_unstable_chemical_components(process, 6) # Broken

