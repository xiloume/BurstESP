"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

from itertools import count
import struct
from pyglet.text import Label
from vlabel import VLabel
from pyglet.shapes import Rectangle
from helpers import CONFIG, OFFSETS, calculate_distance, object_to_screen, \
     TEXT_OFFSET_X, TEXT_OFFSET_Y
from mapping import Player as PlayerM
from Modules.display_object import DisplayObject

RECTANGLE_SIZEX = 5
RECTANGLE_SIZEY = 5
RECTANGLE_COLOR = (255, 0, 0)


class Player(DisplayObject):
    """
    Class to generate information for a Player object in memory
    """

    def __init__(self, memory_reader, actor_id, address, my_coords, raw_name, batch, crew_data):
        """
        Upon initialization of this class, we immediately initialize the
        DisplayObject parent class as well (to utilize common methods)

        We then set our class variables and perform all of our info collecting
        functions, like finding the actors base address and converting the
        "raw" name to a more readable name per our Mappings. We also create
        a circle and label and add it to our batch for display to the screen.

        All of this data represents a "Player". If you want to add more, you will
        need to add another class variable under __init__ and in the update()
        function

        :param memory_reader: The SoT MemoryHelper Object we use to read memory
        :param address: The address in which the AActor begins
        :param my_coords: a dictionary of the local players coordinates
        :param raw_name: The raw actor name used to translate w/ mapping.py
        """
        # Initialize our super-class
        super().__init__(memory_reader)

        self.actor_id = actor_id
        self.address = address
        self.actor_root_comp_ptr = self._get_root_comp_address(address)
        self.my_coords = my_coords
        self.raw_name = raw_name
        self.batch = batch
        self.crew_data = crew_data
        self.playerinfo = self._get_player_info()
        self.color = RECTANGLE_COLOR
        # Generate our Player's info
        try:
            self.name = self.playerinfo["name"]
            self.id = self.playerinfo["id"]
        except:
            self.name = PlayerM.get(self.raw_name).get("Name")
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        self.distance = calculate_distance(self.coords, self.my_coords)

        self.screen_coords = object_to_screen(self.my_coords, self.coords)

        # All of our actual display information & rendering
        self.text_str = self._built_text_string()
        self.text_render = self._build_text_render()
        self.text_render.visible = False
        self.icon = self._build_Rectangle_render()
        self.icon.visible = False

        # Used to track if the display object needs to be removed
        self.to_delete = False

    def _build_Rectangle_render(self) -> Rectangle:
        """
        Creates a circle located at the screen coordinates (if they exist).
        Uses the color specified in our globals w/ a size of 10px radius.
        Assigns the object to our batch & group
        """
        if self.screen_coords:
            return Rectangle(self.screen_coords[0], self.screen_coords[1],
                          RECTANGLE_SIZEX, RECTANGLE_SIZEY, color=self.color, batch=self.batch)

        return Rectangle(0, 0, RECTANGLE_SIZEX, RECTANGLE_SIZEY, color=self.color, batch=self.batch)

    def _built_text_string(self) -> str:
        """
        Generates a string used for rendering. Separate function in the event
        you need to add more data (Sunk %, hole count, etc)
        """
        return f"{self.name}[{self.distance}m] {self.id}"

    def _build_text_render(self) -> Label:
        """
        Function to build our actual label which is sent to Pyglet. Sets it to
        be located at the screen coordinated + our text_offsets from helpers.py

        Assigns the object to our batch & group

        :rtype: Label
        :return: What text we want displayed next to the Player
        """
        if self.screen_coords:
            return VLabel(self.text_str,
                          x=self.screen_coords[0] + TEXT_OFFSET_X,
                          y=self.screen_coords[1] + TEXT_OFFSET_Y,
                          font_name ='Times New Roman', font_size=10,
                          batch=self.batch)

        return VLabel(self.text_str, x=0, y=0, batch=self.batch, font_name ='Times New Roman', font_size=10)

    def _get_player_info(self):
        Player_data = []
        
        #pawn = self.rm.read_ptr(self.player_controller + OFFSETS.get('PlayerController.Pawn'))
        #playerstate = self.rm.read_ptr(pawn + OFFSETS.get('Pawn.PlayerState'))
        #name = self.rm.read_name_string(playerstate + OFFSETS.get('PlayerState.PlayerName'))
        playerbyte = self.rm.read_bytes(self.address + OFFSETS.get('PlayerState.PlayerName'), 16)
        player = struct.unpack("<QQ", playerbyte)
        PlayerId = self.rm.read_int(self.address + OFFSETS.get('AthenaPlayerState.PlayerId'))
        name = self.rm.read_name_string(player[0], 16) + self.rm.read_name_string(player[1], 16)
        try:
            for y in range(0, len(self.crew_data.crew_info)):
                var = self.crew_data.crew_info[y]["player"]
                for x in range(0, self.crew_data.crew_info[y]["size"]):
                    playercrew = self.rm.read_ptr(var + OFFSETS.get('Crew.Players'))
                    playercontroller = self.rm.read_ptr(playercrew + 48)
                    playerpawn = self.rm.read_ptr(playercontroller + 1080)
                    PlayerState = self.rm.read_ptr(playerpawn + 1000)
                    crewplayerid = self.rm.read_int(PlayerState + OFFSETS.get('AthenaPlayerState.PlayerId'))
                    if crewplayerid == PlayerId:
                        self.color = self.crew_data.crew_info[y]["color"]
                        print(self.color)
        except Exception as e:
            print(e)
        #PlayerId = self.rm.read_int(playerstate + OFFSETS.get('PlayerState.PlayerId'))
        Player_data = {
            "id": PlayerId,
            "name": name
        }
        return Player_data

    def update(self, my_coords: dict):
        """
        A generic method to update all the interesting data about a Player
        object, to be called when seeking to perform an update on the
        Actor without doing a full-scan of all actors in the game.

        1. Determine if the actor is what we expect it to be
        2. See if any data has changed
        3. Update the data if something has changed

        In theory if all data is the same, we could *not* update our Label's
        text, therefore saving resources. Not implemented, but a possibility
        """
        if self._get_actor_id(self.address) != self.actor_id:
            self.to_delete = True
            self.icon.delete()
            self.text_render.delete()
            return

        self.my_coords = my_coords
        self.playerinfo = self._get_player_info()
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        new_distance = calculate_distance(self.coords, self.my_coords)

        self.screen_coords = object_to_screen(self.my_coords, self.coords)

        if self.screen_coords and new_distance >= 0 and new_distance < 200:
            if CONFIG.get("PLAYER_ENABLED") == False:
                self.icon.visible = False
                self.text_render.visible = False
                return
            else:
                self.icon.visible = True
                self.text_render.visible = True

            # Update the position of our circle and text
            self.icon.position = (self.screen_coords[0], self.screen_coords[1])
            self.text_render.position = (self.screen_coords[0] + TEXT_OFFSET_X, self.screen_coords[1] + TEXT_OFFSET_Y)

            # Update our text to reflect out new distance
            self.distance = new_distance
            self.text_str = self._built_text_string()
            self.text_render.text = self.text_str

        else:
            # if it isn't on our screen, set it to invisible to save resources
            self.icon.visible = False
            self.text_render.visible = False
