def input_dict():
    # currently only handles strings

    another = True
    d = dict()
    while another:
        print()
        key = input('enter key:\n> ')
        val = input('enter value:\n> ')

        d[key] = val

        print("another? ", end = "")
        another = yesno(default = 'y')

    return d

def input_bool(default = None):
    response = None
    responded = False

    # what should the default answer be if the user hits return without typing
    # anything?

    if default:
        if default == 'y':
            y_n = '(Y/n)'
        elif default == 'n':
            y_n = '(y/N)'
        else:
            y_n = '(y/n)'
    else:
        y_n = '(y/n)'

    while not responded:
        response = input(y_n + "\n> ")
        if not response:
            if default:
                if default == 'y':
                    return True
                else:
                    return False
            else:
                print("please enter either 'y' or 'n'.")
                continue

        if not response in ('y','n'):
            print("please enter either 'y' or 'n'.")
        else:
            if response == 'y':
                return True
            else:
                return False

