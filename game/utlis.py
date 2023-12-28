"""
This File include all self-define pygame-related function
# Pygame Function #
Step 1. Pygame Init
Step 2. Set Screen Size
Step 3. Load Resource
Step 4. Select & Show Background
Step 5. Start Working: Create Plays or Replay the scenes
"""
# Third Party Library Import #
import pygame as pg
import time
import os
# Self Library Import #
from . import buttons,recorder,replayer

# load and resize if needed
def load_image(folder:str, filename:str, need_resize = False, scale_size:tuple = (64,64)):
	image = pg.image.load(os.path.join(folder, filename)).convert()
	if need_resize:
		image = pg.transform.scale(image, scale_size)
	return image

def load_background(resource_folder:str):
	background_init = load_image(folder = resource_folder, filename = "init_background.jpg")
	background_fullcourt = load_image(folder = resource_folder,filename = "fullcourt.jpg")
	background_frontcourt_h = load_image(folder = resource_folder,filename = "frontcourt_horizontal_view.jpg")
	background_frontcourt_v = load_image(folder = resource_folder,filename = "frontcourt_vertical_view.jpg")
	return background_init,background_fullcourt,background_frontcourt_h,background_frontcourt_v

def load_background_buttons():
	background_fullcourt_btn = buttons.BackgroundImageButton.get("Fullcourt")
	background_frontcourt_h_btn = buttons.BackgroundImageButton.get("Frontcourt Horizontal")
	background_frontcourt_v_btn = buttons.BackgroundImageButton.get("Frontcourt Vertical")
	background_replay_btn = buttons.BackgroundImageButton.get("Replay")
	return background_fullcourt_btn,background_frontcourt_h_btn,background_frontcourt_v_btn,background_replay_btn

def load_player_ball(resource_folder:str):
	team_player = load_image(folder = resource_folder, filename = "team_player.jpg", need_resize = True)
	rival_player = load_image(folder = resource_folder, filename = "rival_player.jpg", need_resize = True)
	ball = load_image(folder = resource_folder, filename = "ball.png", need_resize = True)
	return team_player,rival_player,ball

def load_player_ball_buttons():
	team_player_btn = buttons.PlayersButton.get("TeamPlayer")
	rival_player_btn = buttons.PlayersButton.get("RivalPlayer")
	ball_btn = buttons.BallButton.get("Ball")
	return team_player_btn,rival_player_btn,ball_btn

def load_tool_buttons():
	reset_btn = buttons.ResetButton.get("Reset")
	replay_btn = buttons.ReplayButton.get("Replay")
	colorpicker_btn = buttons.ColorPickerButton.get("Colorpicker")
	paintbrush_btn = buttons.PaintbrushButton.get("Paintbrush")
	mainscreen_btn = buttons.MainscreenButton.get("Mainscreen")
	name_input_box = buttons.NameInputBox.get("Input")
	save_stage_btn = buttons.SaveButton.get("Stage")
	save_file_btn = buttons.SaveButton.get("File")
	return reset_btn,replay_btn,colorpicker_btn,paintbrush_btn,mainscreen_btn,name_input_box,save_stage_btn,save_file_btn

# add 1 item count
def update_selected_item_status(selected_item_status:dict, selected_item_name:str):
	selected_item_status[selected_item_name] = selected_item_status.get(selected_item_name,0) + 1
	return selected_item_status

# Save File & Record Stage
def save_json_file(recorder:recorder.Recorder, filename:str):
	current_time = time.strftime("%Y-%m-%d_%H%M%S").replace("-", "_")
	save_folder = os.path.join("game","save")
	recorder.name = filename
	savepath = os.path.join(save_folder,f"{recorder.name}_{current_time}.json")
	recorder.save_record(savepath = savepath)
	print("Save JSON")

def playscene(replayer: replayer.Replayer, stage:int, obj_list:list) -> list:
	# images
	selected_items = []
	drawing_positions = []
	for character,pos in replayer.recorder.all_stages[stage]:
		if character == "TeamPlayer":
			selected_items.append((obj_list[0],pos))
		elif character == "RivalPlayer":
			selected_items.append((obj_list[1],pos))
		elif character == "Ball":
			selected_items.append((obj_list[2],pos))
		else:
			raise ValueError("Invalid character")
	# drawings
	if hasattr(replayer.recorder, 'all_drawings'):
		if stage < len(replayer.recorder.all_drawings):
			# must use += (append) to prevent clear drawing_positions affect on replayer.recorder.all_drawings[stage]
			drawing_positions += replayer.recorder.all_drawings[stage]
			# print(stage,"drawing->",drawing_positions)
	return selected_items,drawing_positions

# For btn layout in different background
def buttons_move_x(btns:list,move_diff:int,reverse = False):
	if reverse:
		move_diff = - move_diff
	for btn in btns:
		btn.move_ip(move_diff,0)
