
def _normalise(dictionary: dict[str, str]) -> set[str]:
    """Return the existing keys, lower-cased, for membership checks."""
    return {key.lower() for key in dictionary}


def add_setting(dictionary, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if (key in set(  [i.lower() for i in dictionary.keys()]  )):
        return(f"Setting \'{key}\' already exists! Cannot add a new setting with this name.")
    
    dictionary[key] = value
    return(f"Setting \'{key}\' added with value \'{value}\' successfully!")


def update_setting(dictionary, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if (key in set([i.lower() for i in dictionary.keys()])):
        dictionary[key] = value
        return(f"Setting \'{key}\' updated to \'{value}\' successfully!")
    return(f"Setting \'{key}\' does not exist! Cannot update a non-existing setting.")

def delete_setting(dictionary, key):
    key = key.lower()

    if (key in set([i.lower() for i in dictionary.keys()])):
        dictionary.pop(key)
        return(f"Setting \'{key}\' deleted successfully!")
    return(f"Setting not found!")


def view_settings(dictionary):
    print( dictionary)
    if not dictionary:
        return("No settings available.")
    out = []
    out += ["Current User Settings:"]
    for key, value in dictionary.items():
        out += [f"{key.title()}: {value}"]
    return("\n".join(out) + "\n")


def main() -> None:
    test_settings = {
    "brightness":"high",
    "zoom":"out",
    "contrast":"small"
    }

    view_settings(test_settings)



if __name__ == "__main__":
    main()
