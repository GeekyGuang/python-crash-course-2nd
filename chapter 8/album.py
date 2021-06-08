def make_album(artist, album, number=None):
  albums = {'artist': artist, 'album': album}
  if number:
    albums['number'] = number
  
  return albums

while True:
  artist = input("Please enter a artist, press 'q' to quit: ")
  if artist == 'q':
    break
  
  album = input("Please enter an album, press 'q' to quit: ")
  if album == 'q':
    break

  information = make_album(artist, album)
  print(information)
