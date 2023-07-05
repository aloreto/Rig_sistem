def row_test():
    
    def add_row(cameraname) :
        
        
        if cameraname=='simple control':
            
            
        
            cmds.setParent(column)
            this_row = cmds.rowColumnLayout(numberOfColumns=2  )            
            cmds.text(l= cameraname )        
            start = cmds.intField() 
            cmds.text(l= cameraname )        
            start = cmds.intField()  
            cmds.text(l= cameraname )        
            start = cmds.intField()  
            cmds.text(l= cameraname )        
            start = cmds.intField()  
            cmds.text(l= cameraname )        
            start = cmds.intField()  
            cmds.text(l= cameraname )        
            start = cmds.intField()  
             
            
        else:
            
            print'THIS IS NOW WORKING'
              
      

    window = cmds.window(title='lotsa rows')
    column = cmds.columnLayout()
    
    cmds.optionMenuGrp( label='Module Type', columnWidth=(20, 60), columnAlign2=['left', 'left'], height=40, changeCommand=add_row)
    cmds.menuItem( label='--choose a moddule--' )
    cmds.menuItem( label='simple control' )
    cmds.menuItem( label='FK chain' )
    cmds.menuItem( label='IK chain' )

    

    
        
        
        
    cmds.button( label='ADD MODULE', width =400, height=50)     



    cmds.showWindow(window)


row_test()