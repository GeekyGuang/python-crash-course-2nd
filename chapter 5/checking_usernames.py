current_users = ['jack', 'rose', 'andy', 'julie', 'killy']
new_users = ['lucy', 'killy']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} has been used")
    else:
        print(f"{new_user} is available")
