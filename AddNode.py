# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from bpy.app.handlers import persistent
import os

def getBlVer():
    blVer = bpy.app.version_string[:-2]
    return blVer

def getPath(folder,file):
    filePath = bpy.app.binary_path[0:-11]
    filePath = os.path.join(filePath,getBlVer())
    filePath = os.path.join(filePath,"scripts")
    filePath = os.path.join(filePath,"addons")
    filePath = os.path.join(filePath,"XyzToon")
    filePath = os.path.join(filePath,folder)
    filePath = os.path.join((filePath),file).replace("\\", "/")
    return filePath

def addNodeTree(nodeTreeName):
    if not nodeTreeName in bpy.data.node_groups:
        with bpy.data.libraries.load(getPath("NodeTREE","Node.blend")) as (dataFrom, dataTo):
            dataTo.node_groups = [nodeTreeName]
        
        for trees in dataTo.node_groups:
            bpy.context.scene.node_tree.nodes.new(type='ShaderNodeGroup')
            bpy.context.scene.node_tree.nodes[-1].node_tree = trees

@persistent
def appendNodeTree(dummy):
    addNodeTree("XyzToon v1.0")

def register():
    bpy.app.handlers.load_post.append(appendNodeTree)

def unregister():
    bpy.app.handlers.load_post.remove(appendNodeTree)

if __name__ == "__main__":
    register()