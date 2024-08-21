import jams

# schema for synthtab
jams.schema.add_namespace('gp_to_JAMS/note_tab.json')

# load
jam = jams.load("learn_jams/synthtab-example.jams")

note_tab = jam.search(namespace='note_tab')

for note in note_tab:
    for data in note:
        # print(note['sandbox'])
        # print(data)
        print(f"time: {data[0]}, duration: {data[1]}, string: {note['sandbox']['string_index']}, open tuning: {note['sandbox']['open_tuning']}, fret: {data[2]['fret']}, velocity: {data[2]['velocity']}")
