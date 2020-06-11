radio.onReceivedString(function (receivedString) {
    basic.showIcon(IconNames.Duck)
    serial.writeLine(receivedString)
    basic.clearScreen()
})
radio.setGroup(1)
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(100)
    basic.clearScreen()
    basic.pause(2000)
})
