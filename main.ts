input.onButtonPressed(Button.A, function () {
    basic.pause(500)
    Proxi.rechtsdrehung()
    basic.pause(3500)
    Proxi.drehungsstopp()
    hand = randint(1, 4)
    if (hand == 1) {
        basic.showLeds(`
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            `)
        music.play(music.createSoundExpression(WaveShape.Noise, 4250, 499, 255, 0, 750, SoundExpressionEffect.None, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    } else if (hand == 2) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . # # # .
            . # # # .
            . # # # .
            `)
        music.play(music.createSoundExpression(WaveShape.Sine, 1, 500, 255, 0, 1000, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    } else if (hand == 3) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
        music.play(music.createSoundExpression(WaveShape.Sawtooth, 1, 500, 255, 0, 1000, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    } else {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
        music.play(music.createSoundExpression(WaveShape.Sine, 1045, 1, 255, 0, 100, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.UntilDone)
    }
})
input.onGesture(Gesture.ScreenUp, function () {
    basic.clearScreen()
})
let hand = 0
basic.showString("Druecke Knopf A")
