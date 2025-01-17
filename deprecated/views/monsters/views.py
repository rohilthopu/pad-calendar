from django.shortcuts import render
from .models import Monster
from skills.models import Skill
from .maps import EXPLICIT_TYPE_MAP, TYPE_MAP
import json
from dungeons.models import Dungeon, Floor


def monster_view(request, card_id):
    template = 'monster.html'
    monster = Monster.objects.get(card_id=card_id)
    evo_list = json.loads(monster.evolutions)
    monsters = Monster.objects.all()

    # The following set of checks is necessary as some cards do not have leader skills, active skills, or ancestors.
    ancestor = None
    if monster.ancestor_id != monster.card_id:
        if monster.ancestor_id != 0:
            ancestor = Monster.objects.get(card_id=monster.ancestor_id)

    active_skill = Skill.objects.get(skill_id=monster.active_skill_id)
    leader_skill = Skill.objects.get(skill_id=monster.leader_skill_id)

    evos = None
    if len(evo_list) > 0:
        evos = get_evos(evo_list)

    evo_mats = get_evo_mats(monster, monsters)
    un_evo_mats = get_un_evo_mats(monster, monsters)

    awakenings = json.loads(monster.awakenings)
    super_awakenings = json.loads(monster.super_awakenings)

    print(awakenings)
    types = get_types(monster)

    dungeons = []

    context = {'active_skill': active_skill, 'leader_skill': leader_skill,
               'monster': monster, 'ancestor': ancestor, "evolutions": evos, "evo_mats": evo_mats,
               "un_evo_mats": un_evo_mats, 'awakenings': awakenings, 'super_awakenings': super_awakenings,
               'types': types, 'dungeons': dungeons}

    return render(request, template, context)


def monster_list(request):
    cards = Monster.objects.exclude(name__contains='?').exclude(name__contains='*').exclude(
        name__contains='Alt.').values('name', 'card_id')

    context = {'cards': cards}
    template = 'monsters.html'
    return render(request, template, context)


def get_evo_mats(monster, monsters):
    evo_mats = []
    if monster.evo_mat_1 != 0:
        evo_mats.append(monsters.get(card_id=monster.evo_mat_1))
    if monster.evo_mat_2 != 0:
        evo_mats.append(monsters.get(card_id=monster.evo_mat_2))
    if monster.evo_mat_3 != 0:
        evo_mats.append(monsters.get(card_id=monster.evo_mat_3))
    if monster.evo_mat_4 != 0:
        evo_mats.append(monsters.get(card_id=monster.evo_mat_4))
    if monster.evo_mat_5 != 0:
        evo_mats.append(monsters.get(card_id=monster.evo_mat_5))
    return evo_mats


def get_un_evo_mats(monster, monsters):
    un_evo_mats = []
    if monster.un_evo_mat_1 != 0:
        un_evo_mats.append(monsters.get(card_id=monster.un_evo_mat_1))
    if monster.un_evo_mat_2 != 0:
        un_evo_mats.append(monsters.get(card_id=monster.un_evo_mat_2))
    if monster.un_evo_mat_3 != 0:
        un_evo_mats.append(monsters.get(card_id=monster.un_evo_mat_3))
    if monster.un_evo_mat_4 != 0:
        un_evo_mats.append(monsters.get(card_id=monster.un_evo_mat_4))
    if monster.un_evo_mat_5 != 0:
        un_evo_mats.append(monsters.get(card_id=monster.un_evo_mat_5))
    return un_evo_mats


def get_types(monster) -> []:
    types = [EXPLICIT_TYPE_MAP[TYPE_MAP[monster.type_1]], EXPLICIT_TYPE_MAP[TYPE_MAP[monster.type_2]],
             EXPLICIT_TYPE_MAP[TYPE_MAP[monster.type_3]]]
    return types


def get_evos(evo_list) -> []:
    evos = []
    for evo in evo_list:
        evo_card = Monster.objects.get(card_id=evo['card_id'])
        if "Alt." not in evo_card.name:
            evos.append(evo_card)
    return evos


def get_dungeons(card_id) -> []:
    dungeon_list = []

    floors = Floor.objects.all()
    for floor in floors:
        drop_data = json.loads(floor.possible_drops)
        for key in drop_data.keys():
            if card_id == int(key):
                dungeon = Dungeon.objects.filter(dungeon_id=floor.dungeon_id)[0]
                if dungeon not in dungeon_list:
                    dungeon_list.append(dungeon)

    return dungeon_list
