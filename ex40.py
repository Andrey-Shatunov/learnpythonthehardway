class Song(object):

    def __init__(self, name, lyrics):
        self.name=name
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    def put_author(self,author):
        self.author=author
        
    def get_name(self):
        print "The name of sing is"+self.name
        
    def get_author(self):
        print "The author of sing is "+self.author
        

text=["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"]
happy_bday = Song("Happy birthday",text)

text=["They rally around tha family", "With pockets full of shells"]
bulls_on_parade = Song("Bulls",text)

text=["All around me are familiar faces", "Worn out places, worn out faces"]
mad_world=Song("Mad world",text)



happy_bday.sing_me_a_song()
print "-"*10
bulls_on_parade.sing_me_a_song()
print "-"*10
mad_world.sing_me_a_song()
print "-"*10
mad_world.get_name()
mad_world.put_author("Author")
mad_world.get_author()
