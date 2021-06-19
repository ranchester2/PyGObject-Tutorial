import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, GLib


class SpinnerWindow(Gtk.Window):
    def __init__(self, *args, **kwargs):
        Gtk.Window.__init__(self, title="Spinner Demo")

        mainBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6,
                          margin_start=10, margin_end=10, margin_top=10, margin_bottom=10)
        self.set_child(mainBox)

        self.spinner = Gtk.Spinner(vexpand=True)
        mainBox.append(self.spinner)

        self.label = Gtk.Label(vexpand=True)
        mainBox.append(self.label)

        self.entry = Gtk.Entry(vexpand=True)
        self.entry.set_text("10")
        mainBox.append(self.entry)

        self.buttonStart = Gtk.Button(label="Start timer", vexpand=True)
        self.buttonStart.connect("clicked", self.on_buttonStart_clicked)
        mainBox.append(self.buttonStart)

        self.buttonStop = Gtk.Button(label="Stop timer", vexpand=True)
        self.buttonStop.set_sensitive(False)
        self.buttonStop.connect("clicked", self.on_buttonStop_clicked)
        mainBox.append(self.buttonStop)

        self.timeout_id = None
        self.connect("destroy", self.on_SpinnerWindow_destroy)

    def on_buttonStart_clicked(self, widget, *args):
        """ Handles "clicked" event of buttonStart. """
        self.start_timer()

    def on_buttonStop_clicked(self, widget, *args):
        """ Handles "clicked" event of buttonStop. """
        self.stop_timer("Stopped from button")

    def on_SpinnerWindow_destroy(self, widget, *args):
        """ Handles destroy event of main window. """
        # ensure the timeout function is stopped
        if self.timeout_id:
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
        self.get_appliation().quit()

    def on_timeout(self, *args, **kwargs):
        """ A timeout function.

        Return True to stop it.
        This is not a precise timer since next timeout
        is recalculated based on the current time."""
        self.counter -= 1
        if self.counter <= 0:
            self.stop_timer("Reached time out")
            return False
        self.label.set_label("Remaining: " + str(int(self.counter / 4)))
        return True

    def start_timer(self):
        """ Start the timer. """
        self.buttonStart.set_sensitive(False)
        self.buttonStop.set_sensitive(True)
        # time out will check every 250 miliseconds (1/4 of a second)
        self.counter = 4 * int(self.entry.get_text())
        self.label.set_label("Remaining: " + str(int(self.counter / 4)))
        self.spinner.start()
        self.timeout_id = GLib.timeout_add(250, self.on_timeout, None)

    def stop_timer(self, alabeltext):
        """ Stop the timer. """
        if self.timeout_id:
            GLib.source_remove(self.timeout_id)
            self.timeout_id = None
        self.spinner.stop()
        self.buttonStart.set_sensitive(True)
        self.buttonStop.set_sensitive(False)
        self.label.set_label(alabeltext)


def on_activate(app):
    win = SpinnerWindow()
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
