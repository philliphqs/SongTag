from dearpygui.dearpygui import *

from resources.variables import Product, Tag

from ui import NavBar, Window

create_context()


def dragViewport():
    drag_deltas = get_mouse_drag_delta()
    viewport_current_pos = get_viewport_pos()
    set_viewport_pos([viewport_current_pos[0] + drag_deltas[0], viewport_current_pos[1] + drag_deltas[1]])


def init():
    Window.show()
    NavBar.show()

    with handler_registry():
        add_mouse_drag_handler(callback=dragViewport)


if __name__ == '__main__':
    init()

    setup_dearpygui()
    show_viewport()
    set_primary_window(Tag.PrimaryWindow, True)
    start_dearpygui()
    destroy_context()
