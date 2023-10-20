def show_keys(keys):
    key_help = ""
    for k in keys:
        mods = ""
        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<25} {}".format(mods, k.desc + "\n")

    return key_help

