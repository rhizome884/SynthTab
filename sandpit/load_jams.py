import jams

# Add our custom schema for guitar notes
# jams.schema.add_namespace('gp_to_JAMS/note_tab.json')

jams_file = "sandpit/jams/00_BN1-129-Eb_comp.jams"

data = jams.load(jams_file)

# print(data)
print(data)

# for anno in data["annotations"]:
#     print(anno["sandbox"])
#     for gp_data in anno["data"]:
#         print(gp_data)
#         for obs in gp_data:
#             print(obs)
