"""
Mason Nodes - Custom Samplers and Schedulers
Custom sampling algorithms and noise schedules for ComfyUI
These integrate with the KSampler system to provide new options
"""

import torch
import math
from comfy.k_diffusion import sampling as k_diffusion_sampling
import comfy.samplers
import comfy.sample


# ============================================
# CUSTOM SCHEDULERS (Noise Schedules)
# ============================================

def mason_aggressive_scheduler(n, sigma_min, sigma_max):
    """
    Aggressive scheduler - faster noise reduction early, very slow at end.
    Good for horror and atmospheric images with deep detail.
    """
    # Use power function to create aggressive curve
    t = torch.linspace(0, 1, n)
    # Power of 3 makes it very aggressive early, slow late
    sigmas = sigma_max * (1 - t ** 0.3) + sigma_min * (t ** 0.3)
    sigmas = torch.cat([sigmas, torch.zeros(1)])
    return sigmas


def mason_detail_scheduler(n, sigma_min, sigma_max):
    """
    Detail-focused scheduler - more steps at low noise levels.
    Best for photorealistic portraits needing fine detail.
    """
    # Spend more time at low noise for detail work
    t = torch.linspace(0, 1, n)
    # Square root curve - slower at start, faster middle, slow at end
    curved = torch.sqrt(t)
    sigmas = sigma_max * (1 - curved) + sigma_min * curved
    sigmas = torch.cat([sigmas, torch.zeros(1)])
    return sigmas


def mason_nsfw_scheduler(n, sigma_min, sigma_max):
    """
    NSFW-optimized scheduler - balanced for anatomical accuracy.
    Moderate early steps, extended detail phase.
    """
    t = torch.linspace(0, 1, n)
    # Use sine curve for smooth transitions
    curved = (1 - torch.cos(t * math.pi)) / 2
    sigmas = sigma_max * (1 - curved) + sigma_min * curved
    sigmas = torch.cat([sigmas, torch.zeros(1)])
    return sigmas


def mason_horror_scheduler(n, sigma_min, sigma_max):
    """
    Horror-optimized scheduler - emphasizes contrast and atmosphere.
    Creates more dramatic noise transitions.
    """
    t = torch.linspace(0, 1, n)
    # Use a stepped curve for horror atmosphere
    curved = t ** 0.7  # Slightly aggressive
    sigmas = sigma_max * (1 - curved) + sigma_min * curved
    sigmas = torch.cat([sigmas, torch.zeros(1)])
    return sigmas


# ============================================
# CUSTOM SCHEDULER NODE
# ============================================

class MasonSchedulerSelector:
    """
    Custom scheduler node that provides Mason-specific noise schedules.
    Use with BasicScheduler or connect to SamplerCustom nodes.
    """
    
    SCHEDULERS = {
        "mason_aggressive": "Aggressive - Fast early, slow detail phase",
        "mason_detail": "Detail Focus - Extra time on fine details", 
        "mason_nsfw": "NSFW Optimized - Balanced for anatomy",
        "mason_horror": "Horror - Dramatic atmospheric transitions",
        "karras": "Karras (Standard) - Popular general purpose",
        "exponential": "Exponential - Smooth decay",
        "normal": "Normal - Linear interpolation",
        "simple": "Simple - Basic linear steps",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "scheduler": (list(cls.SCHEDULERS.keys()), {"default": "mason_detail"}),
                "steps": ("INT", {"default": 30, "min": 1, "max": 1000}),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }
    
    RETURN_TYPES = ("SIGMAS",)
    FUNCTION = "get_sigmas"
    CATEGORY = "Mason/Samplers"
    
    def get_sigmas(self, model, scheduler, steps, denoise):
        total_steps = steps
        if denoise < 1.0:
            if denoise <= 0.0:
                return (torch.FloatTensor([]),)
            total_steps = int(steps / denoise)
        
        # Get model sigma range
        model_sampling = model.get_model_object("model_sampling")
        sigma_min = float(model_sampling.sigma_min)
        sigma_max = float(model_sampling.sigma_max)
        
        # Select scheduler
        if scheduler == "mason_aggressive":
            sigmas = mason_aggressive_scheduler(total_steps, sigma_min, sigma_max)
        elif scheduler == "mason_detail":
            sigmas = mason_detail_scheduler(total_steps, sigma_min, sigma_max)
        elif scheduler == "mason_nsfw":
            sigmas = mason_nsfw_scheduler(total_steps, sigma_min, sigma_max)
        elif scheduler == "mason_horror":
            sigmas = mason_horror_scheduler(total_steps, sigma_min, sigma_max)
        else:
            # Fall back to ComfyUI's built-in schedulers
            sigmas = comfy.samplers.calculate_sigmas(model_sampling, scheduler, total_steps)
        
        # Handle denoise < 1.0
        if denoise < 1.0:
            sigmas = sigmas[-(steps + 1):]
        
        return (sigmas,)


# ============================================
# CUSTOM HYBRID SAMPLER
# ============================================

class MasonHybridSampler:
    """
    Hybrid sampler that uses different samplers for different phases.
    For example: euler_ancestral for structure, dpmpp_2m_sde for detail.
    """
    
    PHASE1_SAMPLERS = ["euler_ancestral", "euler", "dpmpp_2m", "heun"]
    PHASE2_SAMPLERS = ["dpmpp_2m_sde", "dpmpp_2m", "euler", "dpmpp_sde"]
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "total_steps": ("INT", {"default": 30, "min": 1, "max": 100}),
                "phase1_sampler": (cls.PHASE1_SAMPLERS, {"default": "euler_ancestral"}),
                "phase2_sampler": (cls.PHASE2_SAMPLERS, {"default": "dpmpp_2m_sde"}),
                "phase1_steps": ("INT", {"default": 10, "min": 1, "max": 50}),
                "cfg": ("FLOAT", {"default": 7.0, "min": 1.0, "max": 20.0, "step": 0.5}),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"
    CATEGORY = "Mason/Samplers"
    
    def sample(self, model, positive, negative, latent_image, seed, 
               total_steps, phase1_sampler, phase2_sampler, phase1_steps, cfg):
        
        phase2_steps = total_steps - phase1_steps
        
        # Phase 1: Structure building with ancestral sampler
        samples = comfy.sample.sample(
            model, seed, phase1_steps, cfg,
            phase1_sampler, "normal",
            positive, negative,
            latent_image["samples"],
            denoise=1.0
        )
        
        # Phase 2: Detail refinement with deterministic sampler
        samples = comfy.sample.sample(
            model, seed + 1, phase2_steps, cfg,
            phase2_sampler, "karras",
            positive, negative,
            samples,
            denoise=0.5  # Partial denoise for refinement
        )
        
        return ({"samples": samples},)


# ============================================
# SAMPLER CHAIN NODE
# ============================================

class MasonSamplerChain:
    """
    Chain multiple sampling passes with different settings.
    First pass at high denoise, subsequent passes at lower denoise for refinement.
    """
    
    PRESETS = {
        "Two-Pass Quality": {
            "passes": [
                {"steps": 20, "cfg": 7.0, "sampler": "euler_ancestral", "scheduler": "normal", "denoise": 1.0},
                {"steps": 15, "cfg": 6.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras", "denoise": 0.4},
            ]
        },
        "Three-Pass Maximum": {
            "passes": [
                {"steps": 15, "cfg": 7.0, "sampler": "euler", "scheduler": "normal", "denoise": 1.0},
                {"steps": 15, "cfg": 7.0, "sampler": "dpmpp_2m", "scheduler": "karras", "denoise": 0.5},
                {"steps": 10, "cfg": 6.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras", "denoise": 0.3},
            ]
        },
        "Horror Atmosphere": {
            "passes": [
                {"steps": 25, "cfg": 7.5, "sampler": "euler_ancestral", "scheduler": "normal", "denoise": 1.0},
                {"steps": 20, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras", "denoise": 0.35},
            ]
        },
        "NSFW Anatomical": {
            "passes": [
                {"steps": 20, "cfg": 6.5, "sampler": "euler_ancestral", "scheduler": "normal", "denoise": 1.0},
                {"steps": 20, "cfg": 6.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras", "denoise": 0.45},
            ]
        },
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "preset": (list(cls.PRESETS.keys()), {"default": "Two-Pass Quality"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
    
    RETURN_TYPES = ("LATENT", "STRING")
    RETURN_NAMES = ("samples", "passes_info")
    FUNCTION = "sample"
    CATEGORY = "Mason/Samplers"
    
    def sample(self, model, positive, negative, latent_image, preset, seed):
        passes = self.PRESETS[preset]["passes"]
        samples = latent_image["samples"]
        info_parts = []
        
        for i, p in enumerate(passes):
            samples = comfy.sample.sample(
                model, seed + i, p["steps"], p["cfg"],
                p["sampler"], p["scheduler"],
                positive, negative,
                samples,
                denoise=p["denoise"]
            )
            info_parts.append(f"Pass {i+1}: {p['sampler']}, {p['steps']} steps, {p['denoise']} denoise")
        
        return ({"samples": samples}, " | ".join(info_parts))


# ============================================
# SIGMAS MANIPULATION NODES
# ============================================

class MasonSigmasModify:
    """
    Modify existing sigmas to change how the sampler behaves.
    Useful for fine-tuning noise schedules.
    """
    
    MODIFICATIONS = {
        "Stretch Detail Phase": "More time at low noise (detail)",
        "Compress Detail Phase": "Less time at low noise (speed)",
        "Boost Mid Range": "Extra weight on mid-noise levels",
        "Smooth Transitions": "Gentler sigma changes between steps",
        "Sharp Transitions": "More aggressive sigma changes",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "sigmas": ("SIGMAS",),
                "modification": (list(cls.MODIFICATIONS.keys()), {"default": "Stretch Detail Phase"}),
                "strength": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.1}),
            }
        }
    
    RETURN_TYPES = ("SIGMAS",)
    FUNCTION = "modify"
    CATEGORY = "Mason/Samplers"
    
    def modify(self, sigmas, modification, strength):
        sigmas = sigmas.clone()
        n = len(sigmas) - 1  # Exclude final 0
        
        if modification == "Stretch Detail Phase":
            # Make the curve spend more time at low sigma
            for i in range(n):
                t = i / n
                factor = 1.0 - strength * 0.3 * (t ** 0.5)
                sigmas[i] = sigmas[i] * factor
                
        elif modification == "Compress Detail Phase":
            # Speed through the low sigma phase
            for i in range(n):
                t = i / n
                factor = 1.0 + strength * 0.3 * (t ** 0.5)
                sigmas[i] = sigmas[i] * factor
                
        elif modification == "Boost Mid Range":
            # Add extra emphasis to middle sigma values
            for i in range(n):
                t = i / n
                mid_boost = math.sin(t * math.pi) * strength * 0.2
                sigmas[i] = sigmas[i] * (1 + mid_boost)
                
        elif modification == "Smooth Transitions":
            # Apply smoothing between sigma values
            if n > 2:
                smoothed = sigmas.clone()
                for i in range(1, n - 1):
                    blend = strength * 0.3
                    smoothed[i] = sigmas[i] * (1 - blend) + (sigmas[i-1] + sigmas[i+1]) / 2 * blend
                sigmas = smoothed
                
        elif modification == "Sharp Transitions":
            # Increase the difference between steps
            if n > 2:
                for i in range(1, n - 1):
                    mid = (sigmas[0] + sigmas[-2]) / 2
                    diff = sigmas[i] - mid
                    sigmas[i] = mid + diff * (1 + strength * 0.3)
        
        return (sigmas,)


NODE_CLASS_MAPPINGS = {
    "MasonSchedulerSelector": MasonSchedulerSelector,
    "MasonHybridSampler": MasonHybridSampler,
    "MasonSamplerChain": MasonSamplerChain,
    "MasonSigmasModify": MasonSigmasModify,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonSchedulerSelector": "📊 Custom Scheduler (Mason)",
    "MasonHybridSampler": "🔀 Hybrid Sampler (Two-Phase)",
    "MasonSamplerChain": "⛓️ Sampler Chain (Multi-Pass)",
    "MasonSigmasModify": "📈 Sigmas Modifier",
}
