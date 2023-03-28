from matplotlib.widgets import RectangleSelector
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle
from functools import partial


def choice(center, radius):
    fig, current_ax = plt.subplots()
    plt.grid()
    distance = 200000
    current_ax.set_xlim([-distance, distance])
    current_ax.set_ylim([-distance, distance])
    circle_1 = Circle(center[0], radius[0], facecolor='g', fill=False)
    circle_2 = Circle(center[1], radius[1], facecolor='g', fill=False)
    current_ax.add_patch(circle_1)
    current_ax.add_patch(circle_2)

    def line_select_callback(eclick, erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        # print((x1, y1), (x2, y2))

    rectangles = []

    def toggle_selector(event):
        if event.key == 'enter':
            print(' Enter pressed.')
            coordinates = toggle_selector.RS.extents
            center_rectangle = toggle_selector.RS.center
            rectangles.append(coordinates)
            globals()['gui_rect_%s' % len(rectangles)] = Rectangle((coordinates[0], coordinates[2]),
                                                                   coordinates[1] - coordinates[0],
                                                                   coordinates[3] - coordinates[2],
                                                                   facecolor='g',
                                                                   alpha=0.2)
            globals()['gui_r_%s' % len(rectangles)] = current_ax.add_patch(globals()['gui_rect_%s' % len(rectangles)])
            globals()['gui_text_%s' % len(rectangles)] = current_ax.text(center_rectangle[0], center_rectangle[1], str(len(rectangles)))

        if event.key == 'w':
            toggle_selector.RS.update()
            toggle_selector.RS.set_active(False)
            toggle_selector.RS.set_visible(False)
            plt.disconnect(binding_id)

    def choose_rectangle(event):
        def edit_selector(event, k=None):
            if event.key == 'enter':
                coordinates = edit_selector.RS.extents
                center_rectangle = edit_selector.RS.center
                rectangles[k - 1] = coordinates
                globals()['gui_rect_%s' % k] = Rectangle((coordinates[0], coordinates[2]),
                                                         coordinates[1] - coordinates[0],
                                                         coordinates[3] - coordinates[2],
                                                         facecolor='g',
                                                         alpha=0.2)
                globals()['gui_r_%s' % k] = current_ax.add_patch(globals()['gui_rect_%s' % k])
                globals()['gui_text_%s' % k] = current_ax.text(center_rectangle[0], center_rectangle[1], str(k))

            if event.key == 'w':
                edit_selector.RS.update()
                edit_selector.RS.set_active(False)
                edit_selector.RS.set_visible(False)
                plt.disconnect(binding_id_edit)

        for i in range(1, len(rectangles) + 1):
            if event.key == str(i):
                print('edit on')
                globals()['gui_r_%s' % i].remove()
                globals()['gui_text_%s' % i].remove()
                edit_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                                     useblit=True,
                                                     button=[1, 3],
                                                     minspanx=5, minspany=5,
                                                     spancoords='pixels',
                                                     interactive=True)
                edit_selector_partial = partial(edit_selector, k=i)
                binding_id_edit = plt.connect('key_press_event', edit_selector_partial)
                edit_selector.RS.extents = rectangles[i - 1]

    toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                           useblit=True,
                                           button=[1, 3],
                                           minspanx=5, minspany=5,
                                           spancoords='pixels',
                                           interactive=True)

    binding_id = plt.connect('key_press_event', toggle_selector)
    plt.connect('key_press_event', choose_rectangle)

    plt.show()

    return rectangles
