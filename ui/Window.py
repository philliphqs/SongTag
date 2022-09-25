from dearpygui.dearpygui import *

from resources.variables import Product, Tag


def show():
    with window(tag=Tag.PrimaryWindow):
        add_text("")  # Placeholder

        with group(horizontal=True):
            add_text('Title')
            add_input_text(label='Title', default_value='Title')