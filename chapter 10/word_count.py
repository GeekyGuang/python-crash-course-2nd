def word_counts(filename):
  """count the approximate number of words in a file"""
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    pass
  else:
    words = contents.split()
    number_words = len(words)
    print(f"The file {filename} has about {number_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
  word_counts(filename)
