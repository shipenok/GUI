from matplotlib.widgets import RectangleSelector, EllipseSelector
import numpy as np
import matplotlib.pyplot as plt


def line_select_callback(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    print((x1, y1))
    x2, y2 = erelease.xdata, erelease.ydata
    print((x2, y2))


def toggle_selector_1(event):
    print(' Key pressed.')
    if event.key == 'enter':
        if toggle_selector_1.RS.active:
            print(' RectangleSelector deactivated.')
            toggle_selector_1.RS.set_active(False)
        else:
            print(' RectangleSelector activated.')
            toggle_selector_1.RS.set_active(True)

fig, current_ax = plt.subplots()

toggle_selector_1.RS = RectangleSelector(current_ax, line_select_callback,
                                       drawtype='box', useblit=True,
                                       button=[1, 3],
                                       minspanx=5, minspany=5,
                                       spancoords='pixels',
                                       interactive=True)


plt.connect('key_press_event', toggle_selector_1)
plt.show()