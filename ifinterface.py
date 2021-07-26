class InputMode:
    

input_type_dict = {"1": }

def intro():
    print('''
  ____  ______ __  __ _    _   _____                   _      _____                           _             
 / __ \|  ____|  \/  | |  | | |_   _|                 | |    / ____|                         | |            
| |  | | |__  | \  / | |  | |   | |  _ __  _ __  _   _| |_  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  | |  __| | |\/| | |  | |   | | | '_ \| '_ \| | | | __| | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |__| | |____| |  | | |__| |  _| |_| | | | |_) | |_| | |_  | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 \___\_\______|_|  |_|\____/  |_____|_| |_| .__/ \__,_|\__|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                          | |                                                               
                                          |_|                                                               
''')
    print("Create your own QEMU input.")
    print("Select the option that you want to see in your input.")
    print("Then, you can feed your QEMU instance with what you've created.")

def select_input_type():
    print("Select your input type:")
    print("\t1. Periodic wave")
    print("\t2. Switching wave")
    print("\t3. One time input")
    response = input()
    result = response_analyzer(response, input_type_dict)


def response_analyzer(_input, selection_dict):
    for response, selection in selection_dict.items():
        if response == clean_answer(_input):
            return selection
    return -1

def clean_answer(_input):
    cleansed = str(_input).strip()
    cleansed = cleansed.lower()
    return cleansed

if __name__ == "__main__":
    intro()