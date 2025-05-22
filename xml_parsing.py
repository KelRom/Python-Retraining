import xml.dom.minidom

# <this_is_a_tag>
# <skill this_is_an_attribute: "attribute" />

# use parse function to load and parse an XML file'
xml_data = xml.dom.minidom.parse("samplexml.xml")

# print out the document node and print the first child
print(xml_data.nodeName)
print("The first xml child: ", xml_data.firstChild.tagName)

# get a list of XML tags from the document and print each one
skills_set = xml_data.getElementsByTagName("skill")
for skill in skills_set:
    print(skill.getAttribute("name"))

# create a new XML tag and add it into the document
new_skill = xml_data.createElement("skill")
new_skill.setAttribute("name", "graphics programmer")
xml_data.firstChild.appendChild(new_skill)

skills_set = xml_data.getElementsByTagName("skill")
for skill in skills_set:
    print(skill.getAttribute("name"))
