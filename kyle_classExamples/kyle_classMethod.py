class Control():
    
    def __init__(self, name, color, ctrl_shape):

        self.name = name+'_ctrl'
        self.color = color
        self.ctrl_shape = ctrl_shape

        self.adj = []
        self.ctrl = None
        self.shape = None

        self.shape_names = [
            'circle', 
            'box', 
            'diamond'
        ]

        self.create()

    def create(self):
        pass
        # make the adj group
        self.adj.append(cmds.group(self.name.replace('ctrl', 'adj'), em=True))

        # make the control
        self.ctrl = cmds.group(self.name, em=True, parent=self.adj[0])
        self.create_control_shape()

    def create_control_shape(self):
        pass
        if self.ctrl_shape not in self.shape_names:
            raise ValueError('Invalid shape name')
        # create curve shape

        # parent shape to self.ctrl
        # populate self.shape
    
    def add_adj_group(self):
        self.adj.append(cmds.group(self.name.replace('ctrl', 'adj'), em=True, parent=self.adj[-1]))
        cmds.parent(self.ctrl, self.adj[-1])


        