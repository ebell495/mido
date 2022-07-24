FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /mido
WORKDIR /mido
RUN python3 -m pip install . && chmod +x fuzz/fuzz_midi_parser.py