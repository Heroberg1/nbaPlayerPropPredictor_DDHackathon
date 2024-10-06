from ._anvil_designer import Form2Template
from anvil import *
import anvil.server


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # USE CONTENT IN TEXT BOX 1 FOR THE NAME OF THE PREDICTION
    getPrediction(self.text_box_1)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Form2")

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Form3")

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")
