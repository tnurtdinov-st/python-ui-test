class GroupHepler:
    def __init__(self, app):
        self.app = app

    def get_group_list(self):
        self.open_group_editor()
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        root = tree.tree_root()
        group_list = [node.text() for node in root.children()]
        self.close_group_editor()
        return group_list


    def add_new_group(self, name):
        self.open_group_editor()
        self.group_editor.window(auto_id="uxNewAddressButton").click()
        input = self.group_editor.window(class_name="Edit")
        input.set_text(name)
        input.type_keys("\n")
        self.close_group_editor()

    def open_group_editor(self):
        self.app.main_window.window(auto_id="groupButton").click()
        self.group_editor = self.app.application.window(title="Group editor")
        self.group_editor.wait('visible', timeout=20, retry_interval=0.5)
        self.group_editor.set_focus()

    def close_group_editor(self):
        self.group_editor.close()

    def del_group(self, name):
        self.open_group_editor()
        import time
        tree = self.group_editor.window(auto_id="uxAddressTreeView")
        tree.GetItem(['Contact groups', name]).Click()
        self.group_editor.window(auto_id="uxDeleteAddressButton").click()
        self.del_window = self.app.application.window(title="Delete group")
        self.del_window.window(auto_id="uxDeleteAllRadioButton").click()
        #time.sleep(1)
        self.del_window.window(auto_id="uxOKAddressButton").click()
        time.sleep(1)




