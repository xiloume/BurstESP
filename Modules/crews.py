"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

from helpers import *
import struct
from mapping import ships
from Modules.display_object import DisplayObject
from helpers import crew_tracker


class Crews(DisplayObject):
    """
    Class to generate information about the crews current on our server
    """
    # basic color
    #crew_color = (255, 255, 255, 255)
    # table of color values
    color_tab = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255), (128, 0, 127, 255), (0, 128, 127, 255)]

    def __init__(self, memory_reader, actor_id, address):
        """
        be located at the screen coordinated + our text_offsets from helpers.py
        The function of this class is to collect all of the data about the crews
        currently on our server. `CrewService` is effectively just a list of
        `Crew` structures in memory, which we will iterating over to collect the
        requisite data.

        Previously, you were able to collect player names from this data but we
        cannot any longer. Instead we will simply use it to get a count of how
        many players are on the server and on each crew.

        :param memory_reader: The SoT MemoryHelper Object we use to read memory
        :param actor_id: The actor ID of our CrewService. Used to validate if
        there is an unexpected change
        :param address: The address in which our CrewService lives
        """
        # Initialize our super-class
        super().__init__(memory_reader)

        self.rm = memory_reader
        self.actor_id = actor_id
        self.address = address
        self.crew_color = (255, 0, 0, 255)

        # Collect and store information about the crews on the server
        self.crew_info = self._get_crews_info()

        # Sum all of the crew sizes into our total_players variable
        self.total_players = sum(crew['size'] for crew in self.crew_info)

        # All of our actual display information & rendering
        self.crew_str = self._built_text_string()

        # Used to track if the display object needs to be removed
        self.to_delete = False

    def _built_text_string(self):
        """
        Generates a string used for rendering. Separate function in the event
        you need to add more data or want to change formatting
        """
        output = ""
        for x in range(len(self.crew_info)):
            
            # We store all of the crews in a tracker dictionary. This allows us
            # to assign each crew a "Short"-ID based on count on the server.
            short_id = crew_tracker.get(self.crew_info[x]['guid'], None)
            output += f"{self.crew_info[x]['crewlabel']}{short_id}:{self.crew_info[x]['size']} Pirates\n"
        return output
    #return a different color for a crew
    def _get_color(self, len, color):
        """
        Returns the color for the crew
        """
        print(color)
        if self.color_tab[len] != color:
                self.crew_color = self.color_tab[len]
        return self.crew_color


    def _get_crews_info(self):
        # Find the starting address for our Crews TArray
        crew_raw = self.rm.read_bytes(self.address + OFFSETS.get('CrewService.Crews'), 16)
        # (Crews_Data<Array>, Crews length, Crews max)
        crews = struct.unpack("<Qii", crew_raw)
        # Will contain all of our condensed Crew Data
        crews_data = []
        # For each crew on the server
        for x in range(0, crews[1]):
            # Each crew has a unique ID composed of four ints, maybe be useful if you
            # add functionality around Crews on your own
            crew_guid_raw = self.rm.read_bytes(crews[0] + (OFFSETS.get('Crew.Size') * x), 16)
            crew_guid = struct.unpack("<iiii", crew_guid_raw)

            # Read the TArray of Players on the the specific Crew, used to determine
            # Crew size
            crew_raw = self.rm.read_bytes(
                crews[0] + OFFSETS.get('Crew.Players') + (OFFSETS.get('Crew.Size') * x), 16
            )
            # read the ship data
            crew_max_players = self.rm.read_int(crews[0] + OFFSETS.get('Crew.Size') * x + OFFSETS.get('Crew.CrewSessionTemplate') + OFFSETS.get('CrewSessionTemplate.CrewMaxPlayer'))
            #crew_max_players = struct.unpack("<i", crew_max_players)
            #crew_session = struct.unpack("<iiiiiiiiiiiiii", crewsession)
            #crew_ship = self.rm.read_bytes(crew_session + OFFSETS.get('Crew.CrewMaxPlayer'), 4)

            # Players<Array>, current length, max length
            crew = struct.unpack("<Qii", crew_raw)

            if crew_max_players == 2:
                crewlabel = "sloop "
            elif crew_max_players == 3:
                crewlabel = "brig   "
            else:
                crewlabel = "galion"
            #print(crew_guid[0], crewlabel)
            # If our crew has more than 0 people on it, we care about it, so we add it to our tracker
            color = self._get_color(x, self.crew_color)
            if crew[1] > 0:
                crew_data = {
                    "guid": crew_guid,
                    "size": crew[1],
                    "crewlabel": crewlabel,
                    "color": color
                }
                crews_data.append(crew_data)
                
                if crew_guid not in crew_tracker:
                    crew_tracker[crew_guid] = len(crew_tracker)+1
        return crews_data

    def update(self, my_coords):
        """
        A generic method to update all the interesting data about the
        crews on our server. To be called when seeking to perform an update on
        the CrewService actor without reinitializing our class.

        1. Determine if our actor is what we expect it to be
        2. Pull the latest crew information
        3. Update our strings accordingly
        """
        if self._get_actor_id(self.address) != self.actor_id:
            self.to_delete = True
            return
        self.crew_info = self._get_crews_info()
        self.crew_str = self._built_text_string()
