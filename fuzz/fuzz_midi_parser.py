#!/usr/local/bin/python3
import atheris
import sys

import mido


@atheris.instrument_func
def TestOneInput(data):
    mido.parse_all(data)    


atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()