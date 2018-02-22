class ShortcutError(Exception):
    pass

class ShortcutTargetError(ShortcutError):
    pass

class ShortcutNoDesktopError(ShortcutError):
    pass

class ShortcutNoMenuError(ShortcutError):
    pass
