from IDMT_SMT_Guitar import load_stacked_notes_xml

xml_file = "sandpit/nocturneNr2.xml"

xml_data = load_stacked_notes_xml(xml_file)

for k, v in xml_data.items():
    print(k, v)
