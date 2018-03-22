import bpy
import json
from collections import OrderedDict

class Json(): 
    def read(self,path): 
        try:
            f=open(path, 'r')
            dump=json.load(f, object_pairs_hook=OrderedDict)
            f.close()
            return dump
        except:
            raise Exception("\n\nMissing or invalid json: {}.".format(path)) 


def blender_staircase(self,"result.json"):
    json=Json()
    g=json.read(f)
    t=0
    tt=0
    for k,v in g['staircases'].items():
        if t==80:
            tt=-20
            t=0
        for i in v:
            bpy.ops.mesh.primitive_cube_add(location=i['center'])
            bpy.ops.transform.resize(value=i['size'])
            bpy.ops.transform.translate(value=(t,tt,0))
        t+=10

