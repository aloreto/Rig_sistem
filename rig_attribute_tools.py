'''

---- importing module and functions -----
You have to do both, import the module and then import each function as you need it.

import sys
sys.path.append('C:/Users/TINTO/Documents/maya/2020/scripts/Rig_sistem/rig_utilities.py')

import rig_utilities
reload (rig_utilities)

from rig_utilities import float_attributeCreator
from rig_utilities import enum_attributeCreator

'''

#import maya.cmds as cmds


'''
Atribute creation and locking functions
----------------------------------------
'''

# Attribute creation functions
#-----------------------------

def integer_attributeCreator(Object, attributeName, maxValue=2, minValue=0, defaultValue=0):  

    newIntegerAttribute = cmds.addAttr(Object, longName = attributeName,  attributeType = 'long', min = minValue,  max = maxValue,  defaultValue = defaultValue)    
    cmds.setAttr('{}.{}'.format(Object, attributeName), channelBox=True)    


def float_attributeCreator(Object, attributeName, maxValue=2, minValue=0, defaultValue=0):  

    newIntegerAttribute = cmds.addAttr(Object, longName = attributeName,  attributeType = 'double', min = minValue,  max = maxValue,  defaultValue = defaultValue)    
    cmds.setAttr('{}.{}'.format(Object, attributeName), channelBox=True)       


def boolean_attributeCreator(Object, attributeName, defaultValue=0):  

    newIntegerAttribute = cmds.addAttr(Object, longName = attributeName,  attributeType = 'bool', min = minValue,  max = maxValue,  defaultValue = defaultValue)    
    cmds.setAttr('{}.{}'.format(Object, attributeName), channelBox=True)     


def enum_attributeCreator(Object, attributeName, stringValues=[]): 

    # the "stringValues" variable gets a list with the unum names. Example [hat, cap, hair]
    # The enum names to be shown in the attribute drop down is given to maya with a semicolon inbetween each name
    # maya will receive this example 'hat:cap:hair'
    # the 'join' command will connect all ellements in the stringValues and the : inside the '' string simbols will be added inbetween
    enum_name_list = enum_name_list = ':'.join(stringValues)
   
    newIntegerAttribute = cmds.addAttr(Object, longName = attributeName,  attributeType = 'enum', enumName=enum_name_list)    
    cmds.setAttr('{}.{}'.format(Object, attributeName), channelBox=True)    


# Attribute locking functions
#----------------------------- 

def attributeLocker (controlName,                     
                    lock_translations = False,
                    lock_rotations = False,
                    lock_Scale = False,
                    lock_visibility = True,  
                    lock_T_X = False, lock_T_Y = False, lock_T_Z = False,
                    lock_R_X = False, lock_R_Y = False, lock_R_Z = False, 
                    lock_S_X = False, lock_S_Y = False, lock_S_Z = False,
                    customAttributes = []):

    if lock_translations is True: 
        for axis in ('X','Y','Z'):
            cmds.setAttr('{}.translate{}'.format(controlName, axis), lock = True)          
    
    if lock_rotations is True:
        for axis in ('X','Y','Z'):
            cmds.setAttr('{}.rotate{}'.format(controlName, axis), lock = True)      

    if lock_Scale is True:
        for axis in ('X','Y','Z'):
                    cmds.setAttr('{}.scale{}'.format(controlName, axis), lock = True)   

    if lock_visibility is True:
        cmds.setAttr('{}.visibility'.format(controlName), lock = True)   

    if lock_T_X is True:
        cmds.setAttr('{}.translateX'.format(controlName), lock = True)    

    if lock_T_Y is True:
        cmds.setAttr('{}.translateY'.format(controlName), lock = True) 

    if lock_T_Z is True:
        cmds.setAttr('{}.translateZ'.format(controlName), lock = True)    

    if lock_R_X is True:
        cmds.setAttr('{}.rotateX'.format(controlName), lock = True)

    if lock_R_X is True:
        cmds.setAttr('{}.rotateX'.format(controlName), lock = True) 

    if lock_R_Y is True:
        cmds.setAttr('{}.rotateY'.format(controlName), lock = True) 

    if lock_R_Z is True:
        cmds.setAttr('{}.rotateZ'.format(controlName), lock = True)  

    if lock_S_X is True:
        cmds.setAttr('{}.scaleX'.format(controlName), lock = True) 

    if lock_S_Y is True:
        cmds.setAttr('{}.scaleY'.format(controlName), lock = True)

    if lock_S_Y is True:
        cmds.setAttr('{}.scaleZ'.format(controlName), lock = True)

    if customAttributes != None:
        for item in customAttributes:
            cmds.setAttr('{}.{}'.format(controlName, item), lock = True)
       


        

    


                


       
