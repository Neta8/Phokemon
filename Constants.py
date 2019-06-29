HP = "HP"
ATK = "ATK"
DEF = "DEF"
SPATK = "SPATK"
SPDEF = "SPDEF"
SPEED = "SPEED"

PHYSICAL = "physical"
SPECIAL = "Special"

DO_ATTACK = "attack"
DO_ATTACK_SELECTION = "selected_attack"

NATURES = [
    "Hardy",
    "Lonely",
    "Brave",
    "Adamant",
    "Naughty",
    "Bold",
    "Docile",
    "Relaxed",
    "Impish",
    "Lax",
    "Timid",
    "Hasty",
    "Serious",
    "Jolly",
    "Naive",
    "Moldest",
    "Mild",
    "Quiet",
    "Bashful",
    "Rash",
    "Calm",
    "Gentle",
    "Sassy",
    "Careful",
    "Quirky"
]
NATURE_MATRIX = [
    {HP: 1, ATK: 1, DEF: 1, SPATK: 1, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1.1, DEF: 0.9, SPATK: 1, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1.1, DEF: 1, SPATK: 1, SPDEF: 1, SPEED: 0.9},
    {HP: 1, ATK: 1.1, DEF: 1, SPATK: 0.9, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1.1, DEF: 1, SPATK: 1, SPDEF: 0.9, SPEED: 1},
    {HP: 1, ATK: 0.9, DEF: 1.1, SPATK: 1, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 1, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 1.1, SPATK: 1, SPDEF: 1, SPEED: 0.9},
    {HP: 1, ATK: 1, DEF: 1.1, SPATK: 0.9, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 1.1, SPATK: 1, SPDEF: 0.9, SPEED: 1},
    {HP: 1, ATK: 0.9, DEF: 1, SPATK: 1, SPDEF: 1, SPEED: 1.1},
    {HP: 1, ATK: 1, DEF: 0.9, SPATK: 1, SPDEF: 1, SPEED: 1.1},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 1, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 0.9, SPDEF: 1, SPEED: 1.1},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 1, SPDEF: 0.9, SPEED: 1.1},
    {HP: 1, ATK: 0.9, DEF: 1, SPATK: 1.1, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 0.9, SPATK: 1.1, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 1, SPDEF: 1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 1.1, SPDEF: 0.9, SPEED: 1},
    {HP: 1, ATK: 0.9, DEF: 1, SPATK: 1, SPDEF: 1.1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 0.9, SPATK: 1, SPDEF: 1.1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 1, SPDEF: 1.1, SPEED: 0.9},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 0.9, SPDEF: 1.1, SPEED: 1},
    {HP: 1, ATK: 1, DEF: 1, SPATK: 1, SPDEF: 1, SPEED: 1}
]
