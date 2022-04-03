from Tki.KiWidgets import *
from Tki.KiFont import KiFont

Window = KiWindow()
Window.SetTitle("Demo")
Window.SetTtkStyle(Style_SunValley, Theme_Light)

Font = KiFont(Root=Window.GetWidget(), Weight="normal")

ScrollBar = KiScrollBar()
ScrollBar

Text = KiTextView(YScroll=ScrollBar.SetValue)
Text.PackWidget(Fill=Fill_BOTH, Expand=Expand_NO)

Window.Run()
