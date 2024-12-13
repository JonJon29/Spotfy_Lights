import tinytuya
# Connect to Device
d = tinytuya.BulbDevice(
    dev_id = 'bf2ac18cbc375e3dfeofah"',
    address = 'Auto',      # Or set to 'Auto' to auto-discover IP address
    local_key = "'.lNPP4{j[KRUh&J",

    version=3.3)

# Get Status
data = d.status() 
print('set_status() result %r' % data)

# Turn On
d.turn_on()
