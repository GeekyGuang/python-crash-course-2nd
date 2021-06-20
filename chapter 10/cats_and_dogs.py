cats = ['lily', 'cathy', 'annie']
dogs = ['goofy', 'droopy', 'cindy']

def create_file(filename, names):
  with open(filename, 'w') as f:
    for name in names:
      f.write(f"{name}\n")

create_file('cats.txt', cats)
create_file('dogs.txt', dogs)

