# literki = 'abcdefgh';
# literki2 = 'unknow';
# fin = '';
# fin = literki[2:4]+'qwe'+literki2[3:6];
# print(fin)
import xml.etree.ElementTree as ET
tree = ET.parse('countries.xml')
root = tree.getroot()
userwamt= input("Do you want to view (1) or edit (2) the file?")

if userwamt == "1":
    for child in root:
        print(child.tag, child.attrib)
        for subchild in child:
            print(subchild.tag, subchild.text)
        print(" ")
        
elif userwamt == "2":
    userwamt2 = input("Do you want to modify a country (1) or an attribute? (2)")
    if userwamt2 == "1":
        userwamt3 = input("Do you want to add (1), modify (2) or delete (3) a country?")
        if userwamt3 == "1":
            newcountry = ET.Element("country")
            newcountry.attrib["name"] = input("Enter the name of the country")
            root.append(newcountry)
        elif userwamt3 == "2":
            userwamt4 = input("Enter the current name of the country you want to modify: ")
            for child in root:
                if child.attrib["name"] == userwamt4:
                    new_name = input("Enter the new name of the country: ")
                    child.attrib["name"] = new_name  
        elif userwamt3 == "3":
            userwamt5 = input("Enter the name of the country you want to delete")
            for child in root:
                if child.attrib["name"] == userwamt5:
                    root.remove(child)
                    
    elif userwamt2 == "2":
        userwamt21 = input("Do you want to add (1), modify (2) or delete (3) an attribute?")
        if userwamt21 == "1":
            userwamt211 = input("Enter the name of the country you want to add an attribute to: ")
            for child in root:
                if child.attrib["name"] == userwamt211:
                    newattribute = ET.Element(input("Enter the name of the attribute: "))
                    newattribute.text = input("Enter the value of the attribute: ")
                    child.append(newattribute)
        elif userwamt21 == "2":
            userwamt212 = input("Enter the name of the country you want to modify an attribute of: ")
            for child in root:
                if child.attrib["name"] == userwamt212:
                    userwamt2121 = input("Enter the name of the attribute you want to modify: ")
                    for subchild in child:
                        if subchild.tag == userwamt2121:
                            subchild.text = input("Enter the new value of the attribute: ")
        elif userwamt21 == "3":
            userwamt213 = input("Enter the name of the country you want to delete an attribute from: ")
            for child in root:
                if child.attrib["name"] == userwamt213:
                    userwamt2131 = input("Enter the name of the attribute you want to delete: ")
                    for subchild in child:
                        if subchild.tag == userwamt2131:
                            child.remove(subchild)
                    
                    
tree.write('countries.xml')
