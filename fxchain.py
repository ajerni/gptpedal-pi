from pyo import *

def fxChain(input, selections):
    fx1_params = selections.get("disto", {})
    fx1 = Disto(
        input,
        drive=fx1_params.get("drive", 0.75),
        slope=fx1_params.get("slope", 0.5),
        mul=fx1_params.get("mul", 1),
        add=fx1_params.get("add", 0),
    )
    fx1_out = Interp(input, fx1, interp=fx1_params.get("use", 0))
    if fx1_params.get("use") == 1:
        fx1.ctrl(title="Distortion")

    fx2_params = selections.get("delay", {})
    fx2 = Delay(
        fx1_out,
        delay=fx2_params.get("delay", 0.25),
        feedback=fx2_params.get("feedback", 0),
        maxdelay=fx2_params.get("maxdelay", 1),
        mul=fx2_params.get("mul", 1),
        add=fx2_params.get("add", 0),
    )
    fx2_out = Interp(fx1_out, fx2, interp=fx2_params.get("use", 0))
    if fx2_params.get("use") == 1:
        fx2.ctrl(title="Delay")

    fx3_params = selections.get("sdelay", {})
    fx3 = SDelay(
        fx2_out,
        delay=fx3_params.get("delay", 0.25),
        maxdelay=fx3_params.get("maxdelay", 1),
        mul=fx3_params.get("mul", 1),
        add=fx3_params.get("add", 0),
    )
    fx3_out = Interp(fx2_out, fx3, interp=fx3_params.get("use", 0))
    if fx3_params.get("use") == 1:
        fx3.ctrl(title="SDelay")

    fx4_params = selections.get("waveguide", {})
    fx4 = Waveguide(
        fx3_out,
        freq=fx4_params.get("freq", 100),
        dur=fx4_params.get("dur", 10),
        minfreq=fx4_params.get("minfreq", 20),
        mul=fx4_params.get("mul", 1),
        add=fx4_params.get("add", 0),
    )
    fx4_out = Interp(fx3_out, fx4, interp=fx4_params.get("use", 0))
    if fx4_params.get("use") == 1:
        fx4.ctrl(title="Waveguide")

    fx5_params = selections.get("allpass", {})
    fx5 = AllpassWG(
        fx4_out,
        freq=fx5_params.get("freq", 100),
        feed=fx5_params.get("feed", 0.95),
        detune=fx5_params.get("detune", 0.5),
        minfreq=fx5_params.get("minfreq", 20),
        mul=fx5_params.get("mul", 1),
        add=fx5_params.get("add", 0),
    )
    fx5_out = Interp(fx4_out, fx5, interp=fx5_params.get("use", 0))
    if fx5_params.get("use") == 1:
        fx5.ctrl(title="Allpass")

    fx6_params = selections.get("freeverb", {})
    fx6 = Freeverb(
        fx5_out,
        size=fx6_params.get("size", 0.5),
        damp=fx6_params.get("damp", 0.5),
        bal=fx6_params.get("bal", 0.5),
        mul=fx6_params.get("mul", 1),
        add=fx6_params.get("add", 0),
    )
    fx6_out = Interp(fx5_out, fx6, interp=fx6_params.get("use", 0))
    if fx6_params.get("use") == 1:
        fx6.ctrl(title="Freeverb")

    fx7_params = selections.get("monoreverb", {})
    fx7 = WGVerb(
        fx6_out,
        feedback=fx7_params.get("feedback", 0.5),
        cutoff=fx7_params.get("cutoff", 5000),
        bal=fx7_params.get("bal", 0.5),
        mul=fx7_params.get("mul", 1),
        add=fx7_params.get("add", 0),
    )
    fx7_out = Interp(fx6_out, fx7, interp=fx7_params.get("use", 0))
    if fx7_params.get("use") == 1:
        fx7.ctrl(title="Mono Reverb")

    fx8_params = selections.get("chorus", {})
    fx8 = Chorus(
        fx7_out,
        depth=fx8_params.get("depth", 1),
        feedback=fx8_params.get("feedback", 0.25),
        bal=fx8_params.get("bal", 0.5),
        mul=fx8_params.get("mul", 1),
        add=fx8_params.get("add", 0),
    )
    fx8_out = Interp(fx7_out, fx8, interp=fx8_params.get("use", 0))
    if fx8_params.get("use") == 1:
        fx8.ctrl(title="Chorus")

    fx9_params = selections.get("harmonizer", {})
    fx9 = Harmonizer(
        fx8_out,
        transpo=fx9_params.get("transpo", -7.0),
        feedback=fx9_params.get("feedback", 0),
        winsize=fx9_params.get("winsize", 0.1),
        mul=fx9_params.get("mul", 1),
        add=fx9_params.get("add", 0),
    )
    fx9_out = Interp(fx8_out, fx9, interp=fx9_params.get("use", 0))
    if fx9_params.get("use") == 1:
        fx9.ctrl(title="Harmonizer")

    fx10_params = selections.get("simpledelay", {})
    fx10 = Delay1(
        fx9_out,
        mul=fx10_params.get("mul", 1),
        add=fx10_params.get("add", 0),
    )
    fx10_out = Interp(fx9_out, fx10, interp=fx10_params.get("use", 0))
    if fx10_params.get("use") == 1:
        fx10.ctrl(title="Delay 1")

    fx11_params = selections.get("stereoreverb", {})
    fx11 = STRev(
        fx10_out,
        inpos=fx11_params.get("inpos", 0.5),
        revtime=fx11_params.get("revtime", 1),
        cutoff=fx11_params.get("cutoff", 5000),
        bal=fx11_params.get("bal", 0.5),
        roomSize=fx11_params.get("roomSize", 1),
        firstRefGain=fx11_params.get("firstRefGain", -3),
        mul=fx11_params.get("mul", 1),
        add=fx11_params.get("add", 0),
    )
    fx11_out = Interp(fx10_out, fx11, interp=fx11_params.get("use", 0))
    if fx11_params.get("use") == 1:
        fx11.ctrl(title="Stereo Reverb")

    fx12_params = selections.get("smoothdelay", {})
    fx12 = SmoothDelay(
        fx11_out,
        delay=fx12_params.get("delay", 0.25),
        feedback=fx12_params.get("feedback", 0),
        crossfade=fx12_params.get("crossfade", 0.05),
        maxdelay=fx12_params.get("maxdelay", 1),
        mul=fx12_params.get("mul", 1),
        add=fx12_params.get("add", 0),
    )
    fx12_out = Interp(fx11_out, fx12, interp=fx12_params.get("use", 0))
    if fx12_params.get("use") == 1:
        fx12.ctrl(title="Smooth Delay")

    fx13_params = selections.get("freqshift", {})
    fx13 = FreqShift(
        fx12_out,
        shift=fx13_params.get("shift", 100),
        mul=fx13_params.get("mul", 1),
        add=fx13_params.get("add", 0),
    )
    fx13_out = Interp(fx12_out, fx13, interp=fx13_params.get("use", 0))
    if fx13_params.get("use") == 1:
        fx13.ctrl(title="Frequency Shifter")

    return fx13_out
