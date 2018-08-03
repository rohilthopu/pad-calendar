from django.shortcuts import render
from .models import CardJP, MonsterData, ActiveSkill, LeaderSkill
import json
from .maps import EXPLICIT_TYPE_MAP


def cardView(request, card_id):
    template = 'monster_jp.html'
    mnstr = MonsterData.objects.get(cardID=card_id)
    card = CardJP.objects.get(monster=mnstr)
    cards = CardJP.objects.all()
    monsters = MonsterData.objects.all()

    # The following set of checks is necessary as some cards do not have leader skills, active skills, or ancestors.
    ancestor = None
    if mnstr.ancestorID != mnstr.cardID:
        if mnstr.ancestorID != 0:
            ancestor = cards.get(monster=MonsterData.objects.get(cardID=mnstr.ancestorID))

    leaderskill = None
    if card.leaderSkill is not None:
        leaderskill = card.leaderSkill.all().first()

    activeskill = None
    if card.activeSkill is not None:
        activeskill = card.activeSkill.all().first()

    evos = None
    if len(mnstr.evolutions.all()) > 0:
        evos = []

        for evo in mnstr.evolutions.all():
            evoCard = cards.get(monster=MonsterData.objects.get(cardID=evo.evo))
            if "Alt." not in evoCard.monster.name:
                evos.append(evoCard)

    evomats = getEvoMats(mnstr, cards, monsters)
    unevomats = getUnEvoMats(mnstr, cards, monsters)

    awakenings = json.loads(mnstr.awakenings)
    sawakenings = json.loads(mnstr.superAwakenings)

    types = getTypes(mnstr)

    context = {'activeskill': activeskill, 'leaderskill': leaderskill,
               'monster': card.monster, 'ancestor': ancestor, "evolutions": evos, "evomats": evomats,
               "unevomats": unevomats, 'awakenings': awakenings, 'sawakenings': sawakenings, 'types': types}

    return render(request, template, context)


def cardList(request):
    rawCards = MonsterData.objects.order_by('cardID').all()
    cards = []
    cardID = []

    for card in rawCards:
        if "*" not in card.name:
            if "Alt." not in card.name:
                cards.append(card.name)
                cardID.append(card.cardID)

    cardList = zip(cards, cardID)
    context = {'cards': cardList}
    template = 'monster_list_jp.html'
    return render(request, template, context)


def activeSkillListView(request):
    names = ActiveSkill.objects.values_list('name', flat=True)
    sids = ActiveSkill.objects.values_list('skillID', flat=True)

    aSkills = zip(names, sids)

    context = {'skills': aSkills}
    template = 'active_skill_list_jp.html'

    return render(request, template, context)


def activeSkillView(request, id):
    activeskill = ActiveSkill.objects.get(skillID=id)
    monsters = MonsterData.objects.filter(activeSkillID=activeskill.skillID)

    context = {'activeskill': activeskill, "monsters": monsters}
    template = 'active_skill_jp.html'
    return render(request, template, context)


def leaderSkillListView(request):
    names = LeaderSkill.objects.values_list('name', flat=True)
    sids = LeaderSkill.objects.values_list('skillID', flat=True)

    lSkills = zip(names, sids)
    context = {'skills': lSkills}
    template = 'leader_skill_list_jp.html'
    return render(request, template, context)


def leaderSkillView(request, id):
    leaderskill = LeaderSkill.objects.get(skillID=id)
    monsters = MonsterData.objects.filter(leaderSkillID=leaderskill.skillID)

    context = {'leaderskill': leaderskill, "monsters": monsters}
    template = 'leader_skill_jp.html'
    return render(request, template, context)


def getEvoMats(monster, cards, monsters):
    evomats = []

    if monster.evomat1 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.evomat1)))
    if monster.evomat2 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.evomat2)))
    if monster.evomat3 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.evomat3)))
    if monster.evomat4 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.evomat4)))
    if monster.evomat5 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.evomat5)))

    return evomats


def getUnEvoMats(monster, cards, monsters):
    evomats = []

    if monster.unevomat1 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.unevomat1)))
    if monster.unevomat2 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.unevomat2)))
    if monster.unevomat3 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.unevomat3)))
    if monster.unevomat4 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.unevomat4)))
    if monster.unevomat5 != 0:
        evomats.append(cards.get(monster=monsters.get(cardID=monster.unevomat5)))

    return evomats


def getTypes(monster) -> []:
    types = []
    types.append(EXPLICIT_TYPE_MAP[int(monster.type1)])
    types.append(EXPLICIT_TYPE_MAP[int(monster.type2)])
    types.append(EXPLICIT_TYPE_MAP[int(monster.type3)])
    return types
