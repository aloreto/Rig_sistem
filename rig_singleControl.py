

import maya.cmds as cmds
import sys
import os

'''
------   Synopsis of workflow  -------

This module can create a single control based on a place holder object
The "place holder" object will control the characteristics of the control with attritutes
The attributes will define the following capabilities:

1- sub-control count
2- adjustment group count
3- adjustment group names
4- control name
5- control shape
6- control color
7- lock axis translation
8- lock axis rotation
9- lock visibility
10- lock scale
11- build priority
12- build stage


The "control building process" will go through this process:

1- Query all existing "single control place holders"
2- Query and set STAGE and PRIORITY attributes 
3- Create a list of controls to be build based on: [first by STAGE and second by PRIORITY] 
4- Start building each control based on that list
5- Query all control characteristics attributes
6- Query place holder control's child
6- Build the control
7- Parent each control to it's corresponding child placeholder control
8- organize contraint nodes under a group outside of the default place.
9- Impost saved skinning

Utilities in this single control module:

1- Attribute creation
2- Control shape creation
4- Lock attribute

Note: The singleConstrol module will contain all utilities necessary for ALL FUTURE CONTROL FUNCTIONS
Like: attribute creation, control shape creation, etc....

'''

 

def integer_attributeCreator(Object, attributeName, maxValue=-10, minValue=10, defaultValue=0):  

    newAttribute = cmds.addAttr(Object, longName = attributeName,  attributeType = 'long', min = minValue,  max = maxValue,  defaultValue = defaultValue)
    cmds.setAttr('{}.{}'.format(Object, attributeName), channelBox=true)
    return newAttribute

   
            



class ControlShape_creator():

    def __init__(self, controlName, shapeStyle, color, adjustment_nodes = None):

        self.controlName = controlName
        self.shapeStyle = shapeStyle
        self.color = color

        if adjustment_nodes is None:
            self.adjustment_nodes = []
        else:
            self.adjustment_nodes = adjustment_nodes
    


class Attribute_locker():

    def __init__(self, controlName,
                    lock_translations = False,
                    lock_rotations = False,
                    lock_Scale = False,
                    lock_visibility = True,  
                    lock_T_X = False, lock_T_Y = False, lock_T_Z = False,
                    lock_R_X = False, lock_R_Y = False, lock_R_Z = False, 
                    lock_S_X = False, lock_S_Y = False, lock_S_Z = False,
                    customAttributes=None):

        self, controlName = controlName
        self.lock_translations = lock_translations
        self.lock_rotations = lock_rotations
        self.lock_Scale = lock_Scale
        self.lock_visibility = lock_visibility
        self.lock_T_X = lock_T_X
        self.lock_T_Y = lock_T_Y
        self.lock_T_Z = lock_T_Z
        self.lock_R_X = lock_R_X
        self.lock_R_Y = lock_R_Y
        self.lock_R_Z = lock_R_Z
        self.lock_S_X = lock_S_X
        self.lock_S_Y = lock_S_Y
        self.lock_S_Z = lock_S_Z

        if customAttributes is None:
            customAttributes = []
        else:
            self.customAttributes = customAttributes







