def show_user_profile(firt_name, last_name, **others):
    others['first'] = firt_name
    others['last'] = last_name

    return others


profile = show_user_profile('t', 'w', hobby="football", fruit="banana")
print(profile)
