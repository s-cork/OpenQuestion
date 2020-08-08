from ._anvil_designer import vega_liteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class vega_lite(vega_liteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.tag.form_shown=False

    self.tag.vl_spec={
  "$schema": "https://vega.github.io/schema/vega-lite/v4.json",
  "data": {"url": "https://vega.github.io/vega-lite/data/cars.json"},
  "mark": "point",
  "encoding": {
    "x": {"field": "Horsepower", "type": "quantitative"},
    "y": {"field": "Miles_per_Gallon", "type": "quantitative"},
    "color": {"field": "Origin", "type": "nominal"}  
  }
}
  
  def form_show(self, **event_args):
    
    if not self.tag.form_shown:
      self.tag.form_shown=True
      self.vega_embed()
      
  def vega_embed(self, **event_args):
    
    spec=self.tag.vl_spec
    data_name=spec['data'].get('name', None)
    data_values=get_open_form().tag.data_dicts.get(data_name, None)
    
    if data_name and data_values:
      self.call_js('vega_embed_named_data', self.tag.vl_spec, 
                data_name, data_values)
      
    else: #not data_name and not data_values:
        self.call_js('vega_embed_no_named_data', self.tag.vl_spec)
        
    
        
    