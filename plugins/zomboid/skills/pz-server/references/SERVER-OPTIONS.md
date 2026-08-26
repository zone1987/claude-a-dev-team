[
 {
  "type": "boolean",
  "field": "pvp",
  "name": "PVP",
  "default": true
 },
 {
  "type": "boolean",
  "field": "pvpLogToolChat",
  "name": "PVPLogToolChat",
  "default": true
 },
 {
  "type": "boolean",
  "field": "pvpLogToolFile",
  "name": "PVPLogToolFile",
  "default": true
 },
 {
  "type": "boolean",
  "field": "pauseEmpty",
  "name": "PauseEmpty",
  "default": true
 },
 {
  "type": "boolean",
  "field": "globalChat",
  "name": "GlobalChat",
  "default": true
 },
 {
  "type": "string",
  "field": "chatStreams",
  "name": "ChatStreams",
  "default": "s,r,a,w,y,sh,f,all",
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "open",
  "name": "Open",
  "default": true
 },
 {
  "type": "text",
  "field": "serverWelcomeMessage",
  "name": "ServerWelcomeMessage",
  "default": "Welcome to Project Zomboid Multiplayer! <LINE> <LINE> To interact with the Chat panel: press Tab, T, or Enter. <LINE> <LINE> The Tab key will change the target stream of the message. <LINE> <LINE> Global Streams: /all <LINE> Local Streams: /say, /yell <LINE> Special Steams: /whisper, /safehouse, /faction. <LINE> <LINE> Press the Up arrow to cycle through your message history. Click the Gear icon to customize chat. <LINE> <LINE> Happy surviving!",
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "displayUserName",
  "name": "DisplayUserName",
  "default": true
 },
 {
  "type": "boolean",
  "field": "showFirstAndLastName",
  "name": "ShowFirstAndLastName",
  "default": false
 },
 {
  "type": "boolean",
  "field": "usernameDisguises",
  "name": "UsernameDisguises",
  "default": false
 },
 {
  "type": "boolean",
  "field": "hideDisguisedUserName",
  "name": "HideDisguisedUserName",
  "default": false
 },
 {
  "type": "boolean",
  "field": "switchZombiesOwnershipEachUpdate",
  "name": "SwitchZombiesOwnershipEachUpdate",
  "default": false
 },
 {
  "type": "string",
  "field": "spawnPoint",
  "name": "SpawnPoint",
  "default": "0,0,0",
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "safetySystem",
  "name": "SafetySystem",
  "default": true
 },
 {
  "type": "boolean",
  "field": "showSafety",
  "name": "ShowSafety",
  "default": true
 },
 {
  "type": "integer",
  "field": "safetyToggleTimer",
  "name": "SafetyToggleTimer",
  "min": 0,
  "max": 1000,
  "default": 2
 },
 {
  "type": "integer",
  "field": "safetyCooldownTimer",
  "name": "SafetyCooldownTimer",
  "min": 0,
  "max": 1000,
  "default": 3
 },
 {
  "type": "integer",
  "field": "safetyDisconnectDelay",
  "name": "SafetyDisconnectDelay",
  "min": 0,
  "max": 60,
  "default": 60
 },
 {
  "type": "string",
  "field": "spawnItems",
  "name": "SpawnItems",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "integer",
  "field": "defaultPort",
  "name": "DefaultPort",
  "min": 0,
  "max": 65535,
  "default": 16261
 },
 {
  "type": "integer",
  "field": "udpPort",
  "name": "UDPPort",
  "min": 0,
  "max": 65535,
  "default": 16262
 },
 {
  "type": "integer",
  "field": "resetId",
  "name": "ResetID",
  "min": 0,
  "max": 2147483647,
  "default": 1000000000
 },
 {
  "type": "string",
  "field": "mods",
  "name": "Mods",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "string",
  "field": "map",
  "name": "Map",
  "default": "Muldraugh, KY",
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "doLuaChecksum",
  "name": "DoLuaChecksum",
  "default": true
 },
 {
  "type": "boolean",
  "field": "denyLoginOnOverloadedServer",
  "name": "DenyLoginOnOverloadedServer",
  "default": true
 },
 {
  "type": "boolean",
  "field": "isPublic",
  "name": "Public",
  "default": false
 },
 {
  "type": "string",
  "field": "publicName",
  "name": "PublicName",
  "default": "My PZ Server",
  "maxLength": 64
 },
 {
  "type": "text",
  "field": "publicDescription",
  "name": "PublicDescription",
  "default": "",
  "maxLength": 256
 },
 {
  "type": "integer",
  "field": "maxPlayers",
  "name": "MaxPlayers",
  "min": 1,
  "max": 254,
  "default": 32
 },
 {
  "type": "integer",
  "field": "pingLimit",
  "name": "PingLimit",
  "min": 0,
  "max": 2147483647,
  "default": 0
 },
 {
  "type": "boolean",
  "field": "safehousePreventsLootRespawn",
  "name": "SafehousePreventsLootRespawn",
  "default": true
 },
 {
  "type": "boolean",
  "field": "dropOffWhiteListAfterDeath",
  "name": "DropOffWhiteListAfterDeath",
  "default": false
 },
 {
  "type": "boolean",
  "field": "noFire",
  "name": "NoFire",
  "default": false
 },
 {
  "type": "boolean",
  "field": "announceDeath",
  "name": "AnnounceDeath",
  "default": false
 },
 {
  "type": "boolean",
  "field": "announceAnimalDeath",
  "name": "AnnounceAnimalDeath",
  "default": false
 },
 {
  "type": "integer",
  "field": "saveWorldEveryMinutes",
  "name": "SaveWorldEveryMinutes",
  "min": 0,
  "max": 2147483647,
  "default": 0
 },
 {
  "type": "boolean",
  "field": "playerSafehouse",
  "name": "PlayerSafehouse",
  "default": false
 },
 {
  "type": "boolean",
  "field": "adminSafehouse",
  "name": "AdminSafehouse",
  "default": false
 },
 {
  "type": "boolean",
  "field": "safehouseAllowTrepass",
  "name": "SafehouseAllowTrepass",
  "default": true
 },
 {
  "type": "boolean",
  "field": "safehouseAllowFire",
  "name": "SafehouseAllowFire",
  "default": true
 },
 {
  "type": "boolean",
  "field": "safehouseAllowLoot",
  "name": "SafehouseAllowLoot",
  "default": true
 },
 {
  "type": "boolean",
  "field": "safehouseAllowRespawn",
  "name": "SafehouseAllowRespawn",
  "default": false
 },
 {
  "type": "integer",
  "field": "safehouseDaySurvivedToClaim",
  "name": "SafehouseDaySurvivedToClaim",
  "min": 0,
  "max": 2147483647,
  "default": 0
 },
 {
  "type": "integer",
  "field": "safeHouseRemovalTime",
  "name": "SafeHouseRemovalTime",
  "min": 0,
  "max": 2147483647,
  "default": 144
 },
 {
  "type": "boolean",
  "field": "safehouseAllowNonResidential",
  "name": "SafehouseAllowNonResidential",
  "default": false
 },
 {
  "type": "boolean",
  "field": "safehouseDisableDisguises",
  "name": "SafehouseDisableDisguises",
  "default": true
 },
 {
  "type": "integer",
  "field": "maxSafezoneSize",
  "name": "MaxSafezoneSize",
  "min": 0,
  "max": 2147483647,
  "default": 20000
 },
 {
  "type": "boolean",
  "field": "allowDestructionBySledgehammer",
  "name": "AllowDestructionBySledgehammer",
  "default": true
 },
 {
  "type": "boolean",
  "field": "sledgehammerOnlyInSafehouse",
  "name": "SledgehammerOnlyInSafehouse",
  "default": false
 },
 {
  "type": "boolean",
  "field": "war",
  "name": "War",
  "default": false
 },
 {
  "type": "integer",
  "field": "warStartDelay",
  "name": "WarStartDelay",
  "min": 60,
  "max": 2147483647,
  "default": 600
 },
 {
  "type": "integer",
  "field": "warDuration",
  "name": "WarDuration",
  "min": 60,
  "max": 2147483647,
  "default": 3600
 },
 {
  "type": "integer",
  "field": "warSafehouseHitPoints",
  "name": "WarSafehouseHitPoints",
  "min": 0,
  "max": 2147483647,
  "default": 3
 },
 {
  "type": "string",
  "field": "serverPlayerId",
  "name": "ServerPlayerID",
  "default": 2147483647,
  "maxLength": -1
 },
 {
  "type": "integer",
  "field": "rconPort",
  "name": "RCONPort",
  "min": 0,
  "max": 65535,
  "default": 27015
 },
 {
  "type": "string",
  "field": "rconPassword",
  "name": "RCONPassword",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "discordEnable",
  "name": "DiscordEnable",
  "default": false
 },
 {
  "type": "string",
  "field": "discordToken",
  "name": "DiscordToken",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "string",
  "field": "discordChatChannel",
  "name": "DiscordChatChannel",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "string",
  "field": "discordLogChannel",
  "name": "DiscordLogChannel",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "string",
  "field": "discordCommandChannel",
  "name": "DiscordCommandChannel",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "string",
  "field": "webhookAddress",
  "name": "WebhookAddress",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "string",
  "field": "password",
  "name": "Password",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "integer",
  "field": "maxAccountsPerUser",
  "name": "MaxAccountsPerUser",
  "min": 0,
  "max": 2147483647,
  "default": 0
 },
 {
  "type": "boolean",
  "field": "allowCoop",
  "name": "AllowCoop",
  "default": true
 },
 {
  "type": "boolean",
  "field": "sleepAllowed",
  "name": "SleepAllowed",
  "default": false
 },
 {
  "type": "boolean",
  "field": "sleepNeeded",
  "name": "SleepNeeded",
  "default": false
 },
 {
  "type": "boolean",
  "field": "knockedDownAllowed",
  "name": "KnockedDownAllowed",
  "default": false
 },
 {
  "type": "boolean",
  "field": "sneakModeHideFromOtherPlayers",
  "name": "SneakModeHideFromOtherPlayers",
  "default": true
 },
 {
  "type": "boolean",
  "field": "ultraSpeedDoesnotAffectToAnimals",
  "name": "UltraSpeedDoesnotAffectToAnimals",
  "default": false
 },
 {
  "type": "string",
  "field": "workshopItems",
  "name": "WorkshopItems",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "steamScoreboard",
  "name": "SteamScoreboard",
  "default": false
 },
 {
  "type": "boolean",
  "field": "steamVac",
  "name": "SteamVAC",
  "default": true
 },
 {
  "type": "boolean",
  "field": "uPnp",
  "name": "UPnP",
  "default": true
 },
 {
  "type": "boolean",
  "field": "voiceEnable",
  "name": "VoiceEnable",
  "default": true
 },
 {
  "type": "double",
  "field": "voiceMinDistance",
  "name": "VoiceMinDistance",
  "min": 0.0,
  "max": 100000.0,
  "default": 10.0
 },
 {
  "type": "double",
  "field": "voiceMaxDistance",
  "name": "VoiceMaxDistance",
  "min": 0.0,
  "max": 100000.0,
  "default": 100.0
 },
 {
  "type": "boolean",
  "field": "voice3d",
  "name": "Voice3D",
  "default": true
 },
 {
  "type": "double",
  "field": "speedLimit",
  "name": "SpeedLimit",
  "min": 10.0,
  "max": 150.0,
  "default": 70.0
 },
 {
  "type": "boolean",
  "field": "loginQueueEnabled",
  "name": "LoginQueueEnabled",
  "default": false
 },
 {
  "type": "integer",
  "field": "loginQueueConnectTimeout",
  "name": "LoginQueueConnectTimeout",
  "min": 20,
  "max": 1200,
  "default": 60
 },
 {
  "type": "string",
  "field": "serverBrowserAnnouncedIp",
  "name": "server_browser_announced_ip",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "playerRespawnWithSelf",
  "name": "PlayerRespawnWithSelf",
  "default": false
 },
 {
  "type": "boolean",
  "field": "playerRespawnWithOther",
  "name": "PlayerRespawnWithOther",
  "default": false
 },
 {
  "type": "double",
  "field": "fastForwardMultiplier",
  "name": "FastForwardMultiplier",
  "min": 1.0,
  "max": 100.0,
  "default": 40.0
 },
 {
  "type": "boolean",
  "field": "disableSafehouseWhenOwnerConnected",
  "name": "DisableSafehouseWhenOwnerConnected",
  "default": false
 },
 {
  "type": "boolean",
  "field": "faction",
  "name": "Faction",
  "default": true
 },
 {
  "type": "integer",
  "field": "factionDaySurvivedToCreate",
  "name": "FactionDaySurvivedToCreate",
  "min": 0,
  "max": 2147483647,
  "default": 0
 },
 {
  "type": "integer",
  "field": "factionPlayersRequiredForTag",
  "name": "FactionPlayersRequiredForTag",
  "min": 1,
  "max": 2147483647,
  "default": 1
 },
 {
  "type": "boolean",
  "field": "disableRadioStaff",
  "name": "DisableRadioStaff",
  "default": false
 },
 {
  "type": "boolean",
  "field": "disableRadioAdmin",
  "name": "DisableRadioAdmin",
  "default": true
 },
 {
  "type": "boolean",
  "field": "disableRadioGm",
  "name": "DisableRadioGM",
  "default": true
 },
 {
  "type": "boolean",
  "field": "disableRadioOverseer",
  "name": "DisableRadioOverseer",
  "default": false
 },
 {
  "type": "boolean",
  "field": "disableRadioModerator",
  "name": "DisableRadioModerator",
  "default": false
 },
 {
  "type": "boolean",
  "field": "disableRadioInvisible",
  "name": "DisableRadioInvisible",
  "default": true
 },
 {
  "type": "string",
  "field": "clientCommandFilter",
  "name": "ClientCommandFilter",
  "default": "-vehicle.*;+vehicle.damageWindow;+vehicle.fixPart;+vehicle.installPart;+vehicle.uninstallPart",
  "maxLength": -1
 },
 {
  "type": "string",
  "field": "clientActionLogs",
  "name": "ClientActionLogs",
  "default": "ISEnterVehicle;ISExitVehicle;ISTakeEngineParts;",
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "perkLogs",
  "name": "PerkLogs",
  "default": true
 },
 {
  "type": "integer",
  "field": "itemNumbersLimitPerContainer",
  "name": "ItemNumbersLimitPerContainer",
  "min": 0,
  "max": 9000,
  "default": 0
 },
 {
  "type": "integer",
  "field": "bloodSplatLifespanDays",
  "name": "BloodSplatLifespanDays",
  "min": 0,
  "max": 365,
  "default": 0
 },
 {
  "type": "boolean",
  "field": "allowNonAsciiUsername",
  "name": "AllowNonAsciiUsername",
  "default": false
 },
 {
  "type": "boolean",
  "field": "banKickGlobalSound",
  "name": "BanKickGlobalSound",
  "default": true
 },
 {
  "type": "boolean",
  "field": "removePlayerCorpsesOnCorpseRemoval",
  "name": "RemovePlayerCorpsesOnCorpseRemoval",
  "default": false
 },
 {
  "type": "boolean",
  "field": "trashDeleteAll",
  "name": "TrashDeleteAll",
  "default": false
 },
 {
  "type": "boolean",
  "field": "pvpMeleeWhileHitReaction",
  "name": "PVPMeleeWhileHitReaction",
  "default": false
 },
 {
  "type": "boolean",
  "field": "mouseOverToSeeDisplayName",
  "name": "MouseOverToSeeDisplayName",
  "default": true
 },
 {
  "type": "boolean",
  "field": "hidePlayersBehindYou",
  "name": "HidePlayersBehindYou",
  "default": true
 },
 {
  "type": "double",
  "field": "pvpMeleeDamageModifier",
  "name": "PVPMeleeDamageModifier",
  "min": 0.0,
  "max": 500.0,
  "default": 30.0
 },
 {
  "type": "double",
  "field": "pvpFirearmDamageModifier",
  "name": "PVPFirearmDamageModifier",
  "min": 0.0,
  "max": 500.0,
  "default": 50.0
 },
 {
  "type": "double",
  "field": "carEngineAttractionModifier",
  "name": "CarEngineAttractionModifier",
  "min": 0.0,
  "max": 10.0,
  "default": 0.5
 },
 {
  "type": "boolean",
  "field": "playerBumpPlayer",
  "name": "PlayerBumpPlayer",
  "default": false
 },
 {
  "type": "integer",
  "field": "mapRemotePlayerVisibility",
  "name": "MapRemotePlayerVisibility",
  "min": 1,
  "max": 4,
  "default": 1
 },
 {
  "type": "integer",
  "field": "backupsCount",
  "name": "BackupsCount",
  "min": 1,
  "max": 300,
  "default": 5
 },
 {
  "type": "boolean",
  "field": "backupsOnStart",
  "name": "BackupsOnStart",
  "default": true
 },
 {
  "type": "boolean",
  "field": "backupsOnVersionChange",
  "name": "BackupsOnVersionChange",
  "default": true
 },
 {
  "type": "integer",
  "field": "backupsPeriod",
  "name": "BackupsPeriod",
  "min": 0,
  "max": 1500,
  "default": 0
 },
 {
  "type": "boolean",
  "field": "disableVehicleTowing",
  "name": "DisableVehicleTowing",
  "default": false
 },
 {
  "type": "boolean",
  "field": "disableTrailerTowing",
  "name": "DisableTrailerTowing",
  "default": false
 },
 {
  "type": "boolean",
  "field": "disableBurntTowing",
  "name": "DisableBurntTowing",
  "default": false
 },
 {
  "type": "string",
  "field": "badWordListFile",
  "name": "BadWordListFile",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "string",
  "field": "goodWordListFile",
  "name": "GoodWordListFile",
  "default": "",
  "maxLength": -1
 },
 {
  "type": "enum",
  "field": "badWordPolicy",
  "name": "BadWordPolicy",
  "numValues": 3,
  "default": 3
 },
 {
  "type": "string",
  "field": "badWordReplacement",
  "name": "BadWordReplacement",
  "default": "[HIDDEN]",
  "maxLength": 16
 },
 {
  "type": "enum",
  "field": "antiCheatSafety",
  "name": "AntiCheatSafety",
  "numValues": 4,
  "default": 2
 },
 {
  "type": "enum",
  "field": "antiCheatSpeed",
  "name": "AntiCheatSpeed",
  "numValues": 4,
  "default": 2
 },
 {
  "type": "enum",
  "field": "antiCheatNoClip",
  "name": "AntiCheatNoClip",
  "numValues": 4,
  "default": 4
 },
 {
  "type": "enum",
  "field": "antiCheatHit",
  "name": "AntiCheatHit",
  "numValues": 4,
  "default": 2
 },
 {
  "type": "enum",
  "field": "antiCheatPacketException",
  "name": "AntiCheatPacketException",
  "numValues": 4,
  "default": 4
 },
 {
  "type": "enum",
  "field": "antiCheatPermission",
  "name": "AntiCheatPermission",
  "numValues": 4,
  "default": 2
 },
 {
  "type": "enum",
  "field": "antiCheatXp",
  "name": "AntiCheatXP",
  "numValues": 4,
  "default": 2
 },
 {
  "type": "enum",
  "field": "antiCheatSafeHouse",
  "name": "AntiCheatSafeHouse",
  "numValues": 4,
  "default": 2
 },
 {
  "type": "enum",
  "field": "antiCheatPlayer",
  "name": "AntiCheatPlayer",
  "numValues": 4,
  "default": 2
 },
 {
  "type": "enum",
  "field": "antiCheatChecksum",
  "name": "AntiCheatChecksum",
  "numValues": 4,
  "default": 2
 },
 {
  "type": "integer",
  "field": "multiplayerStatisticsPeriod",
  "name": "MultiplayerStatisticsPeriod",
  "min": 0,
  "max": 10,
  "default": 1
 },
 {
  "type": "boolean",
  "field": "disableScoreboard",
  "name": "DisableScoreboard",
  "default": false
 },
 {
  "type": "boolean",
  "field": "hideAdminsInPlayerList",
  "name": "HideAdminsInPlayerList",
  "default": false
 },
 {
  "type": "integer",
  "field": "maxPacketsPerSecond",
  "name": "MaxPacketsPerSecond",
  "min": 100,
  "max": 1000,
  "default": 300
 },
 {
  "type": "boolean",
  "field": "showCoordinates",
  "name": "ShowCoordinates",
  "default": false
 },
 {
  "type": "string",
  "field": "seed",
  "name": "Seed",
  "default": {
   "$ref": "zombie.network.GameServer.seed"
  },
  "maxLength": -1
 },
 {
  "type": "boolean",
  "field": "usePhysicsHitReaction",
  "name": "UsePhysicsHitReaction",
  "default": false
 },
 {
  "type": "integer",
  "field": "chatMessageCharacterLimit",
  "name": "ChatMessageCharacterLimit",
  "min": 64,
  "max": 1024,
  "default": 200
 },
 {
  "type": "integer",
  "field": "chatMessageSlowModeTime",
  "name": "ChatMessageSlowModeTime",
  "min": 1,
  "max": 30,
  "default": 3
 }
]