from pywinauto.application import Application as WinApplication
from fixture.group import GroupHepler
class Application:

    def __init__(self, target):
        self.application =  WinApplication(backend="win32").start(target)
        self.main_window = self.application.window(title="Free Address Book")
        self.main_window.wait('visible', timeout=20, retry_interval=0.5)
        self.main_window.set_focus()
        self.groups = GroupHepler(self)

    def destroy(self):
        self.main_window.close()

