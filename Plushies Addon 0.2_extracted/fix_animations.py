import json
import os

# Mapping of geometry to their root bone names
bone_mapping = {
    'Atlatitan_plushies': 'Plush_Bone',
    'Grottoceratops_Plushie': 'Plushie_Bone',
    'Plush_Relicheirus': 'Plushie_Bone',
    'Plush_Subteranadon': 'Plushie_Bone',
    'Plush_Tremersaurus': 'Plushie_Bone',
    'vallumraptor_plushie_1': 'Item',
    'vallumraptor_plushie_2': 'Item',
    'vallumraptor_plushie_3': 'Item',
    'vallumraptor_plushie': 'root',  # This one is correct
}

for geo_name, bone_name in bone_mapping.items():
    anim_file = f'Plushies Resources/animations/entity/{geo_name}_placed.animation.json'
    
    if os.path.exists(anim_file):
        with open(anim_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update the bone name in the animation
        anim_key = f'animation.{geo_name}_placed.idle'
        if anim_key in data['animations']:
            # Get current bones dict
            bones_dict = data['animations'][anim_key].get('bones', {})
            
            # If it has 'root', replace with correct bone name
            if 'root' in bones_dict and bone_name != 'root':
                bones_dict[bone_name] = bones_dict.pop('root')
                data['animations'][anim_key]['bones'] = bones_dict
                
                with open(anim_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
                
                print(f'Updated {geo_name}: root -> {bone_name}')
            else:
                print(f'Skipped {geo_name}: already using {bone_name}')

print('\nDone!')
