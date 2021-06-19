import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


def on_activate(app):
    win = Gtk.Window()
    # TODO: for some reason here it gives 2 arguments, which is too much
    # but works in "button_example.py"
    win.connect("destroy", app.quit)
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
