from .enums import *
from .jokers import *

ANTE_BASE_CHIPS = [
    [
        100,
        300,
        800,
        2000,
        5000,
        11000,
        20000,
        35000,
        50000,
        110000,
        560000,
        7200000,
        300000000,
        47000000000,
        2.9e13,
        7.7e16,
        8.6e20,
        4.2e25,
        9.2e30,
        9.2e36,
        4.3e43,
        9.7e50,
        1.0e59,
        5.8e67,
        1.6e77,
        2.4e87,
        1.9e98,
        8.4e109,
        2.0e122,
        2.7e135,
        2.1e149,
        9.9e163,
        2.7e179,
        4.4e195,
        4.4e212,
        2.8e230,
        1.1e249,
        2.7e268,
        4.5e288,
        4.8e309,
    ],
    [
        100,
        300,
        900,
        2600,
        8000,
        20000,
        36000,
        60000,
        100000,
        230000,
        1100000,
        14000000,
        600000000,
        94000000000,
        5.8e13,
        1.5e17,
        1.7e21,
        8.4e25,
        1.8e31,
        1.8e37,
        8.6e43,
        1.9e51,
        2.1e59,
        1.1e68,
        3.3e77,
        4.9e87,
        3.9e98,
        1.6e110,
        4.0e122,
        5.5e135,
        4.3e149,
        1.9e164,
        5.4e179,
        8.9e195,
        8.9e212,
        5.6e230,
        2.2e249,
        5.5e268,
        9.0e288,
        9.6e309,
    ],
    [
        100,
        300,
        1000,
        3200,
        9000,
        25000,
        60000,
        110000,
        200000,
        460000,
        2200000,
        29000000,
        1200000000,
        1.8e11,
        1.1e14,
        3.0e17,
        3.4e21,
        1.6e26,
        3.7e31,
        3.7e37,
        1.7e44,
        3.8e51,
        4.2e59,
        2.3e68,
        6.6e77,
        9.8e87,
        7.8e98,
        3.3e110,
        8.1e122,
        1.1e136,
        8.6e149,
        3.9e164,
        1.0e180,
        1.7e196,
        1.7e213,
        1.1e231,
        4.4e249,
        1.1e269,
        1.8e289,
        1.9e310,
    ],
]
BLIND_COLORS = {
    Blind.SMALL_BLIND: "#324ba0",
    Blind.BIG_BLIND: "#db9832",
    Blind.THE_HOOK: "#9c472d",
    Blind.THE_CLUB: "#bcca98",
    Blind.THE_PSYCHIC: "#e8c256",
    Blind.THE_GOAD: "#ad6193",
    Blind.THE_WINDOW: "#a8a296",
    Blind.THE_MANACLE: "#575757",
    Blind.THE_PILLAR: "#7a6855",
    Blind.THE_HEAD: "#a99eb2",
    Blind.THE_HOUSE: "#5d85a5",
    Blind.THE_WALL: "#835ba1",
    Blind.THE_WHEEL: "#6fbd82",
    Blind.THE_ARM: "#6765eb",
    Blind.THE_FISH: "#5183b8",
    Blind.THE_WATER: "#cbdfea",
    Blind.THE_MOUTH: "#a5748d",
    Blind.THE_NEEDLE: "#606d39",
    Blind.THE_FLINT: "#d6713f",
    Blind.THE_MARK: "#633b47",
    Blind.THE_EYE: "#5370dd",
    Blind.THE_TOOTH: "#a73933",
    Blind.THE_PLANT: "#779185",
    Blind.THE_SERPENT: "#5b9857",
    Blind.THE_OX: "#ad6025",
    Blind.AMBER_ACORN: "#f0a63a",
    Blind.VERDANT_LEAF: "#6aa588",
    Blind.VIOLET_VESSEL: "#8672da",
    Blind.CRIMSON_HEART: "#9f3c37",
    Blind.CERULEAN_BELL: "#459af6",
}
BLIND_INFO = {
    Blind.SMALL_BLIND: [1, 1, 3],
    Blind.BIG_BLIND: [1, 1.5, 4],
    Blind.THE_HOOK: [1, 2, 5],
    Blind.THE_CLUB: [1, 2, 5],
    Blind.THE_PSYCHIC: [1, 2, 5],
    Blind.THE_GOAD: [1, 2, 5],
    Blind.THE_WINDOW: [1, 2, 5],
    Blind.THE_MANACLE: [1, 2, 5],
    Blind.THE_PILLAR: [1, 2, 5],
    Blind.THE_HEAD: [1, 2, 5],
    Blind.THE_HOUSE: [2, 2, 5],
    Blind.THE_WALL: [2, 4, 5],
    Blind.THE_WHEEL: [2, 2, 5],
    Blind.THE_ARM: [2, 2, 5],
    Blind.THE_FISH: [2, 2, 5],
    Blind.THE_WATER: [2, 2, 5],
    Blind.THE_MOUTH: [2, 2, 5],
    Blind.THE_NEEDLE: [2, 1, 5],
    Blind.THE_FLINT: [2, 2, 5],
    Blind.THE_MARK: [2, 2, 5],
    Blind.THE_EYE: [3, 2, 5],
    Blind.THE_TOOTH: [3, 2, 5],
    Blind.THE_PLANT: [4, 2, 5],
    Blind.THE_SERPENT: [5, 2, 5],
    Blind.THE_OX: [6, 2, 5],
    Blind.AMBER_ACORN: [8, 2, 8],
    Blind.VERDANT_LEAF: [8, 2, 8],
    Blind.VIOLET_VESSEL: [8, 6, 8],
    Blind.CRIMSON_HEART: [8, 2, 8],
    Blind.CERULEAN_BELL: [8, 2, 8],
}
CARD_EDITION_CHANCES = {
    Edition.BASE: 92,
    Edition.POLYCHROME: 1.2,
    Edition.HOLOGRAPHIC: 2.8,
    Edition.FOIL: 4,
}
CARD_EDITION_CHANCES_GLOW_UP = {
    Edition.BASE: 68,
    Edition.POLYCHROME: 4.8,
    Edition.HOLOGRAPHIC: 11.2,
    Edition.FOIL: 16,
}
CARD_EDITION_CHANCES_HONE = {
    Edition.BASE: 84,
    Edition.POLYCHROME: 2.4,
    Edition.HOLOGRAPHIC: 5.6,
    Edition.FOIL: 8,
}
CARD_EDITION_CHANCES_ILLUSION = {
    Edition.BASE: 80,
    Edition.POLYCHROME: 3,
    Edition.HOLOGRAPHIC: 7,
    Edition.FOIL: 10,
}
# CHALLENGE_SETUPS = {
#     Challenge.THE_OMELETTE: ChallengeSetup(
#         initial_jokers=([Egg()] * 5),
#         banned_jokers={
#             JokerType.TO_THE_MOON,
#             JokerType.ROCKET,
#             JokerType.GOLDEN_JOKER,
#             JokerType.SATELLITE,
#         },
#         banned_vouchers={Voucher.SEED_MONEY, Voucher.MONEY_TREE},
#     ),
#     Challenge.FIFTEEN_MINUTE_CITY: ChallengeSetup(
#         initial_jokers=[RideTheBus(is_eternal=True), Shortcut(is_eternal=True)],
#         deck_cards=[
#             Card(rank, suit)
#             for suit in Suit
#             for rank in [
#                 Rank.KING,
#                 Rank.KING,
#                 Rank.QUEEN,
#                 Rank.QUEEN,
#                 Rank.JACK,
#                 Rank.JACK,
#                 Rank.TEN,
#                 Rank.NINE,
#                 Rank.EIGHT,
#                 Rank.SEVEN,
#                 Rank.SIX,
#                 Rank.FIVE,
#                 Rank.FOUR,
#             ]
#         ],
#     ),
#     Challenge.RICH_GET_RICHER: ChallengeSetup(
#         initial_vouchers={Voucher.SEED_MONEY, Voucher.MONEY_TREE}, starting_money=100
#     ),
#     Challenge.ON_A_KNIFES_EDGE: ChallengeSetup(
#         initial_jokers=[CeremonialDagger(is_eternal=True, is_pinned=True)]
#     ),
#     Challenge.X_RAY_VISION: ChallengeSetup(),
#     Challenge.MAD_WORLD: ChallengeSetup(
#         initial_jokers=[
#             Pareidolia(edition=Edition.NEGATIVE, is_eternal=True),
#             BusinessCard(is_eternal=True),
#         ],
#         banned_blinds={Blind.THE_PLANT},
#         deck_cards=[Card(rank, suit) for suit in Suit for rank in list(Rank)[5:]],
#     ),
#     Challenge.LUXURY_TAX: ChallengeSetup(hand_size=10),
#     Challenge.NON_PERISHABLE: ChallengeSetup(
#         banned_jokers={
#             JokerType.GROS_MICHEL,
#             JokerType.ICE_CREAM,
#             JokerType.CAVENDISH,
#             JokerType.TURTLE_BEAN,
#             JokerType.RAMEN,
#             JokerType.DIET_COLA,
#             JokerType.SELTZER,
#             JokerType.POPCORN,
#             JokerType.MR_BONES,
#             JokerType.INVISIBLE_JOKER,
#             JokerType.LUCHADOR,
#         },
#         banned_blinds={Blind.VERDANT_LEAF},
#     ),
#     Challenge.MEDUSA: ChallengeSetup(
#         initial_jokers=(MarbleJoker(is_eternal=True)),
#         deck_cards=[
#             Card(rank, suit, enhancement=(Enhancement.STONE if rank.is_face else None))
#             for suit in Suit
#             for rank in Rank
#         ],
#     ),
#     Challenge.DOUBLE_OR_NOTHING: ChallengeSetup(
#         deck_cards=[Card(rank, suit, seal=Seal.RED) for suit in Suit for rank in Rank]
#     ),
#     Challenge.TYPECAST: ChallengeSetup(banned_blinds={Blind.VERDANT_LEAF}),
#     Challenge.INFLATION: ChallengeSetup(
#         initial_jokers=[CreditCard()],
#         banned_vouchers={Voucher.CLEARANCE_SALE, Voucher.LIQUIDATION},
#     ),
#     Challenge.BRAM_POKER: ChallengeSetup(
#         initial_jokers=[Vampire(is_eternal=True)],
#         initial_consumables=[
#             Consumable(Tarot.THE_EMPRESS),
#             Consumable(Tarot.THE_EMPEROR),
#         ],
#         initial_vouchers={Voucher.MAGIC_TRICK, Voucher.ILLUSION},
#     ),
#     Challenge.FRAGILE: ChallengeSetup(
#         initial_jokers=[OopsAllSixes(edition=Edition.NEGATIVE, is_eternal=True)] * 2
#     ),
# }
EDITION_COSTS = {
    Edition.BASE: 0,
    Edition.FOIL: 2,
    Edition.HOLOGRAPHIC: 3,
    Edition.POLYCHROME: 5,
    Edition.NEGATIVE: 5,
}
HAND_BASE_SCORE = {
    PokerHand.FLUSH_FIVE: [160, 16.0],
    PokerHand.FLUSH_HOUSE: [140, 14.0],
    PokerHand.FIVE_OF_A_KIND: [120, 12.0],
    PokerHand.STRAIGHT_FLUSH: [100, 8.0],
    PokerHand.FOUR_OF_A_KIND: [60, 7.0],
    PokerHand.FULL_HOUSE: [40, 4.0],
    PokerHand.FLUSH: [35, 4.0],
    PokerHand.STRAIGHT: [30, 4.0],
    PokerHand.THREE_OF_A_KIND: [30, 3.0],
    PokerHand.TWO_PAIR: [20, 2.0],
    PokerHand.PAIR: [10, 2.0],
    PokerHand.HIGH_CARD: [5, 1.0],
}
HAND_SCALING = {
    PokerHand.FLUSH_FIVE: [50, 3.0],
    PokerHand.FLUSH_HOUSE: [40, 4.0],
    PokerHand.FIVE_OF_A_KIND: [35, 3.0],
    PokerHand.STRAIGHT_FLUSH: [40, 4.0],
    PokerHand.FOUR_OF_A_KIND: [30, 3.0],
    PokerHand.FULL_HOUSE: [25, 2.0],
    PokerHand.FLUSH: [15, 2.0],
    PokerHand.STRAIGHT: [30, 3.0],
    PokerHand.THREE_OF_A_KIND: [20, 2.0],
    PokerHand.TWO_PAIR: [20, 1.0],
    PokerHand.PAIR: [15, 1.0],
    PokerHand.HIGH_CARD: [10, 1.0],
}
JOKER_BASE_COSTS = {
    JokerType.JOKER: 2,
    JokerType.GREEDY_JOKER: 5,
    JokerType.LUSTY_JOKER: 5,
    JokerType.WRATHFUL_JOKER: 5,
    JokerType.GLUTTONOUS_JOKER: 5,
    JokerType.JOLLY_JOKER: 3,
    JokerType.ZANY_JOKER: 4,
    JokerType.MAD_JOKER: 4,
    JokerType.CRAZY_JOKER: 4,
    JokerType.DROLL_JOKER: 4,
    JokerType.SLY_JOKER: 3,
    JokerType.WILY_JOKER: 4,
    JokerType.CLEVER_JOKER: 4,
    JokerType.DEVIOUS_JOKER: 4,
    JokerType.CRAFTY_JOKER: 4,
    JokerType.HALF_JOKER: 5,
    JokerType.CREDIT_CARD: 1,
    JokerType.BANNER: 5,
    JokerType.MYSTIC_SUMMIT: 5,
    JokerType.EIGHT_BALL: 5,
    JokerType.MISPRINT: 4,
    JokerType.RAISED_FIST: 5,
    JokerType.CHAOS_THE_CLOWN: 4,
    JokerType.SCARY_FACE: 4,
    JokerType.ABSTRACT_JOKER: 4,
    JokerType.DELAYED_GRATIFICATION: 4,
    JokerType.GROS_MICHEL: 5,
    JokerType.EVEN_STEVEN: 4,
    JokerType.ODD_TODD: 4,
    JokerType.SCHOLAR: 4,
    JokerType.BUSINESS_CARD: 4,
    JokerType.SUPERNOVA: 5,
    JokerType.RIDE_THE_BUS: 6,
    JokerType.EGG: 4,
    JokerType.RUNNER: 5,
    JokerType.ICE_CREAM: 5,
    JokerType.SPLASH: 3,
    JokerType.BLUE_JOKER: 5,
    JokerType.FACELESS_JOKER: 4,
    JokerType.GREEN_JOKER: 4,
    JokerType.SUPERPOSITION: 4,
    JokerType.TODO_LIST: 4,
    JokerType.CAVENDISH: 4,
    JokerType.RED_CARD: 5,
    JokerType.SQUARE_JOKER: 4,
    JokerType.RIFF_RAFF: 6,
    JokerType.PHOTOGRAPH: 5,
    JokerType.RESERVED_PARKING: 6,
    JokerType.MAIL_IN_REBATE: 4,
    JokerType.HALLUCINATION: 4,
    JokerType.FORTUNE_TELLER: 6,
    JokerType.JUGGLER: 4,
    JokerType.DRUNKARD: 4,
    JokerType.GOLDEN_JOKER: 6,
    JokerType.POPCORN: 5,
    JokerType.WALKIE_TALKIE: 4,
    JokerType.SMILEY_FACE: 4,
    JokerType.GOLDEN_TICKET: 5,
    JokerType.SWASHBUCKLER: 4,
    JokerType.HANGING_CHAD: 4,
    JokerType.SHOOT_THE_MOON: 5,
    JokerType.JOKER_STENCIL: 8,
    JokerType.FOUR_FINGERS: 7,
    JokerType.MIME: 5,
    JokerType.CEREMONIAL_DAGGER: 6,
    JokerType.MARBLE_JOKER: 6,
    JokerType.LOYALTY_CARD: 5,
    JokerType.DUSK: 5,
    JokerType.FIBONACCI: 8,
    JokerType.STEEL_JOKER: 7,
    JokerType.HACK: 6,
    JokerType.PAREIDOLIA: 5,
    JokerType.SPACE_JOKER: 5,
    JokerType.BURGLAR: 6,
    JokerType.BLACKBOARD: 6,
    JokerType.SIXTH_SENSE: 6,
    JokerType.CONSTELLATION: 6,
    JokerType.HIKER: 5,
    JokerType.CARD_SHARP: 6,
    JokerType.MADNESS: 7,
    JokerType.SEANCE: 6,
    JokerType.VAMPIRE: 7,
    JokerType.SHORTCUT: 7,
    JokerType.HOLOGRAM: 7,
    JokerType.CLOUD_NINE: 7,
    JokerType.ROCKET: 6,
    JokerType.MIDAS_MASK: 7,
    JokerType.LUCHADOR: 5,
    JokerType.GIFT_CARD: 6,
    JokerType.TURTLE_BEAN: 6,
    JokerType.EROSION: 6,
    JokerType.TO_THE_MOON: 5,
    JokerType.STONE: 6,
    JokerType.LUCKY_CAT: 6,
    JokerType.BULL: 6,
    JokerType.DIET_COLA: 6,
    JokerType.TRADING_CARD: 6,
    JokerType.FLASH_CARD: 5,
    JokerType.SPARE_TROUSERS: 6,
    JokerType.RAMEN: 6,
    JokerType.SELTZER: 6,
    JokerType.CASTLE: 6,
    JokerType.MR_BONES: 5,
    JokerType.ACROBAT: 6,
    JokerType.SOCK_AND_BUSKIN: 6,
    JokerType.TROUBADOUR: 6,
    JokerType.CERTIFICATE: 6,
    JokerType.SMEARED_JOKER: 7,
    JokerType.THROWBACK: 6,
    JokerType.ROUGH_GEM: 7,
    JokerType.BLOODSTONE: 7,
    JokerType.ARROWHEAD: 7,
    JokerType.ONYX_AGATE: 7,
    JokerType.GLASS_JOKER: 6,
    JokerType.SHOWMAN: 5,
    JokerType.FLOWER_POT: 6,
    JokerType.MERRY_ANDY: 7,
    JokerType.OOPS_ALL_SIXES: 4,
    JokerType.THE_IDOL: 6,
    JokerType.SEEING_DOUBLE: 6,
    JokerType.MATADOR: 7,
    JokerType.SATELLITE: 6,
    JokerType.CARTOMANCER: 6,
    JokerType.ASTRONOMER: 8,
    JokerType.BOOTSTRAPS: 7,
    JokerType.DNA: 8,
    JokerType.VAGABOND: 8,
    JokerType.BARON: 8,
    JokerType.OBELISK: 8,
    JokerType.BASEBALL_CARD: 8,
    JokerType.ANCIENT_JOKER: 8,
    JokerType.CAMPFIRE: 9,
    JokerType.BLUEPRINT: 10,
    JokerType.WEE_JOKER: 8,
    JokerType.HIT_THE_ROAD: 8,
    JokerType.THE_DUO: 8,
    JokerType.THE_TRIO: 8,
    JokerType.THE_FAMILY: 8,
    JokerType.THE_ORDER: 8,
    JokerType.THE_TRIBE: 8,
    JokerType.STUNTMAN: 7,
    JokerType.INVISIBLE_JOKER: 8,
    JokerType.BRAINSTORM: 10,
    JokerType.DRIVERS_LICENSE: 7,
    JokerType.BURNT_JOKER: 8,
    JokerType.CANIO: 20,
    JokerType.TRIBOULET: 20,
    JokerType.YORICK: 20,
    JokerType.CHICOT: 20,
    JokerType.PERKEO: 20,
}
JOKER_EDITION_CHANCES = {
    Edition.BASE: 96,
    Edition.NEGATIVE: 0.3,
    Edition.POLYCHROME: 0.3,
    Edition.HOLOGRAPHIC: 1.4,
    Edition.FOIL: 2,
}
JOKER_EDITION_CHANCES_HONE = {
    Edition.BASE: 92,
    Edition.NEGATIVE: 0.3,
    Edition.POLYCHROME: 0.9,
    Edition.HOLOGRAPHIC: 2.8,
    Edition.FOIL: 4,
}
JOKER_EDITION_CHANCES_GLOW_UP = {
    Edition.BASE: 84,
    Edition.NEGATIVE: 0.3,
    Edition.POLYCHROME: 2.1,
    Edition.HOLOGRAPHIC: 5.6,
    Edition.FOIL: 8,
}
JOKER_BASE_RARITY_WEIGHTS = {Rarity.COMMON: 70, Rarity.UNCOMMON: 25, Rarity.RARE: 5}
JOKER_CLASSES = {
    JokerType.BLUEPRINT: Blueprint,
    JokerType.BRAINSTORM: Brainstorm,
    JokerType.SPACE_JOKER: SpaceJoker,
    JokerType.DNA: DNA,
    JokerType.TODO_LIST: ToDoList,
    JokerType.MIDAS_MASK: MidasMask,
    JokerType.GREEDY_JOKER: GreedyJoker,
    JokerType.LUSTY_JOKER: LustyJoker,
    JokerType.WRATHFUL_JOKER: WrathfulJoker,
    JokerType.GLUTTONOUS_JOKER: GluttonousJoker,
    JokerType.EIGHT_BALL: EightBall,
    JokerType.DUSK: Dusk,
    JokerType.FIBONACCI: Fibonacci,
    JokerType.SCARY_FACE: ScaryFace,
    JokerType.HACK: Hack,
    JokerType.EVEN_STEVEN: EvenSteven,
    JokerType.ODD_TODD: OddTodd,
    JokerType.SCHOLAR: Scholar,
    JokerType.BUSINESS_CARD: BusinessCard,
    JokerType.HIKER: Hiker,
    JokerType.PHOTOGRAPH: Photograph,
    JokerType.ANCIENT_JOKER: AncientJoker,
    JokerType.WALKIE_TALKIE: WalkieTalkie,
    JokerType.SELTZER: Seltzer,
    JokerType.SMILEY_FACE: SmileyFace,
    JokerType.GOLDEN_TICKET: GoldenTicket,
    JokerType.SOCK_AND_BUSKIN: SockAndBuskin,
    JokerType.HANGING_CHAD: HangingChad,
    JokerType.ROUGH_GEM: RoughGem,
    JokerType.BLOODSTONE: Bloodstone,
    JokerType.ARROWHEAD: Arrowhead,
    JokerType.ONYX_AGATE: OnyxAgate,
    JokerType.THE_IDOL: TheIdol,
    JokerType.TRIBOULET: Triboulet,
    JokerType.MIME: Mime,
    JokerType.RAISED_FIST: RaisedFist,
    JokerType.BARON: Baron,
    JokerType.RESERVED_PARKING: ReservedParking,
    JokerType.SHOOT_THE_MOON: ShootTheMoon,
    JokerType.JOKER: Joker,
    JokerType.JOLLY_JOKER: JollyJoker,
    JokerType.ZANY_JOKER: ZanyJoker,
    JokerType.MAD_JOKER: MadJoker,
    JokerType.CRAZY_JOKER: CrazyJoker,
    JokerType.DROLL_JOKER: DrollJoker,
    JokerType.SLY_JOKER: SlyJoker,
    JokerType.WILY_JOKER: WilyJoker,
    JokerType.CLEVER_JOKER: CleverJoker,
    JokerType.DEVIOUS_JOKER: DeviousJoker,
    JokerType.CRAFTY_JOKER: CraftyJoker,
    JokerType.HALF_JOKER: HalfJoker,
    JokerType.JOKER_STENCIL: JokerStencil,
    JokerType.CEREMONIAL_DAGGER: CeremonialDagger,
    JokerType.BANNER: Banner,
    JokerType.MYSTIC_SUMMIT: MysticSummit,
    JokerType.LOYALTY_CARD: LoyaltyCard,
    JokerType.MISPRINT: Misprint,
    JokerType.STEEL_JOKER: SteelJoker,
    JokerType.ABSTRACT_JOKER: AbstractJoker,
    JokerType.GROS_MICHEL: GrosMichel,
    JokerType.SUPERNOVA: Supernova,
    JokerType.BLACKBOARD: Blackboard,
    JokerType.ICE_CREAM: IceCream,
    JokerType.BLUE_JOKER: BlueJoker,
    JokerType.CONSTELLATION: Constellation,
    JokerType.SUPERPOSITION: Superposition,
    JokerType.CAVENDISH: Cavendish,
    JokerType.CARD_SHARP: CardSharp,
    JokerType.RED_CARD: RedCard,
    JokerType.MADNESS: Madness,
    JokerType.SEANCE: Seance,
    JokerType.HOLOGRAM: Hologram,
    JokerType.VAGABOND: Vagabond,
    JokerType.EROSION: Erosion,
    JokerType.FORTUNE_TELLER: FortuneTeller,
    JokerType.STONE: StoneJoker,
    JokerType.BULL: Bull,
    JokerType.FLASH_CARD: FlashCard,
    JokerType.POPCORN: Popcorn,
    JokerType.CAMPFIRE: Campfire,
    JokerType.ACROBAT: Acrobat,
    JokerType.SWASHBUCKLER: Swashbuckler,
    JokerType.THROWBACK: Throwback,
    JokerType.GLASS_JOKER: GlassJoker,
    JokerType.FLOWER_POT: FlowerPot,
    JokerType.SEEING_DOUBLE: SeeingDouble,
    JokerType.MATADOR: Matador,
    JokerType.THE_DUO: TheDuo,
    JokerType.THE_TRIO: TheTrio,
    JokerType.THE_FAMILY: TheFamily,
    JokerType.THE_ORDER: TheOrder,
    JokerType.THE_TRIBE: TheTribe,
    JokerType.STUNTMAN: Stuntman,
    JokerType.DRIVERS_LICENSE: DriversLicense,
    JokerType.BOOTSTRAPS: Bootstraps,
    JokerType.CANIO: Canio,
    JokerType.RIDE_THE_BUS: RideTheBus,
    JokerType.RUNNER: Runner,
    JokerType.GREEN_JOKER: GreenJoker,
    JokerType.SQUARE_JOKER: SquareJoker,
    JokerType.VAMPIRE: Vampire,
    JokerType.OBELISK: Obelisk,
    JokerType.LUCKY_CAT: LuckyCat,
    JokerType.SPARE_TROUSERS: SpareTrousers,
    JokerType.RAMEN: Ramen,
    JokerType.CASTLE: Castle,
    JokerType.WEE_JOKER: WeeJoker,
    JokerType.HIT_THE_ROAD: HitTheRoad,
    JokerType.YORICK: Yorick,
    JokerType.BASEBALL_CARD: BaseballCard,
    JokerType.FACELESS_JOKER: FacelessJoker,
    JokerType.MAIL_IN_REBATE: MailInRebate,
    JokerType.TRADING_CARD: TradingCard,
    JokerType.BURNT_JOKER: BurntJoker,
    JokerType.FOUR_FINGERS: FourFingers,
    JokerType.CREDIT_CARD: CreditCard,
    JokerType.MARBLE_JOKER: MarbleJoker,
    JokerType.CHAOS_THE_CLOWN: ChaosTheClown,
    JokerType.DELAYED_GRATIFICATION: DelayedGratification,
    JokerType.PAREIDOLIA: Pareidolia,
    JokerType.EGG: Egg,
    JokerType.BURGLAR: Burglar,
    JokerType.SPLASH: Splash,
    JokerType.SIXTH_SENSE: SixthSense,
    JokerType.RIFF_RAFF: RiffRaff,
    JokerType.SHORTCUT: Shortcut,
    JokerType.CLOUD_NINE: CloudNine,
    JokerType.ROCKET: Rocket,
    JokerType.LUCHADOR: Luchador,
    JokerType.GIFT_CARD: GiftCard,
    JokerType.TURTLE_BEAN: TurtleBean,
    JokerType.TO_THE_MOON: ToTheMoon,
    JokerType.HALLUCINATION: Hallucination,
    JokerType.JUGGLER: Juggler,
    JokerType.DRUNKARD: Drunkard,
    JokerType.GOLDEN_JOKER: GoldenJoker,
    JokerType.DIET_COLA: DietCola,
    JokerType.MR_BONES: MrBones,
    JokerType.TROUBADOUR: Troubadour,
    JokerType.CERTIFICATE: Certificate,
    JokerType.SMEARED_JOKER: SmearedJoker,
    JokerType.SHOWMAN: Showman,
    JokerType.MERRY_ANDY: MerryAndy,
    JokerType.OOPS_ALL_SIXES: OopsAllSixes,
    JokerType.INVISIBLE_JOKER: InvisibleJoker,
    JokerType.SATELLITE: Satellite,
    JokerType.CARTOMANCER: Cartomancer,
    JokerType.ASTRONOMER: Astronomer,
    JokerType.CHICOT: Chicot,
    JokerType.PERKEO: Perkeo,
}
JOKER_TYPE_RARITIES = {
    Rarity.COMMON: list(JokerType)[:61],
    Rarity.UNCOMMON: list(JokerType)[61 : 61 + 64],
    Rarity.RARE: list(JokerType)[61 + 64 : 61 + 64 + 20],
    Rarity.LEGENDARY: list(JokerType)[61 + 64 + 20 : 61 + 64 + 20 + 5],
}
NON_ETERNAL_JOKERS = {
    JokerType.GROS_MICHEL,
    JokerType.ICE_CREAM,
    JokerType.CAVENDISH,
    JokerType.POPCORN,
    JokerType.LUCHADOR,
    JokerType.TURTLE_BEAN,
    JokerType.DIET_COLA,
    JokerType.RAMEN,
    JokerType.SELTZER,
    JokerType.MR_BONES,
    JokerType.INVISIBLE_JOKER,
}
NON_PERISHABLE_JOKERS = {
    JokerType.RIDE_THE_BUS,
    JokerType.RUNNER,
    JokerType.GREEN_JOKER,
    JokerType.RED_CARD,
    JokerType.SQUARE_JOKER,
    JokerType.CEREMONIAL_DAGGER,
    JokerType.CONSTELLATION,
    JokerType.MADNESS,
    JokerType.VAMPIRE,
    JokerType.HOLOGRAM,
    JokerType.ROCKET,
    JokerType.LUCKY_CAT,
    JokerType.FLASH_CARD,
    JokerType.SPARE_TROUSERS,
    JokerType.CASTLE,
    JokerType.GLASS_JOKER,
    JokerType.OBELISK,
    JokerType.WEE_JOKER,
}
PROHIBITED_ANTE_1_TAGS = {
    Tag.NEGATIVE,
    Tag.STANDARD,
    Tag.METEOR,
    Tag.BUFFOON,
    Tag.HANDY,
    Tag.GARBAGE,
    Tag.ETHEREAL,
    Tag.TOP_UP,
    Tag.ORBITAL,
}
SHOP_BASE_CARD_WEIGHTS = {BaseJoker: 20, Tarot: 4, Planet: 4}
SHOP_BASE_PACK_WEIGHTS = {
    Pack.ARCANA: 4,
    Pack.JUMBO_ARCANA: 2,
    Pack.MEGA_ARCANA: 0.5,
    Pack.CELESTIAL: 4,
    Pack.JUMBO_CELESTIAL: 2,
    Pack.MEGA_CELESTIAL: 0.5,
    Pack.SPECTRAL: 0.6,
    Pack.JUMBO_SPECTRAL: 0.3,
    Pack.MEGA_SPECTRAL: 0.07,
    Pack.STANDARD: 4,
    Pack.JUMBO_STANDARD: 2,
    Pack.MEGA_STANDARD: 0.5,
    Pack.BUFFOON: 1.2,
    Pack.JUMBO_BUFFOON: 0.6,
    Pack.MEGA_BUFFOON: 0.5,
}
TAG_PACKS = {
    Tag.BUFFOON: Pack.MEGA_BUFFOON,
    Tag.CHARM: Pack.MEGA_ARCANA,
    Tag.METEOR: Pack.MEGA_CELESTIAL,
    Tag.ETHEREAL: Pack.SPECTRAL,
    Tag.STANDARD: Pack.MEGA_STANDARD,
}
UPGRADED_EDITION_WEIGHTS = {
    Edition.FOIL: 12.5,
    Edition.HOLOGRAPHIC: 8.75,
    Edition.POLYCHROME: 3.75,
}
