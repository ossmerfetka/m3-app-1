from ._anvil_designer import ItemTemplateTemplate
from anvil import *

class ItemTemplate(ItemTemplateTemplate):

  def __init__(self, **properties):
    self.init_components(**properties)
    self.form_show()

  def form_show(self, **event_args):
    try:
      self.label_name.text = self.item['name']
      self.label_price.text = self.item['description']
      self.image.source = f"http://localhost:8000/{self.item['image_path']}"
    except:
      pass