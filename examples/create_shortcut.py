from shortcut import ShortCutter
s = ShortCutter()
s.create_desktop_shortcut("python")
s.create_menu_shortcut("python")
s.create_desktop_shortcut("python", target_name="my python")
s.create_menu_shortcut("python", target_name="my python")