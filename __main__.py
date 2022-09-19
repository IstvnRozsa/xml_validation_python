from functools import cache
from lxml import etree
from termcolor import colored, cprint


def validate(xml_root:str, xsd_root:str):
    schema_root = etree.parse(xsd_root)
    schema = etree.XMLSchema(schema_root)
    parser = etree.XMLParser(schema = schema)

    try:
        root = etree.parse(xml_root, parser=parser)
        print("-"*35)
        cprint("Minden rendben ugy nez ki", "green", "on_green")
        print("-"*35)
        return root
    except etree.XMLSyntaxError as error_text:
        error = colored("Hiba", "yellow")
        print("-"*20 +  error + "-"*20)
        cprint(error_text, "red")
        print("-"*20 + error + "-"*20)



def main():
    validate("movies.xml", "movies.xsd")

if __name__ == "__main__":
    main()
