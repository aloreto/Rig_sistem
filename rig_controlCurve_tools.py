'''
This module will hold all control curve tools

1- query curcve cv points
2- save control cv data into a json file
3- recreate control curves
4- change control curve COLORS
5- Flip / Mirror control curve shapes

'''

#-----------------------------------------
# importing libraries
#-----------------------------------------
import os
import json
from maya import cmds as cmds
from maya import OpenMaya as om # this is the maya API library
import re 
# "re" Maya API library (Support for regular expressions)
# methods included are: __delattr__, __getattribute__, __setattr__, etc...

#-----------------------------------------
# UTILITIES
#-----------------------------------------


def jsonFilePath_validator(path = None):
    # this function verifies teh path given to the function. The path is the json file containing the curve shape vertex information 
    # jason file path verification. Does the file exists or not? do you want to overrite it?

    # os.path is a sub-module of the OS module in python
    # this method returns a boolean output. It evaluates whether a file is a "EXISTS" or NOT
    if os.path.isfile(path):
        #creating a dialog in maya that asks if you want to overrite the file given or not
        confirmMessage = cmds.confirmDialog(title = 'Overwrite existing file?',
                                            nessage = 'The file' + path + 'already exists. Do you want to overwrite it?',
                                            button = ['Yes', 'No'],
                                            defaultButton = 'Yes',
                                            cancelButton = 'No',
                                            dismissString = 'no') 

        # if the path given doesn't exists (this comes from the 'os.path.isfile' evaluation) warn it doesn't exists
        if confirm == 'No':
            cmds.warning('The file' + path + 'was not saved')
            # if that files doesn't exists, the function will return None (nothing)
            return 0
        # if the path was found, then return True 
        return 1   


def saveJasonData(path = None, data = None):
    # the previous function was the path and file validator. This new function is the one that actually writes/saves the jason file
    # the "data" variable contains the dictionary holding all the curve's knots and vertices data

    if jsonFilePath_validator(path):

        # The yntax for the open command is: "open(file, mode)"
        # the modes are: 'r' = read, 'a' = append, 'w' = write, 'x' = create
        f = open(path, 'w')
        f.write(json.dumps(data, sort_keys = 1, indent = 4, separators = (',', ':')))
        f.close()
        return 1

    return 0


def loadJasonData():
    if os.path.isfile(path):
        # here the mode is in "read" as we are only loading the information in the json file
        f = open(path, 'r') 
        # the variable 'data' will now store the information read from the json file
        # this line combines two functions: 1- read the file "f". 2- '.loads' then converts to a 'python dictionary' the data read from the json file
        data = json.loads(f.read())
        f.close()
        # now, we return the data unloaded from this process with the variable 'data'
        return data

    else:
        # notece that the strngs use "" instead of ''. This is because the doesn't clashes with the '' from the strings
        cmds.error("The file" + path + "doesn't exists")


def getKnotsData(curveShape = None):
    
    # Here, the Open Maya library will be used
    # ".MObject" creates an instance of an object for us to use. To access any maya object you have to initialize it with this command
    mObj = om.MObject()
    # "MCurveList" creates an empty list in open maya where we can add Maya Active objects to it    
    # This is so we can manipulate multiple data elements in one list
    sel = MCurveList()
    # adding the curve passed to the function to the object list instance. This is the curve for which we want to get the vertices value to store the shape
    sel.add(curveShape)
    #"getDependNode" is a method of the "MCurveList" class. It finds the node under an object. Here we want the node with ID [0] (the shape)
    # we are getting the element [0] from the instanced object "mObj", which is the curve nourb we passed to the function
    sel.getDependNode(0, mObj)

    # now here the code gets the data from that instanced object
    # to get the nurb information a new class will be used "MFnNurbsCurve"
    
    nbsCurve = om.MFnNurbsCurve(mObj)
    # the function needed to get the knots of the curve needs to be set as an array type of output. Here we are setting that array
    nbsKnots = om.MdoubleArray()
    # now, we call the class method "getKnots" from the class "MFnNurbsCurve" to get the values
    nbsCurve.getKnots(nbsKnots)

    # finally, we loop through the list of knots stored int he nbs array (knots list) created before
    #[i] is the number of items or id length
    return [nbsKnots[i]
            # for each item in the index "i" return it.
             for i in range(nbsKnots.length())]


#-----------------------------------------
# CALL FUNCTIONS (to be called from UI)
#-----------------------------------------

def validateCurve(Curve= None):

    # finding what type of object the given name is and save that in a variable
    ObjectNodeType = cmds.nodeType(Curve)
    # Fnding the shape of the object given and save that in a variable
    CurrentShape = cmds.listRelatives(Curve, children=True, shapes=True)
    #find what thype of node the previous shape is and saving that into a variable
    checkNurbsTypeObject = cmds.nodeType(CurrentShape)

    # now we are evaluating the previous variables to see if the object is a 'transorm' and if the shape is a 'nurbsCurve'
    if ObjectNodeType == 'transform' and checkNurbsTypeObject == 'nurbsCurve':
        # if the object is a transorm and also is a nurbsCurve set the name of the shape as a valid nurbsCuve object
        curveShape = CurrentShape        
        print('The selected curve shape is {}'.format(curveShape))
        
    else:
        # this error is the same as a print, except that shows as an error in the output 
        cmds.error('The object' + Curve + 'is not a valid curve')    

    return curveShape    


def getCurveShape_data(Curve = None):
    # Returns a dictionary containing all the necessery information for rebuilding the curve passed to the function
    # callling the validator function to get the shape and check it's a nurbsCurve
    curveShape = validateCurve(Curve)

    # Declaring an empty list that will contain the dictionary of curve data per curveShape name
    CurveShapesList = []

    # looping on each curveShape given and create a dictionary of data for each
    for curveShape in curveShapes:

        # setting the dictionary by fetching the date using getAttr function
        CurveShapeDict = {
                        'points':[],
                        'knots':[],
                        'form': cmds.getAttr(curveShape + '.form'),
                        'degree': cmds.getAttr(curveShape + '.degree'),
                        'colour': cmds.getAttr(curveShape + '.overrideColor'), }

        # empty list that will hold the data of the points and knots
        points = []

        # looping on each controlPOint of the curve and getting the size array with positioning info
        for i in range(cmds.getAttr(curveShape + 'controlPoints', size=True)):
            # now we append that information to the dictionary key value set before as 'points'
            points.append(cmds.getAttr(curveShape + '.controlPoints[{}]'.format(i)[0]))

        # asigning the points values
        CurveShapeDict['points'] = points
        # getting and assigning the knots data of the curve by calling the utility function 'getKnotsData'
        CurveShapeDict ['knots'] = getKnotsData(curveShape)
        # finally appending all the dictionary with info on the specific curve shape to the list
        
        CurveShapesList.append(CurveShapeDict)

    return CurveShapesList   

  

def saveToLib(Curve=None, shapeName=None):

    # Saves the shape data to a shape file in the SHAPE_LIBRARY_PATH directory'''
    # calling the function that gets all the construction information data from the given curveShape
    curveShape = getCurveShape_data(Curve)

    # setting the path where the json file with the curve data will be save
    path = os.path.join(SHAPE_LIBRARY_PATH, re.sub("\s", "", shapeName) + ".json")

    for shapeDict in curveShape:
        shapeDict.pop("colour", None)

    # calling the function that saves the actual .jason file
    utils.saveData(path, CurveShape)
    
    

def loadFromLib(shape=None):
    # Loads the shape data from the shape file in the SHAPE_LIBRARY_PATH directory'''
     # setting the path where the json file exists
    path = os.path.join(SHAPE_LIBRARY_PATH, shape + ".json")
    # calling the function that loads the curve construction data from the .json file
    data = utils.loadData(path)
    # returnign the data loaded from the .json file
    return data


def setShape(Curve, CurveShapeList):
    # note that here we are passing the returned data fetched by the "getCurveShape_data" function
    # Creates a new shape on the Curve transform, using the properties in the CurveShapeDict
    # Checking if the object is a nurbsCurve   
    CurveShapes = validateCurve(Curve)

    # checking the curve color that the object has
    oldColour = mc.getAttr(CurveShapes[0] + ".overrideColor")
    # deleteing the CurveSHape. A new one will be created
    mc.delete(CurveShapes)

    # Looping on the construction data dictionary. i is an item key in the dictionary
    # enumerate give an id number position to each i item in the dictionary
    for i, CurveShapeDict in enumerate(CurveShapeList):
        # creating a temporary curve using the data from the json file
        tmpCurve = cmds.curve(p=CurveShapeDict["points"], k=CurveShapeDict["knots"], d=CurveShapeDict["degree"], per=bool(CurveShapeDict["form"]))
        # Getting the shape of the just created temp curve
        newShape = cmds.listRelatives(tmpCurve, s=1)[0]
        # parenting the new shape curve to the transform of our initial curve
        cmds.parent(newShape, Curve, r=1, s=1)
        # deleting transform of temp curve we created
        cmds.delete(tmpCurve)
        # renaming the new shape created from the temp curve so it haves the corret name base on the original "Curve" transform
        newShape = cmds.rename(newShape, Curve + "Shape" + str(i + 1).zfill(2))
        # setting overrideEnable so color is shown
        cmds.setAttr(newShape + ".overrideEnabled", 1)
        # settign the new color evaluation
        if "colour" in CurveShapeDict.keys():
            setColour(newShape, CurveShapeDict["colour"])
        else:
            setColour(newShape, oldColour)


def setColour(Curve, colour):
    # Sets the overrideColor of a curve
    if cmds.nodeType(Curve) == "transform":
        CurveShapes = cmds.listRelatives(Curve)
    else:
        CurveShapes = [Curve]
    for Curve in CurveShapes:
        cmds.setAttr(Curve + ".overrideColor", colour)


def getColour(Curve):
    #Returns the overrideColor of a curve
    if mc.nodeType(Curve) == "transform":
        Curve = cmds.listRelatives(Curve)[0]
    return cmds.getAttr(Curve + ".overrideColor")





