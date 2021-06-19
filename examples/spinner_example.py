import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class SpinnerAnimation(Gtk.Window):
    def __init__(self):

        Gtk.Window.__init__(self, title="Spinner")
        self.connect("destroy", lambda b : self.get_application().quit())

        self.button = Gtk.ToggleButton(label="Start Spinning")
        self.button.connect("toggled", self.on_button_toggled)
        self.button.set_active(False)

        self.spinner = Gtk.Spinner()

        self.grid = Gtk.Grid(margin_start=3, margin_end=3,
                             margin_top=3, margin_bottom=3)
        self.grid.attach(self.button, 0, 0, 1, 1)
        self.grid.attach_next_to(
            self.spinner, self.button, Gtk.PositionType.BOTTOM, 1, 2
        )
        self.grid.set_row_homogeneous(True)

        self.set_child(self.grid)

    def on_button_toggled(self, button):

        if button.get_active():
            self.spinner.start()
            self.button.set_label("Stop Spinning")

        else:
            self.spinner.stop()
            self.button.set_label("Start Spinning")


def on_activate(app):
    myspinner = SpinnerAnimation()
    app.add_window(myspinner)
    myspinner.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
