def on_button_pressed_a():
    global hand
    Proxi.rechtsdrehung()
    basic.pause(2000)
    Proxi.drehungsstopp()
    hand = randint(1, 4)
    if hand == 1:
        basic.show_leds("""
            # # . . #
            # # . # .
            . . # . .
            # # . # .
            # # . . #
            """)
        music.play(music.create_sound_expression(WaveShape.NOISE,
                4250,
                499,
                255,
                0,
                750,
                SoundExpressionEffect.NONE,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
    elif hand == 2:
        basic.show_leds("""
            . . . . .
            . # . # .
            . # # # .
            . # # # .
            . # # # .
            """)
        music.play(music.create_sound_expression(WaveShape.SINE,
                1,
                500,
                255,
                0,
                1000,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
    elif hand == 3:
        basic.show_leds("""
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            """)
        music.play(music.create_sound_expression(WaveShape.SAWTOOTH,
                1,
                500,
                255,
                0,
                1000,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            music.PlaybackMode.UNTIL_DONE)
    else:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            """)
        music.play(music.create_sound_expression(WaveShape.SINE,
                1045,
                1,
                255,
                0,
                100,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

hand = 0
for index in range(2):
    basic.show_string("Drücke Knopf A")