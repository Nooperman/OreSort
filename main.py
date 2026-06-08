import shlex
import json

with open('orestore.json', 'r', encoding='utf-8') as oreindex:
    ores = json.load(oreindex)

compArr = []
unrecognizedOres = []
print(
    """Welcome to my Ore Sorter! This will help out with your ore comps
    because sorting ores by their rarity can be annoying, so I made this little program that will automize that for you!
    \n Note: Please, if the ore has a space in it's name, write it with an underscore, since shlex lexes every single word in one big string, so spaces...
            meaning you would have an array with example: ['a','flare','v2'] which is 3 different components and that would not be recognized...
    \n Another Note: Cave exclusives will be sorted incorrectly (no caves to multiply by), I will add that function in the future, where it recognizes it's cave type 
                        and multiplies the cave type by the ores rarity (no cave constant)"""
)
oreImp = input("\nInput all ores present in your ore comp (in the form of spaces inbetween the names of the ores and/or underscores instead of spaces for multiword ores): ")
segmented_oreImp = shlex.split(oreImp)
for segment in segmented_oreImp:
    try:
        compArr.append((segment.replace("_", " "), ores[segment.replace("_", " ")]))
        sorted_arr = sorted(compArr, key=lambda x: (x[1], x[0]))
    except:
        unrecognizedOres.append(segment.replace("_", " "))
for index, component in enumerate(sorted_arr):
    print(f"{index + 1}# {component[0]} - 1/{component[1]:,}")
if unrecognizedOres: 
    print(f"\nUnrecognized ores: {', '.join(unrecognizedOres)}") 

# Made by Coldrain - Credits: Stax (ore index)




