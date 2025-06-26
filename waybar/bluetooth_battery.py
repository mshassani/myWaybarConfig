import dbus

bus = dbus.SystemBus()
manager = dbus.Interface(bus.get_object('org.bluez', '/'), 'org.freedesktop.DBus.ObjectManager')
objects = manager.GetManagedObjects()

for path, interfaces in objects.items():
    if 'org.bluez.Device1' in interfaces:
        device = interfaces['org.bluez.Device1']
        if 'Battery' in device:
            print(f"{device['Name']} {device['Battery']}%")
