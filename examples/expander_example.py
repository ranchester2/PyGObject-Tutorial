import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class ExpanderExample(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Expander Demo")

        self.set_size_request(350, 100)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.set_child(vbox)

        text_expander = Gtk.Expander(
                label="This expander displays additional information"
        )
        text_expander.set_expanded(True)
        vbox.append(text_expander)

        msg = """
This message is quite long, complicated even:
    - It has a list with a sublist:
        - of 3 elements;
        - taking several lines;
        - with indentation.
"""
        details = Gtk.Label(label=msg)
        text_expander.set_child(details)

        widget_expander = Gtk.Expander(label="Expand for more controls")
        vbox.append(widget_expander)

        expander_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        widget_expander.set_child(expander_hbox)

        expander_hbox.append(Gtk.Label(label="Text message", hexpand=True))
        expander_hbox.append(Gtk.Button(label="Click me", hexpand=True))

        self.show()


def on_activate(app):
    win = ExpanderExample()
    win.connect("destroy", lambda b : app.quit())
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)
app.run(None)
