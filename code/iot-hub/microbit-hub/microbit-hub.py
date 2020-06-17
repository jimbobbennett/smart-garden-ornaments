def on_received_string(receivedString):
    basic.show_icon(IconNames.DUCK)
    serial.write_line(receivedString)
    basic.clear_screen()
radio.on_received_string(on_received_string)

radio.set_group(1)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    basic.clear_screen()
    basic.pause(2000)
basic.forever(on_forever)
