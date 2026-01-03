import json
import os
import glob

# Item ID to placed entity mapping
items_to_update = {
    'aquatitan_amber_texture': 'Plushies Behavior/items/Atlatitan/aquatitan_amber_texture.item.json',
    'aquatitan_base_texture': 'Plushies Behavior/items/Atlatitan/aquatitan_base_textue.item.json',
    'aquatitan_tectonic_texture': 'Plushies Behavior/items/Atlatitan/aquatitan_tectonic_texture.item.json',
    'LUX_texture': 'Plushies Behavior/items/Atlatitan/LUX_texture.item.json',
    'sunny_edition_aquatitan': 'Plushies Behavior/items/Atlatitan/sunny_edition_aquatitan.item.json',
    'Grottoceratops_Plushie': 'Plushies Behavior/items/Grottoceratops_Plushie/Grottoceratops_Plushie.item.json',
    'Grottoceratops_Plushie1': 'Plushies Behavior/items/Grottoceratops_Plushie/Grottoceratops_Plushie1.item.json',
    'Grottoceratops_Plushie2': 'Plushies Behavior/items/Grottoceratops_Plushie/Grottoceratops_Plushie2.item.json',
    'Grottoceratops_Plushie3': 'Plushies Behavior/items/Grottoceratops_Plushie/Grottoceratops_Plushie3.item.json',
    'plush_relicheirus_1': 'Plushies Behavior/items/Plush_Relicheirus/Relicherirus_1.json',
    'plush_relicheirus_2': 'Plushies Behavior/items/Plush_Relicheirus/Relicherirus_2.json',
    'plush_relicheirus_3': 'Plushies Behavior/items/Plush_Relicheirus/Relicherirus_3.json',
    'plush_relicheirus_4': 'Plushies Behavior/items/Plush_Relicheirus/Relicherirus_4.json',
    'plush_subteranadon_1': 'Plushies Behavior/items/Plush_Subteranadon/1000086515.json',
    'plush_subteranadon_2': 'Plushies Behavior/items/Plush_Subteranadon/1000086516.json',
    'plush_subteranadon_normal': 'Plushies Behavior/items/Plush_Subteranadon/subteranadon normal.json',
    'plush_subteranodon_amber': 'Plushies Behavior/items/Plush_Subteranadon/subterranodon amber.json',
    'plush_subteranodon_tectonic': 'Plushies Behavior/items/Plush_Subteranadon/subterranodon tectonic.json',
    'plush_tremersaurus_1': 'Plushies Behavior/items/Plush_Tremersaurus/tremer_1.json',
    'plush_tremersaurus_2': 'Plushies Behavior/items/Plush_Tremersaurus/tremer_2.json',
    'plush_tremersaurus_3': 'Plushies Behavior/items/Plush_Tremersaurus/tremer_3.json',
    'plush_tremersaurus_4': 'Plushies Behavior/items/Plush_Tremersaurus/tremer_4.json',
    'plush_tremersaurus_5': 'Plushies Behavior/items/Plush_Tremersaurus/tremer_5.json',
    'plush_tremersaurus_6': 'Plushies Behavior/items/Plush_Tremersaurus/tremer_6.json',
    'plush_tremersaurus_7': 'Plushies Behavior/items/Plush_Tremersaurus/tremer_7.json',
    'plush_tremersaurus_8': 'Plushies Behavior/items/Plush_Tremersaurus/tremer_8.json',
    'vallumraptor_plushie_1_6': "Plushies Behavior/items/Vallum's Critters/geo 1/vallumraptor_plushie_1_6.item.json",
    'vallumraptor_plushie_1_66': "Plushies Behavior/items/Vallum's Critters/geo 1/vallumraptor_plushie_1_66.item.json",
    'vallumraptor_plushie_1_7': "Plushies Behavior/items/Vallum's Critters/geo 1/vallumraptor_plushie_1_7.item.json",
    'vallumraptor_plushie_2': "Plushies Behavior/items/Vallum's Critters/geo 2/vallumraptor_plushie_2.item.json",
    'vallumraptor_plushie_2_2': "Plushies Behavior/items/Vallum's Critters/geo 2/vallumraptor_plushie_2_2.item.json",
    'vallumraptor_plushie_3_1': "Plushies Behavior/items/Vallum's Critters/geo 3/vallumraptor_plushie_3_1.item.json",
    'vallumraptor_plushie_3_2': "Plushies Behavior/items/Vallum's Critters/geo 3/vallumraptor_plushie_3_2.item.json",
    'vallumraptor_plushie_1_1': "Plushies Behavior/items/Vallum's Critters/vallumraptor_plushie/vallumraptor_plushie_1_1.item.json",
    'vallumraptor_plushie_4': "Plushies Behavior/items/Vallum's Critters/vallumraptor_plushie/vallumraptor_plushie_4.item.json",
    'vallumraptor_plushie_7': "Plushies Behavior/items/Vallum's Critters/vallumraptor_plushie/vallumraptor_plushie_7.item.json",
    'vallumraptor_plushie_8': "Plushies Behavior/items/Vallum's Critters/vallumraptor_plushie/vallumraptor_plushie_8.item.json",
}

print('Updating item files...')
updated = 0
for item_id, item_path in items_to_update.items():
    if os.path.exists(item_path):
        with open(item_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update the entity_placer to point to the placed entity
        if 'minecraft:item' in data and 'components' in data['minecraft:item']:
            if 'minecraft:entity_placer' in data['minecraft:item']['components']:
                data['minecraft:item']['components']['minecraft:entity_placer']['entity'] = f'myname:{item_id}_placed'
                
                with open(item_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent='\t')
                
                updated += 1
                print(f'  Updated: {item_path}')
            else:
                print(f'  SKIPPED (no entity_placer): {item_path}')
        else:
            print(f'  SKIPPED (invalid structure): {item_path}')
    else:
        print(f'  NOT FOUND: {item_path}')

print(f'\nUpdated {updated} item files!')
