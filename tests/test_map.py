"""
from map.py
"""

from tuxemon.core.control import PygameControl
from tuxemon.core import prepare
from tuxemon.core.components.player import Player
from os import curdir
from os.path import join

base_dir = curdir + "/tuxemon/"
prepare.init()
control = PygameControl(prepare.ORIGINAL_CAPTION)
control.auto_state_discovery()
control.add_player(Player(prepare.CONFIG.player_npc))
state = control.push_state("WorldState")
map_name = join(prepare.BASEDIR, prepare.DATADIR, 'maps', 'test_cotton_town.tmx')
state.change_map(map_name)

path = state.pathfind(
    (1, 39),
    (36, 4),
)

assert len(path) == 70
