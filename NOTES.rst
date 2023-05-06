Move the CIT json files into position for custom-model-data with bitmasks (this is based on info in the file path **not** the .properties file)::

    cd assets/minecraft/optifine/cit/enchs
    find * -iname '*.json' -not -iname 'pumpkin*' -not -iname 'crossbow*' -not -iname 'shield*' -not -iname 'fishing*' -not -iname 'trident*' | while read optifinepath ; do item_name="${optifinepath##*/}" enchants="${optifinepath#*/}" ; item_name="${item_name%.*}" enchants=( $(sed 's/^.\///;s/[0-9]//g;s/\(\/[xz]\)\?\/[^\/]*.json//g;s/\// /g;s/vanising/vanishing/' <<< "$enchants") ) ; newpath="../../../models/item/${optifinepath%%/*}/$(python3 ~/vcs/Fission-Mailed-mcpack/enchants_to_bitmask.py "$item_name" "${enchants[@]}").json" ; mkdir -p "${newpath%/*}" ; git mv "$optifinepath" "$newpath" ; echo git rm --ignore-unmatch "${optifinepath%.json}.properties" ; done

Flint and steel is special because it doesn't do layer masks at all::

    # FIXME: mcmeta files are named wrong and don't have the .png included
    find . -iname 'flint_and_steel.png' -or -iname 'flint_and_steel.png.mcmeta'  | while read optifinepath ; do enchants="${optifinepath#*/}" ; enchants=( $(sed 's/^.\///;s/[0-9]//g;s/\(\/[xz]\)\?\/[^\/]*.png\(.mcmeta\)\?//g;s/\// /g;s/vanising/vanishing/' <<< "$enchants") ) ; newpath="../../../textures/item/$(python3 ~/vcs/Fission-Mailed-mcpack/enchants_to_bitmask.py "${enchants[@]}").${optifinepath##*.}" ; mkdir -p "${newpath%/*}" ; git mv "$optifinepath" "$newpath" ; git rm --ignore-unmatch "${optifinepath%.png}.properties" ; done
    cd ../../../models/items
    for f in ../../textures/item/flint_and_steel/0b*.png ; do texture="${f#*/textures/}" ; texture="${texture%.png}" ; printf '{"parent":"minecraft:item/generated","textures":{"layer0":"%s"}}' "$texture" | jq . >"flint_and_steel/${texture##*/}.json" ; done

Python sort key function for the below::

     def sort_key(i):
         """This data **must** be sorted, because Minecraft is dumb."""
         return i['predicate'].get('custom_model_data', 0), i['model']

Creating the item files themselves (Python used because I couldn't do the binary2decimal conversion in Bash)::

    for material in ['wooden','stone','iron','golden','diamond','netherite']:
      for item in ['axe','pickaxe','shovel','sword','hoe']:
        data = {"parent": f"minecraft:item/{item}","textures":{"base":f"item/{material}_{item}"}}
        data['overrides'] = [{"predicate": {"custom_model_data": 6450000 + int(p.name.split('.')[0], 2)}, "model": 'item/'+str(p)[:-5]} for p in pathlib.Path('.').glob(f'*/{material}_{item}/0b*.json')]
        data['overrides'].sort(key=sort_key)
        with pathlib.Path(f'./{material}_{item}.json').open('w') as f:
          json.dump(data, f, indent=4)

Same again, for rods::

    for item in ['rods/carrot_on_a_stick','rods/warped_fungus_on_a_stick']:
      data = {"parent": f"minecraft:item/rods/rod","textures":{"base":f"bait": "item/rods/{item.split('/')[1][:-11]}"}}
      data['overrides'] = [{"predicate": {"custom_model_data": 6450000 + int(p.name.split('.')[0], 2)}, "model": 'item/'+str(p)[:-5]} for p in pathlib.Path('.').glob(f'{item}/0b*.json')]
      data['overrides'].sort(key=sort_key)
      with pathlib.Path(f'./{item.split("/")[1]}.json').open('w') as f:
        json.dump(data, f, indent=4)

Same again, for shears::

    data = {"parent": f"minecraft:item/misc/shears","textures":{"base":f"item/shears"}}
    data['overrides'] = [{"predicate": {"custom_model_data": 6450000 + int(p.name.split('.')[0], 2)}, "model": 'item/'+str(p)[:-5]} for p in pathlib.Path('.').glob(f'shears/shears/0b*.json')]
    data['overrides'].sort(key=sort_key)
    with pathlib.Path(f'./shears.json').open('w') as f:
      json.dump(data, f, indent=4)

# FIXME: Same again for flint_and_steel

Same again, but specifically for bows, since their animation is a bit more complex::

    data = {"parent": "minecraft:item/bows/bow","textures": {"base": "item/bow/base"},
            "display": {
                        "thirdperson_righthand": {"rotation": [ -80, 260, -40 ],"translation": [ -1, -2, 2.5 ],"scale": [ 0.9, 0.9, 0.9 ]},
                        "thirdperson_lefthand": {"rotation": [ -80, -280, 40 ],"translation": [ -1, -2, 2.5 ],"scale": [ 0.9, 0.9, 0.9 ]},
                        "firstperson_righthand": {"rotation": [ 0, -90, 25 ],"translation": [ 1.13, 3.2, 1.13],"scale": [ 0.68, 0.68, 0.68 ]},
                        "firstperson_lefthand": {"rotation": [ 0, 90, -25 ],"translation": [ 1.13, 3.2, 1.13],"scale": [ 0.68, 0.68, 0.68 ]}},
            "overrides": [
                          {"predicate": {"pulling": 1},"model": "item/bows/bow_pulling_0"},
                          {"predicate": {"pulling": 1,"pull": 0.65},"model": "item/bows/bow_pulling_1"},
                          {"predicate": {"pulling": 1,"pull": 0.9},"model": "item/bows/bow_pulling_2"}]}
    custom_overrides = []
    for p in pathlib.Path('./bow/bow_pulling_0/').iterdir():
        custom_model_data = 6450000 + int(p.name.split('.')[0], 2)
        data['overrides'].append({"predicate": {"custom_model_data": custom_model_data}, "model": 'item/'+str(p)[:-5].replace('bow_pulling_0', 'bow')})
        data['overrides'].append({"predicate": {"custom_model_data": custom_model_data,"pulling":1}, "model": 'item/'+str(p)[:-5]})
        data['overrides'].append({"predicate": {"custom_model_data": custom_model_data,"pulling":1,"pull":0.65}, "model": 'item/'+str(p)[:-5].replace('bow_pulling_0', 'bow_pulling_1')})
        data['overrides'].append({"predicate": {"custom_model_data": custom_model_data,"pulling":1,"pull":0.9}, "model": 'item/'+str(p)[:-5].replace('bow_pulling_0', 'bow_pulling_2')})

    data['overrides'].sort(key=sort_key)
    with pathlib.Path(f'./bow.json').open('w') as f:
      json.dump(data, f, indent=4)

Same again for flint and steel, which is extra special because it doesn't use layer masks at all::

    data = {"parent": f"minecraft:item/generated","textures":{"layer0": "minecraft:item/flint_and_steel"}}
    data['overrides'] = [{"predicate": {"custom_model_data": 6450000 + int(p.name.split('.')[0], 2)}, "model": 'item/'+str(p)[:-5]} for p in pathlib.Path('.').glob(f'flint_and_steel/0b*.json')]
    data['overrides'].sort(key=sort_key)
    with pathlib.Path(f'./flint_and_steel.json').open('w') as f:
      json.dump(data, f, indent=4)
