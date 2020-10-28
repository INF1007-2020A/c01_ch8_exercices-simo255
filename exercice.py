#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici
def comparer(fichierr1 : str, fichierr2 : str):
    with open(fichierr1, 'r') as f, open(fichierr2,"r") as k:
        same = True
        while same:
            a= fichierr1.read
            b=fichierr2.read
            same =  a==b
    return -1 if same else fichierr1.tell

def spacetripler(f1):
    with open(f1, "r") as data, open(f2, 'w') as result:
        result.write(data.read().replace(' ', '   '))
    return result

def assign_note_letter(note_file, target_file):
    correspondances = {20: "F", 40: "D", 50: "C", 70: "B", 85: "A"}
    with open(note_file, 'r') as note_data, open(target_file, 'w') as target:
        for line in note_data.readlines():
            note = int(line)
            for grade in correspondances.keys():
                if grade == 85 and note > grade:
                    target.write("A*")
                if note <= grade:
                    target.write(correspondances[grade] + "\n")
                    break
        
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    spacetripler('notes.txt')

    
