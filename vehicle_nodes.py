"""
Mason's Vehicle Nodes for ComfyUI
Land, sea, and air vehicles - SD 1.5 optimized
"""


class LandVehiclePro:
    """Cars, motorcycles, and land vehicles"""
    
    VEHICLES = {
        "sports_car": "sleek sports car, aerodynamic, fast, modern supercar",
        "classic_car": "classic vintage car, chrome details, retro automotive",
        "muscle_car": "American muscle car, powerful engine, aggressive stance",
        "motorcycle": "motorcycle, two-wheeled, chrome and leather, biker",
        "truck": "heavy truck, large vehicle, industrial, powerful",
        "tank": "military tank, armored vehicle, treads, cannon",
        "horse_carriage": "horse-drawn carriage, Victorian, elegant, historical",
        "chariot": "ancient chariot, horses pulling, Roman, battle",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "vehicle": (list(cls.VEHICLES.keys()),),
                "condition": (["showroom", "used", "damaged", "abandoned"],),
                "environment": (["road", "racing", "parked", "action"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("vehicle_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Vehicles"

    def apply(self, prompt, vehicle, condition, environment):
        parts = [prompt]
        parts.append(self.VEHICLES.get(vehicle, ""))
        
        condition_map = {
            "showroom": "pristine condition, brand new, perfect paint",
            "used": "used vehicle, character, lived-in",
            "damaged": "damaged vehicle, dents, scratches, battle scars",
            "abandoned": "abandoned vehicle, rusted, overgrown, forgotten",
        }
        parts.append(condition_map.get(condition, ""))
        
        env_map = {
            "road": "on the road, driving, in motion",
            "racing": "racing, high speed, blurred background, competition",
            "parked": "parked, stationary, detailed view",
            "action": "action shot, dramatic angle, explosive energy",
        }
        parts.append(env_map.get(environment, ""))
        
        return (", ".join([p for p in parts if p]),)


class SeaVehiclePro:
    """Ships, boats, and sea vessels"""
    
    VESSELS = {
        "pirate_ship": "pirate ship, tall mast, black sails, skull and crossbones",
        "galleon": "Spanish galleon, historical sailing ship, gold-laden",
        "warship": "naval warship, cannons, military vessel, armored",
        "yacht": "luxury yacht, modern, sleek, wealthy",
        "fishing_boat": "fishing boat, nets, weathered, working vessel",
        "viking_longship": "Viking longship, dragon prow, oars, Nordic",
        "submarine": "submarine, underwater vessel, military, sleek",
        "rowboat": "small rowboat, wooden, oars, simple vessel",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "vessel": (list(cls.VESSELS.keys()),),
                "state": (["sailing", "anchored", "battle", "sinking", "docked"],),
                "weather": (["calm", "stormy", "foggy", "sunset"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("vessel_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Vehicles"

    def apply(self, prompt, vessel, state, weather):
        parts = [prompt]
        parts.append(self.VESSELS.get(vessel, ""))
        
        state_map = {
            "sailing": "sailing on open water, wind in sails, moving",
            "anchored": "anchored, stationary, at rest on water",
            "battle": "in naval battle, cannons firing, smoke and fire",
            "sinking": "sinking ship, tilted, water flooding, dramatic",
            "docked": "docked at port, harbor, tied to pier",
        }
        parts.append(state_map.get(state, ""))
        
        weather_map = {
            "stormy": "stormy seas, massive waves, lightning, dangerous",
            "foggy": "fog on water, mysterious, low visibility",
            "sunset": "sunset at sea, golden light, romantic",
        }
        if weather != "calm":
            parts.append(weather_map.get(weather, ""))
        
        return (", ".join([p for p in parts if p]),)


class AircraftPro:
    """Aircraft and flying machines"""
    
    AIRCRAFT = {
        "fighter_jet": "military fighter jet, sleek, missiles, modern warfare",
        "helicopter": "helicopter, rotor blades, hovering, versatile",
        "biplane": "vintage biplane, double wings, WWI era, propeller",
        "dragon_mount": "dragon being ridden, fantasy flight, scales and wings",
        "airship": "steampunk airship, dirigible, floating, Victorian sci-fi",
        "spaceship": "spaceship, futuristic, space travel, sci-fi",
        "hot_air_balloon": "colorful hot air balloon, floating, peaceful",
        "pegasus": "flying pegasus, winged horse, mythological, majestic",
    }
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "aircraft": (list(cls.AIRCRAFT.keys()),),
                "flight_state": (["grounded", "takeoff", "flying", "landing", "combat"],),
                "altitude": (["low", "medium", "high", "space"],),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("aircraft_prompt",)
    FUNCTION = "apply"
    CATEGORY = "Mason's Nodes/Vehicles"

    def apply(self, prompt, aircraft, flight_state, altitude):
        parts = [prompt]
        parts.append(self.AIRCRAFT.get(aircraft, ""))
        
        state_map = {
            "grounded": "on the ground, stationary, landed",
            "takeoff": "taking off, leaving ground, ascending",
            "flying": "in flight, soaring through air, airborne",
            "landing": "landing, descending, approaching ground",
            "combat": "in aerial combat, dogfight, action, battle",
        }
        parts.append(state_map.get(flight_state, ""))
        
        alt_map = {
            "low": "low altitude, close to ground",
            "medium": "mid-altitude, clouds nearby",
            "high": "high altitude, above clouds, vast sky",
            "space": "in space, stars visible, zero gravity",
        }
        parts.append(alt_map.get(altitude, ""))
        
        return (", ".join([p for p in parts if p]),)


NODE_CLASS_MAPPINGS = {
    "LandVehiclePro": LandVehiclePro,
    "SeaVehiclePro": SeaVehiclePro,
    "AircraftPro": AircraftPro,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LandVehiclePro": "🚗 Land Vehicle Pro",
    "SeaVehiclePro": "🚢 Sea Vehicle Pro",
    "AircraftPro": "✈️ Aircraft Pro",
}
