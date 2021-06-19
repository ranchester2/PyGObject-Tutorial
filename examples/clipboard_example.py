import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk


class ClipboardWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Clipboard Example")

        grid = Gtk.Grid()

        self.clipboard = self.get_clipboard()
        self.entry = Gtk.Entry()
        self.image = Gtk.Image.new_from_icon_name("process-stop")

        button_copy_text = Gtk.Button(label="Copy Text")
        button_paste_text = Gtk.Button(label="Paste Text")
        button_copy_image = Gtk.Button(label="Copy Image")
        button_paste_image = Gtk.Button(label="Paste Image")

        grid.attach(self.entry, 0, 0, 1, 1)
        grid.attach(self.image, 0, 1, 1, 1)
        grid.attach(button_copy_text, 1, 0, 1, 1)
        grid.attach(button_paste_text, 2, 0, 1, 1)
        grid.attach(button_copy_image, 1, 1, 1, 1)
        grid.attach(button_paste_image, 2, 1, 1, 1)

        button_copy_text.connect("clicked", self.copy_text)
        button_paste_text.connect("clicked", self.paste_text)
        button_copy_image.connect("clicked", self.copy_image)
        button_paste_image.connect("clicked", self.paste_image)

        self.set_child(grid)

    def copy_text(self, widget):
        self.clipboard.set(self.entry.get_text())

    def paste_text(self, widget):
        def handle_text(source, result):
            text = self.clipboard.read_text_finish(result)
            if text is not None:
                self.entry.set_text(text)
            else:
                print("No text on the clipboard")

        self.clipboard.read_text_async(None, handle_text)

    def copy_image(self, widget):
        if self.image.get_storage_type() == Gtk.ImageType.PAINTABLE:
            self.clipboard.set_texture(self.image.get_paintable())
        else:
            print("No image has been pasted yet.")

    def paste_image(self, widget):
        def handle_image(source, result):
            image = self.clipboard.read_texture_finish(result)
            if image is not None:
                self.image.set_from_paintable(image)

        self.clipboard.read_texture_async(None, handle_image)


def on_activate(app):
    win = ClipboardWindow()
    win.connect("destroy", lambda b : app.quit())
    app.add_window(win)
    win.show()


app = Gtk.Application(application_id="org.example.myapp")
app.connect("activate", on_activate)

app.run(None)
