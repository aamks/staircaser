# staircaser
![staircaser](/screenshot.png?raw=true)

Generator of the staircases based on the input cuboid. There are 8 possible
staircases orientations to fit the cuboid. The result is a json file with these
8 sets which can be further used in any 3D software (blender, CAD, etc). The
resulting json can be found in examples/result.json.

The input cuboid is described by these parameteres:

	bottom      : the projection of the staircase onto XY plane
	fheight     : floor height
	floors      : number of floors
	swidth      : single stair width (depth and height are automatic)

The resulting json for the above image is the result of this call:

	Staircaser(bottom=[(0,0,0), (7,5,0)], fheight=3, floors=3, swidth=2)

Once the json is produced, blender can draw the geometries with the script
examples/blender.py. You need to create a similar script for other 3D software.
Basically you just iterate over json and draw each element using, say AutoCad
commands. 
