"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""

from pyglet.text import Label
from vlabel import VLabel
from pyglet.shapes import Circle
from helpers import CONFIG
from helpers import calculate_distance, object_to_screen, \
     TEXT_OFFSET_X, TEXT_OFFSET_Y
from mapping import Chestmap
from Modules.display_object import DisplayObject
# 0 Common (blanc)/  1 peu commun (vert) / 2 rare (bleu) / 3 epique (violet) / 4 legendaire (orange) / 5 rubis (rouge)
CHEST_COLOR = [(255, 255, 255, 255), (0, 255, 0, 255), (0, 0, 255, 255), (255, 0, 255, 255), (255, 165, 0, 255), (255, 0, 0, 255)]
CIRCLE_SIZE = 5  # The size of the indicator circle we want


class Chest(DisplayObject):
    """
    Class to generate information for a Chest object in memory
    """

    def __init__(self, memory_reader, actor_id, address, my_coords, raw_name, batch):
        """
        Upon initialization of this class, we immediately initialize the
        DisplayObject parent class as well (to utilize common methods)

        We then set our class variables and perform all of our info collecting
        functions, like finding the actors base address and converting the
        "raw" name to a more readable name per our Mappings. We also create
        a circle and label and add it to our batch for display to the screen.

        All of this data represents a "Chest". If you want to add more, you will
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

        # Generate our Chest's info
        self.name = Chestmap.get(self.raw_name).get("Name")
        self.color = Chestmap.get(self.raw_name).get("Color")
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        self.distance = calculate_distance(self.coords, self.my_coords)

        self.screen_coords = object_to_screen(self.my_coords, self.coords)

        # All of our actual display information & rendering
        self.text_str = self._built_text_string()
        self.text_render = self._build_text_render()
        self.text_render.visible = False

        # Used to track if the display object needs to be removed
        self.to_delete = False

    def _built_text_string(self) -> str:
        """
        Generates a string used for rendering. Separate function in the event
        you need to add more data (Sunk %, hole count, etc)
        """
        return f"{self.name}[{self.distance}m]"

    def _build_text_render(self) -> Label:
        """
        Function to build our actual label which is sent to Pyglet. Sets it to
        be located at the screen coordinated + our text_offsets from helpers.py

        Assigns the object to our batch & group

        :rtype: Label
        :return: What text we want displayed next to the Chest
        """
        if self.screen_coords and self.distance <= 250:
            return VLabel(self.text_str,
                          x=self.screen_coords[0] ,
                          y=self.screen_coords[1] ,
                          color=CHEST_COLOR[self.color],
                          batch=self.batch, font_name ='Times New Roman', font_size=10)

        return VLabel(self.text_str, x=4000, y=4000, batch=self.batch, font_name ='Times New Roman', font_size=10, color=CHEST_COLOR[self.color])

    def update(self, my_coords: dict):
        """
        A generic method to update all the interesting data about a Chest
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

            self.text_render.delete()
            return

        self.my_coords = my_coords
        self.coords = self._coord_builder(self.actor_root_comp_ptr,
                                          self.coord_offset)
        new_distance = calculate_distance(self.coords, self.my_coords)

        self.screen_coords = object_to_screen(self.my_coords, self.coords)
        if self.screen_coords:
            if CONFIG.get("CHEST_ENABLED") == False:
                self.text_render.visible = False
                return
            else:
                self.text_render.visible = True

            # Update the position of our circle and text
            self.text_render.position = (self.screen_coords[0] - 50, self.screen_coords[1] - 25)

            # Update our text to reflect out new distance
            self.distance = new_distance
            self.text_str = self._built_text_string()
            self.text_render.text = self.text_str

        else:
            # if it isn't on our screen, set it to invisible to save resources
            self.text_render.visible = False
