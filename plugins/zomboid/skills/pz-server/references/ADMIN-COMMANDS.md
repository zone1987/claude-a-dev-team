[
 {
  "class": "zombie.commands.serverCommands.AddAllToWhiteListCommand",
  "commandName": "addalltowhitelist",
  "aliases": [],
  "argVariants": [],
  "capability": "ManipulateWhitelist",
  "helpKey": "UI_ServerOptionDesc_AddAllWhitelist",
  "helpText": null,
  "disabled": true,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   " <LINE>",
   "User",
   " doesn\\'t have a password. <LINE>",
   "Done.",
   "\\u0001 created user \\u0001 with password \\u0001"
  ],
  "messageTemplates": [
   "\\u0001 created user \\u0001 with password \\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AddItemCommand",
  "commandName": "additem",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "([a-zA-Z0-9.-]*[a-zA-Z][a-zA-Z0-9_.-]*)"
    ],
    "optional": "(\\\\d+)",
    "argName": "add item to player"
   },
   {
    "required": [
     "([a-zA-Z0-9.-]*[a-zA-Z][a-zA-Z0-9_.-]*)"
    ],
    "optional": "(\\\\d+)",
    "argName": "add item to me"
   }
  ],
  "capability": "AddItem",
  "helpKey": "UI_ServerOptionDesc_AddItem",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "add item to me",
   "Pass username",
   "add item to player",
   "Cannot spawn over 100 items at a time",
   "No such user",
   "admin",
   "Item \\u0001 doesn\\'t exist.",
   "\\u0001 added item \\u0001 in \\u0001\\'s inventory",
   "Item \\u0001 Added in \\u0001\\'s inventory.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "Item \\u0001 doesn\\'t exist.",
   "\\u0001 added item \\u0001 in \\u0001\\'s inventory",
   "Item \\u0001 Added in \\u0001\\'s inventory.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AddKeyCommand",
  "commandName": "addkey",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(\\\\d+)"
    ],
    "optional": "(.+)",
    "argName": "add item to player"
   },
   {
    "required": [
     "(\\\\d+)"
    ],
    "optional": "(.+)",
    "argName": "add item to me"
   }
  ],
  "capability": "AddItem",
  "helpKey": "UI_ServerOptionDesc_AddKey",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "add item to me",
   "Pass username",
   "add item to player",
   "No such user",
   "Base.Key1",
   "admin",
   "\\u0001 added item \\u0001 in \\u0001\\'s inventory",
   "Key \\u0001 Added in \\u0001\\'s inventory.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "\\u0001 added item \\u0001 in \\u0001\\'s inventory",
   "Key \\u0001 Added in \\u0001\\'s inventory.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AddSteamIDCommand",
  "commandName": "addsteamid",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "ModifyNetworkUsers",
  "helpKey": "UI_ServerOptionDesc_AddSteamID",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "exception occurs",
   "Invalid steamID \\\"\\u0001\\\"",
   "\\u0001 tried to create user with SteamID \\u0001 but it already exists in allowed SteamIDs",
   "SteamID \\u0001 already exists in allowed SteamIDs",
   "\\u0001 added allowed SteamID \\u0001\\u0001"
  ],
  "messageTemplates": [
   "Invalid steamID \\\"\\u0001\\\"",
   "\\u0001 tried to create user with SteamID \\u0001 but it already exists in allowed SteamIDs",
   "SteamID \\u0001 already exists in allowed SteamIDs",
   "\\u0001 added allowed SteamID \\u0001\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AddUserCommand",
  "commandName": "adduser",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "optional": "(.+)"
   }
  ],
  "capability": "ModifyNetworkUsers",
  "helpKey": "UI_ServerOptionDesc_AddUser",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "\\u0001 created user \\u0001 with password \\u0001",
   "\\u0001 created user \\u0001 without password"
  ],
  "messageTemplates": [
   "\\u0001 created user \\u0001 with password \\u0001",
   "\\u0001 created user \\u0001 without password"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AddUserToSafehouseCommand",
  "commandName": "addtosafehouse",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(.+)"
    ]
   }
  ],
  "capability": "CanSetupSafehouses",
  "helpKey": "UI_ServerOptionDesc_AddToSafehouse",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Safehouse \\u0001 not found",
   "Player \\u0001 is already a member of safehouse",
   "Cannot find player with username \\u0001",
   "Cannot find connection for player \\u0001",
   "\\u0001 invited user \\u0001 to safehouse \\u0001",
   "Player \\u0001 invited to safehouse \\u0001"
  ],
  "messageTemplates": [
   "Safehouse \\u0001 not found",
   "Player \\u0001 is already a member of safehouse",
   "Cannot find player with username \\u0001",
   "Cannot find connection for player \\u0001",
   "\\u0001 invited user \\u0001 to safehouse \\u0001",
   "Player \\u0001 invited to safehouse \\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AddUserToWhiteListCommand",
  "commandName": "addusertowhitelist",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "ManipulateWhitelist",
  "helpKey": "UI_ServerOptionDesc_AddWhitelist",
  "helpText": null,
  "disabled": true,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "Invalid username \\\"\\u0001\\\"",
   "\\u0001 created user \\u0001 with password \\u0001",
   "User \\u0001 doesn\\'t have a password.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "Invalid username \\\"\\u0001\\\"",
   "\\u0001 created user \\u0001 with password \\u0001",
   "User \\u0001 doesn\\'t have a password.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AddVehicleCommand",
  "commandName": "addvehicle",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "([a-zA-Z0-9.-]*[a-zA-Z][a-zA-Z0-9_.-]*)"
    ],
    "argName": "Script Only"
   },
   {
    "required": [
     "([a-zA-Z0-9.-]*[a-zA-Z][a-zA-Z0-9_.-]*)",
     "(-?\\\\d+.*\\\\d*),(-?\\\\d+.*\\\\d*),(-?\\\\d+.*\\\\d*)"
    ],
    "argName": "Script And Coordinate"
   },
   {
    "required": [
     "([a-zA-Z0-9.-]*[a-zA-Z][a-zA-Z0-9_.-]*)",
     "(.+)"
    ],
    "argName": "Script And Player"
   }
  ],
  "capability": "ManipulateVehicle",
  "helpKey": "UI_ServerOptionDesc_AddVehicle",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Script And Player",
   "Script And Coordinate",
   "Pass a username or coordinate",
   "Z coordinate must be 0 for now",
   "Vehicle spawned",
   "ERROR: I can not spawn the vehicle. Invalid position. Try to change position.",
   "Script Only",
   "Unknown vehicle script \\\"\\u0001\\\"",
   "\\u0001.\\u0001",
   "User \\\"\\u0001\\\" not found",
   "Invalid location \\u0001,\\u0001,\\u0001"
  ],
  "messageTemplates": [
   "Unknown vehicle script \\\"\\u0001\\\"",
   "\\u0001.\\u0001",
   "User \\\"\\u0001\\\" not found",
   "Invalid location \\u0001,\\u0001,\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AddXPCommand",
  "commandName": "addxp",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(\\\\S+)"
    ],
    "optional": "(-true|-false)"
   }
  ],
  "capability": "AddXP",
  "helpKey": "UI_ServerOptionDesc_AddXp",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "No such user",
   "=",
   "\\n",
   " LINE",
   "-true",
   "admin",
   "List of available perks :\\u0001\\u0001",
   "\\u0001 added \\u0001 \\u0001 xp\\'s to \\u0001",
   "Added \\u0001 \\u0001 xp\\'s to \\u0001",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "List of available perks :\\u0001\\u0001",
   "\\u0001 added \\u0001 \\u0001 xp\\'s to \\u0001",
   "Added \\u0001 \\u0001 xp\\'s to \\u0001",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.AlarmCommand",
  "commandName": "alarm",
  "aliases": [],
  "argVariants": [],
  "capability": "MakeEventsAlarmGunshot",
  "helpKey": "UI_ServerOptionDesc_Alarm",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Alarm sounded",
   "Not in a room"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.ArgType",
  "commandName": null,
  "note": "no CommandName/CommandNames annotation",
  "super": "java.lang.Object"
 },
 {
  "class": "zombie.commands.serverCommands.BanIPCommand",
  "commandName": "banip",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "((?:\\\\d{1,3}\\\\.){3}\\\\d{1,3})"
    ]
   }
  ],
  "capability": "BanUnbanUser",
  "helpKey": "UI_ServerOptionDesc_BanIp",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.BanSteamIDCommand",
  "commandName": "banid",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "BanUnbanUser",
  "helpKey": "UI_ServerOptionDesc_BanSteamId",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Server is not in Steam mode",
   "Expected SteamID but got \\\"\\u0001\\\""
  ],
  "messageTemplates": [
   "Expected SteamID but got \\\"\\u0001\\\""
  ]
 },
 {
  "class": "zombie.commands.serverCommands.BanUserCommand",
  "commandName": "banuser",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "argName": "Ban User Only"
   },
   {
    "required": [
     "(.+)",
     "-ip"
    ],
    "argName": "Ban User And IP"
   },
   {
    "required": [
     "(.+)",
     "-r",
     "(.+)"
    ],
    "argName": "Ban User And Supply Reason"
   },
   {
    "required": [
     "(.+)",
     "-ip",
     "-r",
     "(.+)"
    ],
    "argName": "Ban User And IP And Supply Reason"
   }
  ],
  "capability": "BanUnbanUser",
  "helpKey": "UI_ServerOptionDesc_BanUser",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Ban User And IP",
   "Ban User And IP And Supply Reason",
   "Thunder",
   "Ban User Only",
   "Ban User And Supply Reason"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.ChangeOptionCommand",
  "commandName": "changeoption",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(\\\\w+)",
     "(.*)"
    ]
   }
  ],
  "capability": "ChangeAndReloadServerOptions",
  "helpKey": "UI_ServerOptionDesc_ChangeOptions",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Password",
   "ClientCommandFilter",
   "admin",
   "\\u0001 changed option \\u0001=\\u0001",
   "\\u0001(\\u0001)"
  ],
  "messageTemplates": [
   "\\u0001 changed option \\u0001=\\u0001",
   "\\u0001(\\u0001)"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.CheckModsNeedUpdate",
  "commandName": "checkModsNeedUpdate",
  "aliases": [],
  "argVariants": [],
  "capability": "ManipulateMods",
  "helpKey": "UI_ServerOptionDesc_CheckModsNeedUpdate",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Checking started. The answer will be written in the log file and in the chat"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.ChopperCommand",
  "commandName": "chopper",
  "aliases": [],
  "argVariants": [
   {
    "optional": "([a-zA-Z0-9.-]*[a-zA-Z][a-zA-Z0-9_.-]*)"
   }
  ],
  "capability": "MakeEventsAlarmGunshot",
  "helpKey": "UI_ServerOptionDesc_Chopper",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "stop",
   "Chopper deactivated",
   "start",
   "Chopper activated",
   "Chopper launched",
   "admin",
   "\\u0001 did chopper"
  ],
  "messageTemplates": [
   "\\u0001 did chopper"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.ClearCommand",
  "commandName": "clear",
  "aliases": [],
  "argVariants": [],
  "capability": "LoginOnServer",
  "helpKey": null,
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Console cleared",
   "<LINE>",
   "\\u0001\\u0001"
  ],
  "messageTemplates": [
   "\\u0001\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.ConnectionsCommand",
  "commandName": "connections",
  "aliases": [
   "list"
  ],
  "argVariants": [],
  "capability": "SeePlayersConnected",
  "helpKey": "UI_ServerOptionDesc_Connections",
  "helpText": null,
  "disabled": true,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   " <LINE>",
   "\\n",
   "\\u0001connection=\\u0001/\\u0001 \\u0001 player=\\u0001/4 id=\\u0001 username=\\\"\\u0001\\\" fullyConnected=\\u0001\\u0001",
   "\\u0001Players listed"
  ],
  "messageTemplates": [
   "\\u0001connection=\\u0001/\\u0001 \\u0001 player=\\u0001/4 id=\\u0001 username=\\\"\\u0001\\\" fullyConnected=\\u0001\\u0001",
   "\\u0001Players listed"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.CreateHorde2Command",
  "commandName": "createhorde2",
  "aliases": [],
  "argVariants": [
   {
    "varArgs": true
   }
  ],
  "capability": "CreateHorde",
  "helpKey": "UI_ServerOptionDesc_CreateHorde2",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "-count",
   "-radius",
   "-x",
   "-y",
   "-z",
   "-outfit",
   "-crawler",
   "-isFallOnFront",
   "-isFakeDead",
   "-knockedDown",
   "-isInvulnerable",
   "-isSitting",
   "-health",
   "-isRecordingAnims",
   "-heightOffset",
   "-isRagdolling",
   "-onFire",
   "false",
   "Zombie spawn commands are capped at 500 maximum zombies per command",
   "invalid location",
   "admin",
   "IMPORTANT",
   "Horde spawned.",
   "invalid outfit \\u0001",
   "\\u0001 created a horde of \\u0001 zombies near \\u0001,\\u0001"
  ],
  "messageTemplates": [
   "invalid outfit \\u0001",
   "\\u0001 created a horde of \\u0001 zombies near \\u0001,\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.CreateHordeCommand",
  "commandName": "createhorde",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(\\\\d+)"
    ],
    "optional": "(.+)"
   }
  ],
  "capability": "CreateHorde",
  "helpKey": "UI_ServerOptionDesc_CreateHorde",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "IMPORTANT",
   "Horde spawned.",
   "Specify a player to create the horde near to.",
   "User \\\"\\u0001\\\" not found",
   "\\u0001 created a horde of \\u0001 zombies near \\u0001,\\u0001"
  ],
  "messageTemplates": [
   "User \\\"\\u0001\\\" not found",
   "\\u0001 created a horde of \\u0001 zombies near \\u0001,\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.DebugPlayerCommand",
  "commandName": "debugplayer",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "ConnectWithDebug",
  "helpKey": null,
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "/debugplayer \\\"username\\\"",
   "no such user",
   "no connection for user",
   "debug off",
   "debug on"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.GodModeCommand",
  "commandName": "godmod",
  "aliases": [
   "godmode"
  ],
  "argVariants": [
   {
    "optional": "(-true|-false)"
   }
  ],
  "capability": "ToggleGodModHimself",
  "helpKey": "UI_ServerOptionDesc_GodMod",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "-true",
   "admin",
   "\\u0001 enabled godmode on \\u0001",
   "User \\u0001 is now invincible.",
   "\\u0001 disabled godmode on \\u0001",
   "User \\u0001 is no longer invincible.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "\\u0001 enabled godmode on \\u0001",
   "User \\u0001 is now invincible.",
   "\\u0001 disabled godmode on \\u0001",
   "User \\u0001 is no longer invincible.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.GodModePlayerCommand",
  "commandName": "godmodplayer",
  "aliases": [
   "godmodeplayer"
  ],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "optional": "(-true|-false)"
   }
  ],
  "capability": "ToggleGodModEveryone",
  "helpKey": "UI_ServerOptionDesc_GodModPlayer",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "-true",
   "-false",
   "Wrong arguments!",
   "admin",
   "\\u0001 enabled godmode on \\u0001",
   "User \\u0001 is now invincible.",
   "\\u0001 disabled godmode on \\u0001",
   "User \\u0001 is no longer invincible.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "\\u0001 enabled godmode on \\u0001",
   "User \\u0001 is now invincible.",
   "\\u0001 disabled godmode on \\u0001",
   "User \\u0001 is no longer invincible.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.GrantAdminCommand",
  "commandName": "grantadmin",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "ChangeAccessLevel",
  "helpKey": null,
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.GunShotCommand",
  "commandName": "gunshot",
  "aliases": [],
  "argVariants": [],
  "capability": "MakeEventsAlarmGunshot",
  "helpKey": "UI_ServerOptionDesc_Gunshot",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "Gunshot fired",
   "\\u0001 did gunshot"
  ],
  "messageTemplates": [
   "\\u0001 did gunshot"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.HelpCommand",
  "commandName": "help",
  "aliases": [],
  "argVariants": [
   {
    "optional": "(\\\\w+)"
   }
  ],
  "capability": "LoginOnServer",
  "helpKey": "UI_ServerOptionDesc_Help",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   " <LINE>",
   "\\n",
   "List of",
   "server",
   " commands :",
   "*",
   " :",
   "Unknown command /\\u0001"
  ],
  "messageTemplates": [
   "Unknown command /\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.InvisibleCommand",
  "commandName": "invisible",
  "aliases": [],
  "argVariants": [
   {
    "optional": "(-true|-false)"
   }
  ],
  "capability": "ToggleInvisibleHimself",
  "helpKey": "UI_ServerOptionDesc_Invisible",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "-false",
   "-true",
   "admin",
   "\\u0001 enabled invisibility on \\u0001",
   "User \\u0001 is now invisible.",
   "\\u0001 disabled invisibility on \\u0001",
   "User \\u0001 is no longer invisible.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "\\u0001 enabled invisibility on \\u0001",
   "User \\u0001 is now invisible.",
   "\\u0001 disabled invisibility on \\u0001",
   "User \\u0001 is no longer invisible.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.InvisiblePlayerCommand",
  "commandName": "invisibleplayer",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "optional": "(-true|-false)"
   }
  ],
  "capability": "ToggleInvisibleEveryone",
  "helpKey": "UI_ServerOptionDesc_InvisiblePlayer",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "-true",
   "-false",
   "Wrong arguments!",
   "admin",
   "\\u0001 enabled invisibility on \\u0001",
   "User \\u0001 is now invisible.",
   "\\u0001 disabled invisibility on \\u0001",
   "User \\u0001 is no longer invisible.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "\\u0001 enabled invisibility on \\u0001",
   "User \\u0001 is now invisible.",
   "\\u0001 disabled invisibility on \\u0001",
   "User \\u0001 is no longer invisible.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.KickUserCommand",
  "commandName": "kick",
  "aliases": [
   "kickuser"
  ],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   },
   {
    "required": [
     "(.+)",
     "-r",
     "(.+)"
    ]
   }
  ],
  "capability": "KickUser",
  "helpKey": "UI_ServerOptionDesc_Kick",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "UI_Policy_Kick",
   "UI_Policy_KickReason",
   "command-kick",
   "This user can\\'t be kicked.",
   "RumbleThunder",
   "\\u0001 kicked user \\u0001",
   "User \\u0001 kicked.",
   "User \\u0001 doesn\\'t exist."
  ],
  "messageTemplates": [
   "\\u0001 kicked user \\u0001",
   "User \\u0001 kicked.",
   "User \\u0001 doesn\\'t exist."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.KickUserFromSafehouseCommand",
  "commandName": "kickfromsafehouse",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(.+)"
    ]
   }
  ],
  "capability": "CanSetupSafehouses",
  "helpKey": "UI_ServerOptionDesc_KickFromSafehouse",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Safehouse \\u0001 not found",
   "Player \\u0001 not a member of safehouse \\u0001",
   "\\u0001 kicked user \\u0001 from safehouse \\u0001",
   "Player \\u0001 kicked from a safehouse \\u0001"
  ],
  "messageTemplates": [
   "Safehouse \\u0001 not found",
   "Player \\u0001 not a member of safehouse \\u0001",
   "\\u0001 kicked user \\u0001 from safehouse \\u0001",
   "Player \\u0001 kicked from a safehouse \\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.LightningCommand",
  "commandName": "lightning",
  "aliases": [],
  "argVariants": [
   {
    "optional": "(.+)"
   }
  ],
  "capability": "MakeEventsAlarmGunshot",
  "helpKey": "UI_ServerOptionDesc_Lightning",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Pass a username",
   "admin",
   "Lightning triggered",
   "User \\\"\\u0001\\\" not found",
   "\\u0001 thunder start"
  ],
  "messageTemplates": [
   "User \\\"\\u0001\\\" not found",
   "\\u0001 thunder start"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.ListCommand",
  "commandName": "list",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "LoginOnServer",
  "helpKey": "UI_ServerOptionDesc_List",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "animals",
   "Server animals list:\\n",
   "Client animals list:\\n",
   "*",
   "world",
   "hutch",
   "\\n",
   "Subsystem error:"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.LogCommand",
  "commandName": "log",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(.+)"
    ]
   }
  ],
  "capability": "DebugConsole",
  "helpKey": "UI_ServerOptionDesc_SetLogLevel",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Debug type \\\"%s\\\" log level is set to \\\"%s\\\"",
   "all",
   "All debug type log levels are set to \\\"%s\\\"",
   "save",
   "DebugLog save succeeded",
   "DebugLog save failed",
   "All packet types logging is enabled",
   "none",
   "All packet types logging is disabled",
   "Packet type \\\"%s\\\" logging is \\\"%s\\\"",
   "enabled",
   "disabled",
   "UI_ServerOptionDesc_SetLogLevel",
   "\\\"packet type\\\"",
   "\\\"log severity\\\""
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.NoClipCommand",
  "commandName": "noclip",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "optional": "(-true|-false)"
   },
   {
    "optional": "(-true|-false)"
   }
  ],
  "capability": "ToggleNoclipHimself",
  "helpKey": "UI_ServerOptionDesc_NoClip",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "-true",
   "-false",
   "Not enough rights",
   "admin",
   "\\u0001 enabled noclip on \\u0001",
   "User \\u0001 won\\'t collide.",
   "\\u0001 disabled noclip on \\u0001",
   "User \\u0001 will collide.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "\\u0001 enabled noclip on \\u0001",
   "User \\u0001 won\\'t collide.",
   "\\u0001 disabled noclip on \\u0001",
   "User \\u0001 will collide.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.PlayersCommand",
  "commandName": "players",
  "aliases": [],
  "argVariants": [],
  "capability": "SeePlayersConnected",
  "helpKey": "UI_ServerOptionDesc_Players",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   " <LINE>",
   "\\n",
   "-",
   "Players connected (\\u0001):"
  ],
  "messageTemplates": [
   "Players connected (\\u0001):"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.QuitCommand",
  "commandName": "quit",
  "aliases": [],
  "argVariants": [],
  "capability": "QuitWorld",
  "helpKey": "UI_ServerOptionDesc_Quit",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "Quit",
   "\\u0001 closed server"
  ],
  "messageTemplates": [
   "\\u0001 closed server"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.ReleaseSafehouseCommand",
  "commandName": "releasesafehouse",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "CanSetupSafehouses",
  "helpKey": "UI_ServerOptionDesc_ReleaseSafeHouse",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Safehouse \\u0001 not found",
   "\\u0001 released safehouse \\u0001",
   "Safehouse \\u0001 released"
  ],
  "messageTemplates": [
   "Safehouse \\u0001 not found",
   "\\u0001 released safehouse \\u0001",
   "Safehouse \\u0001 released"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.ReloadAllLuaCommand",
  "commandName": "reloadalllua",
  "aliases": [
   "reloadluaall"
  ],
  "argVariants": [],
  "capability": "ReloadLuaFiles",
  "helpKey": "UI_ServerOptionDesc_ReloadLua",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Lua files reloaded",
   "\\u0001 Reloaded \\u0001/\\u0001"
  ],
  "messageTemplates": [
   "\\u0001 Reloaded \\u0001/\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.ReloadLuaCommand",
  "commandName": "reloadlua",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(\\\\S+)"
    ]
   }
  ],
  "capability": "ReloadLuaFiles",
  "helpKey": "UI_ServerOptionDesc_ReloadLua",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Lua file reloaded",
   "Unknown Lua file"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.ReloadOptionsCommand",
  "commandName": "reloadoptions",
  "aliases": [],
  "argVariants": [],
  "capability": "ChangeAndReloadServerOptions",
  "helpKey": "UI_ServerOptionDesc_ReloadOptions",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "Options reloaded",
   "\\u0001 reloaded options"
  ],
  "messageTemplates": [
   "\\u0001 reloaded options"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.RemoveAdminCommand",
  "commandName": "removeadmin",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "ChangeAccessLevel",
  "helpKey": null,
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.RemoveCommand",
  "commandName": "remove",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "AnimalCheats",
  "helpKey": "UI_ServerOptionDesc_Remove",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "animals",
   "Animals removed",
   "zombies",
   "Zombies removed",
   "corpses",
   "Corpses removed",
   "vehicles",
   "Vehicles removed",
   "Subsystem error: \\u0001"
  ],
  "messageTemplates": [
   "Subsystem error: \\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.RemoveItemCommand",
  "commandName": "removeitem",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "([a-zA-Z0-9.-]*[a-zA-Z][a-zA-Z0-9_.-]*)",
     "(\\\\d+)"
    ]
   }
  ],
  "capability": "EditItem",
  "helpKey": "UI_ServerOptionDesc_RemoveItem",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "%s removed %d items %s from inventory",
   "admin",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.RemoveMapSymbolsForUserCommand",
  "commandName": "removemapsymbolsforuser",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "argName": "Remove Map Symbols For User"
   }
  ],
  "capability": "EditMapSymbols",
  "helpKey": "UI_ServerOptionDesc_RemoveMapSymbolsForUser",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "removed %d symbols",
   "Remove Map Symbols For User"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.RemoveSteamIDCommand",
  "commandName": "removesteamid",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "ModifyNetworkUsers",
  "helpKey": "UI_ServerOptionDesc_RemoveSteamID",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "exception occurs",
   "Invalid steamID \\\"\\u0001\\\"",
   "\\u0001 tried to remove user with SteamID \\u0001 but it doesn\\'t exists in allowed SteamIDs",
   "SteamID \\u0001 doesn\\'t exists in allowed SteamIDs",
   "\\u0001 removed allowed SteamID \\u0001\\u0001"
  ],
  "messageTemplates": [
   "Invalid steamID \\\"\\u0001\\\"",
   "\\u0001 tried to remove user with SteamID \\u0001 but it doesn\\'t exists in allowed SteamIDs",
   "SteamID \\u0001 doesn\\'t exists in allowed SteamIDs",
   "\\u0001 removed allowed SteamID \\u0001\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.RemoveUserFromWhiteList",
  "commandName": "removeuserfromwhitelist",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "ManipulateWhitelist",
  "helpKey": "UI_ServerOptionDesc_RemoveWhitelist",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "\\u0001 removed user \\u0001 from whitelist"
  ],
  "messageTemplates": [
   "\\u0001 removed user \\u0001 from whitelist"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.RemoveZombiesCommand",
  "commandName": "removezombies",
  "aliases": [],
  "argVariants": [
   {
    "varArgs": true
   }
  ],
  "capability": "ManipulateZombie",
  "helpKey": "UI_ServerOptionDesc_RemoveZombies",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "-radius",
   "-reanimated",
   "-x",
   "-y",
   "-z",
   "-remove",
   "Zombies removed.",
   "invalid z",
   "admin",
   "IMPORTANT",
   "\\u0001 removed zombies near \\u0001,\\u0001"
  ],
  "messageTemplates": [
   "\\u0001 removed zombies near \\u0001,\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.SaveCommand",
  "commandName": "save",
  "aliases": [],
  "argVariants": [],
  "capability": "SaveWorld",
  "helpKey": "UI_ServerOptionDesc_Save",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "World saved"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.ServerMessageCommand",
  "commandName": "servermsg",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "DisplayServerMessage",
  "helpKey": "UI_ServerOptionDesc_ServerMsg",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Message sent."
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.SetAccessLevelCommand",
  "commandName": "setaccesslevel",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(\\\\w+)"
    ]
   }
  ],
  "capability": "ChangeAccessLevel",
  "helpKey": "UI_ServerOptionDesc_SetAccessLevel",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "none"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.SetPasswordCommand",
  "commandName": "setpassword",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(.+)"
    ]
   }
  ],
  "capability": "ModifyNetworkUsers",
  "helpKey": "UI_ServerOptionDesc_SetPassword",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "exception occurs",
   "\\u0001 changing password for the \\u0001"
  ],
  "messageTemplates": [
   "\\u0001 changing password for the \\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.SetTimeSpeedCommand",
  "commandName": "setTimeSpeed",
  "aliases": [
   "sts"
  ],
  "argVariants": [
   {
    "required": [
     "(\\\\d+)"
    ]
   }
  ],
  "capability": "ConnectWithDebug",
  "helpKey": "UI_ServerOptionDesc_SetTimeSpeed",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Multiplier was set on the following value: \\u0001"
  ],
  "messageTemplates": [
   "Multiplier was set on the following value: \\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.ShowOptionsCommand",
  "commandName": "showoptions",
  "aliases": [],
  "argVariants": [],
  "capability": "SeePublicServerOptions",
  "helpKey": "UI_ServerOptionDesc_ShowOptions",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   " <LINE>",
   "\\n",
   "ServerWelcomeMessage",
   "List of Server Options:\\u0001",
   "\\u0001* \\u0001=\\u0001\\u0001",
   "\\u0001* ServerWelcomeMessage=\\u0001"
  ],
  "messageTemplates": [
   "List of Server Options:\\u0001",
   "\\u0001* \\u0001=\\u0001\\u0001",
   "\\u0001* ServerWelcomeMessage=\\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.StartRainCommand",
  "commandName": "startrain",
  "aliases": [],
  "argVariants": [
   {
    "optional": "(\\\\d+)"
   }
  ],
  "capability": "StartStopRain",
  "helpKey": "UI_ServerOptionDesc_StartRain",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Invalid intensity value",
   "admin",
   "Rain started",
   "\\u0001 started rain"
  ],
  "messageTemplates": [
   "\\u0001 started rain"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.StartStormCommand",
  "commandName": "startstorm",
  "aliases": [],
  "argVariants": [
   {
    "optional": "(\\\\d+)"
   }
  ],
  "capability": "StartStopRain",
  "helpKey": "UI_ServerOptionDesc_StartStorm",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Invalid duration value",
   "admin",
   "Thunderstorm started",
   "\\u0001 started thunderstorm"
  ],
  "messageTemplates": [
   "\\u0001 started thunderstorm"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.StatisticsCommand",
  "commandName": "stats",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "optional": "(.+)"
   }
  ],
  "capability": "GetStatistic",
  "helpKey": "UI_ServerOptionDesc_Statistics",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "list",
   ",",
   "version",
   "all"
  ],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.StopRainCommand",
  "commandName": "stoprain",
  "aliases": [],
  "argVariants": [],
  "capability": "StartStopRain",
  "helpKey": "UI_ServerOptionDesc_StopRain",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "Rain stopped",
   "\\u0001 stopped rain"
  ],
  "messageTemplates": [
   "\\u0001 stopped rain"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.StopWeatherCommand",
  "commandName": "stopweather",
  "aliases": [],
  "argVariants": [],
  "capability": "StartStopRain",
  "helpKey": "UI_ServerOptionDesc_StopWeather",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "admin",
   "Weather stopped",
   "\\u0001 stopped weather"
  ],
  "messageTemplates": [
   "\\u0001 stopped weather"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.TeleportCommand",
  "commandName": "teleport",
  "aliases": [
   "tp"
  ],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "TeleportToPlayer",
  "helpKey": "UI_ServerOptionDesc_Teleport",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Need player to teleport to, ex /teleport user1 user2",
   "admin",
   "\\u0001 teleport to \\u0001",
   "teleported to \\u0001 please wait two seconds to show the map around you.",
   "Can\\'t find player \\u0001"
  ],
  "messageTemplates": [
   "\\u0001 teleport to \\u0001",
   "teleported to \\u0001 please wait two seconds to show the map around you.",
   "Can\\'t find player \\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.TeleportPlayerCommand",
  "commandName": "teleportplayer",
  "aliases": [
   "tpp"
  ],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(.+)"
    ]
   }
  ],
  "capability": "TeleportPlayerToAnotherPlayer",
  "helpKey": "UI_ServerOptionDesc_TeleportPlayer",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "An Observer can only teleport himself",
   "admin",
   "Can\\'t find player \\u0001",
   "No connection for player \\u0001",
   "\\u0001 teleported \\u0001 to \\u0001",
   "teleported \\u0001 to \\u0001"
  ],
  "messageTemplates": [
   "Can\\'t find player \\u0001",
   "No connection for player \\u0001",
   "\\u0001 teleported \\u0001 to \\u0001",
   "teleported \\u0001 to \\u0001"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.TeleportToCommand",
  "commandName": "teleportto",
  "aliases": [
   "tpto"
  ],
  "argVariants": [
   {
    "required": [
     "(.+)",
     "(-?\\\\d+.*\\\\d*),(-?\\\\d+.*\\\\d*),(-?\\\\d+.*\\\\d*)"
    ],
    "argName": "Teleport user"
   },
   {
    "required": [
     "(-?\\\\d+.*\\\\d*),(-?\\\\d+.*\\\\d*),(-?\\\\d+.*\\\\d*)"
    ],
    "argName": "teleport me"
   }
  ],
  "capability": "TeleportToCoordinates",
  "helpKey": "UI_ServerOptionDesc_TeleportTo",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "teleport me",
   "Teleport user",
   "An Observer can only teleport himself",
   "Error",
   "admin",
   "\\u0001 teleported to \\u0001,\\u0001,\\u0001",
   "teleported to \\u0001,\\u0001,\\u0001 please wait two seconds to show the map around you.",
   "Can\\'t find player \\u0001",
   "\\u0001 teleported to \\u0001,\\u0001,\\u0001 please wait two seconds to show the map around you."
  ],
  "messageTemplates": [
   "\\u0001 teleported to \\u0001,\\u0001,\\u0001",
   "teleported to \\u0001,\\u0001,\\u0001 please wait two seconds to show the map around you.",
   "Can\\'t find player \\u0001",
   "\\u0001 teleported to \\u0001,\\u0001,\\u0001 please wait two seconds to show the map around you."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.ThunderCommand",
  "commandName": "thunder",
  "aliases": [],
  "argVariants": [
   {
    "optional": "(.+)"
   }
  ],
  "capability": "StartStopRain",
  "helpKey": "UI_ServerOptionDesc_Thunder",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Pass a username",
   "admin",
   "Thunder triggered",
   "User \\\"\\u0001\\\" not found",
   "\\u0001 thunder start"
  ],
  "messageTemplates": [
   "User \\\"\\u0001\\\" not found",
   "\\u0001 thunder start"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.UnbanIPCommand",
  "commandName": "unbanip",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "((?:\\\\d{1,3}\\\\.){3}\\\\d{1,3})"
    ]
   }
  ],
  "capability": "BanUnbanUser",
  "helpKey": "UI_ServerOptionDesc_UnBanIp",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.UnbanSteamIDCommand",
  "commandName": "unbanid",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "BanUnbanUser",
  "helpKey": "UI_ServerOptionDesc_UnBanSteamId",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "Server is not in Steam mode",
   "Expected SteamID but got \\\"\\u0001\\\"",
   "SteamID \\u0001 is now unbanned"
  ],
  "messageTemplates": [
   "Expected SteamID but got \\\"\\u0001\\\"",
   "SteamID \\u0001 is now unbanned"
  ]
 },
 {
  "class": "zombie.commands.serverCommands.UnbanUserCommand",
  "commandName": "unbanuser",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ]
   }
  ],
  "capability": "BanUnbanUser",
  "helpKey": "UI_ServerOptionDesc_UnBanUser",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [],
  "messageTemplates": []
 },
 {
  "class": "zombie.commands.serverCommands.VoiceBanCommand",
  "commandName": "voiceban",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "optional": "(-true|-false)"
   },
   {
    "optional": "(-true|-false)"
   }
  ],
  "capability": "BanUnbanUser",
  "helpKey": "UI_ServerOptionDesc_VoiceBan",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "-true",
   "-false",
   "admin",
   "\\u0001 ban voice \\u0001",
   "User \\u0001 voice is banned.",
   "\\u0001 unban voice \\u0001",
   "User \\u0001 voice is unbanned.",
   "User \\u0001 not found."
  ],
  "messageTemplates": [
   "\\u0001 ban voice \\u0001",
   "User \\u0001 voice is banned.",
   "\\u0001 unban voice \\u0001",
   "User \\u0001 voice is unbanned.",
   "User \\u0001 not found."
  ]
 },
 {
  "class": "zombie.commands.serverCommands.WorldGeneratorCommand",
  "commandName": "worldgen",
  "aliases": [],
  "argVariants": [
   {
    "required": [
     "(.+)"
    ],
    "optional": "(.+)"
   }
  ],
  "capability": "SaveWorld",
  "helpKey": "UI_ServerOptionDesc_Worldgen",
  "helpText": null,
  "disabled": false,
  "super": "zombie.commands.CommandBase",
  "stringConstants": [
   "slow",
   "start",
   "recheck",
   "stop",
   "Stopped",
   "status",
   "Preparing for generating map: \\u0001/\\u0001 using \\u0001 threads",
   "Generating map: \\u0001/\\u0001 using \\u0001 threads"
  ],
  "messageTemplates": [
   "Preparing for generating map: \\u0001/\\u0001 using \\u0001 threads",
   "Generating map: \\u0001/\\u0001 using \\u0001 threads"
  ]
 }
]