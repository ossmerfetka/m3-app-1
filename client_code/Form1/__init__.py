from ._anvil_designer import Form1Template
from anvil import *
import anvil.http

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    print('shpwn\n\n')
    url = "http://localhost:8000/items"
    items = anvil.http.request(url, method="GET", json=True)
    print(items)
    #items = [{'name':'elo', 'description':'pomidory'}]
    self.repeating_panel_1.items = items
    self.repeating_panel_2.items = items
    self.repeating_panel_2.layout = 'horizontal'

    for item in self.items:
      # Add a custom panel for each image
      item_panel = FlowPanel()
      item_panel.width = '200px'  # Optional: control the width of each item

      # Add an image component to each item
      image = Image(source=f"http://localhost:8000/{item['image_path']}")
      image.width = 150  # Control the width of the image

      # Add image to the panel
      item_panel.add_component(image)

      # Add the item panel to the repeating panel
      self.repeating_panel_2.add_component(item_panel)


    
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    print('elo')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""

    url = "http://localhost:8000/items"
    
    response = anvil.http.request(url, method="GET", json=True)
    print(response)

  def form_show(self, **event_args):
    print('shpwn\n\n')
    