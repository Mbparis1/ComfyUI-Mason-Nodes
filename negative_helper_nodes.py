"""
Mason's Negative Prompt Helper Nodes for ComfyUI
Fix common SD 1.5 issues with targeted negative prompts
"""


class AnatomyFixer:
    """Comprehensive negative prompts for body anatomy issues"""
    
    FOCUS = {
        "full_body": (
            "bad anatomy, wrong anatomy, deformed body, mutated body, "
            "extra limbs, missing limbs, floating limbs, disconnected limbs, "
            "malformed limbs, extra arms, extra legs, fused legs, "
            "too many fingers, extra fingers, missing fingers, fused fingers, "
            "long neck, twisted torso, unnatural proportions, contorted body, "
            "bad proportions, gross proportions, mutated, malformed"
        ),
        "upper_body": (
            "bad anatomy, deformed torso, wrong proportions, extra arms, "
            "missing arms, malformed arms, twisted shoulders, bent spine, "
            "unnatural arm position, fused arms, extra breasts, asymmetric torso"
        ),
        "lower_body": (
            "bad anatomy, deformed legs, extra legs, missing legs, "
            "fused legs, twisted hips, wrong leg proportions, bent knees wrong, "
            "malformed feet, extra feet, missing feet, floating legs"
        ),
        "hands": (
            "bad hands, mutated hands, extra fingers, missing fingers, "
            "fused fingers, too many fingers, malformed hands, wrong hand anatomy, "
            "deformed fingers, extra thumbs, missing thumbs, webbed fingers, "
            "long fingers, short fingers, bent fingers wrong"
        ),
        "feet": (
            "bad feet, mutated feet, extra toes, missing toes, "
            "deformed feet, malformed feet, wrong foot anatomy, webbed toes, "
            "floating feet, disconnected feet"
        ),
    }
    
    SEVERITY = {
        "light": "",
        "medium": ", poorly drawn, amateur, low quality",
        "heavy": ", poorly drawn, amateur, low quality, worst quality, horrible anatomy",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "negative_prompt": ("STRING", {"default": "", "multiline": True}),
                "focus": (list(cls.FOCUS.keys()),),
                "severity": (list(cls.SEVERITY.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Negative Helpers"

    def build(self, negative_prompt, focus, severity):
        fix = self.FOCUS.get(focus, "")
        sev = self.SEVERITY.get(severity, "")
        if negative_prompt:
            return (f"{negative_prompt}, {fix}{sev}",)
        return (f"{fix}{sev}",)


class FaceFixer:
    """Negative prompts specifically for face issues"""
    
    FIXES = {
        "general": (
            "bad face, deformed face, ugly face, mutated face, "
            "asymmetric face, crooked face, blurry face, low quality face, "
            "wrong facial proportions, distorted features"
        ),
        "eyes": (
            "bad eyes, deformed eyes, asymmetric eyes, crossed eyes, "
            "misaligned eyes, uneven eyes, wrong eye color, dead eyes, "
            "empty eyes, extra eyes, missing eyes, blurry eyes"
        ),
        "nose": (
            "bad nose, deformed nose, crooked nose, missing nose, "
            "pig nose, wrong nose shape, blurry nose"
        ),
        "mouth": (
            "bad mouth, deformed mouth, crooked mouth, missing teeth, "
            "too many teeth, bad teeth, missing lips, deformed lips"
        ),
        "comprehensive": (
            "bad face, deformed face, ugly face, mutated face, asymmetric face, "
            "bad eyes, crossed eyes, deformed eyes, asymmetric eyes, "
            "bad nose, deformed nose, bad mouth, deformed mouth, "
            "bad teeth, missing teeth, double face, multiple faces, "
            "face out of frame, poorly drawn face, cloned face"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "negative_prompt": ("STRING", {"default": "", "multiline": True}),
                "fix_type": (list(cls.FIXES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Negative Helpers"

    def build(self, negative_prompt, fix_type):
        fix = self.FIXES.get(fix_type, "")
        if negative_prompt:
            return (f"{negative_prompt}, {fix}",)
        return (fix,)


class HandFixer:
    """Specialized negative prompts for hand issues"""
    
    HAND_FIXES = {
        "basic": (
            "bad hands, wrong hands, deformed hands, "
            "extra fingers, missing fingers, fused fingers"
        ),
        "detailed": (
            "bad hands, wrong hands, deformed hands, mutated hands, "
            "extra fingers, missing fingers, fused fingers, too many fingers, "
            "long fingers, short fingers, bent fingers, webbed fingers, "
            "extra thumbs, missing thumbs, wrong finger count, "
            "malformed hands, ugly hands, poorly drawn hands"
        ),
        "extreme": (
            "bad hands, wrong hands, deformed hands, mutated hands, "
            "extra fingers, missing fingers, fused fingers, too many fingers, "
            "six fingers, seven fingers, four fingers, three fingers, "
            "long fingers, short fingers, bent fingers, webbed fingers, "
            "extra thumbs, missing thumbs, wrong finger count, "
            "malformed hands, ugly hands, poorly drawn hands, "
            "mangled hands, twisted hands, broken hands, "
            "hands growing from wrong place, floating hands, disconnected hands"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "negative_prompt": ("STRING", {"default": "", "multiline": True}),
                "intensity": (list(cls.HAND_FIXES.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Negative Helpers"

    def build(self, negative_prompt, intensity):
        fix = self.HAND_FIXES.get(intensity, "")
        if negative_prompt:
            return (f"{negative_prompt}, {fix}",)
        return (fix,)


class AIArtifactKiller:
    """Remove common AI generation artifacts and tells"""
    
    ARTIFACTS = {
        "basic": (
            "watermark, signature, text, logo, banner, "
            "jpeg artifacts, compression artifacts, noise"
        ),
        "quality": (
            "low quality, worst quality, bad quality, "
            "blurry, out of focus, poorly drawn, amateur, "
            "lowres, low resolution, pixelated"
        ),
        "ai_tells": (
            "ai generated, artificial, fake looking, plastic skin, "
            "uncanny valley, unnatural, weird texture, "
            "overly smooth, too perfect, inhuman"
        ),
        "comprehensive": (
            "watermark, signature, text, logo, banner, username, "
            "jpeg artifacts, compression artifacts, noise, grain, "
            "low quality, worst quality, bad quality, normal quality, "
            "blurry, out of focus, poorly drawn, amateur, ugly, "
            "lowres, low resolution, pixelated, cropped, "
            "frame, border, letterbox, black bars, "
            "duplicate, clone, copy, error, glitch"
        ),
        "nsfw_safe": (
            "watermark, signature, text, logo, banner, "
            "bad anatomy, deformed, ugly, mutated, "
            "extra limbs, extra fingers, missing fingers, "
            "bad hands, bad face, blurry, low quality"
        ),
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "negative_prompt": ("STRING", {"default": "", "multiline": True}),
                "removal_type": (list(cls.ARTIFACTS.keys()),),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("negative_prompt",)
    FUNCTION = "build"
    CATEGORY = "Mason's Nodes/Negative Helpers"

    def build(self, negative_prompt, removal_type):
        fix = self.ARTIFACTS.get(removal_type, "")
        if negative_prompt:
            return (f"{negative_prompt}, {fix}",)
        return (fix,)


NODE_CLASS_MAPPINGS = {
    "AnatomyFixer": AnatomyFixer,
    "FaceFixer": FaceFixer,
    "HandFixer": HandFixer,
    "AIArtifactKiller": AIArtifactKiller,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AnatomyFixer": "🦴 Anatomy Fixer (Negative)",
    "FaceFixer": "👤 Face Fixer (Negative)",
    "HandFixer": "✋ Hand Fixer (Negative)",
    "AIArtifactKiller": "🚫 AI Artifact Killer",
}
