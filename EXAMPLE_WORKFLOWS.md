# Mason's Custom Nodes - Example Workflows

## How to Use These Workflows

These are TEXT-BASED workflow guides. In ComfyUI:

1. Add each node in the order listed
2. Connect STRING outputs to STRING inputs in sequence
3. Feed final STRING into your positive prompt

---

## 1. Basic Portrait Workflow

**Purpose:** High-quality photorealistic portrait

```text
Nodes in order:
1. CompleteCharacterBuilder → Set gender, age, ethnicity, features
2. FacialStructureController → Define bone structure
3. EyeDetailMaster → Eye color and expression
4. EyeMakeupController → Makeup if desired
5. LipController → Lip color and shape
6. SkinTextureController → Skin finish
7. HairTextureController → Hair quality
8. FramingController → Set to "close_up"
9. ThreePointLightingSetup → Lighting setup
10. QualityMasterNode → Quality enhancement

Final output → CLIP Text Encode (Positive)
```

---

## 2. Full Body Glamour Workflow

**Purpose:** Full body shots with detailed control

```text
Nodes in order:
1. CompleteCharacterBuilder → Full character setup
2. BodyTypeSelector → Body type, breast size, height
3. BodyProportionEnhancer → Waist, hips, shoulders
4. SkinShineController → Skin moisture/sheen
5. UltimatePoseMaster → Select pose
6. DressSelector OR LingerieSelector → Outfit
7. ClothingFitController → How clothes fit
8. FootwearSelector → Shoes/stockings
9. FramingController → "full_body"
10. RuleOfThirdsPositioner → Subject placement
11. ThreePointLightingSetup → Lighting
12. ColorTemperatureController → Warm/cool
13. RenderStyleController → "photorealistic"
14. QualityMasterNode → Quality boost
```

---

## 3. NSFW Boudoir Workflow

**Purpose:** Intimate/boudoir style content

```text
Nodes in order:
1. CompleteCharacterBuilder → Character with body type focus
2. BodyTypeSelector → Proportions, sizes
3. SkinShineController → "dewy" or "oiled"
4. MuscleDefinitionController → Muscle tone
5. UltimatePoseMaster → "lying_sensual" or similar
6. LingerieSelector → Lingerie type, material, color
7. ClothingStateController → "disheveled" if desired
8. FabricDetailer → Fabric quality
9. MakeupDetailer → Glamour makeup
10. ThreePointLightingSetup → Soft key, subtle fill
11. ShadowController → Soft shadows
12. ColorTemperatureController → "warm"
13. BackgroundComplexityController → "simple_studio"
14. DetailLevelController → "sharp"
15. QualityMasterNode → Quality="ultra"

Negative: bad anatomy, deformed, extra limbs, blurry
```

---

## 4. Animation/Batch Frame Workflow

**Purpose:** Generate consistent frames for animation

```text
For EACH frame (use batch queue or manual):

1. ConsistentSubjectLock → Lock subject description
2. CompleteCharacterBuilder → Same settings every frame
3. BodyTypeSelector → Same settings
4. UltimatePoseMaster OR PoseTransitionBuilder → Pose per frame
5. BatchAnimationBuilder → Frame-specific motion
6. FrameSequenceGenerator → Generate seed for frame
7. MotionStrengthController → Movement intensity
8. ThreePointLightingSetup → Consistent lighting
9. AnimationFrameSaver → Get filename/path

After generating all frames:
- Use VideoCompileHelper → Get ffmpeg command
- Run command in terminal to compile video
```

---

## 5. Artistic Style Workflow

**Purpose:** Non-photorealistic artistic renders

```text
1. CompleteCharacterBuilder → Base character
2. RenderStyleController → "oil_painting", "anime", etc.
3. ArtMovementController → Art style
4. ColorPaletteController → Color scheme
5. ContrastStyleController → Lighting mood
6. UltimatePoseMaster → Pose
7. DetailLevelController → "soft_dreamy" to "hyper_detailed"
8. AnimeRealisticBlender → Style balance
9. VintageFilterController → Era filter if desired
```

---

## 6. Wet/Pool Scene Workflow

**Purpose:** Pool, shower, or wet scenes

```text
1. CompleteCharacterBuilder → Character
2. SwimwearSelector → Bikini type and pattern
3. SkinShineController → "wet" or "sweaty"
4. WetClothingController → "soaking"
5. HairMovementController → "wet" or "static"
6. UltimatePoseMaster → Pose
7. ReflectionController → "water" or "wet_floor"
8. ThreePointLightingSetup → Outdoor lighting
9. ColorTemperatureController → "warm" for sunny
10. ParticleController → Water droplets if desired
```

---

## Quick Reference: Node Categories

| Category | Use For |
|----------|---------|
| Character | Base subject creation |
| Face Detail | Facial features, makeup |
| Body Detail | Proportions, muscle, skin |
| Hair Detail | Hair texture, volume, color |
| Outfit | Clothing, lingerie, swimwear |
| Pose | Body positioning |
| Composition | Camera, framing |
| Lighting | Light setup |
| Style | Artistic effects |
| Motion | Animation frames |

---

## Tips for Best Results

1. **Order matters**: Character → Details → Pose → Outfit → Lighting → Quality
2. **Be specific**: More nodes = more control
3. **Stay consistent**: Same settings for animation frames
4. **Use negatives**: Always include negative prompt
5. **Test singles first**: Get one image right before batch
