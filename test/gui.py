from gi.repository import Gtk, Adw
import sys
from usbtools import searchDevices

import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_default_size(500, 600)
        self.set_title("Samsung FRP bypass")

        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.set_child(self.box1)

        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box1.append(self.box2)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.infoLabel = Gtk.Label(label="Suche nach Samsung-Geräten...")
        self.box2.append(self.infoLabel)

        devices = searchDevices()

        self.statusLabel = Gtk.Label(label=devices)
        self.box2.append(self.statusLabel)


class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = App(application_id="de.marco-kraft.frpbypassgui")
app.run(sys.argv)
