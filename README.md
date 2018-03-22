# staircaser
![staircaser](/staircaser.png?raw=true)

Generator of the staircases based on the input cuboid. There are 16 possible
staircases orientations to fit the cuboid. The result is a json file with these
16 collections which can be further used in any 3D software
(blender/CAD/three.js/etc).

The cuboid is described by these parameteres:

bottom      : the projection of the staircase onto XY plane
fheight     : floor height
floors      : number of floors
swidth      : single stair width (depth and height are automatic)

The resulting json for the above image is the result of these two calls:

Staircase(bottom=[(5,5,0), (11,14,0)], fheight=5.1, floors=1, swidth=2)
Staircase(bottom=[(5,0,0), (12,4,0)], fheight=3, floors=3, swidth=2)

Blender can read the resulting json with the script examples/blender.py


