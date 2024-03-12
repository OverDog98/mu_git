import mido

mid = mido.MidiFile('/Users/sangjin/Desktop/logicx2midi.mid')

print(mid.tracks)
for track in mid.tracks:
    print('Track:', track.name)
    for msg in track:
        print(msg)
        # if msg.type in ['note_on', 'note_off']:
        #     print(msg)

