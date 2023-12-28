"""
Button Control
"""

import pygame as pg

# Background Image Button #
BackgroundImageButton = {
"Fullcourt":pg.Rect(750, 200, 200, 50),
"Frontcourt Horizontal":pg.Rect(750, 300, 200, 50),
"Frontcourt Vertical":pg.Rect(750, 400, 200, 50),
"Replay":pg.Rect(750, 500, 200, 50)
}

# Players Button #
PlayersButton = {
"TeamPlayer": pg.Rect(1000, 100, 150, 50),
"RivalPlayer": pg.Rect(1000, 200, 150, 50),
}

# Ball Button #
BallButton = {
"Ball": pg.Rect(1000, 300, 150, 50)
}

# Name Input Box #
NameInputBox = {
"Input": pg.Rect(1000, 770, 150, 50)
}

# Reset Button #
ResetButton = {
"Reset": pg.Rect(1000, 850, 150, 50)
}

# Save Button #
SaveButton = {
"Stage": pg.Rect(1180, 850, 120, 50),
"File": pg.Rect(1320, 850, 100, 50)
}

# Replay Button (Working Screen)#
ReplayButton = {
"Replay": pg.Rect(1000, 400, 150, 50)
}

# ColorPicker Button (Working Screen)#
ColorPickerButton = {
"Colorpicker": pg.Rect(1000, 500, 150, 50)
}

# Paintbrush Button (Working Screen)#
PaintbrushButton = {
"Paintbrush": pg.Rect(1000, 600, 150, 50)
}

# Mainscreen Button (Working Screen back to Mainscreen)#
MainscreenButton = {
"Mainscreen": pg.Rect(1000, 700, 150, 50)
}