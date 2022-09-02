"""
@Author https://github.com/DougTheDruid
@Source https://github.com/DougTheDruid/SoT-ESP-Framework
"""


ships = {
    # ------------ SHIPS / AI SHIPS ------------
    "BP_SmallShipTemplate_C": {
        "Name": "Sloop (Near)",
    },
    "BP_SmallShipNetProxy_C": {
        "Name": "Sloop",
    },

    "BP_MediumShipTemplate_C": {
        "Name": "Brig (Near)",
    },
    "BP_MediumShipNetProxy_C": {
        "Name": "Brig",
    },

    "BP_LargeShipTemplate_C": {
        "Name": "Gallion (Near)",
    },
    "BP_LargeShipNetProxy_C": {
        "Name": "Gallion",
    },

    "BP_AISmallShipTemplate_C": {
        "Name": "Skeleton Sloop (Near)",
    },
    "BP_AISmallShipNetProxy_C": {
        "Name": "Skeleton Sloop",
    },
    "BP_AILargeShipTemplate_C": {
        "Name": "Skeleton Galleon (Near)",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "Skeleton Galleon",
    },
    "BP_Projectile_CannonBall_C": {
        "name" : "projectile",
    },
    "BP_SkellyFort_RitualSkullCloud_C": {
        "Name": "fort des damnes Event",
    },
    "BP_LegendSkellyFort_SkullCloud_C": {
        "Name": "Fort of Fortune Event",
    },
    "BP_GhostShips_Signal_Flameheart_NetProxy_C": {
        "Name": "Ghost Fleet Event",
    },
    "BP_SkellyFort_SkullCloud_C": {
        "Name": "Skeleton Fort Event",
    },
    "BP_SkellyShip_ShipCloud_C": {
        "Name": "Skeleton Fleet Event",
    },
    "BP_AshenLord_SkullCloud_C": {
        "Name": "Ashen Lord Event",
    },
    "BP_Projectile_CannonBall_C": {
        "name" : "projectil",
    }
    
    # "BP_AggressiveGhostShip_C": {
    #     "Name": "Flameheart Galleon",
    # },  # To implement, must modify ship.py's update method for visibility
}

ship_keys = set(ships.keys())

worldevent = {
    # ------------ EVENT  ------------
    "BP_SkellyFort_RitualSkullCloud_C": {
        "Name": "fort des damnes Event",
    },
    "BP_LegendSkellyFort_SkullCloud_C": {
        "Name": "Fort of Fortune Event",
    },
    "BP_GhostShips_Signal_Flameheart_NetProxy_C": {
        "Name": "Ghost Fleet Event",
    },
    "BP_SkellyFort_SkullCloud_C": {
        "Name": "Skeleton Fort Event",
    },
    "BP_SkellyShip_ShipCloud_C": {
        "Name": "Skeleton Fleet Event",
    },
    "BP_AshenLord_SkullCloud_C": {
        "Name": "Ashen Lord Event",
    },
    "BP_Projectile_CannonBall_C": {
        "name" : "projectil",
    }   
    }    


worldevent_keys = set(worldevent.keys())