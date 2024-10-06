from ._anvil_designer import Form3Template
from anvil import *
import anvil.server


class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    self.text_box_1.text = ""
    self.text_box_2.text = ""
    self.text_box_3.text = ""

    alert("Thank you for your feedback!", buttons = "Close")


  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Form2")

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Form3")

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")

