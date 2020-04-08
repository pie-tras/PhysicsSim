import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

is3d = False

# Subclass QMainWindow to customise your application's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Physics Mega Program")

        layout = QGridLayout()
      
        ## Create some widgets to be placed inside
        btn = QPushButton('Press')
        text = QLineEdit('Enter Text')
        listw = QListWidget()
        p1 = pg.PlotWidget()

        ## Add widgets to the layout in their proper positions
        layout.addWidget(btn, 0, 0)   # button goes in upper-left
        layout.addWidget(text, 1, 0)   # text edit goes in middle-left
        layout.addWidget(listw, 2, 0)  # list widget goes in bottom-left
        
        if not is3d:
            
            x = np.arange(1000)
            y = np.random.normal(size=(3, 1000))
            for i in range(3):
                p1.plot(x, y[i], pen=(i,3))  ## setting pen=(i,3) automaticaly creates three different-colored pens

            layout.addWidget(p1, 0, 1, 3, 1)  # plot goes on right side, spanning 2 rows
        else:

            glvw = gl.GLViewWidget()
            z = pg.gaussianFilter(np.random.normal(size=(50,50)), (1,1))
            p13d = gl.GLSurfacePlotItem(z=z, shader='shaded', color=(0.5, 0.5, 1, 1))
            p13d.translate(-25, -25, 0)
            glvw.addItem(p13d)

            xgrid = gl.GLGridItem()
            ygrid = gl.GLGridItem()
            zgrid = gl.GLGridItem()
            glvw.addItem(xgrid)
            glvw.addItem(ygrid)
            glvw.addItem(zgrid)

            ## rotate x and y grids to face the correct direction
            xgrid.rotate(90, 0, 1, 0)
            ygrid.rotate(90, 1, 0, 0)

            xgrid.scale(3, 3, 3)
            ygrid.scale(3, 3, 3)
            zgrid.scale(3, 3, 3)

            layout.addWidget(glvw, 0, 1, 3, 1)

            glvw.sizeHint = lambda: pg.QtCore.QSize(400, 400)
            # glvw.setSizePolicy(p1.sizePolicy())     

        widget = QWidget()
        widget.setLayout(layout)
        
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

window = MainWindow()
window.show() # IMPORTANT Windows are hidden by default.

# Start the event loop.
app.exec_()


# Your application won't reach here until you exit and the event 
# loop has stopped.