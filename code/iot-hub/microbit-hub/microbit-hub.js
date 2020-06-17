radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showIcon(IconNames.Duck)
    serial.writeLine(receivedString)
    basic.clearScreen()
})
radio.setGroup(1)
basic.forever(function on_forever() {
    basic.showIcon(IconNames.Heart)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(2000)
})
