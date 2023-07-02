# Rig_sistem
 Autorig System (full project including modules)

 Automatic rig system. 
____________________________________________

-SYSTEM BUILD PROCESS DESCRIPTION

The automatic building process will be based on:

1- A tree hierarchy that is DISCONNECTED from the outliner. (it's not simple parenting)
2- There sill be no hierarchy parenting but an EXTRA ATTRIBUTE THAT STABLISH HIERARCHY PARENTING.
3- This is so the controls are all lined up and visible with no hierarchy. To fasciliate order and efficiency for the user.
4- The hierarchy parenting is also eliminated to avoid hiden connections and loops back to previous nodes that slow Paralell workflow. 
5- The hierarchy will be visible in a tree list in the UI. 
6- Draging and droping the rig nodes in the treelist viewport will reorganized the hierarchy and change the extra attribute in the controlGuide.
7- A visible line will show in the maya viewport the hierarchy order.


-SCOPE OF THE TOOL 

In this first stage the system will only require the following modules:

1- Simple control
2- Follow simple control
3- FK chain 
4- IK chain
5- IK spline chain
6- Custom script holder and processing
6- Builder



- UTILITIES NEEDED FOR THE TOOL

1- Relative position query
2- Adjustment group creator 
3- Control curve creator
4- Multy attribute creator
5- Guide attributes query 
6- Edit hierarchy build attribue (and query current hierarchy attribute state)
7- 



