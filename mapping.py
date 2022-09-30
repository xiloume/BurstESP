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
        "Name": "Skeleton Gallion (Near)",
    },
    "BP_AILargeShipNetProxy_C": {
        "Name": "Skeleton Gallion",
    }
    
    # "BP_AggressiveGhostShip_C": {
    #     "Name": "Flameheart Galleon",
    # },  # To implement, must modify ship.py's update method for visibility
}

ship_keys = set(ships.keys())

worldeventMap = {
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
    }
}    

worldevent_keys = set(worldeventMap.keys())

Shipwreck = {
    # ------------ EPAVE  ------------
    "BP_Shipwreck_01_a_NetProxy_C": {
        "Name": "Epave",
    },
    "BP_Seagull01_8POI_C": {
        "Name": "Epave quête",
    }
}

Shipwreck_keys = set(Shipwreck.keys())

Player = {
    # ------------ EPAVE  ------------
    "AthenaPlayerState": {
        "Name": "Joueur",
    }
}

Player_keys = set(Player.keys())

# 0 Common (blanc)/  1 peu commun (vert) / 2 rare (bleu) / 3 epique (violet) / 4 legendaire (orange) / 5 rubis (rouge)
Chestmap = {
     # ------------ COFFRE  ------------
    "BP_AshenChestCollectorsChest_ItemInfo_C": {
        "Name": "Coffre cendré",
        "Color": 0,
    },
    "BP_AshenChestCollectorsChest_Unlocked_ItemInfo_C": {
        "Name": "Coffre cendré",
        "Color": 0,
    },
    "BP_CollectorsChest_ItemInfo_C": {
        "Name": "Coffre au trésor",
        "Color": 0,
    },
    "BP_SK_CoralCollectorsChest_ItemInfo_C": {
        "Name": "Coffre de corail",
        "Color": 0,
    },
    "BP_LockedEquipmentChest_ItemInfo_C": {
        "Name": "Sailor chest",
        "Color": 0,
    },
    "BP_UnLockedEquipmentChest_ItemInfo_C": {
        "Name": "Sailor chest",
        "Color": 0,
    },
    "BP_MerchantCrate_AnyItemCrate_ItemInfo_C": {
        "Name": "Caisse stock.",
        "Color": 0,
    },
    "BP_MerchantCrate_AIShipAnyItemCrate_ItemInfo_C": {
        "Name": "Caisse stock.",
        "Color": 0,
    },
    "BP_MerchantCrate_GhostResourceCrate_ItemInfo_C": {
        "Name": "Caisse stock. damnes",
        "Color": 0,
    },
    "BP_MerchantCrate_GhostCannonballCrate_ItemInfo_C": {
        "Name": "Caisse boulets damnes",
        "Color": 0,
    },
    "BP_PortableAmmoCrate_ItemInfo_C": {
        "Name": "Caisse munitions",
        "Color": 0,
    },
    "BP_MerchantCrate_FirebombCrate_ItemInfo_C": {
        "Name": "Caisse artifices",
        "Color": 0,
    },
    "BP_MerchantCrate_WoodCrate_FullyStocked_ItemInfo_C": {
        "Name": "Caisse planches",
        "Color": 0,
    },
    "BP_MerchantCrate_WoodCrate_ItemInfo_C": {
        "Name": "Caisse planches",
        "Color": 0,
    },
    "BP_MerchantCrate_CannonballCrate_FullyStocked_ItemInfo_C": {
        "Name": "Caisse boulets",
        "Color": 0,
    },
    "BP_MerchantCrate_CannonballCrate_ItemInfo_C": {
        "Name": "Caisse boulets",
        "Color": 0,
    },
    "BP_MerchantCrate_BananaCrate_FullyStocked_ItemInfo_C": {
        "Name": "Caisse fruits",
        "Color": 0,
    },
    "BP_MerchantCrate_BananaCrate_ItemInfo_C": {
        "Name": "Caisse fruits",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Fort_C": {
        "Name": "Coffre forteresse",
        "Color": 0,
    },
    "BP_TreasureChest_Vault_ItemInfo_C": {
        "Name": "Coffre anciens tributs",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Ghost_C": {
        "Name": "Coffre damnes",
        "Color": 0,
    },
    "BP_MerchantCrate_Commodity_GhostCrate_ItemInfo_C": {
        "Name": "Cendre des damnes",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_AIShip_C": {
        "Name": "Coffre capit. squel.",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Mythical_DVR_C": {
        "Name": "Coffre capit. cendré",
        "Color": 0,
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Mythical_C": {
        "Name": "Coffre epave capit.",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Drunken_C": {
        "Name": "Coffre 1000 Grogs",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_ChestOfRage_C": {
        "Name": "Coffre rage",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Weeping_C": {
        "Name": "Coffre chagrin",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_EverlastingSorrow_C": {
        "Name": "Coffre chagrin éternel",
        "Color": 0,
    },
    "BP_TreasureChest_Vault_Mythical_ItemInfo_C": {
        "Name": "Coffre de capit.",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Mythical_C": {
        "Name": "Coffre de capit.",
        "Color": 0,
    }, 
    "BP_SK_CoralChest_ItemInfo_Mythical_C": {
        "Name": "Coffre corail capit.",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Legendary_DVR_C": {
        "Name": "Coffre cendré maraudeur",
        "Color": 0,
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Legendary_C": {
        "Name": "Coffre maraudeur epave",
        "Color": 0,
    },
    "BP_TreasureChest_Vault_Legendary_ItemInfo_C": {
        "Name": "Coffre maraudeur",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Legendary_C": {
        "Name": "Coffre maraudeur",
        "Color": 0,
    },
    "BP_SK_CoralChest_ItemInfo_Legendary_C": {
        "Name": "Coffre maraudeur corail",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Rare_DVR_C": {
        "Name": "Coffre marin cendré",
        "Color": 0,
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Rare_C": {
        "Name": "Coffre épave marin",
        "Color": 0,
    }, 
    "BP_TreasureChest_Vault_Rare_ItemInfo_C": {
        "Name": "Coffre d'aventurier",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Rare_C": {
        "Name": "Coffre d'aventurier",
        "Color": 0,
    },
    "BP_SK_CoralChest_ItemInfo_Rare_C": {
        "Name": "Coffre marin corail",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Common_DVR_C": {
        "Name": "Coffre naufragé cendré",
        "Color": 0,
    },
    "BP_ShipwreckTreasureChest_ItemInfo_Common_C": {
        "Name": "Coffre naufragé épave",
        "Color": 0,
    },
    "BP_TreasureChest_Vault_Common_ItemInfo_C": {
        "Name": "Coffre naufragé",
        "Color": 0,
    },
    "BP_TreasureChest_ItemInfo_Common_C": {
        "Name": "Coffre naufragé",
        "Color": 0,
    },
    "BP_SK_CoralChest_ItemInfo_Common_C":{
        "Name": "Coffre naufragé corail",
        "Color": 0,
    },
    "BP_FireworkCrate_Animals_ItemInfo_C":{
        "Name": "Caisse de feux d'artifice",
        "Color": 0,
    },
    "BP_MerchantCrate_Commodity_SilkCrate_ItemInfo_C":{
        "Name": "Caisse de soi exotique",
        "Color": 0,
    },
    "BP_MerchantCrate_Commodity_TeaCrate_ItemInfo_C":{
        "Name": "Caisse de thé rare",
        "Color": 0,
    },
    "BP_MermaidGem_ItemInfo_Sapphire_C":{
        "Name": "Saphir de sirene",
        "Color": 0,
    },
    "BP_MermaidGem_ItemInfo_Emerald_C":{
        "Name": "Emeraude de sirene",
        "Color": 0,
    },
    "BP_MermaidGem_ItemInfo_Ruby_C":{
        "Name": "Ruby de sirene",
        "Color": 0,
    },
    "BP_SirenGem_ItemInfo_Emerald_C":{
        "Name": "Emeraude de sirene",
        "Color": 0,
    },
    "BP_SirenGem_ItemInfo_Sapphire_C":{
        "Name": "Saphir de sirene",
        "Color": 0,
    },
    "BP_SirenGem_ItemInfo_Ruby_C":{
        "Name": "Ruby de sirene",
        "Color": 0,
    },
    "BP_SKMerchantCommodity_AncientMetals_ItemInfo_C":{
        "Name": "Coffre de Métaux galvaudés",
        "Color": 0,
    },
    "BP_SKMerchantCommodity_AntiCoffee_ItemInfo_C":{
        "Name": "Coffre de café de jadis",
        "Color": 0,
    },
    "BP_TreasureArtifact_ItemInfo_impressive_01_a_C":{
        "Name": "Bibelot diapré",
        "Color": 0,
    },
    "BP_TreasureArtifact_ItemInfo_box_01_a_C":{
        "Name": "Coffre décoratif",
        "Color": 0,
    },
    "BP_TreasureArtifact_ItemInfo_goblet_03_a_C":{
        "Name": "Calice Doré",
        "Color": 0,
    },
    "BP_SKLostCapSkullItemInfo_Common_C":{
        "Name": "Crane corail abject",
        "Color": 0,
    },
    "BP_SKLostCapSkullItemInfo_Mythical_C":{
        "Name": "Crane corail sordide",
        "Color": 5,
    },
    "BP_BountyRewardSkullItemInfo_Rare_C":{
        "Name": "Crane recherché vil",
        "Color": 1,
    },
    "BP_BountyRewardSkullItemInfo_Common_C":{
        "Name": "Crane recherché abject",
        "Color": 0,
    },
    "BP_BountyRewardSkullItemInfo_Mythical_C":{
        "Name": "Crane recherché sordide",
        "Color": 2,
    },
    "BP_BountyRewardSkullItemInfo_Legendary_C":{
        "Name": "Crane recherché infame",
        "Color": 3,
    },
    "BP_BountyRewardSkullItemInfo_Ghost_Common_C":{
        "Name": "Crane fantome infame",
        "Color": 0,
    },
    "BP_SeaFort_KeyVault_ItemInfo_C":{
        "Name": "Clé de la salle au trésor",
        "Color": 0,
    },
    "BP_SeaFort_Key_StoreRoom_ItemInfo_C":{
        "Name": "Clé de la réserve",
        "Color": 0,
    },
    "BP_MerchantCrate_GunpowderBarrel_ItemInfo_C":{
        "Name": "Baril de poudre",
        "Color": 0,
    },
    "BP_EmissaryFlotsam_OrderOfSouls_Rank1_ItemInfo_C":{
        "Name": "Drapeau ordre des ames Lvl1",
        "Color": 0,
    }

}

Chest_keys = set(Chestmap.keys())