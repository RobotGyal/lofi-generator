from music21 import converter, instrument, note, chord
import pickle
import glob 

notes = []

for file in glob.glob("assets/midi/*.midi"):
    midi = converter.parse(file)
    print("\x1b[3;32mParsing %s" % file)


    notes_to_parse = None
    parts = instrument.partitionByInstrument(midi)
    if parts: # file has instrument parts
        notes_to_parse = parts.parts[0].recurse()
    else: # file has notes in a flat structure
        notes_to_parse = midi.flat.notes
    for element in notes_to_parse:
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))

    with open('data/notes', 'wb') as filepath:
        pickle.dump(notes, filepath)

print("\x1b[3;31mMidi Import and Parsing Complete")