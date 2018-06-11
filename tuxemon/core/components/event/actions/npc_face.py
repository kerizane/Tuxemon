# -*- coding: utf-8 -*-
#
# Tuxemon
# Copyright (c) 2014-2017 William Edwards <shadowapex@gmail.com>,
#                         Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import absolute_import

from tuxemon.core.components.event import get_npc
from tuxemon.core.components.event.eventaction import EventAction


class NpcFaceAction(EventAction):
    """ Makes the NPC face a certain direction.

    Valid Parameters: npc_slug, direction

    Direction parameter can be: "left", "right", "up", or "down"
    """
    name = "npc_face"
    valid_parameters = [
        (str, "npc_slug"),
        (str, "direction")
    ]

    def start(self):
        npc = get_npc(self.game, self.parameters.npc_slug)
        if self.parameters.direction == "player":
            npc.facing = self.get_player_direction(npc)
        else:
            npc.facing = self.parameters.direction

    def get_player_direction(self, npc):
        """ Gets the direction of the player in relation to the npc
        """
        y_offset = npc.tile_pos[1] - self.game.player1.tile_pos[1]
        x_offset = npc.tile_pos[0] - self.game.player1.tile_pos[0]
        # Are they further away vertically or horizontally?
        look_on_y_axis = abs(y_offset) >= abs(x_offset)

        if look_on_y_axis:
            player_location = "up" if y_offset > 0 else "down"
        else:
            player_location = "left" if x_offset > 0 else "right"

        return player_location
