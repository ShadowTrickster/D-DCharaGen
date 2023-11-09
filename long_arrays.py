import random
import arrays as a

bandit = f"was born in the streets, fighting for {a.pronoun} and {a.pronoun}'s sister's life. A fight {a.pronoun} sadly lost."
priest = f"was aclaimed by the church of the sun but realized a dark secret, so dark that {a.pronoun} faith completly banished."
shaman = f"was living in the woods when a mad scientist decided to try chemicals in the habitants of it, resulting decades of agony."
murderer = f"was never captured by authorities for the endless masacre that took place in {a.city}, but everyone knows {a.pronoun} was the one responsible for it."
experiment = f"was an experiment made to satisfy weapon demands in {a.city}, now running free but, is {a.pronoun} really free?"
tragedy = random.choice([bandit, priest, shaman, murderer, experiment])

hair_l = random.choice(["Long", "short"])
hair_c = random.choice(["black", "white", "blonde"])
body = random.choice(["heavy", "slim"])
eyes_c = random.choice(["brown","blue","gray"])
eyes_s = random.choice(["calming", "piercing"])
figure = random.choice(["imponent", "righteous", "calming"])
desc = f"{figure} figure, with {hair_l} {hair_c} hair and {eyes_c} {eyes_s} eyes"