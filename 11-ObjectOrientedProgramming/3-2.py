class Song:
   def __init__(self,performer,title,album,year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year
   def __str__(self):
      return f'{self.album}, {self.title}, {self.album}, {self.year}'

# object creatio
song1 = Song("Kali","Pole Marysi","Wiesz co się kruszy", "2013")

song2 = Song("Paluch", "Szaman", "Ostatni krzyk osiedla", "2016")

## object usage
print(f"{song1}, end=''")
print(f"song2, end='' ")