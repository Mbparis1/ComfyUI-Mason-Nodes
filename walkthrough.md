# ComfyUI Custom Nodes - Complete Walkthrough

## Summary

Explosive expansion to **~340 total nodes** — covering LoRA emulation, micro-details, NSFW acts, and virtual rigging.
**Zero VRAM overhead. SD 1.5 Optimized.**

## Major Additions (Session 2)

### 1. LoRA Emulators (Zero VRAM)

| Module | Nodes | Purpose |
|--------|-------|---------|
| `lora_emulator_nodes.py` | 8 | Base replacements (Detail, Skin, Body, Face) |
| `lora_emulator_extended_nodes.py` | 8 | Extended (Hair, Pose, Makeup, Clothing) |
| `nsfw_lora_emulator_nodes.py` | 6 | NSFW specific (Fluids, Arousal, Fetish) |

### 2. Advanced Control & Acts

| Module | Nodes | Purpose |
|--------|-------|---------|
| `nsfw_act_nodes.py` | 6 | Specific acts (Oral, Penetration, Group) |
| `nsfw_niche_act_nodes.py` | 6 | BDSM, Roleplay, Solo, POV |
| `pose_architect_nodes.py` | 6 | **Virtual Stick Figure** (Text-based rigging) |
| `fantasy_nsfw_nodes.py` | 6 | Monster girls, transformation, wings/horns |
| `cosplay_costume_nodes.py` | 5 | Heroine, magical girl, armor, sci-fi |
| `visual_pose_nodes.py` | 3 | **Draws ControlNet skeletons on CPU** |
| `nsfw_mechanics_nodes.py` | 5 | Deep mechanics (Oral, Penetration, Anal) |

### 3. Optimization & Micro-Details

| Module | Nodes | Purpose |
|--------|-------|---------|
| `system_optimization_nodes.py` | 3 | 2GB VRAM configs & guides |
| `efficiency_nodes.py` | 5 | Token limiters, consistency, multi-pass |
| `micro_detail_nodes.py` | 8 | Eyelashes, lip gloss, film grain |
| `accessory_detail_nodes.py` | 6 | Jewelry, nails, piercings |

### 6. Phase 10 - The Master's Touch (Advanced Realism)

| Module | Nodes | Purpose |
|--------|-------|---------|
| `aesthetic_nodes.py` | 2 | Mood Director (Noir, Cyberpunk), Color Grading |
| `interaction_nodes.py` | 3 | **Physics:** Skin pressure, fabric stretch, fluid pooling |
| `expression_nodes.py` | 3 | **Micro-Expressions:** Eye rolls, lip biting, flushed skin |
| `narrative_nodes.py` | 2 | Scenario Architects (Secret Affair, Office Scandal) |
| `extreme_nsfw_nodes.py` | 4 | **The Dirtiest:** Extreme fluids, anatomical precision, messy rooms |

### 7. Phase 11 - Act Perfection (Precision Act Masters)

| Module | Nodes | Purpose |
|--------|-------|---------|
| `nsfw_act_perfection_nodes.py` | 5 | **Perfection:** Deep Throat (gagging), Groping (squeeze), Anal, Vaginal, Manual |

### 4. Automation & Ease of Use (Session 3)

| Module | Nodes | Purpose |
|--------|-------|---------|
| `dynamic_prompt_nodes.py` | 4 | Wildcards `{red\|blue}`, Cyclers, Randomization |
| `pose_preset_nodes.py` | 2 | **50+ Pre-Configured Poses** (Dropdown menu) |
| `workflow_utils_nodes.py` | 4 | Project structure, State saving, **Concatenation** |

### 5. Drag-and-Drop Workflow Library (`/workflows`)

| Filename | Description |
|----------|-------------|
| `Mason_Omni_Creator.json` | **The Master Workflow.** Connects Emulators, Pose Presets, Oral Mechanics, and Dynamics into ONE prompt. |
| `Mason_Basic_Setup.json` | Simple portrait setup with Wildcard support. |
| `Mason_NSFW_Boudoir.json` | Specialized for lingerie, oils, and sensual lighting. |
| `Mason_Animation_Setup.json` | For generating consistent frame sequences. |
| `Mason_FullBody_Glamour.json` | Full body shots with clothing fit and body shape controls. |
| `Mason_Artistic_Style.json` | Painting/Anime styles without realism focus. |
| `Mason_Wet_Scene.json` | Pool/Shower scenes with water droplets and reflections. |
| `Mason_Visual_Pose_Verify.json` | Use this to SEE the stick figure before you generate. |
| `Mason_Extreme_Acts.json` | **The Absolute Limit.** Uses Fluid Dynamics, Anatomical Detail, and Pleasure Expressions for maximum intensity. |
| `Mason_Perfect_Acts.json` | **Act Precision.** Specialized for Deep Throat, Groping, and Finger Play with realistic anatomical cues. |

---

## Strategy for Low VRAM Quality

1. **Use Emulators:** Replace 5-6 LoRAs with `UltimateLoRAEmulator` + `NSFWBodyPartsLoRA`.
2. **Use Pose Architect:** Instead of ControlNet, use `UpperBodyRig` + `LowerBodyRig`.
3. **Visual Confirmation:** Use `PoseVisualizer` to see the stick figure before generating (avoids wasted runs).
4. **Upscale:** Generate small (384x512), then img2img upscale using `MultiPassQualityGuide`.

## GitHub

All pushed to: [ComfyUI-Mason-Nodes](https://github.com/Mbparis1/ComfyUI-Mason-Nodes)

## Total: ~362 nodes
