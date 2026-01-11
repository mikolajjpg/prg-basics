class Song:
   def __init__(self,performer,title,album,year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year
   def __str__(self):
      return (f"Performer: {self.performer}\n"
              f"Title:     {self.title}\n"
              f"Album:     {self.album}\n"
              f"Year:      {self.year}")

# object creatio
song1 = Song("Kali","Pole Marysi","Wiesz co się kruszy", 2013)

song2 = Song("Paluch", "Szaman", "Ostatni krzyk osiedla", 2016)

## object usage
print(song1)
print()
print(song2)