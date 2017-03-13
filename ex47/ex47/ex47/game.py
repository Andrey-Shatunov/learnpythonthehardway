class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
		
    def rename_room(self,new_name):
	self.name=new_name
	
    def rename_direction(self,new_direction):
        self.direction=new_direction
