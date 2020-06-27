from ._anvil_designer import toolbarTemplate
from anvil import *

class toolbar(toolbarTemplate):
  
  def __init__(self, spacer_bool, center_widgets, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    if spacer_bool:
      self.add_component(Spacer())
      
    if center_widgets:
      self.flow_panel.align='center'
    

#   def widget_control(self, **event_args):
#     """This method is called when the link is clicked"""
#     widgets.widget_control(comp)
    
    