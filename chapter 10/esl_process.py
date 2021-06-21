from titles import titles
i = 1
while i <= 1305:
    title = '### ' + titles[i-1] + '\n\n'
    filename = str(i)+'.txt'

    try:
        with open(filename, encoding='utf-8', errors='ignore') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"file {filename} not found")
        break
    else:
        if '[start of' in contents.lower():
            index = contents.lower().index('[start of')
            start = contents.index('\n', index)
            end = contents.lower().index('[end of')
        elif '<start of' in contents.lower():
            index = contents.lower().index('<start of')
            start = contents.index('\n', index)
            end = contents.lower().index('<end of')
        else:
            print(f"{filename} misson failed!")
            i += 1
            continue

        final_contents = contents[start:end].strip()

        with open('final_ESL.txt', 'a', encoding='utf-8') as f:
            f.write(title + final_contents + '\n\n')

    i += 1

if i > 1305:
    print("Completed!")
