"""
Mason Nodes - Custom KSampler Nodes
Complete KSampler replacement + specialized preset samplers
These can fully replace the standard ComfyUI KSampler
"""

import torch
import comfy.samplers
import comfy.sample
import latent_preview


class MasonKSamplerFull:
    """
    COMPLETE KSampler replacement with all standard options.
    Drop-in replacement for the default KSampler with added preset support.
    Has EVERY option the standard KSampler has, plus Mason presets.
    """
    
    PRESETS = {
        "-- Use Manual Settings --": None,  # Use the manual inputs below
        "Photorealistic Portrait": {"steps": 30, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Photorealistic Full Body": {"steps": 35, "cfg": 6.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Anime/Cartoon": {"steps": 25, "cfg": 8.0, "sampler": "euler_ancestral", "scheduler": "normal"},
        "NSFW Realistic": {"steps": 35, "cfg": 6.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "NSFW Anime": {"steps": 28, "cfg": 7.5, "sampler": "euler_ancestral", "scheduler": "normal"},
        "Horror/Dark": {"steps": 40, "cfg": 7.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Fast Draft": {"steps": 15, "cfg": 7.0, "sampler": "euler", "scheduler": "normal"},
        "Maximum Quality": {"steps": 50, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Low VRAM Safe": {"steps": 20, "cfg": 7.0, "sampler": "euler", "scheduler": "normal"},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                # Standard KSampler inputs - COMPLETE
                "model": ("MODEL",),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "steps": ("INT", {"default": 30, "min": 1, "max": 10000}),
                "cfg": ("FLOAT", {"default": 7.0, "min": 0.0, "max": 100.0, "step": 0.1, "round": 0.01}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS,),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS,),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            },
            "optional": {
                # Mason preset override - if selected, overrides manual settings
                "preset": (list(cls.PRESETS.keys()), {"default": "-- Use Manual Settings --"}),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    OUTPUT_NODE = False
    FUNCTION = "sample"
    CATEGORY = "Mason/Samplers"
    
    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, 
               positive, negative, latent_image, denoise=1.0, preset="-- Use Manual Settings --"):
        
        # If preset is selected, override manual settings
        if preset != "-- Use Manual Settings --" and self.PRESETS[preset] is not None:
            p = self.PRESETS[preset]
            steps = p["steps"]
            cfg = p["cfg"]
            sampler_name = p["sampler"]
            scheduler = p["scheduler"]
        
        # Perform sampling - exact same as standard KSampler
        samples = comfy.sample.sample(
            model, 
            seed, 
            steps, 
            cfg, 
            sampler_name, 
            scheduler, 
            positive, 
            negative, 
            latent_image["samples"],
            denoise=denoise
        )
        
        return ({"samples": samples},)


class MasonKSamplerAdvanced:
    """
    COMPLETE Advanced KSampler replacement.
    Equivalent to KSamplerAdvanced with start/end step control.
    Full control over the sampling process with preset support.
    """
    
    PRESETS = {
        "-- Use Manual Settings --": None,
        "Two-Pass Upscale": {"steps": 30, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Inpainting": {"steps": 25, "cfg": 7.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Refiner Pass": {"steps": 20, "cfg": 6.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "add_noise": (["enable", "disable"],),
                "noise_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "steps": ("INT", {"default": 30, "min": 1, "max": 10000}),
                "cfg": ("FLOAT", {"default": 7.0, "min": 0.0, "max": 100.0, "step": 0.1, "round": 0.01}),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS,),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS,),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "start_at_step": ("INT", {"default": 0, "min": 0, "max": 10000}),
                "end_at_step": ("INT", {"default": 10000, "min": 0, "max": 10000}),
                "return_with_leftover_noise": (["disable", "enable"],),
            },
            "optional": {
                "preset": (list(cls.PRESETS.keys()), {"default": "-- Use Manual Settings --"}),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    OUTPUT_NODE = False
    FUNCTION = "sample"
    CATEGORY = "Mason/Samplers"
    
    def sample(self, model, add_noise, noise_seed, steps, cfg, sampler_name, scheduler,
               positive, negative, latent_image, start_at_step, end_at_step, 
               return_with_leftover_noise, preset="-- Use Manual Settings --"):
        
        # Apply preset if selected
        if preset != "-- Use Manual Settings --" and self.PRESETS[preset] is not None:
            p = self.PRESETS[preset]
            steps = p["steps"]
            cfg = p["cfg"]
            sampler_name = p["sampler"]
            scheduler = p["scheduler"]
        
        # Handle noise settings
        force_full_denoise = True
        if return_with_leftover_noise == "enable":
            force_full_denoise = False
        
        disable_noise = False
        if add_noise == "disable":
            disable_noise = True
        
        # Perform advanced sampling
        samples = comfy.sample.sample(
            model,
            noise_seed,
            steps,
            cfg,
            sampler_name,
            scheduler,
            positive,
            negative,
            latent_image["samples"],
            denoise=1.0,
            disable_noise=disable_noise,
            start_step=start_at_step,
            last_step=end_at_step,
            force_full_denoise=force_full_denoise
        )
        
        return ({"samples": samples},)


class MasonSmartSampler:
    """
    Smart KSampler - Simplified interface with content-aware presets.
    Just select what you're generating and it picks optimal settings.
    """
    
    PRESETS = {
        "Photorealistic Portrait": {
            "steps": 30, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras",
            "description": "Best for realistic human faces and portraits"
        },
        "Photorealistic Full Body": {
            "steps": 35, "cfg": 6.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras",
            "description": "Best for full body realistic photos"
        },
        "Anime/Cartoon": {
            "steps": 25, "cfg": 8.0, "sampler": "euler_ancestral", "scheduler": "normal",
            "description": "Best for anime and cartoon styles"
        },
        "NSFW Realistic": {
            "steps": 35, "cfg": 6.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras",
            "description": "Optimized for NSFW realistic content"
        },
        "NSFW Anime": {
            "steps": 28, "cfg": 7.5, "sampler": "euler_ancestral", "scheduler": "normal",
            "description": "Optimized for NSFW anime/hentai"
        },
        "Horror/Dark": {
            "steps": 40, "cfg": 7.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras",
            "description": "Optimized for horror and dark content"
        },
        "Fast Draft": {
            "steps": 15, "cfg": 7.0, "sampler": "euler", "scheduler": "normal",
            "description": "Quick preview generation"
        },
        "Maximum Quality": {
            "steps": 50, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras",
            "description": "Highest quality, slowest generation"
        },
        "Low VRAM Safe": {
            "steps": 20, "cfg": 7.0, "sampler": "euler", "scheduler": "normal",
            "description": "Memory efficient for low VRAM GPUs"
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
                "preset": (list(cls.PRESETS.keys()), {"default": "Photorealistic Portrait"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }
    
    RETURN_TYPES = ("LATENT", "STRING")
    RETURN_NAMES = ("samples", "settings_used")
    FUNCTION = "sample"
    CATEGORY = "Mason/Samplers"
    
    def sample(self, model, positive, negative, latent_image, preset, seed, denoise=1.0):
        p = self.PRESETS[preset]
        
        samples = comfy.sample.sample(
            model, seed, p["steps"], p["cfg"], p["sampler"], p["scheduler"],
            positive, negative, latent_image["samples"], denoise=denoise
        )
        
        settings_str = f"Preset: {preset} | Steps: {p['steps']} | CFG: {p['cfg']} | Sampler: {p['sampler']} | Scheduler: {p['scheduler']}"
        
        return ({"samples": samples}, settings_str)


class MasonHorrorSampler:
    """Horror-optimized sampler with intensity levels."""
    
    INTENSITY = {
        "Subtle Horror": {"steps": 30, "cfg": 6.5, "sampler": "dpmpp_2m", "scheduler": "karras"},
        "Standard Horror": {"steps": 35, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Intense Gore": {"steps": 40, "cfg": 7.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Maximum Brutality": {"steps": 50, "cfg": 8.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Atmospheric Dread": {"steps": 45, "cfg": 6.0, "sampler": "dpmpp_2m_sde", "scheduler": "exponential"},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "intensity": (list(cls.INTENSITY.keys()), {"default": "Standard Horror"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"
    CATEGORY = "Mason/Private/Horror"
    
    def sample(self, model, positive, negative, latent_image, intensity, seed):
        s = self.INTENSITY[intensity]
        samples = comfy.sample.sample(model, seed, s["steps"], s["cfg"], s["sampler"], 
                                       s["scheduler"], positive, negative, 
                                       latent_image["samples"], denoise=1.0)
        return ({"samples": samples},)


class MasonNSFWSampler:
    """NSFW-optimized sampler with content type presets."""
    
    CONTENT_TYPE = {
        "Realistic Softcore": {"steps": 30, "cfg": 6.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Realistic Hardcore": {"steps": 35, "cfg": 6.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Anime Softcore": {"steps": 25, "cfg": 7.5, "sampler": "euler_ancestral", "scheduler": "normal"},
        "Anime Hentai": {"steps": 28, "cfg": 7.0, "sampler": "euler_ancestral", "scheduler": "normal"},
        "Maximum Detail": {"steps": 45, "cfg": 6.5, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "content_type": (list(cls.CONTENT_TYPE.keys()), {"default": "Realistic Hardcore"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"
    CATEGORY = "Mason/NSFW"
    
    def sample(self, model, positive, negative, latent_image, content_type, seed):
        s = self.CONTENT_TYPE[content_type]
        samples = comfy.sample.sample(model, seed, s["steps"], s["cfg"], s["sampler"],
                                       s["scheduler"], positive, negative,
                                       latent_image["samples"], denoise=1.0)
        return ({"samples": samples},)


class MasonQuickSampler:
    """Ultra-simple sampler - just quality level and seed."""
    
    QUALITY = {
        "Draft (Fastest)": {"steps": 12, "cfg": 7.0, "sampler": "euler", "scheduler": "normal"},
        "Preview": {"steps": 18, "cfg": 7.0, "sampler": "euler", "scheduler": "normal"},
        "Standard": {"steps": 25, "cfg": 7.0, "sampler": "dpmpp_2m", "scheduler": "karras"},
        "High Quality": {"steps": 35, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
        "Best Quality": {"steps": 50, "cfg": 7.0, "sampler": "dpmpp_2m_sde", "scheduler": "karras"},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "quality": (list(cls.QUALITY.keys()), {"default": "Standard"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"
    CATEGORY = "Mason/Samplers"
    
    def sample(self, model, positive, negative, latent_image, quality, seed):
        s = self.QUALITY[quality]
        samples = comfy.sample.sample(model, seed, s["steps"], s["cfg"], s["sampler"],
                                       s["scheduler"], positive, negative,
                                       latent_image["samples"], denoise=1.0)
        return ({"samples": samples},)


class MasonImg2ImgSampler:
    """Image-to-image sampler with named denoise levels."""
    
    MODIFICATION = {
        "Subtle Changes (5%)": {"denoise": 0.05, "steps": 20},
        "Light Touch (15%)": {"denoise": 0.15, "steps": 22},
        "Moderate Edit (30%)": {"denoise": 0.30, "steps": 25},
        "Significant Change (50%)": {"denoise": 0.50, "steps": 28},
        "Major Rework (70%)": {"denoise": 0.70, "steps": 30},
        "Almost New (85%)": {"denoise": 0.85, "steps": 32},
        "Full Regenerate (100%)": {"denoise": 1.0, "steps": 35},
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "modification": (list(cls.MODIFICATION.keys()), {"default": "Moderate Edit (30%)"}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "cfg": ("FLOAT", {"default": 7.0, "min": 1.0, "max": 15.0, "step": 0.5}),
            }
        }
    
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"
    CATEGORY = "Mason/Samplers"
    
    def sample(self, model, positive, negative, latent_image, modification, seed, cfg=7.0):
        s = self.MODIFICATION[modification]
        samples = comfy.sample.sample(model, seed, s["steps"], cfg, "dpmpp_2m_sde", "karras",
                                       positive, negative, latent_image["samples"],
                                       denoise=s["denoise"])
        return ({"samples": samples},)


NODE_CLASS_MAPPINGS = {
    "MasonKSamplerFull": MasonKSamplerFull,
    "MasonKSamplerAdvanced": MasonKSamplerAdvanced,
    "MasonSmartSampler": MasonSmartSampler,
    "MasonHorrorSampler": MasonHorrorSampler,
    "MasonNSFWSampler": MasonNSFWSampler,
    "MasonQuickSampler": MasonQuickSampler,
    "MasonImg2ImgSampler": MasonImg2ImgSampler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MasonKSamplerFull": "🎛️ Mason KSampler (Full Replacement)",
    "MasonKSamplerAdvanced": "🎛️ Mason KSampler Advanced",
    "MasonSmartSampler": "⚡ Smart Sampler (Presets)",
    "MasonHorrorSampler": "🔪 Horror Sampler (Private)",
    "MasonNSFWSampler": "🔥 NSFW Sampler (Optimized)",
    "MasonQuickSampler": "🚀 Quick Sampler (Simple)",
    "MasonImg2ImgSampler": "🖼️ Img2Img Sampler",
}
