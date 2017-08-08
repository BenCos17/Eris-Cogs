import os
import discord
from discord.ext import commands
import random
from functools import reduce

dragonart = """
```
                                                 /===-_---~~~~~~~~~------____
                                                |===-~___                _,-'
                 -==\\                         `//~\\   ~~~~`---.___.-~~
             ______-==|                         | |  \\           _-~`
       __--~~~  ,-/-==\\                        | |   `\        ,'
    _-~       /'    |  \\                      / /      \      /
  .'        /       |   \\                   /' /        \   /'
 /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _)   ;  ),   __--~~
                    '~~--_/      _-~/-  / \   '-~ \
                   {\__--_/}    / \\_>- )<__\      \
                   /'   (_/  _-~  | |__>--<__|      |
                  |0  0 _/) )-~     | |__>--<__|     |
                  / /~ ,_/       / /__>---<__/      |
                 o o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   ;'( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `
```
"""

dickwords = [
    'dick',
    'chode',
    'schlong',
    'unit',
    'member',
    'johnson',
    'my little friend',
    'pocket weasel',
    'sausage',
    'man meat'
]

dickwords += [
    'adolph',
    'albino Cave Dweller',
    'baby-arm',
    'baby-maker',
    'baloney pony',
    'beaver basher',
    'beef whistle',
    'bell on a pole',
    'bishop',
    'bob Dole',
    'boomstick',
    'braciole',
    'bratwurst',
    'burrito',
    'candle',
    'choad',
    'chopper',
    'chub',
    'chubby',
    'cock',
    'cranny axe',
    'cum gun',
    'custard launcher',
    'dagger',
    'deep-V diver',
    'dick',
    'dickie',
    'ding dong',
    'mcdork',
    'dink',
    'dipstick',
    'disco stick',
    'dog head',
    'dong',
    'donger',
    'dork',
    'dragon',
    'drum stick',
    'dude piston',
    'easy Rider',
    'eggroll',
    'excalibur',
    'fang',
    'ferret',
    'fire hose',
    'flesh flute',
    'flesh tower',
    'froto',
    'fuck rod',
    'fudge sickle',
    'fun stick',
    'gigi',
    'groin',
    'heat-seeking moisture missile',
    'hog',
    'hose',
    'jackhammer',
    'jimmy',
    'john',
    'john Thomas',
    'johnson',
    'joystick',
    'junk',
    'kickstand',
    'king sebastian',
    'knob',
    'krull the warrior king',
    'lap rocket',
    'leaky hose',
    'lingam',
    'little Bob',
    'little Elvis',
    'lizard',
    'longfellow',
    'love muscle',
    'love rod',
    'love stick',
    'luigi',
    'manhood',
    'mayo shooting hotdog gun',
    'meat constrictor',
    'meat injection',
    'meat popsicle',
    'meat stick',
    'meat thermometer',
    'member',
    'meter long king kong dong',
    'microphone',
    'middle stump',
    'moisture and heat seeking venomous throbbing python of love',
    'mr. Knish',
    'mushroom head',
    'mutton',
    'netherrod',
    'old boy',
    'old fellow',
    'old man',
    'one-eyed monster',
    'one-eyed snake',
    'one-eyed trouser-snake',
    'one-eyed wonder weasel',
    'one-eyed yogurt slinger',
    'pecker',
    'pedro',
    'peepee',
    'percy',
    'peter',
    'pied Piper',
    'pig skin bus',
    'pink oboe',
    'piss weasle',
    'piston',
    'plug',
    'pnor',
    'poinswatter',
    'popeye',
    'pork sword',
    'prick',
    'private eye',
    'private part',
    'purple-headed yogurt flinger',
    'purple-helmeted warrior of love',
    'quiver bone',
    'ramburglar',
    'rod',
    'rod of pleasure',
    'roundhead',
    'sausage',
    'schlong',
    'dongadoodle',
    'schmeckel',
    'schmuck, shmuck',
    'schnitzel',
    'schwanz',
    'schwartz',
    'sebastianic sword',
    'shaft',
    'short arm',
    'single barrelled pump action bollock yogurt shotgun',
    'skin flute',
    'soldier',
    'spawn hammer',
    'steamin’ semen truck',
    'stick shift',
    'surfboard',
    'tallywhacker',
    'tan Bannana',
    'tassle',
    'third leg',
    'thumper',
    'thunderbird',
    'thundersword',
    'tinker',
    'todger',
    'tonk',
    'tool',
    'trouser snake',
    'tubesteak',
    'twig',
    'twig & berries',
    'twinkie',
    'vein',
    'wand',
    'wang',
    'wang doodle',
    'wanger',
    'wee wee',
    'whoopie stick',
    'wick',
    'wiener',
    'wiener Schnitzel',
    'willy',
    'wing dang doodle',
    'winkie',
    'yingyang',
    'yogurt gun'
]

vag_words = [
    'vag',
    'vajayjay',
    'box',
    'nether regions',
    'lady business',
    'lady v',
    'hoo-haw',
    'cha-cha',
    'lady bits',
    'crotch',
    'muff',
    'kitty',
    'cooch',
    'cooter',
    'snatch',
    'snapper',
    'beaver',
    'cookie',
    'cupcake',
    'coin purse',
    'lady flower',
    'honey pot',
    'poon',
    'punani',
    'twat',
    'gash',
    'banana basket',
    'flower pot',
    'fine china',
    'juice box',
    'pink panther',
    'hot pocket',
    'bikini bizkit',
    'penis fly trap',
    'vertical smile',
    'dew flaps',
    'flaming lips',
    'puff pillow',
    'notorious v.a.g.',
    'furburger',
    'bearded clam',
    'sausage wallet',
    'panty hamster',
    'meat curtains',
    'penis garage',
    'ink taco',
    'axe wound',
    'penis snuggie',
    'pussy',
    'cunt'
]

dickwords = list(set(dickwords))


def setup(bot):
    async def message_events(message):
        # DO NOT RESPOND TO SELF MESSAGES
        if bot.user.id == message.author.id or message.content.startswith('.'):
            return

        # BLACKLIST CHANNELS
        blacklist = [
            'news',
            'rpg'
        ]
        message_channel = message.channel.name.lower()
        if reduce(
            lambda acc, n: acc or (n == message_channel),
            blacklist,
            False):
            return


        clean_message = message.clean_content.lower()

        if 'zeb' in clean_message:
            new_message = await bot.send_message(message.channel, 'Daisuki, Zeb-kun!')
            await bot.add_reaction(new_message, '🐍')
            await bot.add_reaction(new_message, '🍆')
            await bot.add_reaction(new_message, '💦')

        elif 'masters' in [x.name.lower() for x in message.author.roles] and random.random() <= 0.01:
            await bot.send_message(message.channel, 'PIPE DOWN NIGGA')

        elif 'snek' in clean_message:
            await bot.send_message(message.channel, ':snake: ~ !! I :black_heart: you senpai !! ~ :snake:')
        elif 'blood' in clean_message:
            await bot.send_message(message.channel, 'B̵̪̳̣͍̙̳̬̭͞͝L͢͏̸͏̧̙̼͓̘̯͉̩̩̞͚͕̲̰̼̘̦ͅÒ̮͈̖͔̰̞͝O̵͖͔̟̰͔͚̬͟͝ͅḐ̸̭͙̜̺̞͍͎͔͜͡͡ ̨̨̟̝̦̬̩̳̖͟ͅF̤̭̬͙̀̀͘͠O̶̯̠̞̲̫̱̻̮͎̦̳̝͉̮̕ͅŔ̡͈͕̼͖̥̰̭̟̝͟ ̡̲̯͉̤͈̘͎̬͎̺̟͞T̴̸̟̺̬̼̣̖͓̩̯͇̣̩̺̮͘Ḫ̣̥͍͙͍͓͔͈̖̬̘̩͔͖̝͖̀͘E̶̡̛̯̞̱̯̗͍͖͇̹̖̳̩̥̳̳̙͢͝ ̡͓͍͕͔̳̠͍̥̞̙͖̙̦͕̠̪̘̕ͅB̪͕̻̺͈̤̟̻͖̣͙̪̝̭̀͘͠Ḻ̵̨̞̯̥̭͈̪̻̰̭́́͝O̧͜͏̰͓̘̖̘̬̤ͅǪ̥̟̘̪̱͔͇̖͟D̸̡҉̶̫͕͖̹̤̜̪̟̝̯͚ ̵̨̛̯̺̤̮̲͓̦̜̪̕͝G̙̩͖̭̘̤̩̕Ǫ͎͉̲̤͓͇̦̖̯͇̥͔͓̣̘̦̪̀D͘͘͏͡͏͙̠͈̮̱̼')
        elif 'skull' in clean_message:
            await bot.send_message(message.channel, 'S̡̟͉̻͔̩͕͙̳͜͟͜K҉̵͏̳͕͉͈̟͙̰͖͍̦͙̱̙̥̤̞̱U͏̥̲͉̞͉̭͟͟ͅL̵̶̯̼̪͉̮̰͙͍͟͜Ḻ̶̗̬̬͉̗̖̮̰̹̺̬̺͢͢͡ͅͅŚ̶̢͎̳̯͚̠̞͉̦̙̥̟̲̺̗̮̱͚̬͡͠ ̶̡̧̲̟͖̤͓̮̮͕̭͍̟͔͓͚̺̣̱͙͍͜͜F̶̡̢̨̯͖͎̻̝̱͚̣̦̭̞̣̰̳̣̩O̴̴̷̠̜̥̭̳̩̤͎̦̲͈͝ͅŔ̡̨̼̝̩̣͙̬̱̫͉̭͈̗̙͢͡ ͠͏̗̙͎̫̟̜̻̹̹̘̬̖ͅT̴͉̙̥̲̠͎̭͇͚̟͝͡Ḩ̺͕̦̭̪̼̼̮̰͍̲͍̯̗͇͘͘͝͝E̡̻̮̘̭͎̥̺̘͉̟̪̮̮͜͢͡ ̡̰͙̮͙͈̠͍̞̠̀͠Ṣ̷̡̡̛̜̞̣͙͇̭̣̳͕̖̺̱̳̭͖͞ͅͅK̵҉̨͇̭̯͍̱̞̦͎̥̼͢U̡̧̯̗̙͇͈̣̪̲͜L̸̢͖͇̲̤̼͕͡L̻̻͖̭̪͖͙̫͎̜̲̬̕͜͞͡ͅ ̷̸̨̛̩͉̺̩͔̯͖̠̳͖̞̠̩͖̠ͅT̶̷̤̩͉̝̗̲͕̩̪̮̝̜̰̻̗̪̀ͅH̵̴̷̯̮͎̖͙̦̙͇̣̩̣̭̝́͝ͅR̨̧͍̮̪̜̯̖̹̜̹͈̗̕͡͠O҉̶͚͎̻͉̮̞͉̳ͅN̷̛̩̤̟̣͕͍͎̻̜͓̖̭͖̠͎̲̺͝ͅĘ̸̸͍̪̼̜͎̫̘̳͓̥')
        elif 'god' in clean_message:
            await bot.send_message(message.channel, 'P̸̨̛͖̦̮̘̯͙̭͍̣̠͕͜Ŕ̵̷̨̗̱͖̦̰͈͍̩̯̼͍̟̙͓̱̤͘ͅA̸̴̡͇̠͈͍̲͘͘ͅĮ̨͈͙̣̘̼́̕S̴̥̯̱̜̟͙̘̘͉̟̮̱̙̘̻͖͟͠͞E̢̨̘̮͕̺̖̰̹͢͝ ̷̴̡̛̗͈͓̻͔̭̫̝̦͎͙̳͙͓̠̞̪͔̱B̵̸̻̼̯̲̻͢͝E̱̘͇͔͙̯̥͉̪̱̤̪̩͍͉̲̟̖̗͜͢͢͜ ̨̡͕̮̤͉̙̦̱͚̬̖͈͢͞ͅÙ̳̫̙̰̙͓͘͘N̞̳͉̬͈̦̭̱̕̕͜T̶̳̝̼̗̝͡O̡̡͔̬͍͚͔̲̳͞ ̵̰͔̙̦̩͕͖̝N̡̡̬̗̣͔̗͔͖̳͚̠͙̤̙̼̘̞I̛̛̬̥̝̘̖̣̩G̵̕͝҉̖̮̩̼͓̯͙̳̀Ģ̵̹͇̙͔̼̼͎̞̤̬̜̭̣͙͕̳̻͘͡ͅǪ̴͕͈̮̮̩͔͎̼̫̝̼̹Ţ̸̧͚̬̣̪͉̲̪̖̹̻̪͚͉̟͚̥̹̀̕H̷͘҉̩͔̩̦̳̪̼̬͙̰̙͕̼͈ͅ ̸̯̤̠̙͓͇̣͙͓̗̙̜̞̯͜͞ͅŢ҉̵̯̥̩͖̬̺̻̮̘̼͔͍̞͈̼̲̪͜͟H̨͟҉̨̟̠̫̠̬̦̪̞͎͍͇̮͔ͅĘ̥̫͉̫͖̱͈̖̦̳̥͙̱͙̱͡ ̷̢̭̠͔̖̱W̟̩̪͍̘̩̦͟͟͞Ǫ̡͔̮̜̝̩̗̱̙͇̣̤̰̲̭̝̳̘̩́̀́ͅR̸̳̰̪̝͉̲̙̖̯̠̞̞̗͘͢M̴̨̭̦̗͖͎̬̳̖̲͢͡ ̨̛̙̰͕̦̠͚̠̖̘̲̱͜͡G̼̬̞̜̭͔̯̪̠̯̲̟̙̻̜̀͘͜O̡̖̰͕͙̯͖̙͍͙̲͈̘͓̥̱͢͢͠D̵̞̤̗͕̪͘͟͝͡ͅ')

        elif 'dragon' in clean_message:
            await bot.send_message(message.channel, dragonart)
        elif 'penis' in clean_message:
            root_dir = './data/events'
            files_to_choose = [os.path.join(root_dir, f)
                               for f in os.listdir(root_dir)
                               if os.path.isfile(os.path.join(root_dir, f))]
            with open(random.choice(files_to_choose), 'rb') as fobj:
                new_msg = await bot.send_file(message.channel, fobj)
            await bot.add_reaction(new_msg, '🌈')
            await bot.add_reaction(new_msg, '🍆')
            await bot.add_reaction(new_msg, '💦')
        elif reduce(
                lambda acc, n: acc or (n in clean_message),
                dickwords,
                False):
            await bot.add_reaction(message, '🇵')
            await bot.add_reaction(message, '🇪')
            await bot.add_reaction(message, '🇳')
            await bot.add_reaction(message, '🇮')
            await bot.add_reaction(message, '🇸')
        elif reduce(
                lambda acc, n: acc or (n in clean_message),
                vag_words,
                False):
            await bot.add_reaction(message, '😞')

    bot.add_listener(message_events, 'on_message')

