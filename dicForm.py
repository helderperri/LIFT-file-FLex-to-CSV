import os
import xml.etree.ElementTree as et
import csv
import itertools

base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "data\\dic.xml")

tree = et.parse(xml_file)
root =  tree.getroot()

def encode(self,input,errors='strict'):
    return codecs.charmap_encode(input,errors,encoding_table)

with open('dicForm.csv', 'w', encoding="utf-8", newline='') as new_file:
    fieldnames = ['word', 'dateCreated', 'dateModified', 'guid', 'id', 'morph_type', 'cv_pattern', 'pron_number', 'pron']
    # csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
    csv_writer.writeheader()
    for entry in root.findall('entry'):
            pron_text = ""
            cv_pattern = ""
            pron_number = ""

            try:
                check_dateCreated = entry.attrib["dateCreated"]
                if check_dateCreated is None:
                    dateCreated = ""
                else:
                    dateCreated = entry.attrib["dateCreated"]
            except:
                pass

            try:
                check_dateModified = entry.attrib["dateModified"]
                if check_dateModified is None:
                    dateModified = ""
                else:
                    dateModified = entry.attrib["dateModified"]
            except:
                pass

            try:
                check_guid = entry.attrib["guid"]
                if check_guid is None:
                    guid = ""
                else:
                    guid = entry.attrib["guid"]
            except:
                pass

            try:
                check_id = entry.attrib["id"]
                if check_id is None:
                    id = ""
                else:
                    id = entry.attrib["id"]
            except:
                pass


            try:
                check_word = entry.find("lexical-unit")
                if check_word is None:
                    word = ""
                else:
                    word = entry.find("lexical-unit").find("form").find("text").text
            except:
                pass

            try:
                check_morph_type = entry.find("trait[@name='morph-type']")
                if check_word is None:
                    morph_type = ""
                else:
                    morph_type = entry.find("trait[@name='morph-type']").attrib["value"]
            except:
                pass

            check_prons = entry.find("pronunciation")
            if check_prons is None:
                try:
                    pron_text = ""
                    cv_pattern = ""
                    pron_number = ""
                    csv_writer.writerow({'word':word, 'dateCreated':dateCreated, 'dateModified':dateModified, 'guid':guid, 'id':id, 'morph_type':morph_type, 'cv_pattern':cv_pattern, 'pron_number':pron_number, 'pron':pron_text})
                    print(id)
                except:
                    pass
            else:
                try:
                    prons = entry.findall("pronunciation")
                    i_pron = iter(prons)
                    pron_number = 0
                    while True:
                        pron = next(i_pron)
                        pron_number = pron_number + 1


                        pron_text = pron.find("form").find("text").text

                        try:
                            check_pron_text = pron.find("form")
                            if check_pron_text is None:
                                pron_text = ""
                            else:
                                pron_text = pron.find("form").find("text").text
                        except:
                            pass

                        try:
                            check_cv_pattern = pron.find("field[@type='cv-pattern']")
                            if check_cv_pattern is None:
                                cv_pattern = ""

                            else:
                                cv_pattern = pron.find("field").find("form").find("text").text
                        except:
                            pass
                        csv_writer.writerow({'word':word, 'dateCreated':dateCreated, 'dateModified':dateModified, 'guid':guid, 'id':id, 'morph_type':morph_type, 'cv_pattern':cv_pattern, 'pron_number':pron_number, 'pron':pron_text})
                        print(id)

                except:
                    pass
