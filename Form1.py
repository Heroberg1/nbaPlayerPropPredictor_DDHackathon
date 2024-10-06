from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #USE CONTENT IN TEXT BOX 1 FOR THE NAME OF THE PREDICTION
    points = anvil.server.call('say_hello', self.text_box_1.text)
    self.label_1.text = str(self.text_box_1.text + " is predicted to get " + str(points) + " points.")
  
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Form2')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Form3')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.text = "LeBron James"
    self.button_1_click()

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.text_box_1.text = "Luka Doncic"
    self.button_1_click()



