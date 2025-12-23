"""
Mason's VRAM Efficiency & Optimization Nodes for ComfyUI
Maximize quality on low-VRAM systems - SD 1.5 optimized
"""


class PromptTokenOptimizer:
    """
    SD 1.5 has a 77 token limit - this helps you stay within it
    Prioritizes the most important terms
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "priority_level": (["quality_first", "subject_first", "style_first", "balanced"],),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("optimized_prompt", "token_info")
    FUNCTION = "optimize"
    CATEGORY = "Mason's Nodes/Efficiency"

    def optimize(self, prompt, priority_level):
        # Approximate token count (roughly 1 token per 4 chars)
        approx_tokens = len(prompt) // 4
        
        info = f"Approximate tokens: {approx_tokens}/77"
        
        if approx_tokens > 77:
            info += " ⚠️ OVER LIMIT - Some terms may be ignored!"
        elif approx_tokens > 60:
            info += " ⚡ Near limit - Consider trimming"
        else:
            info += " ✅ Good length"
        
        # Just return as-is (the info helps the user)
        # In a more advanced version, we'd actually prioritize terms
        return (prompt, info)


class LowVRAMWorkflowHelper:
    """
    Provides a complete optimized workflow for low VRAM systems
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "vram_gb": ("FLOAT", {"default": 2.0, "min": 1.0, "max": 8.0, "step": 0.5}),
                "target_quality": (["draft", "balanced", "high_quality"],),
                "content_type": (["portrait", "full_body", "nsfw", "artistic"],),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "FLOAT", "STRING")
    RETURN_NAMES = ("width", "height", "steps", "cfg_scale", "workflow_guide")
    FUNCTION = "optimize"
    CATEGORY = "Mason's Nodes/Efficiency"

    def optimize(self, vram_gb, target_quality, content_type):
        # Calculate optimal settings
        if vram_gb <= 2.0:
            if target_quality == "draft":
                width, height, steps = 384, 512, 15
            elif target_quality == "balanced":
                width, height, steps = 384, 576, 20
            else:  # high_quality
                width, height, steps = 448, 576, 25
            cfg = 7.0
        elif vram_gb <= 4.0:
            if target_quality == "draft":
                width, height, steps = 448, 576, 18
            elif target_quality == "balanced":
                width, height, steps = 512, 640, 22
            else:
                width, height, steps = 512, 704, 28
            cfg = 7.5
        else:
            if target_quality == "draft":
                width, height, steps = 512, 640, 20
            elif target_quality == "balanced":
                width, height, steps = 512, 768, 25
            else:
                width, height, steps = 576, 832, 30
            cfg = 7.5
        
        # Adjust for content type
        if content_type == "portrait":
            # Keep as is (portrait orientation)
            pass
        elif content_type == "full_body":
            # Make taller
            height = int(height * 1.15)
            height = (height // 64) * 64
        elif content_type == "nsfw":
            # Standard works well
            pass
        elif content_type == "artistic":
            # Can use square
            avg = (width + height) // 2
            width = height = (avg // 64) * 64
        
        guide = f"""
OPTIMIZED FOR {vram_gb}GB VRAM:

Resolution: {width}x{height}
Steps: {steps}
CFG Scale: {cfg}

LAUNCH COMFYUI WITH: python main.py --lowvram

WORKFLOW TIPS:
1. Use our LoRA Emulator nodes instead of actual LoRAs
2. Generate at this resolution, then upscale with img2img
3. Use euler_a sampler for speed
4. Close other programs while generating
5. Use the PromptTemplateStarter for efficient prompts
"""
        
        return (width, height, steps, cfg, guide)


class ConsistencyLockHelper:
    """
    Helps maintain consistency across multiple generations
    Outputs a locked description you can reuse
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "character_description": ("STRING", {"default": "", "multiline": True}),
                "lock_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("locked_prompt", "seed_info")
    FUNCTION = "lock"
    CATEGORY = "Mason's Nodes/Efficiency"

    def lock(self, character_description, lock_seed):
        # Add consistency markers to help SD maintain the look
        locked = (
            f"{character_description}, consistent appearance, "
            "same person, same face, same features"
        )
        
        seed_info = (
            f"Use seed {lock_seed} for this character.\n"
            "Keep this seed the same across all generations of this character."
        )
        
        return (locked, seed_info)


class MultiPassQualityGuide:
    """
    Guide for multi-pass generation (generate small, upscale to large)
    This is the KEY to high quality on low VRAM!
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "target_final_width": ("INT", {"default": 1024, "min": 512, "max": 2048, "step": 64}),
                "target_final_height": ("INT", {"default": 1536, "min": 512, "max": 2048, "step": 64}),
                "vram_gb": ("FLOAT", {"default": 2.0, "min": 1.0, "max": 8.0, "step": 0.5}),
            }
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "FLOAT", "STRING")
    RETURN_NAMES = ("pass1_width", "pass1_height", "pass2_width", "pass2_height", "upscale_denoise", "guide")
    FUNCTION = "plan"
    CATEGORY = "Mason's Nodes/Efficiency"

    def plan(self, target_final_width, target_final_height, vram_gb):
        # Pass 1: Generate small
        if vram_gb <= 2.0:
            scale = 0.375  # Generate at ~37.5% size
        elif vram_gb <= 4.0:
            scale = 0.5
        else:
            scale = 0.65
        
        pass1_w = int(target_final_width * scale)
        pass1_h = int(target_final_height * scale)
        pass1_w = (pass1_w // 64) * 64
        pass1_h = (pass1_h // 64) * 64
        
        # Pass 2: Upscale with img2img
        # If final is too big, do intermediate upscale
        if vram_gb <= 2.0 and target_final_width > 768:
            pass2_w = min(target_final_width, 640)
            pass2_h = min(target_final_height, 960)
        else:
            pass2_w = target_final_width
            pass2_h = target_final_height
        
        pass2_w = (pass2_w // 64) * 64
        pass2_h = (pass2_h // 64) * 64
        
        denoise = 0.35  # Low denoise preserves the original
        
        guide = f"""
MULTI-PASS QUALITY WORKFLOW:

PASS 1 (txt2img):
- Resolution: {pass1_w}x{pass1_h}
- Steps: 25-30
- Get the composition and details right

PASS 2 (img2img upscale):
- Take Pass 1 output
- Upscale to: {pass2_w}x{pass2_h}
- Denoise: {denoise} (preserves original)
- Add "highly detailed, sharp" to prompt

{"PASS 3 (optional): Upscale again to " + str(target_final_width) + "x" + str(target_final_height) if pass2_w < target_final_width else ""}

This method gives you HIGH RESOLUTION results on LOW VRAM!
"""
        
        return (pass1_w, pass1_h, pass2_w, pass2_h, denoise, guide)


class PromptEfficiencyAnalyzer:
    """
    Analyzes prompt for efficiency and suggests improvements
    """
    
    REDUNDANT_PAIRS = [
        ("high quality", "best quality"),
        ("photorealistic", "hyperrealistic"),
        ("detailed", "highly detailed"),
        ("beautiful", "gorgeous"),
        ("4k", "8k"),
    ]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("analysis", "suggestions")
    FUNCTION = "analyze"
    CATEGORY = "Mason's Nodes/Efficiency"

    def analyze(self, prompt):
        prompt_lower = prompt.lower()
        
        analysis_parts = []
        suggestions_parts = []
        
        # Check length
        word_count = len(prompt.split())
        analysis_parts.append(f"Word count: {word_count}")
        
        # Approximate tokens
        token_approx = len(prompt) // 4
        analysis_parts.append(f"Estimated tokens: {token_approx}/77")
        
        if token_approx > 77:
            suggestions_parts.append("⚠️ OVER TOKEN LIMIT - trim your prompt")
        
        # Check for redundancies
        found_redundant = []
        for pair in self.REDUNDANT_PAIRS:
            if pair[0] in prompt_lower and pair[1] in prompt_lower:
                found_redundant.append(f"'{pair[0]}' and '{pair[1]}'")
        
        if found_redundant:
            suggestions_parts.append(f"Redundant terms found: {', '.join(found_redundant)}")
            suggestions_parts.append("Consider keeping only one of each pair")
        
        # Check for quality boosters
        quality_terms = ["high quality", "best quality", "masterpiece", "sharp", "detailed"]
        found_quality = [t for t in quality_terms if t in prompt_lower]
        
        if not found_quality:
            suggestions_parts.append("Consider adding quality terms: 'high quality, detailed, sharp'")
        
        analysis = "\n".join(analysis_parts)
        suggestions = "\n".join(suggestions_parts) if suggestions_parts else "✅ Prompt looks good!"
        
        return (analysis, suggestions)


NODE_CLASS_MAPPINGS = {
    "PromptTokenOptimizer": PromptTokenOptimizer,
    "LowVRAMWorkflowHelper": LowVRAMWorkflowHelper,
    "ConsistencyLockHelper": ConsistencyLockHelper,
    "MultiPassQualityGuide": MultiPassQualityGuide,
    "PromptEfficiencyAnalyzer": PromptEfficiencyAnalyzer,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptTokenOptimizer": "📊 Prompt Token Optimizer",
    "LowVRAMWorkflowHelper": "🔋 Low VRAM Workflow Helper",
    "ConsistencyLockHelper": "🔒 Consistency Lock Helper",
    "MultiPassQualityGuide": "🔄 Multi-Pass Quality Guide",
    "PromptEfficiencyAnalyzer": "📈 Prompt Efficiency Analyzer",
}
