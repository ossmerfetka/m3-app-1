from ._anvil_designer import Form1Template
from anvil import *
import anvil.http

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
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
    print(response.json())

