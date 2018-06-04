class ShortcutError(Exception):
    pass

class ShortcutNoDesktopError(ShortcutError):
    pass

class ShortcutNoMenuError(ShortcutError):
    pass

class ShortcutTargetNotFound(ShortcutError):
    pass
