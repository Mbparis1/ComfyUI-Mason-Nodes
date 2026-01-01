"""
Mason's Multi-Character Composition Nodes for ComfyUI
Scene composition with multiple subjects - SD 1.5 optimized
"""


class DualCharacterPose:
    """Positions two characters in relation to each other"""
    
    ARRANGEMENTS = {
        "face_to_face": "two people facing each other, eye contact, close proximity",
        "side_by_side": "two people standing side by side, shoulder to shoulder",
        "behind": "one person behind another, embrace from behind",
        "above_below": "one person above, one below, vertical arrangement",
        "intertwined": "two people intertwined, limbs wrapped around each other",
        "mirror": "two people mirroring each other, symmetrical pose",
    }
    
    DISTANCES = {
        "intimate": "intimate distance, bodies touching, very close",
        "personal": "personal space, arms length, close but not touching",
        "social": "social distance, visible gap between subjects",
        "distant": "far apart, separated by space",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "arrangement": (list(cls.ARRANGEMENTS.keys()),),
                "distance": (list(cls.DISTANCES.keys()),),
                "interaction_type": (["romantic", "confrontational", "friendly", "professional", "passionate"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("dual_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Multi-Character"

    def apply(self, prompt, arrangement, distance, interaction_type):
        parts = [prompt, "two people"]
        parts.append(self.ARRANGEMENTS.get(arrangement, ""))
        parts.append(self.DISTANCES.get(distance, ""))
        
        interaction_map = {
            "romantic": "romantic atmosphere, tender moment, loving",
            "confrontational": "tension between them, confrontational, intense stare",
            "friendly": "friendly interaction, casual, relaxed together",
            "professional": "professional relationship, formal interaction",
            "passionate": "passionate embrace, intense desire, heat between them",
        }
        parts.append(interaction_map.get(interaction_type, ""))
        
        return (", ".join([p for p in parts if p]),)


class GroupSceneComposer:
    """Composes scenes with three or more people"""
    
    FORMATIONS = {
        "triangle": "three people in triangular formation, balanced composition",
        "line": "people standing in a line, horizontal arrangement",
        "circle": "people arranged in a circle, facing center",
        "crowd": "crowd of people, multiple subjects, busy scene",
        "pairs_and_solo": "group with pair and lone figure, varied positions",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "group_size": (["three", "four", "five", "crowd"],),
                "formation": (list(cls.FORMATIONS.keys()),),
                "focus": (["equal", "center_focus", "foreground_focus", "background_group"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("group_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Multi-Character"

    def apply(self, prompt, group_size, formation, focus):
        parts = [prompt]
        
        size_map = {
            "three": "three people, trio",
            "four": "four people, quartet",
            "five": "five people, group of five",
            "crowd": "crowd of people, many subjects, large group",
        }
        parts.append(size_map.get(group_size, ""))
        parts.append(self.FORMATIONS.get(formation, ""))
        
        focus_map = {
            "equal": "all subjects equally visible, balanced focus",
            "center_focus": "center figure in focus, others slightly blurred",
            "foreground_focus": "foreground subject sharp, background people softer",
            "background_group": "main subject foreground, group in background",
        }
        parts.append(focus_map.get(focus, ""))
        
        return (", ".join([p for p in parts if p]),)


class CharacterInteraction:
    """Defines specific interactions between characters"""
    
    INTERACTIONS = {
        "handshake": "shaking hands, formal greeting, hand clasped",
        "embrace": "embracing, hugging, arms wrapped around",
        "kiss": "kissing, lips touching, romantic moment",
        "fight": "fighting, combat, physical altercation",
        "dance": "dancing together, movement, rhythm",
        "conversation": "in conversation, talking, gesturing",
        "carrying": "one carrying another, bridal carry or piggyback",
        "leaning": "leaning on each other, casual closeness, support",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "interaction": (list(cls.INTERACTIONS.keys()),),
                "intensity": (["gentle", "moderate", "intense", "extreme"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("interaction_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Multi-Character"

    def apply(self, prompt, interaction, intensity):
        parts = [prompt]
        parts.append(self.INTERACTIONS.get(interaction, ""))
        
        intensity_map = {
            "gentle": "gentle, soft, tender",
            "moderate": "moderate intensity, natural",
            "intense": "intense, passionate, strong",
            "extreme": "extreme intensity, powerful, overwhelming",
        }
        parts.append(intensity_map.get(intensity, ""))
        
        return (", ".join([p for p in parts if p]),)


class PositionMapper:
    """Maps characters to specific spatial positions"""
    
    HORIZONTAL = {
        "left": "subject on left side of frame",
        "center": "subject in center of frame",
        "right": "subject on right side of frame",
    }
    
    VERTICAL = {
        "top": "subject in upper portion of frame",
        "middle": "subject in middle of frame",
        "bottom": "subject in lower portion of frame",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "character_label": ("STRING", {"default": "character A"}),
                "h_position": (list(cls.HORIZONTAL.keys()),),
                "v_position": (list(cls.VERTICAL.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("positioned_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Multi-Character"

    def apply(self, prompt, character_label, h_position, v_position):
        h = self.HORIZONTAL.get(h_position, "")
        v = self.VERTICAL.get(v_position, "")
        return (f"{prompt}, {character_label} {h}, {v}",)


NODE_CLASS_MAPPINGS = {
    "DualCharacterPose": DualCharacterPose,
    "GroupSceneComposer": GroupSceneComposer,
    "CharacterInteraction": CharacterInteraction,
    "PositionMapper": PositionMapper,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DualCharacterPose": "👥 Dual Character Pose",
    "GroupSceneComposer": "👨‍👩‍👧‍👦 Group Scene Composer",
    "CharacterInteraction": "🤝 Character Interaction",
    "PositionMapper": "📍 Position Mapper",
}
