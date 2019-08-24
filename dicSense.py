import os
import xml.etree.ElementTree as et
import csv
import itertools


base_path = os.path.dirname(os.path.realpath(__file__))
xml_file = os.path.join(base_path, "new_data\\dic.xml")

tree = et.parse(xml_file)
root =  tree.getroot()

def encode(self,input,errors='strict'):
    return codecs.charmap_encode(input,errors,encoding_table)

with open('dicSense.csv', 'w', encoding="utf-8", newline='') as new_file:
    fieldnames = ['word', 'dateCreated', 'dateModified', 'guid', 'id', 'morph_type', 'sense_id', 'sense_number', 'grammatical_info', 'scientific_name', 'gloss_pt', 'gloss_en', 'gloss_es', 'gloss_fr', 'definition_pt', 'definition_en', 'definition_es', 'definition_fr', 'example_number', 'example_ver', 'free_pt', 'free_en', 'free_es', 'free_fr']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
    # csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=';')
    csv_writer.writeheader()
    for entry in root.findall('entry'):
            sense_id = ""
            sense_number = ""
            grammatical_info = ""
            scientific_name = ""
            gloss_pt = ""
            gloss_en = ""
            gloss_es = ""
            gloss_fr = ""
            definition_pt = ""
            definition_en = ""
            definition_es = ""
            definition_fr = ""
            example_number = ""
            example_ver = ""
            free_pt = ""
            free_en = ""
            free_es = ""
            free_fr = ""

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

            check_sense = entry.find("sense")
            if check_sense is None:
                try:
                    csv_writer.writerow({'word':word, 'dateCreated':dateCreated, 'dateModified':dateModified, 'guid':guid, 'id':id, 'morph_type':morph_type, "sense_id":sense_id, 'sense_number':sense_number, 'grammatical_info':grammatical_info, 'scientific_name':scientific_name, 'gloss_pt':gloss_pt, 'gloss_en':gloss_en, 'gloss_es':gloss_es, 'gloss_fr':gloss_fr, 'definition_pt':definition_pt, 'definition_en':definition_en, 'definition_es':definition_es, 'definition_fr':definition_fr, 'example_number':example_number, 'example_ver':example_ver, 'free_pt':free_pt, 'free_en':free_en, 'free_es':free_es, 'free_fr':free_fr})
                    print(id)

                except:
                    pass
            else:
                try:
                    senses = entry.findall("sense")
                    i_sense = iter(senses)
                    sense_number = 0                    # sense_counter = intertools.count()
                    while True:
                        sense = next(i_sense)
                        sense_number = sense_number + 1

                        try:
                            check_sense_id = sense.attrib["id"]
                            if check_sense_id is None:
                                sense_id = ""
                            else:
                                sense_id = sense.attrib["id"]
                        except:
                            pass

                        try:
                            check_grammatical_info = sense.find("grammatical-info")
                            if check_grammatical_info is None:
                                grammatical_info = ""
                            else:
                                grammatical_info = sense.find("grammatical-info").attrib["value"]
                        except:
                            pass

                        try:
                            check_scientific_name = sense.find("field[@type='scientific-name']")
                            if check_scientific_name is None:
                                scientific_name = ""
                            else:
                                scientific_name = sense.find("field[@type='scientific-name']").find("form").find("text").text
                        except:
                            pass

                        try:
                            check_gloss_pt = sense.find("gloss[@lang='pt']")
                            if check_gloss_pt is None:
                                gloss_pt = ""
                            else:
                                gloss_pt = sense.find("gloss[@lang='pt']").find("text").text
                        except:
                            pass

                        try:
                            check_gloss_en = sense.find("gloss[@lang='en']")
                            if check_gloss_en is None:
                                gloss_en = ""
                            else:
                                gloss_en = sense.find("gloss[@lang='en']").find("text").text
                        except:
                            pass

                        try:
                            check_gloss_es = sense.find("gloss[@lang='es']")
                            if check_gloss_es is None:
                                gloss_es = ""
                            else:
                                gloss_es = sense.find("gloss[@lang='es']").find("text").text
                        except:
                            pass

                        try:
                            check_gloss_fr = sense.find("gloss[@lang='fr']")
                            if check_gloss_fr is None:
                                gloss_fr = ""
                            else:
                                gloss_fr = sense.find("gloss[@lang='fr']").find("text").text
                        except:
                            pass

                        check_definition = sense.find("definition")

                        if check_definition is None:
                            definition_pt = ""
                            definition_en = ""
                            definition_es = ""
                            definition_fr = ""


                        else:
                            try:
                                check_definition_pt = sense.find("definition").find("form[@lang='pt']")
                                if check_definition_pt is None:
                                    definition_pt = ""
                                else:
                                    definition_pt = sense.find("definition").find("form[@lang='pt']").find("text").text
                            except:
                                pass

                            try:
                                check_definition_en = sense.find("definition").find("form[@lang='en']")
                                if check_definition_en is None:
                                    definition_en = ""
                                else:
                                    definition_en = sense.find("definition").find("form[@lang='en']").find("text").text
                            except:
                                pass

                            try:
                                check_definition_es = sense.find("definition").find("form[@lang='es']")
                                if check_definition_es is None:
                                    definition_es = ""
                                else:
                                    definition_es = sense.find("definition").find("form[@lang='es']").find("text").text
                            except:
                                pass

                            try:
                                check_definition_fr = sense.find("definition").find("form[@lang='fr']")
                                if check_definition_es is None:
                                    definition_fr = ""
                                else:
                                    definition_fr = sense.find("definition").find("form[@lang='fr']").find("text").text
                            except:
                                pass

                        check_example = sense.find("example")

                        if check_example is None:
                            try:
                                example_number = ""
                                example_ver = ""
                                free_pt = ""
                                free_en = ""
                                free_es = ""
                                free_fr = ""
                                csv_writer.writerow({'word':word, 'dateCreated':dateCreated, 'dateModified':dateModified, 'guid':guid, 'id':id, 'morph_type':morph_type, "sense_id":sense_id, 'sense_number':sense_number, 'grammatical_info':grammatical_info, 'scientific_name':scientific_name, 'gloss_pt':gloss_pt, 'gloss_en':gloss_en, 'gloss_es':gloss_es, 'gloss_fr':gloss_fr, 'definition_pt':definition_pt, 'definition_en':definition_en, 'definition_es':definition_es, 'definition_fr':definition_fr, 'example_number':example_number, 'example_ver':example_ver, 'free_pt':free_pt, 'free_en':free_en, 'free_es':free_es, 'free_fr':free_fr})
                                print(id)
                            except:
                                pass

                        else:
                            try:
                                examples = sense.findall("example")
                                i_example = iter(examples)
                                example_number = 0
                                while True:
                                    example = next(i_example)
                                    example_number = example_number + 1

                                    try:
                                        check_example_ver = example.find("form")
                                        if check_example_ver is None:
                                            example_ver = ""
                                        else:
                                            example_ver = example.find("form").find("text").text
                                    except:
                                        pass

                                    try:
                                        check_trans = example.find("translation")
                                        if check_trans is None:
                                            free_pt = ""
                                            free_en = ""
                                            free_es = ""
                                            free_fr = ""
                                            csv_writer.writerow({'word':word, 'dateCreated':dateCreated, 'dateModified':dateModified, 'guid':guid, 'id':id, 'morph_type':morph_type, "sense_id":sense_id, 'sense_number':sense_number, 'grammatical_info':grammatical_info, 'scientific_name':scientific_name, 'gloss_pt':gloss_pt, 'gloss_en':gloss_en, 'gloss_es':gloss_es, 'gloss_fr':gloss_fr, 'definition_pt':definition_pt, 'definition_en':definition_en, 'definition_es':definition_es, 'definition_fr':definition_fr, 'example_number':example_number, 'example_ver':example_ver, 'free_pt':free_pt, 'free_en':free_en, 'free_es':free_es, 'free_fr':free_fr})
                                            print(id)

                                        else:
                                            try:
                                                check_free_pt = example.find("translation").find("form[@lang='pt']")
                                                if check_free_pt is None:
                                                    free_pt = ""
                                                else:
                                                    free_pt = example.find("translation").find("form[@lang='pt']").find("text").text
                                            except:
                                                pass
                                            try:
                                                check_free_en = example.find("translation").find("form[@lang='en']")
                                                if check_free_en is None:
                                                    free_en = ""
                                                else:
                                                    free_en = example.find("translation").find("form[@lang='en']").find("text").text
                                            except:
                                                pass
                                            try:
                                                check_free_es = example.find("translation").find("form[@lang='es']")
                                                if check_free_pt is None:
                                                    free_es = ""
                                                else:
                                                    free_es = example.find("translation").find("form[@lang='es']").find("text").text
                                            except:
                                                pass
                                            try:
                                                check_free_fr = example.find("translation").find("form[@lang='fr']")
                                                if check_free_fr is None:
                                                    free_fr = ""
                                                else:
                                                    free_fr = example.find("translation").find("form[@lang='fr']").find("text").text
                                            except:
                                                pass
                                            csv_writer.writerow({'word':word, 'dateCreated':dateCreated, 'dateModified':dateModified, 'guid':guid, 'id':id, 'morph_type':morph_type, "sense_id":sense_id, 'sense_number':sense_number, 'grammatical_info':grammatical_info, 'scientific_name':scientific_name, 'gloss_pt':gloss_pt, 'gloss_en':gloss_en, 'gloss_es':gloss_es, 'gloss_fr':gloss_fr, 'definition_pt':definition_pt, 'definition_en':definition_en, 'definition_es':definition_es, 'definition_fr':definition_fr, 'example_number':example_number, 'example_ver':example_ver, 'free_pt':free_pt, 'free_en':free_en, 'free_es':free_es, 'free_fr':free_fr})
                                            print(id)

                                    except:
                                        pass


                            except:
                                pass

                except:
                    pass
