from matplotlib.widgets import RectangleSelector, EllipseSelector
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def choice(distance):

    fig, current_ax = plt.subplots()
    plt.grid()
    current_ax.set_xlim([0,distance])
    current_ax.set_ylim([0,distance])

    def line_select_callback(eclick, erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata

    rectangles = []

    def toggle_selector(event):
        print(' Key pressed.')
        if event.key == 'enter':
            coordinates = toggle_selector.RS.extents
            center = toggle_selector.RS.center
            rect = plt.Rectangle((coordinates[0], coordinates[2]),
                                 abs(coordinates[1]-coordinates[0]),
                                 abs(coordinates[3]-coordinates[2]),
                                 facecolor='g',
                                 alpha=0.2)
            current_ax.add_patch(rect)
            rectangles.append(coordinates)
            current_ax.text(center[0], center[1], str(len(rectangles)))

        if event.key == 'w':
            toggle_selector.RS.update()
            toggle_selector.RS.set_active(False)
            toggle_selector.RS.set_visible(False)
            plt.disconnect(binding_id)

    toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                           useblit=True,
                                           button=[1, 3],
                                           minspanx=5, minspany=5,
                                           spancoords='pixels',
                                           interactive=True,
                                           state_modifier_keys=dict(square='shift'))

    binding_id = plt.connect('key_press_event', toggle_selector)
    plt.show()
    return rectangles
