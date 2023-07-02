shoulder_ctrl = Control('shoulder', 'blue', 'circle')
elbow_ctrl = Control('elbow', 'blue', 'circle')
wrist_ctrl = Control('wrist', 'blue', 'circle')

cmds.xform(shoulder_ctrl.adj1, ws=True, m=[])
cmds.xform(elbow_ctrl.adj1, ws=True, m=[])
cmds.xform(wrist_ctrl.adj1, ws=True, m=[])

cmds.addAttr(wrist_ctrl.ctrl, ln='ikfk', )

wrist_ctrl.add_adj_group()

adj_name = wrist_ctrl_name.replace()
new_adj_grp = add_adj_group(wrist_adj, wrist_ctrl, adj_name)


def add_adj_group(last_adj, ctrl, name):
    pass
    # do stuff