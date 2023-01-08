import usb.core


def searchDevices():
    return usb.core.find()


SAMSUNG_GALAXY_ID_VENDOR = 0x04e8
SAMSUNG_GALAXY_ID_PRODUCT = 0x6860

i = 1
for device in usb.core.find(find_all=1):
    print(f"Device {i}: \n")
    print(f"Hersteller: {device.idVendor}\n")
    i = i + 1
"""     if device.manufacturer:
        print(device.manufacturer)
    else:
        print("No manufacturer") """


"""
device = usb.core.find()
print(device.manufacturer)
 """
