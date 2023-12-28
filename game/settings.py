"""
Setting Control
"""

VERSION = "1.0.0"

INIT_WINDOW_SIZE = (1100,800)

WORKING_WINDOW_WIDTH = 450

PIC_FILE = [
"ball.png",
"frontcourt_horizontal_view.jpg",
"frontcourt_vertical_view.jpg",
"fullcourt.jpg",
"rival_player.jpg",
"team_player.jpg",
"init_background.jpg"
]

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Loop Parms
selected_background:bool = False
background = None
create_workscreen:bool = False
selected_btn:bool = False
selected_item = None
selected_item_name:str = ""
selected_item_status = {"TeamPlayer":0,"RivalPlayer":0,"Ball":0}
# Only for View (Save Img and Pos)
selected_items = []
# Only for Record (Save Name and Pos)
record_selected_items = []
input_editable:bool = False
tactics_name = "Input Name"
save_file:bool = False
record_stage:bool = False
all_stages = []
replay_mode_active:bool = False
replay_mode:bool = False
replay_stage = 0
# Replay Time Setting (2s 1 scene)
switch_scene_timer = 0
switch_scene_interval = 5000
initialized_replay_mode:bool = False
# Paintbrush
drawing_mode:bool = False
drawing:bool = False
drawing_positions = []
all_drawings = []
# Buttons x diff
frontcourt_h_btns_diff_x:int = -65
frontcourt_v_btns_diff_x:int = 0
fullcourt_btns_diff_x:int = 440