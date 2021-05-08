import random
def test_del_group(app):
    if len(app.groups.get_group_list())==0:
        app.groups.add_new_group("test_group")
    if len(app.groups.get_group_list())==1:
        app.groups.add_new_group("test_group2")
    old_list = app.groups.get_group_list()
    group = random.choice(old_list)
    app.groups.del_group(group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)
