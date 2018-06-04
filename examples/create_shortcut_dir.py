from shortcut import ShortCutter
s = ShortCutter()

#s.create_desktop_shortcut("c:\\Users\\")
#s.create_menu_shortcut("c:\\Users\\")
#s.create_desktop_shortcut("c:\\Users\\", target_name="my users")
#s.create_menu_shortcut("c:\\Users\\", target_name="my users")

s.create_desktop_shortcut("/home/pi/")
s.create_menu_shortcut("/home/pi/")
s.create_desktop_shortcut("/home/pi/", target_name="pi home")
s.create_menu_shortcut("/home/pi/", target_name="pi home")
