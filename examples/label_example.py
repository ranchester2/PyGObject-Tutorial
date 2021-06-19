import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class LabelWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Label Example")

        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=10, hexpand=True)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=10, hexpand=True)
        vbox_right.set_homogeneous(False)

        hbox.append(vbox_left)
        hbox.append(vbox_right)

        label = Gtk.Label(label="This is a normal label", vexpand=True)
        vbox_left.append(label)

        label = Gtk.Label(vexpand=True)
        label.set_text("This is a left-justified label.\nWith multiple lines.")
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.append(label)

        label = Gtk.Label(
            label="This is a right-justified label.\nWith multiple lines.",
            vexpand=True
        )
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.append(label)

        label = Gtk.Label(
            label="This is an example of a line-wrapped label.  It "
            "should not be taking up the entire             "
            "width allocated to it, but automatically "
            "wraps the words to fit.\n"
            "     It supports multiple paragraphs correctly, "
            "and  correctly   adds "
            "many          extra  spaces. ",
            vexpand=True
        )
        label.set_wrap(True)
        label.set_max_width_chars(32)
        vbox_right.append(label)

        label = Gtk.Label(
            label="This is an example of a line-wrapped, filled label. "
            "It should be taking "
            "up the entire              width allocated to it.  "
            "Here is a sentence to prove "
            "my point.  Here is another sentence. "
            "Here comes the sun, do de do de do.\n"
            "    This is a new paragraph.\n"
            "    This is another newer, longer, better "
            "paragraph.  It is coming to an end, "
            "unfortunately.",
            vexpand=True
        )
        label.set_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        label.set_max_width_chars(32)
        vbox_right.append(label)

        label = Gtk.Label(vexpand=True)
        label.set_markup(
            "Text can be <small>small</small>, <big>big</big>, "
            "<b>bold</b>, <i>italic</i> and even point to "
            'somewhere in the <a href="https://www.gtk.org" '
            'title="Click to find out more">internets</a>.'
        )
        label.set_wrap(True)
        label.set_max_width_chars(48)
        vbox_left.append(label)

        label = Gtk.Label.new_with_mnemonic(
            "_Press Alt + P to select button to the right"
        )
        label.set_vexpand(True)
        vbox_left.append(label)
        label.set_selectable(True)

        button = Gtk.Button(label="Click at your own risk", vexpand=True)
        label.set_mnemonic_widget(button)
        vbox_right.append(button)

        self.set_child(hbox)


def on_activate(app):
    window = LabelWindow()
    window.connect("destroy", app.quit)
    app.add_window(window)
    window.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
