"""
Mason's Weapon & Prop Nodes for ComfyUI
Weapons, magical items, and props - SD 1.5 optimized
"""


class MeleeWeaponPro:
    """Swords, axes, and melee weapons"""
    
    WEAPONS = {
        "longsword": "elegant longsword, double-edged blade, cruciform hilt, knightly",
        "katana": "Japanese katana, curved blade, samurai sword, razor sharp",
        "battle_axe": "massive battle axe, double-headed, Viking, brutal",
        "dagger": "ornate dagger, short blade, assassin's weapon, concealed",
        "spear": "long spear, pointed tip, polearm, warrior's weapon",
        "mace": "heavy mace, flanged head, crushing weapon, medieval",
        "scythe": "death's scythe, curved blade, grim reaper, ominous",
        "rapier": "elegant rapier, thin blade, dueling sword, nobleman's weapon",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "weapon": (list(cls.WEAPONS.keys()),),
                "material": (["steel", "enchanted", "obsidian", "gold_inlaid", "rusted"],),
                "held_by": (["wielded", "sheathed", "displayed", "dropped"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("weapon_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Props"

    def apply(self, prompt, weapon, material, held_by):
        parts = [prompt]
        parts.append(self.WEAPONS.get(weapon, ""))
        
        material_map = {
            "steel": "polished steel blade, quality metalwork",
            "enchanted": "enchanted weapon, glowing runes, magical aura",
            "obsidian": "obsidian blade, volcanic glass, dark and deadly",
            "gold_inlaid": "gold inlaid details, precious, royal weapon",
            "rusted": "rusted blade, ancient, weathered by time",
        }
        parts.append(material_map.get(material, ""))
        
        held_map = {
            "wielded": "being wielded, in fighting stance, combat ready",
            "sheathed": "sheathed at hip, holstered, ready to draw",
            "displayed": "displayed on wall, trophy, decorative",
            "dropped": "dropped on ground, abandoned, aftermath of battle",
        }
        parts.append(held_map.get(held_by, ""))
        
        return (", ".join([p for p in parts if p]),)


class RangedWeaponPro:
    """Bows, guns, and ranged weapons"""
    
    WEAPONS = {
        "longbow": "English longbow, wooden, tall as archer, medieval",
        "crossbow": "heavy crossbow, mechanical, deadly accurate",
        "compound_bow": "modern compound bow, pulleys, precision, hunting",
        "revolver": "classic revolver, six-shooter, Western, gunslinger",
        "sniper_rifle": "sniper rifle, scope, long-range, precision",
        "flintlock_pistol": "flintlock pistol, pirate weapon, historical",
        "plasma_rifle": "sci-fi plasma rifle, energy weapon, futuristic",
        "throwing_knives": "throwing knives, balanced, assassin tools",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "weapon": (list(cls.WEAPONS.keys()),),
                "state": (["aiming", "holstered", "firing", "loading"],),
                "condition": (["new", "used", "antique", "customized"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ranged_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Props"

    def apply(self, prompt, weapon, state, condition):
        parts = [prompt]
        parts.append(self.WEAPONS.get(weapon, ""))
        
        state_map = {
            "aiming": "aiming weapon, looking down sights, ready to fire",
            "holstered": "weapon holstered, secured, carried",
            "firing": "firing weapon, muzzle flash, action shot",
            "loading": "loading weapon, reloading, preparing",
        }
        parts.append(state_map.get(state, ""))
        
        condition_map = {
            "used": "well-used, worn grip, experienced weapon",
            "antique": "antique weapon, collector's item, historical",
            "customized": "customized weapon, modified, personalized",
        }
        if condition != "new":
            parts.append(condition_map.get(condition, ""))
        
        return (", ".join([p for p in parts if p]),)


class MagicalItemPro:
    """Magical items, artifacts, and enchanted objects"""
    
    ITEMS = {
        "wizard_staff": "wizard's staff, gnarled wood, crystal top, magical focus",
        "crystal_ball": "crystal ball, fortune telling, swirling mists, prophetic",
        "magic_wand": "magic wand, slender, precious wood, spell-casting",
        "enchanted_ring": "enchanted ring, glowing gem, finger ring, powerful",
        "spellbook": "ancient spellbook, leather-bound, glowing pages, arcane",
        "amulet": "protective amulet, pendant, magical protection, artifact",
        "potion_bottle": "potion bottle, glowing liquid, alchemical, mysterious",
        "holy_grail": "holy grail, golden chalice, divine artifact, legendary",
        "orb_of_power": "orb of power, floating sphere, crackling energy, immense power",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "item": (list(cls.ITEMS.keys()),),
                "magic_type": (["arcane", "divine", "dark", "elemental", "ancient"],),
                "activation": (["dormant", "active", "overloading", "awakening"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("item_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Props"

    def apply(self, prompt, item, magic_type, activation):
        parts = [prompt]
        parts.append(self.ITEMS.get(item, ""))
        
        magic_map = {
            "arcane": "arcane magic, mystical energy, wizard's power",
            "divine": "divine magic, holy light, blessed, sacred",
            "dark": "dark magic, corrupted, evil energy, forbidden",
            "elemental": "elemental magic, fire/ice/lightning, natural power",
            "ancient": "ancient magic, primordial, older than time",
        }
        parts.append(magic_map.get(magic_type, ""))
        
        activation_map = {
            "dormant": "dormant power, waiting to be awakened",
            "active": "actively glowing, magic visible, power flowing",
            "overloading": "overloading with power, dangerous, unstable",
            "awakening": "awakening, power building, dramatic moment",
        }
        parts.append(activation_map.get(activation, ""))
        
        return (", ".join([p for p in parts if p]),)


class ShieldArmorPro:
    """Shields, armor pieces, and defensive equipment"""
    
    DEFENSE = {
        "tower_shield": "tall tower shield, full body coverage, knight's defense",
        "round_shield": "round shield, Viking, boss center, painted",
        "buckler": "small buckler, parrying shield, duelist",
        "energy_shield": "energy shield, sci-fi, force field, glowing barrier",
        "magic_barrier": "magic barrier, arcane shield, spell protection",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "defense": (list(cls.DEFENSE.keys()),),
                "material": (["steel", "wood", "enchanted", "energy"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("shield_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Props"

    def apply(self, prompt, defense, material):
        d = self.DEFENSE.get(defense, "")
        m_map = {
            "steel": "steel construction, metal, strong",
            "wood": "wooden shield, leather straps, natural",
            "enchanted": "enchanted, glowing runes, magical protection",
            "energy": "pure energy, glowing, sci-fi tech",
        }
        m = m_map.get(material, "")
        return (f"{prompt}, {d}, {m}",)


NODE_CLASS_MAPPINGS = {
    "MeleeWeaponPro": MeleeWeaponPro,
    "RangedWeaponPro": RangedWeaponPro,
    "MagicalItemPro": MagicalItemPro,
    "ShieldArmorPro": ShieldArmorPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MeleeWeaponPro": "⚔️ Melee Weapon Pro",
    "RangedWeaponPro": "🏹 Ranged Weapon Pro",
    "MagicalItemPro": "🔮 Magical Item Pro",
    "ShieldArmorPro": "🛡️ Shield Armor Pro",
}
