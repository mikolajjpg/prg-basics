class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
      self.channel_list = []
      self.volume = 0
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
   def channel_no_switch(self,channel_no):
      self.channel_no = channel_no

   def set_channels(self,channels_list):
      self.channel_list += channels_list

   def volume_up(self):
      if self.volume < 10:
         self.volume += 1

   def volume_down(self):
      if self.volume > 0:
         self.volume -= 1
   
   def show_channels(self):
         for i, channel in enumerate(self.channel_list, start=1):
            print(f'{i}. {channel}')
      
         
   def display_info(self):
      if self.is_on == True and len(self.channel_list) >= self.channel_no:
         print(f'TV is on, channel {self.channel_no} ({self.channel_list[self.channel_no-1]}) (volume:{self.volume})')
      elif self.is_on == True and len(self.channel_list) < self.channel_no :
         print(f'TV is on, channel {self.channel_no} (not found)')
      elif self.is_on == False:
         print(f'TV is off')
         

def main():

   my_tv = TV()

   my_tv.turn_on()
   my_tv.set_channels(['TVP1','TVP2','Polsat', 'TVN', 'Filmbox', 'Discovery','Canal+','Polska24'])
   my_tv.display_info()
   my_tv.volume_up()
   my_tv.volume_up()
   my_tv.volume_up()
   my_tv.channel_no_switch(2)
   my_tv.display_info()
   my_tv.volume_down()
   my_tv.volume_down()
   my_tv.channel_no_switch(3)
   my_tv.display_info()
   my_tv.channel_no_switch(4)
   my_tv.display_info()
   my_tv.channel_no_switch(5)
   my_tv.display_info()
   my_tv.channel_no_switch(6)
   my_tv.display_info()
   my_tv.channel_no_switch(7)
   my_tv.display_info()
   my_tv.channel_no_switch(9)
   my_tv.display_info()

   
if __name__ =="__main__":
    main()


      
