import json
import os

# Plushie data mapping
plushies = [
    {'item': 'aquatitan_amber_texture', 'texture': 'textures/entity/attachable/aquatitan_amber_texture', 'geo': 'geometry.Atlatitan_plushies_placed'},
    {'item': 'aquatitan_base_texture', 'texture': 'textures/entity/attachable/aquatitan_base_texture', 'geo': 'geometry.Atlatitan_plushies_placed'},
    {'item': 'aquatitan_tectonic_texture', 'texture': 'textures/entity/attachable/aquatitan_tectonic_texture', 'geo': 'geometry.Atlatitan_plushies_placed'},
    {'item': 'LUX_texture', 'texture': 'textures/entity/attachable/LUX_texture', 'geo': 'geometry.Atlatitan_plushies_placed'},
    {'item': 'sunny_edition_aquatitan', 'texture': 'textures/entity/attachable/sunny_edition_aquatitan', 'geo': 'geometry.Atlatitan_plushies_placed'},
    {'item': 'Grottoceratops_Plushie', 'texture': 'textures/entity/attachable/Grottoceratops_Plushie/texture', 'geo': 'geometry.Grottoceratops_Plushie_placed'},
    {'item': 'Grottoceratops_Plushie1', 'texture': 'textures/entity/attachable/Grottoceratops_Plushie/texture1', 'geo': 'geometry.Grottoceratops_Plushie_placed'},
    {'item': 'Grottoceratops_Plushie2', 'texture': 'textures/entity/attachable/Grottoceratops_Plushie/texture2', 'geo': 'geometry.Grottoceratops_Plushie_placed'},
    {'item': 'Grottoceratops_Plushie3', 'texture': 'textures/entity/attachable/Grottoceratops_Plushie/texture3', 'geo': 'geometry.Grottoceratops_Plushie_placed'},
    {'item': 'plush_relicheirus_1', 'texture': 'textures/entity/attachable/Plush_Relicheirus/texture1', 'geo': 'geometry.Plush_Relicheirus_placed'},
    {'item': 'plush_relicheirus_2', 'texture': 'textures/entity/attachable/Plush_Relicheirus/texture2', 'geo': 'geometry.Plush_Relicheirus_placed'},
    {'item': 'plush_relicheirus_3', 'texture': 'textures/entity/attachable/Plush_Relicheirus/texture3', 'geo': 'geometry.Plush_Relicheirus_placed'},
    {'item': 'plush_relicheirus_4', 'texture': 'textures/entity/attachable/Plush_Relicheirus/texture4', 'geo': 'geometry.Plush_Relicheirus_placed'},
    {'item': 'plush_subteranadon_1', 'texture': 'textures/entity/attachable/Plush_Subterranodon/1000086515', 'geo': 'geometry.Plush_Subteranadon_placed'},
    {'item': 'plush_subteranadon_2', 'texture': 'textures/entity/attachable/Plush_Subterranodon/1000086516', 'geo': 'geometry.Plush_Subteranadon_placed'},
    {'item': 'plush_subteranadon_normal', 'texture': 'textures/entity/attachable/Plush_Subterranodon/subterranodon normal', 'geo': 'geometry.Plush_Subteranadon_placed'},
    {'item': 'plush_subteranodon_amber', 'texture': 'textures/entity/attachable/Plush_Subterranodon/subterranodon amber', 'geo': 'geometry.Plush_Subteranadon_placed'},
    {'item': 'plush_subteranodon_tectonic', 'texture': 'textures/entity/attachable/Plush_Subterranodon/subterranodon tectonic', 'geo': 'geometry.Plush_Subteranadon_placed'},
    {'item': 'plush_tremersaurus_1', 'texture': 'textures/entity/attachable/Plush_Tremersaurus/Tremer_1', 'geo': 'geometry.Plush_Tremersaurus_placed'},
    {'item': 'plush_tremersaurus_2', 'texture': 'textures/entity/attachable/Plush_Tremersaurus/tremer_2', 'geo': 'geometry.Plush_Tremersaurus_placed'},
    {'item': 'plush_tremersaurus_3', 'texture': 'textures/entity/attachable/Plush_Tremersaurus/tremer_3', 'geo': 'geometry.Plush_Tremersaurus_placed'},
    {'item': 'plush_tremersaurus_4', 'texture': 'textures/entity/attachable/Plush_Tremersaurus/tremer_4', 'geo': 'geometry.Plush_Tremersaurus_placed'},
    {'item': 'plush_tremersaurus_5', 'texture': 'textures/entity/attachable/Plush_Tremersaurus/tremer_5', 'geo': 'geometry.Plush_Tremersaurus_placed'},
    {'item': 'plush_tremersaurus_6', 'texture': 'textures/entity/attachable/Plush_Tremersaurus/tremer_6', 'geo': 'geometry.Plush_Tremersaurus_placed'},
    {'item': 'plush_tremersaurus_7', 'texture': 'textures/entity/attachable/Plush_Tremersaurus/tremer_7', 'geo': 'geometry.Plush_Tremersaurus_placed'},
    {'item': 'plush_tremersaurus_8', 'texture': 'textures/entity/attachable/Plush_Tremersaurus/tremer_8', 'geo': 'geometry.Plush_Tremersaurus_placed'},
    {'item': 'vallumraptor_plushie_1_6', 'texture': 'textures/entity/attachable/geo 1/1000085576', 'geo': 'geometry.vallumraptor_plushie_1_placed'},
    {'item': 'vallumraptor_plushie_1_66', 'texture': 'textures/entity/attachable/geo 1/1000085566', 'geo': 'geometry.vallumraptor_plushie_1_placed'},
    {'item': 'vallumraptor_plushie_1_7', 'texture': 'textures/entity/attachable/geo 1/1000085577', 'geo': 'geometry.vallumraptor_plushie_1_placed'},
    {'item': 'vallumraptor_plushie_2', 'texture': 'textures/entity/attachable/vallumraptor_plushie_2', 'geo': 'geometry.vallumraptor_plushie_2_placed'},
    {'item': 'vallumraptor_plushie_2_2', 'texture': 'textures/entity/attachable/geo 2/vallumraptor_plushie_2', 'geo': 'geometry.vallumraptor_plushie_2_placed'},
    {'item': 'vallumraptor_plushie_3_1', 'texture': 'textures/entity/attachable/geo 3/1000086381', 'geo': 'geometry.vallumraptor_plushie_3_placed'},
    {'item': 'vallumraptor_plushie_3_2', 'texture': 'textures/entity/attachable/geo 3/1000086312', 'geo': 'geometry.vallumraptor_plushie_3_placed'},
    {'item': 'vallumraptor_plushie_1_1', 'texture': 'textures/entity/attachable/vallumraptor_plushie/vallumraptor_plushie_1_1', 'geo': 'geometry.vallumraptor_plushie_placed'},
    {'item': 'vallumraptor_plushie_4', 'texture': 'textures/entity/attachable/vallumraptor_plushie/1000085284', 'geo': 'geometry.vallumraptor_plushie_placed'},
    {'item': 'vallumraptor_plushie_7', 'texture': 'textures/entity/attachable/vallumraptor_plushie/1000086377', 'geo': 'geometry.vallumraptor_plushie_placed'},
    {'item': 'vallumraptor_plushie_8', 'texture': 'textures/entity/attachable/vallumraptor_plushie/1000086378', 'geo': 'geometry.vallumraptor_plushie_placed'},
]

# Template for behavior entity
def create_entity(item_id):
    return {
        'format_version': '1.20.50',
        'minecraft:entity': {
            'description': {
                'identifier': f'myname:{item_id}_placed',
                'is_spawnable': False,
                'is_summonable': True
            },
            'components': {
                'minecraft:collision_box': {'width': 0.5, 'height': 0.5},
                'minecraft:health': {'value': 1, 'max': 1},
                'minecraft:physics': {'has_gravity': True, 'has_collision': True},
                'minecraft:pushable': {'is_pushable': False, 'is_pushable_by_piston': False},
                'minecraft:damage_sensor': {'triggers': [{'cause': 'all', 'deals_damage': False}]},
                'minecraft:knockback_resistance': {'value': 1.0},
                'minecraft:persistent': {},
                'minecraft:interact': {
                    'interactions': [{
                        'interact_text': 'action.hint.pickup',
                        'swing': True,
                        'on_interact': {
                            'filters': {'test': 'is_sneaking', 'subject': 'other', 'value': True},
                            'event': 'myname:pickup',
                            'target': 'self'
                        }
                    }]
                }
            },
            'events': {
                'myname:pickup': {
                    'queue_command': {
                        'command': [
                            f'give @s[type=player] myname:{item_id} 1',
                            'kill @s'
                        ]
                    }
                }
            }
        }
    }

# Template for client entity
def create_client_entity(item_id, texture, geo):
    anim_id = geo.replace('_placed', '').split('.')[-1]
    return {
        'format_version': '1.10.0',
        'minecraft:client_entity': {
            'description': {
                'identifier': f'myname:{item_id}_placed',
                'materials': {'default': 'entity_alphatest'},
                'textures': {'default': texture},
                'geometry': {'default': geo},
                'render_controllers': ['controller.render.default'],
                'spawn_egg': {'base_color': '#553399', 'overlay_color': '#88CCFF'},
                'animations': {'idle': f'animation.{anim_id}_placed.idle'},
                'scripts': {'animate': ['idle']}
            }
        }
    }

# Template for animations (one per geometry type)
def create_animation(geo_id):
    return {
        'format_version': '1.8.0',
        'animations': {
            f'animation.{geo_id}_placed.idle': {
                'loop': True,
                'animation_length': 2.0,
                'bones': {
                    'root': {
                        'rotation': {
                            '0.0': [0, 0, 0],
                            '1.0': [0, 5, 0],
                            '2.0': [0, 0, 0]
                        }
                    }
                }
            }
        }
    }

# Create behavior entities
print('Creating behavior entities...')
for p in plushies:
    entity_path = f'Plushies Behavior/entities/{p["item"]}_placed.json'
    os.makedirs(os.path.dirname(entity_path), exist_ok=True)
    with open(entity_path, 'w', encoding='utf-8') as f:
        json.dump(create_entity(p['item']), f, indent=2)

print(f'Created {len(plushies)} behavior entities!')

# Create client entities
print('\nCreating client entities...')
for p in plushies:
    client_path = f'Plushies Resources/entity/{p["item"]}_placed.entity.json'
    os.makedirs(os.path.dirname(client_path), exist_ok=True)
    with open(client_path, 'w', encoding='utf-8') as f:
        json.dump(create_client_entity(p['item'], p['texture'], p['geo']), f, indent=2)

print(f'Created {len(plushies)} client entities!')

# Create animations (one per unique geometry)
unique_geos = list(set(p['geo'] for p in plushies))
print(f'\nCreating {len(unique_geos)} unique animations...')
for geo in unique_geos:
    geo_name = geo.replace('_placed', '').split('.')[-1]
    anim_path = f'Plushies Resources/animations/entity/{geo_name}_placed.animation.json'
    os.makedirs(os.path.dirname(anim_path), exist_ok=True)
    with open(anim_path, 'w', encoding='utf-8') as f:
        json.dump(create_animation(geo_name), f, indent=2)
    print(f'  Created: {anim_path}')

print('\nDone!')
