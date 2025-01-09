from balatro_enums import *
from balatro_jokers import *

NON_COPYABLE_JOKERS = {
    JokerType.CREDIT_CARD,
    JokerType.CHAOS,
    JokerType.DELAYED_GRAT,
    JokerType.EGG,
    JokerType.SPLASH,
    JokerType.JUGGLER,
    JokerType.DRUNKARD,
    JokerType.GOLDEN,
    JokerType.FOUR_FINGERS,
    JokerType.PAREIDOLIA,
    JokerType.SIXTH_SENSE,
    JokerType.SHORTCUT,
    JokerType.CLOUD_9,
    JokerType.ROCKET,
    JokerType.MIDAS_MASK,
    JokerType.GIFT,
    JokerType.TURTLE_BEAN,
    JokerType.TO_THE_MOON,
    JokerType.TRADING,
    JokerType.MR_BONES,
    JokerType.TROUBADOUR,
    JokerType.SMEARED,
    JokerType.RING_MASTER,
    JokerType.MERRY_ANDY,
    JokerType.OOPS,
    JokerType.SATELLITE,
    JokerType.ASTRONOMER,
    JokerType.INVISIBLE,
    JokerType.CHICOT,
}

JOKER_CLASSES = {
    JokerType.BLUEPRINT: Blueprint,
    JokerType.BRAINSTORM: Brainstorm,
    JokerType.SPACE: SpaceJoker,
    JokerType.DNA: DNA,
    JokerType.TODO_LIST: ToDoList,
    JokerType.MIDAS_MASK: MidasMask,
    JokerType.GREEDY_JOKER: GreedyJoker,
    JokerType.LUSTY_JOKER: LustyJoker,
    JokerType.WRATHFUL_JOKER: WrathfulJoker,
    JokerType.GLUTTENOUS_JOKER: GluttonousJoker,
    JokerType.EIGHT_BALL: EightBall,
    JokerType.DUSK: Dusk,
    JokerType.FIBONACCI: Fibonacci,
    JokerType.SCARY_FACE: ScaryFace,
    JokerType.HACK: Hack,
    JokerType.EVEN_STEVEN: EvenSteven,
    JokerType.ODD_TODD: OddTodd,
    JokerType.SCHOLAR: Scholar,
    JokerType.BUSINESS: BusinessCard,
    JokerType.HIKER: Hiker,
    JokerType.PHOTOGRAPH: Photograph,
    JokerType.ANCIENT: AncientJoker,
    JokerType.WALKIE_TALKIE: WalkieTalkie,
    JokerType.SELZER: Seltzer,
    JokerType.SMILEY: SmileyFace,
    JokerType.TICKET: GoldenTicket,
    JokerType.SOCK_AND_BUSKIN: SockAndBuskin,
    JokerType.HANGING_CHAD: HangingChad,
    JokerType.ROUGH_GEM: RoughGem,
    JokerType.BLOODSTONE: Bloodstone,
    JokerType.ARROWHEAD: Arrowhead,
    JokerType.ONYX_AGATE: OnyxAgate,
    JokerType.IDOL: TheIdol,
    JokerType.TRIBOULET: Triboulet,
    # ----
    JokerType.MIME: Mime,
    JokerType.RAISED_FIST: RaisedFist,
    JokerType.BARON: Baron,
    JokerType.RESERVED_PARKING: ReservedParking,
    JokerType.SHOOT_THE_MOON: ShootTheMoon,
    JokerType.JOKER: Jimbo,
    JokerType.JOLLY: JollyJoker,
    JokerType.ZANY: ZanyJoker,
    JokerType.MAD: MadJoker,
    JokerType.CRAZY: CrazyJoker,
    JokerType.DROLL: DrollJoker,
    JokerType.SLY: SlyJoker,
    JokerType.WILY: WilyJoker,
    JokerType.CLEVER: CleverJoker,
    JokerType.DEVIOUS: DeviousJoker,
    JokerType.CRAFTY: CraftyJoker,
    JokerType.HALF: HalfJoker,
    JokerType.STENCIL: JokerStencil,
}
