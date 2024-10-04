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
from . import (AddNode)

bl_info = {
    "name" : "XyzToon",
    "author" : "Xyz25632",
    "description" : "",
    "blender" : (3, 5, 1),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Material"
}

class settingPanel(bpy.types.Panel):
    bl_label = "XyzToon"
    bl_idname = "SETTING"
    bl_category = "XyzToon设置"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout
        layout.label(text = "XyzToon已启用")

def register():
    bpy.utils.register_class(settingPanel)
    AddNode.register()

def unregister():
    bpy.utils.unregister_class(settingPanel)
    AddNode.unregister()

if __name__ == "__main__":
    register()