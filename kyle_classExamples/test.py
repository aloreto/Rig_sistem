import maya.cmds as cmds


modules_list=('simple control','FK chain','IK chain','Spline IK','follow control')


def parameter_field_adder('moduleName'):
    
    print 'pepe'
    
    if module_name == 'simple control':  
        cmds.textField(text='name')
        cmds.textField(text='control shape')
        cmds.textField(text='sub-control count')    
        
       



cmds.window( widthHeight=(300, 600) )

cmds.rowColumnLayout( height=(300))
scrollLayout = cmds.scrollLayout(horizontalScrollBarThickness=16, verticalScrollBarThickness=16, height=300)
cmds.rowColumnLayout( numberOfColumns=1 )


for module in modules_list:
    
    cmds.button( label=module, width = 300, command= parameter_field_adder(), height=50)
    cmds.separator(h=10)
    
cmds.setParent('..')
cmds.setParent('..')		

cmds.rowColumnLayout()






cmds.setParent('..')	



cmds.showWindow()


    