import jams

# Create the top level JAMS container
jam = jams.JAMS()
# A track in JAMS must have a duration 
jam.file_metadata.duration = 8.0
# Create a beat annotation
ann = jams.Annotation(namespace='beat', time=0, duration=jam.file_metadata.duration)
ann.append(time=0.33, duration=0.0, confidence=1, value=1)
# Update the annotations metadata by directly setting its field
ann.annotation_metadata = jams.AnnotationMetadata(data_source='Well paid students')
ann.annotation_metadata.curator = jams.Curator(name='Rincewind',
                                               email='rincewind@unseen.edu')
# Add our new annotation to the jam
jam.annotations.append(ann)
# We can update the annotation at any time, and add a new observation
ann.append(time=0.66, duration=0.0, confidence=1, value=1)

# # Serialize the annotation to a string and print
# jam_str = jam.dumps(indent=2)
# print(type(jam_str))
# print(jam_str)

# Save a jam file
jam.save("my_first.jams")
