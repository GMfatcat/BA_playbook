# Third Party Library Import #
import pygame as pg
import os
import sys

# Self Library Import #
from game import settings
from game import recorder
from game import replayer
from game import colorpicker
from game.utlis import *

# Helper Function #
def check_version(version):
	print(f"Software Version: {version}")

def check_files(check_files_folder:str, check_list:list):
	for file in check_list:
		filepath = os.path.join("resource", check_files_folder, file)
		if not os.path.exists(filepath):
			raise ValueError(f"{filepath} not found")
	print("Finish Checking files")

# Game Loop
def game_loop(window_size: tuple):
	# ------------ INIT SECTION ----------- #
	pg.init()
	screen = pg.display.set_mode(window_size,pg.RESIZABLE)
	font = pg.font.Font(None, 26)
	pg.display.set_caption("Basketball Playbook Creator")
	cursor = pg.cursors.broken_x
	pg.mouse.set_cursor(*cursor)

	# ------------ LOAD RESOURCE ----------- #
	resource_folder = os.path.join("resource","pic")
	# load 3 backgrounds & btns
	bg_init,bg_fullcourt,bg_frontcourt_h,bg_frontcourt_v = load_background(resource_folder = resource_folder)
	bg_fullcourt_btn,bg_frontcourt_h_btn,bg_frontcourt_v_btn,bg_replay_btn = load_background_buttons()

	# load players & ball & btns
	team_player,rival_player,ball = load_player_ball(resource_folder = resource_folder)
	team_player_btn,rival_player_btn,ball_btn = load_player_ball_buttons()

	# load tools btns
	reset_btn,replay_btn,colorpicker_btn,paintbrush_btn,mainscreen_btn,name_input_box,save_stage_btn,save_file_btn = load_tool_buttons()
	working_btns = [team_player_btn,rival_player_btn,ball_btn,reset_btn,
	                replay_btn,colorpicker_btn,paintbrush_btn,mainscreen_btn,
	                name_input_box,save_stage_btn,save_file_btn]

	# ------------ MAIN LOOP ----------- #
	# New Recorder Init
	new_recorder = recorder.Recorder()

	# Other Init Parms
	# workingscreen_btns_diff_x = 0
	selected_color = colorpicker.ColorPicker.selected_color #init with red (255,0,0)
	print("Init Color:",selected_color)
	selected_background = settings.selected_background
	background = settings.background
	create_workscreen = settings.create_workscreen
	selected_btn = settings.selected_btn
	selected_item = settings.selected_item
	selected_item_name = settings.selected_item_name
	selected_item_status = settings.selected_item_status

	# Only for View (Save Img and Pos)
	selected_items = settings.selected_items
	# Only for Record (Save Name and Pos)
	record_selected_items = settings.record_selected_items

	input_editable = settings.input_editable
	tactics_name = settings.tactics_name
	save_file = settings.save_file
	record_stage = settings.record_stage
	all_stages = settings.all_stages
	replay_mode_active = settings.replay_mode_active
	replay_mode = settings.replay_mode
	replay_stage = settings.replay_stage

	# Replay Time Setting (2s 1 scene)
	clock = pg.time.Clock()
	switch_scene_timer = settings.switch_scene_timer
	switch_scene_interval = settings.switch_scene_interval
	initialized_replay_mode = settings.initialized_replay_mode

	# Paintbrush
	drawing_mode = settings.drawing_mode
	drawing = settings.drawing
	drawing_positions = settings.drawing_positions
	all_drawings = settings.all_drawings

	# Start Looping
	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			elif event.type == pg.KEYDOWN and input_editable:
				if event.key == pg.K_BACKSPACE:
					tactics_name = tactics_name[:-1]
				else:
					tactics_name += event.unicode
			elif event.type == pg.MOUSEBUTTONUP:
				if drawing:
					drawing = False
					print("End of drawing line")
			elif event.type == pg.MOUSEBUTTONDOWN:
				# Select Background
				x,y = event.pos
				if not selected_background:
					if bg_fullcourt_btn.collidepoint(x, y):
						selected_background = True
						background = bg_fullcourt
						new_recorder.court = "fullcourt"
						workingscreen_btns_diff_x = settings.fullcourt_btns_diff_x
						buttons_move_x(btns = working_btns,move_diff = workingscreen_btns_diff_x)
					elif bg_frontcourt_h_btn.collidepoint(x, y):
						selected_background = True
						background = bg_frontcourt_h
						new_recorder.court = "frontcourt_h"
						workingscreen_btns_diff_x = settings.frontcourt_h_btns_diff_x
						buttons_move_x(btns = working_btns,move_diff = workingscreen_btns_diff_x)
					elif bg_frontcourt_v_btn.collidepoint(x, y):
						selected_background = True
						background = bg_frontcourt_v
						new_recorder.court = "frontcourt_v"
						workingscreen_btns_diff_x = settings.frontcourt_v_btns_diff_x
						buttons_move_x(btns = working_btns,move_diff = workingscreen_btns_diff_x)
					elif bg_replay_btn.collidepoint(x, y):
						replay_mode_active = True
						selected_background = True
						# select file and decide which background to use
						save_data = replayer.load_file()
						new_replayer = replayer.Replayer(recorder = new_recorder, json_data = save_data)
						print("Replayer properties:")
						print(new_replayer.recorder.__dict__)
						# check which background needs to be load in load files
						court = new_replayer.recorder.court
						if court == "frontcourt_v":
							background = bg_frontcourt_v
							workingscreen_btns_diff_x = 0
						elif court == "frontcourt_h":
							background = bg_frontcourt_h
							workingscreen_btns_diff_x = 0
						elif court == "fullcourt":
							background = bg_fullcourt
							workingscreen_btns_diff_x = 0
						else:
							raise ValueError("Invalid court in save_data")
						# Go into replay mode but not replay immediately(there's a replay btn in working stage)
				# Select Player & Ball
				else:
					if team_player_btn.collidepoint(x, y):
						selected_item = team_player
						selected_btn = True
						selected_item_name = "TeamPlayer"
						# print("Select Player")
					if rival_player_btn.collidepoint(x, y):
						selected_item = rival_player
						selected_btn = True
						selected_item_name = "RivalPlayer"
						# print("Select Rival Player")
					if ball_btn.collidepoint(x, y):
						selected_item = ball
						selected_btn = True
						selected_item_name = "Ball"
						# print("Select Ball")
					if reset_btn.collidepoint(x, y):
						selected_items.clear()
						record_selected_items.clear()
						drawing_positions.clear()
						for key in selected_item_status:
							selected_item_status[key] = 0
						print("Reset current stage editing")
					# Start replay scene in working stage (can't use replay in edit mode)
					if replay_btn.collidepoint(x, y) and replay_mode_active:
						replay_mode = True
						# clear the screen first
						selected_items.clear()
						drawing_positions.clear()
					if colorpicker_btn.collidepoint(x, y):
						selected_color = colorpicker.OpenColorPicker()
						print("Select color:",selected_color)
					if paintbrush_btn.collidepoint(x, y):
						drawing_mode = not drawing_mode
						print("Drawing_mode changed")
					if event.button == 1 and drawing_mode and not replay_mode:
						drawing = True
					# Back to mainscreen
					if mainscreen_btn.collidepoint(x, y):
						selected_background = False
						create_workscreen = False
						buttons_move_x(btns = working_btns,move_diff = workingscreen_btns_diff_x, reverse = True)
						# reset screen size
						screen = pg.display.set_mode(window_size,pg.RESIZABLE)
					# Input editable only click on the box
					if name_input_box.collidepoint(x, y):
						input_editable = True
					else:
						input_editable = False
					# Save Stage & File btn
					if save_stage_btn.collidepoint(x, y):
						record_stage = True
					if save_file_btn.collidepoint(x, y):
						save_file = True
					# if selected btn and another mouse right click(decide position)
					if selected_btn and event.button == 3:
						mouse_x, mouse_y = pg.mouse.get_pos()
						selected_position = (mouse_x, mouse_y)
						selected_items.append((selected_item,selected_position))
						record_selected_items.append((selected_item_name,selected_position))
						selected_item_status = update_selected_item_status(selected_item_status,selected_item_name)
						# print(selected_item_status)
						# print(record_selected_items)
						# Reset Status
						selected_btn = False
						selected_item_name = ""

		# Init Screen & 3 btns
		if not selected_background:
			screen.blit(bg_init, (0,0))
			pg.draw.rect(screen, settings.BLACK, bg_fullcourt_btn)
			pg.draw.rect(screen, settings.BLACK, bg_frontcourt_h_btn)
			pg.draw.rect(screen, settings.BLACK, bg_frontcourt_v_btn)
			pg.draw.rect(screen, settings.BLACK, bg_replay_btn)

			# Text
			text1 = font.render("Fullcourt", True, settings.WHITE)
			text2 = font.render("Frontcourt Horizontal", True, settings.WHITE)
			text3 = font.render("Frontcourt Vertical", True, settings.WHITE)
			text4 = font.render("Replay", True, settings.WHITE)

			# Version Text
			version_text = font.render(f"Version = {settings.VERSION}", True, settings.WHITE)

			# Draw Text
			screen.blit(text1, (bg_fullcourt_btn.x + 70, bg_fullcourt_btn.y + 15))
			screen.blit(text2, (bg_frontcourt_h_btn.x + 20, bg_frontcourt_h_btn.y + 15))
			screen.blit(text3, (bg_frontcourt_v_btn.x + 30, bg_frontcourt_v_btn.y + 15))
			screen.blit(text4, (bg_replay_btn.x + 80, bg_replay_btn.y + 15))
			screen.blit(version_text, (bg_frontcourt_v_btn.x + 200, bg_frontcourt_v_btn.y + 360))
		# Working Stage
		else:
			if not create_workscreen:
				# get background width and height to modify new screen size
				bg_width, bg_height = background.get_size()
				working_screen = pg.display.set_mode((bg_width + settings.WORKING_WINDOW_WIDTH,bg_height),pg.RESIZABLE)
				create_workscreen = True
			# TODO: Maybe add some color for background (at least dark mode and white mode)
			working_screen.fill(settings.WHITE)
			working_screen.blit(background, (0, 0))
			# Draw & Show Player / Ball / Tools  Buttons #
			pg.draw.rect(working_screen, settings.BLACK, team_player_btn)
			pg.draw.rect(working_screen, settings.BLACK, rival_player_btn)
			pg.draw.rect(working_screen, settings.BLACK, ball_btn)
			pg.draw.rect(working_screen, settings.BLACK, reset_btn)
			pg.draw.rect(working_screen, settings.BLACK, replay_btn)
			pg.draw.rect(working_screen, selected_color, colorpicker_btn)
			pg.draw.rect(working_screen, settings.BLACK, paintbrush_btn)
			pg.draw.rect(working_screen, settings.BLACK, mainscreen_btn)
			pg.draw.rect(working_screen, settings.BLACK, name_input_box,2)
			pg.draw.rect(working_screen, settings.BLACK, save_stage_btn)
			pg.draw.rect(working_screen, settings.BLACK, save_file_btn)

			# Text
			text1 = font.render("Team Player", True, settings.WHITE)
			text2 = font.render("Rival Player", True, settings.WHITE)
			text3 = font.render("Ball", True, settings.WHITE)
			text4 = font.render("Reset", True, settings.WHITE)
			tactics_name_text = font.render(tactics_name, True, settings.BLACK)
			text5 = font.render("Save Stage", True, settings.WHITE)
			text6 = font.render("Save File", True, settings.WHITE)
			text7 = font.render("Replay", True, settings.WHITE)
			text9 = font.render("Main menu", True, settings.WHITE)
			if drawing_mode:
				text8 = font.render("Drawing", True, settings.WHITE)
			else:
				text8 = font.render("Not Drawing", True, settings.WHITE)

			# Draw Text
			working_screen.blit(text1, (team_player_btn.x + 30, team_player_btn.y + 15))
			working_screen.blit(text2, (rival_player_btn.x + 30, rival_player_btn.y + 15))
			working_screen.blit(text3, (ball_btn.x + 60, ball_btn.y + 15))
			working_screen.blit(text4, (reset_btn.x + 50, reset_btn.y + 15))
			working_screen.blit(tactics_name_text, (name_input_box.x + 5, name_input_box.y + 15))
			working_screen.blit(text5, (save_stage_btn.x + 15, save_stage_btn.y + 15))
			working_screen.blit(text6, (save_file_btn.x + 15, save_file_btn.y + 15))
			working_screen.blit(text7, (replay_btn.x + 50, replay_btn.y + 15))
			working_screen.blit(text8, (paintbrush_btn.x + 30, paintbrush_btn.y + 15))
			working_screen.blit(text9, (mainscreen_btn.x + 30, mainscreen_btn.y + 15))

			# add some follow effect to the input box
			name_input_box.w = max(100, tactics_name_text.get_width() + 10)

			# Playbook Planning Stage #
			for img,pos in selected_items:
				working_screen.blit(img, pos)

			# Drawing Stage
			if drawing:
				drawing_x, drawing_y = pg.mouse.get_pos()
				# Don't record dots on the button
				if not paintbrush_btn.collidepoint(drawing_x, drawing_y):
					drawing_position = (drawing_x, drawing_y)
					line_color = selected_color
					drawing_positions.append([line_color,drawing_position])

			for color,position in drawing_positions:
				pg.draw.circle(working_screen, color, position, 10)

			# Record Stages & Saving Files
			if record_stage:
				# Must use copy() --> clear() will affect on append() --> FXXK
				all_stages.append(record_selected_items.copy())
				all_drawings.append(drawing_positions.copy())
				record_stage = False
				# clean up the screen for the new stage
				selected_items.clear()
				record_selected_items.clear()
				drawing_positions.clear()
				for key in selected_item_status:
					selected_item_status[key] = 0
				print("Current Record Stages:")
				print(all_stages)
				print("=========")

			if save_file:
				# Record all stages to the recorder
				new_recorder.all_stages = all_stages
				new_recorder.all_drawings = all_drawings
				# Show save data
				print(new_recorder.__dict__)
				save_json_file(recorder = new_recorder, filename = tactics_name)
				save_file = False
				all_stages.clear()
				all_drawings.clear()

			# Replay Mode
			# this if-statement will fix the init replay mode incomplete problem
			if replay_mode and not initialized_replay_mode:
				selected_items,drawing_positions = playscene(replayer = new_replayer, stage = replay_stage, obj_list = [team_player,rival_player,ball])
				initialized_replay_mode = True
				switch_scene_timer = 0

			if replay_mode:
				if replay_stage == new_replayer.recorder.stages:
					replay_mode = False
					initialized_replay_mode = False
					replay_stage = 0
					print("End of Replay")
				else:
					switch_scene_timer += clock.tick()
					# update selected_items for displaying only if the list is empty (decrease complexity)
					if len(selected_items) == 0:
						selected_items,drawing_positions = playscene(replayer = new_replayer, stage = replay_stage, obj_list = [team_player,rival_player,ball])
					if switch_scene_timer >= switch_scene_interval:
						print(f"Replay Stage:{replay_stage}")
						replay_stage += 1
						switch_scene_timer = 0
						selected_items.clear()
						drawing_positions.clear()

		# Update View
		pg.display.flip()

# Main Function #
"""
Step 1. Show Version & Check Resource
Step 2. Init Game & Run
"""
def main():
	# Show Version & Check Resource
	check_version(settings.VERSION)
	check_files(check_files_folder = "pic", check_list = settings.PIC_FILE)
	# Init Game & Run
	game_loop(window_size = settings.INIT_WINDOW_SIZE)

# Start Program #
if __name__ == '__main__':
	main()