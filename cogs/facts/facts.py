import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import aiohttp
import html
import random

class Insult:
    """Insult Cog"""
    def __init__(self, bot):
        self.bot = bot
        self.bearfacts = bearfacts

    @commands.command(pass_context=True, no_pm=True)
    async def fact(self, ctx, user : discord.Member=None):
        """gimme a fact"""
        await self.bot.say(randchoice(randchoice([self.bearfacts, self.snekfacts])))


def setup(bot):
    n = Insult(bot)
    bot.add_cog(n)

snekfacts = [
"Snakes are carnivores (meat eaters).",
"Snakes don't have eyelids.",
"Snakes can't bite food so have to swallow it whole.",
"Snakes have flexible jaws which allow them to eat prey bigger than their head!",
"Snakes are found on every continent of the world except Antarctica.",
"Snakes have internal ears but not external ones.",
"Snakes used in snake charming performances respond to movement, not sound.",
"There are around 3000 different species of snake.",
"Snakes have a unique anatomy which allows them to swallow and digest large prey.",
"Snakes are covered in scales.",
"Snakeskin is smooth and dry.",
"Snakes shed their skin a number of times a year in a process that usually lasts a few days.",
"Some species of snake, such as cobras and black mambas, use venom to hunt and kill their prey. Read more venomous snake facts.",
"Snakes smell with their tongue.",
"Pythons kill their prey by tightly wrapping around it and suffocating it in a process called constriction.",
"Some sea snakes can breathe partially through their skin, allowing for longer dives underwater.",
"Anacondas are large, non-venomous snakes found in South America that can reach over 5 m (16 ft) in length.",
"Python reticulates can grow over 8.7 m (28 ft) in length and are considered the longest snakes in the world.",
"Snake Venom evolved from saliva, which means that it all started with a snake whose mouth was sliiiightly more gross than usual.",
"The worlds longest snake is found in brazil, peru, and chile. It is believed to be over 60 years old.",
"If you laid all the bones in a snake end-to-end, you would have a snake.",
"Biologically speaking, what we call a 'snake' is actually a human digestive tract which has escaped from its host.",
"Some snakes survive for up to two years without a meal.",
"There's an Island in Brazil where civilians are forbidden to go: it has up to 5 snakes per square meter.",
"Snakes kill 100,000 people every year.",
"Snakes can have two heads and fight each other for food.",
"The top ten deadliest snakes can be found in Australia.",
"More people are killed each year by bees than snakes.",
"The boomslang snake's venom causes you to bleed from all holes of your body.",
"Snakes can open their mouth up to 150 degrees.",
"There are no terrestrial (land) snakes in New Zealand.",
"The mortality rate of a Black Mamba snake bite is almost 100%.",
"Powerful acids in snakes' stomachs mean they will explode if given Alka-Seltzer.",
"The Titanoboa lived 60 million years ago and is the largest, longest, and heaviest snake ever discovered.",
"Snakes used in snake charming performances respond to movement, not sound.",
"One drop of the Beaked Sea Snake venom can kill 3 adult men.",
"Snakes have flexible jaws which allow them to eat prey bigger than their head.",
"Snakes don't have eyelids.",
"Snakes use their tongues to smell.",
"51% of Americans fear snakes, most than any other thing in the world.",
"Snakes are unable to close their eyes. They can't blink and they must sleep with their eyes open.",
"There has never been snakes in Ireland because being cold-blooded, snake couldn't survive the frozen ground during the ice age in the past.",
"There are more than 3,000 species of snakes in the world and there is at least one type of snake on every continent except Antarctica.",
"While the snake has a bad rap as a pest, snakes can often be quite helpful and even a fun pet.",
"With so many different species, there are snakes of many different sizes.",
"The world's smallest snake, according to National Geographic, is the thread snake, which grows to only about 3.9 inches (10 centimeters) long. It looks much like an earthworm.",
"The largest snake, the reticulated python, can grow to a whopping 30 feet (9 meters).",
"The largest snake fossil ever discovered is called the Titanoboa. This creature lived 60 million years ago and would have been 50 feet (15 meters) long.",
"It is a common misconception that snakes build nests for their eggs. Only one species of snake, the king cobra, will build a nest for its young.",
"Not all snakes lay eggs, either. About 70 percent of snakes lay eggs. These types of snakes are called oviparous.",
"The other 30 percent give birth to live young, much like mammals.",
"This is because some climates are too cold for eggs to develop and hatch, so snakes living in colder climates do not lay eggs.",
"Snakes are carnivores. This means that they only eat meat.",
"Snakes are often seen as pests, but they actually can help keep pests at bay by eating rodents.",
"Many people think that all snakes kill their prey by biting it and injecting the prey with poison. This isn't true.",
"Cobras, vipers and other related species are the only snakes that use venom to hunt.",
"Most snakes simply swallow their prey whole.",
"Large snakes, such as the python, will strangle their prey to death and then swallow it whole.",
"Snakes can eat other animals 75 to 100 percent bigger than their own size, according to National Geographic.",
"They have been known to eat animals such as crocodiles and cows.",
"To fit the large prey into their mouth, the snake's jaw will unhinge.",
"Once the animal is inside, the snake's body releases enzymes to break the food down into useable energy.",
"Snakes don't need to eat as often as other animals because they have a very slow metabolism rate.",
"King cobras, for example, can live for months without food.",
"Sometimes, though, eating a live animal can result in disaster. Snakes have been known to explode after eating a living animal, though it is not known why.",
"Snakes live in almost every corner of the world.",
"They are found in forests, deserts, swamps and grasslands.",
"Many call underground burrows or the spaces under rocks home.",
"Some snakes, like the cottonmouth water moccasin of North America live in water part of the time.",
"Though they are found all over the world, snakes do not, however, like the cold. This is because they are cold blooded or ectothermic.",
"If it is cold outside, then the snake will be cold, too, since their bodies do not use energy to create heat to warm them.",
"When it is cold, many snakes hibernate in tunnels underground. Others seek warmer areas, such as inside humans' homes.",
"Kingdom: Animalia",
"Subkingdom: Bilateria",
"Infrakingdom: Deuterostomia",
"Phylum: Chordata",
"Subphylum: Vertebrata",
"Infraphylum: Gnathostomata",
"Superclass: Tetrapoda",
"Class: Reptilia",
"Order: Squamata",
"Suborder: Serpentes",
"Infraorders: Scolecophidia (blind snakes) & Alethinophidia (all others)",
"Families: 3 in Scolecophidia; 15 in Alethinophidia",
"Subfamilies: 9 in Alethinophidia",
"Genera: 15 in Scolecophidia ; 316 in Alethinophidia",
"Species: 305 in Scolecophidia; 2,618 in Alethinophidia",
"Black mamba — Dendroaspis polylepis",
"Coral snakes — 6 genera & 81 species, such as Arizona coral snake (Micruroides euryxanthus), Eastern or common coral snake (Micrurus fulvius) and Texas coral snake (Micrurus tener)",
"Corn snake — Pantherophis guttatus",
"Cobras — 28 to 270 species, depending on definition, such as King Cobra (Ophiophagus hannah) and Indian cobra (Naja naja)",
"Water moccasin (Cottonmouth) — Agkistrodon piscivorus",
"Garter snakes — 28 species, such as common garter snake (Thamnophis sirtalis), San Francisco garter snake (Thamnosis sirtalis tetrataenia) and Western ribbon snake (Thamnophis proximus)",
"Rattlesnakes — 32 species, such as Timber rattler (Crotalus horridus), Eastern diamondback (Crotalus adamanteus) and Western diamondback (Crotalus atrox)",
"Corn Snake: These corn snakes are able to angle their scales outward to make them better at catching and digging in to the bark's rough surface. This scale angling created twice as much friction against the bark (compared with the scales remaining flat), pushing the snakes up and letting the snakes sit in trees for an extended amount of time.",
"The rarest and most endangered snake is the St. Lucia racer. It is believed that there are 18 to 100 of these snakes left in existence. Other snakes, such as the Amami Takachiho and the Adelophis copei are considered vulnerable by the International Union for Conservation of Nature and Natural Resources since their populations are decreasing.",
"Snakes don't smell with their noses like humans. They have a forked or split tongue that they use to smell and taste chemical compositions in the air.",
"Snakes don't have eyelids or ears, either, and their eyes don't move. To hear they feel vibrations through the ground.",
"Humans' skin flakes off a little at a time, but snakes shed their entire skin nearly three times a year. This is called molting.",
"Snakes aren't slimy. Their scales are smooth and dry. Corn snakes use their scales as climbing equipment. They can angle the scales so that it digs into bark, allowing them to climb trees.",
"The paradise tree-snake of Southeast Asia can fly. It swings its body through the air and then flattens into a C-shape to catch the airflow. If it flips its body back and forth it can change directions as it falls.",
"There are several ways to tell if a snake is poisonous. For example, if its pupil is shaped like a diamond, then the snake is poisonous.",
"Snakes that are non-poisonous will have round pupils. Color is another good clue.",
"This rhyme helps people tell the difference between coral snakes, which is poisonous, and scarlet king snakes, which is not poisonous: If red touches yellow, it will kill a fellow. If red touches black, it's a friend of Jack.",
"Snakes are vertebrates - that means they have a skeleton, which in the case of snakes is mostly a skull and lots and lots of rib bones.",
"They do not have ears as most of us think of an ear. They do have a sensory ear bone, called the columella, which detects vibrations.",
"Snakes use their tongues to detect smells to find food or stay away from enemies. Their eyes do not move inside their head, and they do not have common eyelids.",
"Some types of snakes have a special pit located near their eyes that allows them to detect small changes in temperature. This allows them to be aware of the heat given off by the bodies of rodents or other animals they might want to eat.",
"A snake's skin is made of a variety of sizes of scales. The scales near the head are small while the scales on the underside of their body are thick and protect their bodies from the ground.",
"A snake continues to grow throughout its life. They periodically shed their skin as part of this growing process.",
"Snakes live on every continent of the world except Antarctica. There are even species which swim in the ocean.",
"Snakes are carnivorous. That means that they eat other animals.",
"Snakes do not have the right kind of teeth to chew their food so they must eat their catch whole.",
"Their jaw is structured in such a way that it allows the mouth to open wider than their own body in order to swallow their prey whole.",
"Once swallowed, the muscles of their body and their hook-shaped teeth help push the food toward the stomach.",
"Their food is then digested over a long period of time — depending upon how warm the snake is. The warmer their bodies, the faster they digest their food.",
"But it generally takes 3–5 days for food to be digested.",
"Very large snakes such as the anaconda from South America eat rather large prey, so their digestion can take weeks.",
"Poisonous or venomous snakes inject poison or venom into their prey. This starts the digestive process even before the snake swallows that food.",
"Snakes tend to eat rats, birds and their eggs, mice, chipmunks, frogs, gophers, and other small rodents.",
"Some species will even consume insects or earthworms.",
"Very large snakes will even eat deer, pigs, monkeys and other large prey.",
"The Kingsnake is known for the fact that it will eat other snakes, including venomous snakes like rattlesnakes.",
"Amphibians and reptiles are cold blooded. Their body temperatures match that of their surroundings. Because of this, cold blooded animals can not survive well in extreme hot or cold. To warm themselves they will move to a sunny rock or roadside. To cool their bodies they will seek shade or sometimes even dig a hole in the ground.",
"The bodies of snakes have no feet, flippers or legs to propel them along. They must use the action of their scales and muscles to scoot their bodies across the ground. The scales on the underside of their bodies are specialized for this purpose like the tread on a tire.",
"Different species of snakes use one of the four manners of movement: concertina, serpentine, sidewinding, and caterpillar.",
"Ok, so not like a bird — with wings — but some snakes do hang from branches and swing themselves into the air. Then by flattening their ribcage and making a side to side motion, they keep their bodies in the air long enough to glide for about 109 yards before crashing to the ground or into another tree.",
"The five different flying snakes are all poisonous and live in the tropical rainforests of Sri Lanka and Southeast Asia.",
"No snakes can fly upwards or take off from the ground.",
"Many species of snakes can move about the water. Some just slide on the surface, while others can actually swim underwater.",
"A few species even live the majority of their lives in the ocean — these are known as sea snakes. They do come to the surface to breathe air, but can often stay down for upwards of an hour.",
"Sea snakes dine on fish and eels.",
"The type of teeth a snake has is dependent upon how the species catches food.",
"All non-poisonous snakes have teeth on the upper jaw and the lower jaw.",
"A snake can often grow more teeth as needed because teeth are sometimes lost while feeding.",
"The teeth are hook-shaped and angle toward the throat.",
"Poisonous snakes have either grooved or hollow fangs. The poison, which comes from glands located under each eye, flows down the groove or through the hollow portion of the fangs and is injected into the prey.",
"Female snakes produce young about twice per year. In some species babies are born alive. Other species lay eggs.",
"In a strange combination of the two, some snakes have eggs that stay in their bodies until the eggs hatch and then the babies are born.",
"Snakes can have anywhere from one to 150 baby snakes at a time.",
"Snake eggs are not hard like a chicken egg, but are leather-like and can be torn open by the baby snake from the inside with a special “egg tooth” that the snake will lose soon after hatching.",
"Snakes do not take care of their offspring, but a few species will protect the eggs and then the new babies for a very short time after they have hatched. Baby snakes are then left to fend for themselves.",
"Some snakes have a camouflage coloring which hides them from predators. Blending into the surroundings also keeps their potential prey from spotting them.",
"Some snakes have coloring which mimics another snake for the purpose of confusing predators. For example, the poisonous Coral snake looks similar to the non-poisonous Scarlet Kingsnake. Both snakes live in North America.",
"Snakes that live in cold climates plan ahead for the winter by eating extra food so that they can hibernate during the coldest season. Their bodies are not really asleep, but in a special condition that makes them appear as if they are dead to people who are not aware.",
"Idaho is home to a number of snakes, both poisonous and nonpoisonous. There are 11 common species of snake found in the state: Rubber Boa, Racer, Ringneck Snake, Night Snake, Striped Whipsnake, Gopher Snake, Longnose Snake, Ground Snake, Common Garter Snake, Western Terrestrial Garter.",
"There are 116 species of snakes in the United States. Only 19 of these species are poisonous. The bite of these creatures can be very dangerous. A person who is bitten by one of these should seek medical attention quickly. Only the rattlesnake is typically found in Idaho.",
"Here are the poisonous snake species found in the U.S.: Copperhead, Cottonmouth water moccasin, 2 kinds of coral snakes, 15 kinds of rattlesnakes.",
"The Western Diamondback Rattlesnake is one of the most feared snakes in North America. There are a number of different rattlesnake species in North and South America. Their coloring is distinctive and they are well known for the diamond-shaped design along their back. They can grow to be from 3 to even more than 5 feet long. They live in a variety of environments including forests, deserts and grasslands. They prefer to be in rocky areas where they can warm themselves against the heat of the rocks or cool themselves in the shade between the rocks.",
"Rattlesnakes are pit vipers. That means that they have a special pit between their eyes that senses temperature — useful for hunting prey. Their diet is mostly small rodents, but they will also dine on frogs, fish and other small creatures. They are very poisonous, so it is wise to stay away should you ever come across one.",
"The best thing you can do is stay away from rocks and to keep your ears tuned to the noise of a rattling sound. And be aware!! Baby rattlesnakes can not rattle until they have shed their skin at least once. A baby rattler is also likely to inject more venom when they bite than an adult will, making a baby rattlesnake's bite more dangerous.",
"The cobra is well known for its hood that it puffs out when in a defensive stance. They are the world's longest venomous snake and are found in the Philippine islands, southern Asia and Africa. The cobra's bite is deadly, but some species of cobra also spit venom at their victim. Snake charmers use cobras for their demonstrations because the cobra is so showy.",
"Boa constrictors belong to the boa and python family. Both species squeeze their prey in order to prevent the animal from taking in air, often killing their victim before eating it whole. They are nonpoisonous. Boas live all over the world while pythons are indigenous to Asia and Africa. Most of them live in caves or other cool places, but have been known to find themselves in cities as people invade their space by building homes and farms.",
"The anaconda has been the topic of many movies which would lead people to believe that they are very aggressive and attack people. But the truth is that they like to be alone and are often difficult for scientists to study because they are so hard to locate. They live in or near the waters of South America and eat amphibians and birds.",
"A fear of snakes can be healthy since it helps us be aware and cautious when we're passing through territory that might have snakes dangerous to us. But we also tend to invent “facts” that aren't true about things we fear."
]

bearfacts = [
"Bears are large, strong omnivores.",
"Omnivore is a fancy word for animals that eat both meat and plants.",
"They belong to the mammal class.",
"Because they are covered in hair, they have a spine, they’re warm-blooded and they feed milk to their babies once they are born.",
"Many people often think of bears as big, ferocious creatures that are brown, black or white.",
"They are definitely big, and yes, they are very strong.",
"They can be scary, but most will only become aggressive when threatened or when their babies are threatened and even then many species of bear won’t attack.",
"Bears are solitary and quite docile animals that have been given a bad reputation.",
"They are smart, shy and are great at hiding when they need to.",
"There is very little information on some bears because researchers have a hard time finding them!",
"Bears come in many different colors, shape, and sizes and they live all over the world, except Antarctica and Australia.",
"Their habitats range from the snowy northern tundra to dense rainforests and high mountains.",
"Most species of bears live to around 25 years of age.",
"There are eight different species of bears.",
"They are Asiatic, Black, Brown, Polar, Panda, Sloth, Spectacled and Sun.",
"Some of these species has a few sub-species.",
"For example, the sub-species of the brown bear include the Grizzly bear and the Kodiak bear.",
"One of the first things you might think about when you talk bears is hibernation.",
"Bear hibernation is different than most hibernating animals.",
"True hibernation (like we see in ground squirrels) involves a drastic drop in body temperature but the hibernating animal will awaken occasionally to go to the bathroom and have a bite to eat before resuming hibernation.",
"Since food is scarce in the winter bears figure that if you can't eat you might as well sleep.",
"Bears that live in colder northern regions sleep in their dens right through the winter.",
"Once spring arrives, the bear (and possibly some cubs) will emerge from the den with a big appetite.",
"It is important to note that not all species of bear will hibernate.",
"Bears like the Asiatic Bear live in warmer climates where food is readily available all year long and there is not need to hibernate.",
"Bears are omnivores just like people.",
"They will hunt animals such as baby deer, caribou, and elk but they are also scavengers, which means that they like leftovers and are happy to eat carrion.",
"Carrion is the decaying flesh of an animal that was killed and left behind by other predators or an animal which died of natural causes.",
"For bears that hibernate, large animals that died during the winter and are preserved by the icy cold, become a very important food source.",
"Bears are very hungry after a long winter sleep and fast food is a blessing for them.",
"Nursing mothers will also need to get their strength up with a nutritious meal if they want to protect their cubs.",
"As scavengers, bears will go through garbage cans and are often spotted at garbage dumps and campsites.",
"Insects, nuts, berries, sap, branches and roots are a big part of a bear’s diet.",
"Bears that live near rivers can catch salmon, and they tend to grow much larger than other species of bear because of this special, yummy treat!",
"Polar bears will find a seal's breathing hole in the ice and wait patiently for a seal to poke its head out for a breath.",
"Sometimes the only part of a seal that the polar bear will eat is the fat which helps them to fatten up for hibernation.",
"A panda bear's diet mainly consists of bamboo.",
"They can eat about 13.5 kg (30 lbs.) a day! That’s a lot!",
"They may eat meat, if given the chance.",
"Unfortunately for the giant panda, bamboo forests are being destroyed by humans who clear the forests to make room for homes, farms and shopping malls.",
"The pandas in the area being developed will often die of starvation.",
"As bears get ready for hibernation, they need to bulk up, and will eat double the amount of food that they normally need.",
"If a female bear isn’t fat enough, she will not be able to give birth to any cubs.",
"Baby bears rely on their mother’s milk for their first year of life and even longer for some species.",
"A bear's senses are very important to its survival.",
"They have great senses of smell, sight and hearing.",
"A bear can smell food, cubs, a mate or danger from miles away.",
"They also rely on other bears' sense of smell when they mark their territory with urine and droppings.",
"Bears have terrific eyesight, too.",
"It helps them to identify ripe fruit and nuts.",
"They use their keen hearing to notice and track smaller animals (food) scurrying around under leaves and brush.",
"Female bears are ready to mate between the ages of 3 and 8 years, but that will depend on their health and their weight.",
"A female bear that is underweight cannot give birth.",
"Bears, who usually prefer to live alone, get together in spring to find a mate.",
"Finding a mate can be quite tricky for the male bear.",
"Throughout the year, the male bear can be a bit of a bully.",
"Since they are larger than females, they have been known to kill females for food.",
"Of course the female might be nervous and untrusting of the large male bear!  The male follows the female at a distance for quite awhile until she feels safe and allows him to get closer.",
"Once they’ve mated the male leaves and may never see her, or the cubs, again.",
"Three to nine months later, depending on the species of bear, cubs are born.",
"For bears that live in colder climates, the cubs are born during hibernation.",
"The mother bear nurses her babies and keeps them warm as they grow and mature.",
"Pandas, Asiatic and Brown bears have a cool internal thing called “delayed implantation”  which allows the female to hold off fertilization of the egg until a later date and time the birth of her cubs to happen during hibernation where they will be born in a safe and warm place.",
"Bear cubs are born helpless.",
"They can’t see or hear and they have no teeth.",
"They are small…like a kitten, weighing around 454 g (1 pound) or less.",
"Mothers will carry their babies by their heads, except for the Sloth bear.",
"She will carry them piggyback for the first few months while she travels or hunts.",
"Bears that live in warm or tropical climates and do not need to hibernate can mate at any time.",
"By the time hibernation has ended the cubs are bigger and full of energy.",
"Bear cubs are really playful.",
"Play fighting is very important for young bears because it teaches them to protect themselves and helps them get stronger.",
"But if things get too rough, mama bear will discipline them by swatting them with her paw!  Ouch!",
"Being a cub is not all fun and games.",
"They are expected to follow their mother and learn how to find food or hunt.",
"It’s kind of like school and will help them to survive on their own.",
"Cubs usually stay with their mothers until they are between 1½ and two years of age.",
"Their mother will send them off on their own before she will mate again.",
"Bear siblings that have left their mothers may stay together for another year for protection.",
"Bears walk flat footed like humans do rather than on their toes like most animals.",
"This allows them to walk upright like people.",
"From far away, this looks really cool, but close up it might be a little frightening to see a really big bear standing in front of you!  This is definitely a good way to scare off danger!  ",
"Their feet are wide and flat with long, sharp claws.",
"The claws on their front paws are longer than on the back, which is useful for climbing trees.",
"Two species that have special feet are the polar bear and the giant panda.",
"The polar bear has partially webbed toes for swimming and walking on snow (kind of like snowshoes!) as well as furry bottoms to keep its feet warm on the ice.",
"Giant pandas do not have a heel pad so they walk more on their toes.",
"Have you ever noticed that bears look pigeon-toed?  This could be to help them hold onto trees that they are climbing and make it easier for them to put food in their mouths.",
"Would it surprise you to know that an adult bear has almost no predators?  Bears are large and can be quite intimidating so they don’t have many enemies.",
"Their biggest enemies are humans and each other.",
"It's the cubs and the smaller females that have to watch out.",
"Other animals, including older male bears, will consider attacking a little cub if its mother is out of site.",
"Female bears are sometimes killed by larger male bears for food, which is why the female can be quite nervous during mating season.",
"When defending themselves bears make themselves look bigger by fluffing up their fur and standing on their hind legs.",
"When angry they will growl, pound their paws on the ground and charge towards whatever is bothering them.",
"They may not attack…but they probably wouldn’t have to after a show like that.",
"Mother bears can be very protective of their cubs and will attack if it becomes necessary.",
"The main predator that all species of bears have to worry about is humans.",
"In many parts of the world, bears are hunted for certain organs, such as their gall bladder, for use in traditional medicines.",
"Some are hunted for their beautiful fur and some are hunted for sport.",
"Bears are extraordinarily intelligent animals. They have far superior navigation skills to humans; excellent memories; large brain to body ratio; and use tools in various contexts from play to hunting.",
"Bears care deeply about family members. They will risk their lives and even fight to the death in order to save a cub or sibling from danger. ",
"Bears have excellent senses of smell, sight and hearing. They can smell food, cubs, a mate or predators from miles away. Their great eyesight allows them to detect when fruits are ripe.",
"Some species of Asiatic bear build nests in the trees. They can use these for hiding, eating and even sleeping.",
"Polar bears are excellent swimmers. They can swim for more than 60 miles without having a break. They also have huge appetites and can eat up to 10% of their own body weight in under an hour.",
"Bears were often honoured in the cultures of many early civilisations. They were seen as a symbol of power, strength and love.",
"Vikings and the Celts have many legends about the strength, protectiveness and prowess of bears.",
"The bear is a common national personification for Russia (and the former USSR) and Germany. The brown bear is Finland’s national animal. ",
"Grizzly bears (Ursus arctos horribilis) have concave faces, a distinctive hump on their shoulders, and long claws about two to four inches long. Both the hump and the claws are traits associated with a grizzly bear’s exceptional digging ability.",
"Grizzlies are often dark brown, but can vary from very light cream to black. The long guard hairs on their backs and shoulders frequently have white tips and give the bears a 'grizzled' appearance, hence the name 'grizzly.'",
"The correct scientific name for the species is “brown bear,” but only coastal bears in Alaska and Canada are referred to as such, while inland bears and those found in the lower 48 states are called grizzly bears.",
"Grizzly bears are omnivores, and their diet can vary widely. They may eat seeds, berries, roots, grasses, fungi, deer, elk, fish, dead animals and insects. In the late summer and early fall, grizzlies enter hyperphagia, a period of 2-4 months when they intensify their calorie intake to put on weight for winter denning. During this time period they can gain more than three pounds a day!",
"Historically, there were around 50,000 grizzly bears in North America. Today, there are an estimated 1,800 grizzly bears remaining in five populations in the lower 48 states. Most of these bears are located in the Northern Continental Divide Population (including Glacier National Park) and the Yellowstone Population. Alaska is home to a healthy grizzly (sometimes called brown bear) population. ",
"Grizzly bears are found many different habitats, from dense forests to subalpine meadows, open plains and arctic tundra. In North America, grizzly bears are found in western Canada, Alaska, Wyoming, Montana, Idaho and a potentially a small population in Washington. Historically, they could be found from Alaska to Mexico and from California to Ohio.",
"Grizzly bears have a better sense of smell than a hound dog and can detect food from miles away.",
"Grizzly bears use “rub trees.” These are trees where they scratch their backs, leaving scent and hair. Biologists can use these trees to collect DNA from many bears living in the area.",
"Grizzly bears are normally solitary animals. However, they are not very territorial and they may be seen feeding together where food is abundant, such as at salmon streams and whitebark pine sites. Females will rear their cubs for 2-3 years.",
"When a female grizzly bear leaves her mother, they often set up their home range quite close to their mother’s home range. Males will typically range further, but may also remain close by.",
"Grizzly bears need to eat a lot in the summer and fall in order to build up sufficient fat reserves to survive the winter denning period. This is particularly true for pregnant females, who must have sufficient fat reserves to give birth to approximately one-pound cubs in January or February and then nurse them to about 20 pounds before emerging from the den in April or May.",
"Grizzly bears are one of the slowest reproducing land mammals. Females do not typically reproduce until they are four or five years old. ",
"Grizzly bears mate between May and July, but the female’s body delays implantation of their eggs in the uterus until October or November. If the female has not gained enough fat over the summer to survive and raise cubs, implantation may not occur. A grizzly’s ability to garner enough quality calories through the summer is not just crucial for her survival, but also for her reproductive ability.",
"Mother bears rear cubs for two to three years. Males do not help raise the cubs. In fact, males can be a danger to the cubs, so females often avoid male grizzly bears while rearing their cubs.",
"Mating Season: Early May through mid-July",
"Gestation: Anywhere from 180-270 days, including delayed implantation.",
"Litter Size: 1-4 cubs, but average is 2-3",
"Bears can eat up to 15% of their body weight in one day.",
"There are 8 species of bear in the world right now.",
"Bears gain up to 200 pounds between spring and fall.",
"Bears reach an age of 30 years or more, if they're lucky.",
"Most bears live north of the equator. There are no bears in Africa, Australia or Antarctica. ",
"Kodiak bears are the largest, weighing in at around 1,700 pounds (770 kilos) and reaching 10 to 12 feet (3.7 meters) in length. The sun bear of the Malay Peninsula, sometimes called the Malay bear, is the smallest type of bear. They weigh between 60 and 100 pounds are about three feet long. ",
"Bears usually have poor eyesight and hearing. However, they have a very keen sense of smell, which aids them in hunting. ",
"A bear is well protected from bee stings by its thick fur. The only unprotected part of a bear's body is its nose. Aside from honey, bears also eat fish, small mammals, fruit, roots, seeds, insects and carrion. ",
"Sun bears are different because of their short fur, which is not shaggy like other bears. They also have a white or yellow marking on their chest which people believe looks like a rising sun, which is how they got their name.",
"The American black bear is the most common bear species in North America. Although some male black bears can weigh up to 900 pounds, most black bears weigh around 300 pounds. They live in the mountainous or heavily wooded areas of southern North America, the Appalachians, the Adirondacks, the Great Lakes region, the Rocky Mountains and Canada. ",
"Black bear cubs usually weigh less than a pound when they are born in the winter. They are blind, furless and for about 40 days do nothing but eat and sleep, curled up with their mother in the den. However, by the following fall, the bears weigh about 40 pounds. ",
"The glacier bear is a rare species of the American black bear. The glacier bear has a mix of gray and black hairs, making it appear a blue color. In fact, despite their name, black bears come in many different shades and colors. Kermode black bears are often a creamy or sometimes pure white and the cinnamon black bears are a rusty brown color. ",
"A grizzly bear has a brown layer of under-fur, which lies close to the skin. It also has outer hairs which are white or silver-tipped. The mix of these hairs, giving a streaked gray 'grizzled' appearance, is how the bear got its name. Grizzly bears can be quite dangerous, especially when injured, and have also attacked humans unprovoked. ",
"Grizzly bears may eat 80 to 90 pounds of food each day in the summer and early fall. This amount increases as the bears prepare for the winter, building a layer of fat that will help them to keep warm and survive. ",
"Grizzly bears live, hunt and feed alone. They don't communicate much, but it is thought that they use their claws to scratch bark of trees, leaving behind their scent so that other bears know the grizzly is around and will keep away. ",
"Grizzly bears come together in the summer when the streams fill with salmon, an important part of a grizzly's diet. ",
"Kodiak bears love salmon and are excellent fishers. Conveniently, they live on Kodiak Island, off the coast of Alaska, which is a spawning ground for salmon. A mother Kodiak bear can catch 15 salmon in an hour to feed herself and her cubs. ",
"Polar bears have slip-proof bristles on their feet. ",
"Polar bears do not live at either of the poles. Rather, they are found in the Arctic region around the North Pole. ",
"Polar bears are better at swimming than any other bear. Than can swim at speeds of three to six miles an hour, thanks to their large forepaws that act like paddles and webbing between their toes. They have long necks, which helps them keep their head above water. ",
"Polar bears have a thick layer of fat beneath their skin for insulation and their fur is made up of an overcoat and an undercoat. The fine, white hairs of the undercoat provide warmth, while the long guard hairs of the overcoat shed water easily and mat together to trap heat from the sun inside them. Polar bears have fur on their paws to keep their feet warm and their black skin absorbs heat. ",
"Polar bears love ringed seal. When they spot a seal sitting on an ice floe, they swim up to it with only their head above water and pounce on the seal. They sometimes sit next to a seal's breathing hole in the ice and grab the seal when it comes up for air. ",
"Sloth bears love to eat termites. The roof of a sloth bear's mouth is hollowed out, creating a vacuum effect when the sloth bear sucks up termites. The sloth bear inserts its mouth into a termite pillar and sucks up the insects, creating a sucking noise that is so loud it can be heard 200 yards away! ",
"Spectacled bears climb trees and stay in the tree for three or four days eating its fruit before they move on to the next tree. Orchard farmers find these bears a nuisance, but spectacled bears scatter the seeds of trees and other plants, making them important for forest growth. "
]
