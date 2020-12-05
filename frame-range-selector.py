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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This addon was generated with the Visual Scripting Addon.
# You can find the addon under https://blendermarket.com/products/serpens
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
sn_tree_name = "Frame Range Selector"
addon_keymaps = []

bl_info = {
    "name": "Frame Range Selector",
    "author": "Jordan Wages",
    "description": "Sets the frame range to match the currently selected strip in the VSE.",
    "location": "",
    "doc_url": "https://github.com/wagesj45/blender-frame-range-selector-addon",
    "warning": "",
    "category": "Sequencer",
    "blender": (2,90,0),
    "version": (1,0,0)
}


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# IMPORTS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import bpy
from bpy.app.handlers import persistent


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# UTILITY FUNCTIONS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def sn_print(*text):
    text = ', '.join(map(str, text))
    print(text) # actual print command
    try: # try to find the area in which the addon is opened and add the print text
        for area in bpy.context.screen.areas:
            if area.type == "NODE_EDITOR":
                if area.spaces[0].node_tree:
                    if area.spaces[0].node_tree.bl_idname == "ScriptingNodesTree":
                        if sn_tree_name == area.spaces[0].node_tree.name:
                            bpy.context.scene.sn_properties.print_texts.add().text = str(text)

        for area in bpy.context.screen.areas:
            area.tag_redraw()
    except: pass
    
def get_enum_identifier(enumItems, name):
    for item in enumItems:
        if item.name == name:
            return item.identifier
            
    return ''

def report_sn_error(self,error):
    self.report({"ERROR"},message="There was an error when running this operation! It has been printed to the console.")
    print("START ERROR | Node Name: ",self.name," | (If you are this addons developer you might want to report this to the Serpens team) ")
    print("")
    print(error)
    print("")
    print("END ERROR - - - - ")
    print("")
    
def get_python_filepath():
    path = os.path.dirname(bpy.data.filepath)
    try:
        __file__
        exported = True
    except:
        exported = False
    if exported:
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    return path

def cast_int(cast):
    int_string = ""
    if type(cast) == str:
        for char in cast:
            if char.isnumeric():
                int_string+=char
    else:
        return cast[0]
    if int_string.isnumeric():
        int_string = int(int_string)
        return int_string
    return 0

def cast_float(cast):
    float_string = ""
    if type(cast) == str:
        for char in cast:
            if char.isnumeric() or char == ".":
                float_string+=char
    else:
        return cast[0]
    if float_string != "" and float_string != ".":
        float_string = float(float_string)
        return float_string
    return 0
    
def cast_vector(cast):
    if type(cast) == bool:
        if cast:
            return (1.0, 1.0, 1.0)
        else:
            return (0.0, 0.0, 0.0)
    elif type(cast) == int:
        return (float(cast), float(cast), float(cast))
    elif type(cast) == float:
        return (cast, cast, cast)
    elif type(cast) == str:
        cast = cast_float(cast)
        return (cast, cast, cast)
    return (0, 0, 0)

def cast_four_vector(cast, four):
    if type(cast) == bool:
        if cast:
            return (1.0, 1.0, 1.0, four)
        else:
            return (0.0, 0.0, 0.0, four)
    elif type(cast) == int:
        return (float(cast), float(cast), float(cast), four)
    elif type(cast) == float:
        return (cast, cast, cast, four)
    elif type(cast) == str:
        cast = cast_float(cast)
        return (cast, cast, cast, four)
    return (0, 0, 0)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# CODE
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class SNA_OT_BTN_ef35dca7ab(bpy.types.Operator):
    bl_idname = 'scripting_nodes.sna_ot_btn_ef35dca7ab'
    bl_label = r"Set Frame Range"
    bl_description = r"Sets the frame range to the currently selected strip"
    bl_options = {"REGISTER","INTERNAL"}
    
    def execute(self, context):
        try:
            pass
            bpy.ops.scripting_nodes.sna_ot_operator_6d5771f989('INVOKE_DEFAULT')
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
class SNA_OT_Operator_6d5771f989(bpy.types.Operator):
    bl_idname = "scripting_nodes.sna_ot_operator_6d5771f989"
    bl_label = "Set Frame Range"
    bl_description = "Sets the frame range to the currently selected strip"
    bl_options = {"REGISTER","UNDO"}
    
    @classmethod
    def poll(cls, context):
        return True
        
    def execute(self, context):
        try:
            pass
            bpy.context.scene.frame_start = bpy.context.scene.sequence_editor.active_strip.frame_start
            bpy.context.scene.frame_end = int((float(bpy.context.scene.sequence_editor.active_strip.frame_final_end)-1.0))
            
        except Exception as exc:
            report_sn_error(self,exc)
        return {"FINISHED"}
        
    def draw(self, context):
        layout = self.layout
    
    
def add_to_panel_cbd8938949(self, context):
    layout = self.layout
    layout.operator("scripting_nodes.sna_ot_btn_ef35dca7ab",text=r"Set Frame Range",emboss=True,depress=False,icon="TEMP")
    
    

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# PROPERTIES
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# REGISTER / UNREGISTER
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def register():
    bpy.utils.register_class(SNA_OT_BTN_ef35dca7ab)
    bpy.utils.register_class(SNA_OT_Operator_6d5771f989)
    bpy.types.SEQUENCER_PT_time.prepend(add_to_panel_cbd8938949)

def unregister():
    global addon_keymaps
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.utils.unregister_class(SNA_OT_BTN_ef35dca7ab)
    bpy.utils.unregister_class(SNA_OT_Operator_6d5771f989)
    bpy.types.SEQUENCER_PT_time.remove(add_to_panel_cbd8938949)
