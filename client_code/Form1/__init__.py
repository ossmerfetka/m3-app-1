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
    self.button_3.visible = False
    self.label = ItemTemplate_copy()
    self.column_test.remove_component(self.item_template)
    self.column_test.add_component(s)


    
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
    