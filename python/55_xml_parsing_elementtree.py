"""
Technique: XML Parsing with xml.etree.ElementTree
Use When:
- XML is still common in enterprise integrations (feeds, legacy APIs)
- ElementTree provides a safe, structured parser
"""

import xml.etree.ElementTree as ET


def extract_titles(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    return [el.text or "" for el in root.findall("./item/title")]


if __name__ == "__main__":
    xml_text = """
    <feed>
      <item><title>First</title></item>
      <item><title>Second</title></item>
    </feed>
    """.strip()
    print(extract_titles(xml_text))
