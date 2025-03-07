from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from balatro import Run

from .enums import *


class BalatroError(Exception):
    """Base class for all Balatro-sepcific exceptions"""


class IllegalActionError(BalatroError):
    """Raised when an action is not allowed in the current state"""


class InvalidArgumentsError(BalatroError):
    """Raised when an action is attempted with invalid arguments"""


class HandSizeOfOneError(IllegalActionError):
    """Raised when an action cannot be performed due to a hand size of one"""


class IllegalBossRerollError(IllegalActionError):
    """Raised when a boss is attempted to be rerolled without the sufficient Voucher"""


class IllegalFoolUseError(IllegalActionError):
    """Raised when the Fool is attempted to be used to create an illegal Consumable"""


class IllegalSkipError(IllegalActionError):
    """Raised when a boss blind is attempted to be skipped"""


class InsufficientFundsError(IllegalActionError):
    """Raised when an action requires more money than available"""


class NoDiscardsRemainingError(IllegalActionError):
    """Raised when discards are attempted when none are left"""


class NotEnoughSpaceError(IllegalActionError):
    """Raised when an action requires more Joker or Consumable slots than available"""


class NoValidJokersError(IllegalActionError):
    """Raised when there are no valid Jokers to be acted upon"""


class EternalJokerSoldError(InvalidArgumentsError):
    """Raised when an eternal Joker is attempted to be sold"""


class MissingForcedSelectedCardError(InvalidArgumentsError):
    """Raised when a hand is played without the Cerulean Bell's forced selected card"""


class PinnedJokerMovedError(InvalidArgumentsError):
    """Raised when a pinned Joker is attempted to be moved"""


@dataclass(eq=False)
class Sellable:
    _extra_sell_value: int = field(default=0, init=False, repr=False)


@dataclass(eq=False)
class BalatroJoker(Sellable):
    _run: Run | None = field(default=None, init=False, repr=False)

    edition: Edition = Edition.BASE
    is_eternal: bool = False
    is_perishable: bool = False
    is_rental: bool = False

    is_debuffed: bool = field(default=False, init=False, repr=False)
    is_flipped: bool = field(default=False, init=False, repr=False)
    num_perishable_rounds_left: int = field(default=5, init=False, repr=False)

    def __post_init__(self) -> None:
        if self.is_eternal and self.is_perishable:
            raise ValueError("Jokers cannot be both eternal and perishable.")

    def __eq__(self, other: BalatroJoker | type[BalatroJoker] | Edition) -> bool:
        match other:
            case BalatroJoker():
                return self is other
            case type() if issubclass(other, BalatroJoker):
                return not self.is_debuffed and isinstance(self, other)
            case Edition():
                return (
                    not self.is_debuffed or other is Edition.NEGATIVE
                ) and self.edition is other

        return NotImplemented

    def __hash__(self) -> int:
        return id(self)

    def __str__(self) -> str:
        raise NotImplementedError

    def _repr_png_(self, card_back: Deck = Deck.RED) -> bytes:
        from .sprites import get_sprite

        return get_sprite(self, card_back=card_back, as_image=False)

    def _blind_selected_ability(self) -> None:
        pass

    def _blind_selected_action(self) -> None:
        pass

    def _boss_blind_triggered_ability(self) -> None:
        pass

    def _boss_defeated_action(self) -> None:
        pass

    def _card_added_action(self, added_card: Card) -> None:
        pass

    def _card_destroyed_action(self, destroyed_card: Card) -> None:
        pass

    def _card_held_ability(self, held_card: Card) -> None:
        pass

    def _card_held_retriggers(self, held_card: Card) -> int:
        return 0

    def _card_scored_ability(
        self,
        scored_card: Card,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        pass

    def _card_scored_action(
        self,
        scored_card: Card,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        pass

    def _card_scored_retriggers(
        self,
        scored_card: Card,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> int:
        return 0

    def _created_action(self) -> None:
        pass

    def _dependent_ability(self, other_joker: BalatroJoker) -> None:
        pass

    def _discard_ability(self, discarded_cards: list[Card]) -> None:
        pass

    def _discard_action(self, discarded_cards: list[Card]) -> None:
        pass

    def _hand_played_ability(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        pass

    def _hand_played_action(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        pass

    def _independent_ability(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        pass

    def _item_sold_action(self, sold_item: Sellable) -> None:
        pass

    def _lucky_card_triggered_action(self) -> None:
        pass

    def _on_blind_selected(self) -> None:
        if self.is_debuffed or self not in self._run._jokers:
            return

        self._blind_selected_ability()
        self._blind_selected_action()

    def _on_boss_blind_triggered(self) -> None:
        if self.is_debuffed:
            return

        self._boss_blind_triggered_ability()

    def _on_boss_defeated(self) -> None:
        if self.is_debuffed:
            return

        self._boss_defeated_action()

    def _on_card_added(self, added_card: Card) -> None:
        if self.is_debuffed:
            return

        self._card_added_action(added_card)

    def _on_card_destroyed(self, destroyed_card: Card) -> None:
        if self.is_debuffed:
            return

        self._card_destroyed_action(destroyed_card)

    def _on_card_held(self, held_card: Card) -> None:
        if self.is_debuffed:
            return

        self._card_held_ability(held_card)

    def _on_card_held_retriggers(self, held_card: Card) -> int:
        if self.is_debuffed:
            return 0

        return self._card_held_retriggers(held_card)

    def _on_card_scored(
        self,
        scored_card: Card,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        if self.is_debuffed:
            return

        self._card_scored_action(
            scored_card, played_cards, scored_card_indices, poker_hands_played
        )
        self._card_scored_ability(
            scored_card, played_cards, scored_card_indices, poker_hands_played
        )

    def _on_card_scored_retriggers(
        self,
        scored_card: Card,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> int:
        if self.is_debuffed:
            return 0

        return self._card_scored_retriggers(
            scored_card, played_cards, scored_card_indices, poker_hands_played
        )

    def _on_created(self, run: Run) -> None:
        self._run = run
        self._created_action()

    def _on_dependent(self, other_joker: BalatroJoker) -> None:
        if self.is_debuffed:
            return

        self._dependent_ability(other_joker)

    def _on_discard(self, discarded_cards: list[Card]) -> None:
        if self.is_debuffed:
            return

        self._discard_action(discarded_cards)
        self._discard_ability(discarded_cards)

    def _on_hand_played(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        if self.is_debuffed:
            return

        self._hand_played_action(played_cards, scored_card_indices, poker_hands_played)
        self._hand_played_ability(played_cards, scored_card_indices, poker_hands_played)

    def _on_independent(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        if self.is_debuffed:
            return

        self._independent_ability(played_cards, scored_card_indices, poker_hands_played)

    def _on_item_sold(self, sold_item: Sellable) -> None:
        if self.is_debuffed:
            return

        self._item_sold_action(sold_item)

    def _on_jokers_moved(self) -> None:
        pass

    def _on_lucky_card_triggered(self) -> None:
        if self.is_debuffed:
            return

        self._lucky_card_triggered_action()

    def _on_pack_opened(self) -> None:
        if self.is_debuffed:
            return

        self._pack_opened_ability()

    def _on_pack_skipped(self) -> None:
        if self.is_debuffed:
            return

        self._pack_skipped_action()

    def _on_planet_used(self) -> None:
        if self.is_debuffed:
            return

        self._planet_used_action()

    def _on_round_ended(self) -> None:
        if self.is_debuffed:
            return

        if self.is_rental:
            self._run._money -= 3

        if self.is_perishable:
            self.num_perishable_rounds_left -= 1
            if self.num_perishable_rounds_left == 0:
                self.is_debuffed = True
                return

        self._round_ended_action()

    def _on_round_ended_money(self) -> int:
        if self.is_debuffed:
            return 0

        return self._round_ended_money()

    def _on_scoring_completed(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        if self.is_debuffed:
            return

        self._scoring_completed_action(
            played_cards, scored_card_indices, poker_hands_played
        )

    def _on_shop_exited(self) -> None:
        if self.is_debuffed:
            return

        self._shop_exited_ability()

    def _on_shop_rerolled(self) -> None:
        if self.is_debuffed:
            return

        self._shop_rerolled_action()

    def _on_sold(self) -> None:
        if self.is_debuffed:
            return

        self._sold_action()
        self._sold_ability()

    def _pack_opened_ability(self) -> None:
        pass

    def _pack_skipped_action(self) -> None:
        pass

    def _planet_used_action(self) -> None:
        pass

    def _round_ended_action(self) -> None:
        pass

    def _round_ended_money(self) -> int:
        return 0

    def _scoring_completed_action(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        pass

    def _shop_exited_ability(self) -> None:
        pass

    def _shop_rerolled_action(self) -> None:
        pass

    def _sold_ability(self) -> None:
        pass

    def _sold_action(self) -> None:
        pass


@dataclass(eq=False)
class CopyJoker(BalatroJoker, ABC):
    _copied_joker: BalatroJoker | None = field(default=None, init=False, repr=False)
    _copy_loop: bool = field(default=False, init=False, repr=False)

    def _blind_selected_ability(self) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._blind_selected_ability()

    def _boss_blind_triggered_ability(self) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._boss_blind_triggered_ability()

    def _card_held_ability(self, held_card: Card) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._card_held_ability(held_card)

    def _card_held_retriggers(self, held_card: Card) -> int:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            return self._copied_joker._card_held_retriggers(held_card)
        return 0

    def _card_scored_ability(
        self,
        scored_card: Card,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._card_scored_ability(
                scored_card, played_cards, scored_card_indices, poker_hands_played
            )

    def _card_scored_retriggers(
        self,
        scored_card: Card,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> int:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            return self._copied_joker._card_scored_retriggers(
                scored_card, played_cards, scored_card_indices, poker_hands_played
            )
        return 0

    def _dependent_ability(self, other_joker: BalatroJoker) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._dependent_ability(other_joker)

    def _discard_ability(self, discarded_cards: list[Card]) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._discard_ability(discarded_cards)

    def _hand_played_ability(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._hand_played_ability(
                played_cards, scored_card_indices, poker_hands_played
            )

    def _independent_ability(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._independent_ability(
                played_cards, scored_card_indices, poker_hands_played
            )

    def _pack_opened_ability(self) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._pack_opened_ability()

    def _shop_exited_ability(self) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._shop_exited_ability()

    def _sold_ability(self) -> None:
        if (
            not self._copy_loop
            and self._copied_joker is not None
            and not self._copied_joker.is_debuffed
        ):
            self._copied_joker._sold_ability()

    @abstractmethod
    def _on_jokers_moved(self) -> None:
        pass


@dataclass(eq=False)
class Consumable(Sellable):
    card: Tarot | Planet | Spectral
    is_negative: bool = False

    def __eq__(self, other: Consumable | Tarot | Planet | Spectral) -> bool:
        match other:
            case Consumable():
                return self is other
            case Tarot() | Planet() | Spectral():
                return self.card is other

        return NotImplemented

    def _repr_png_(self) -> bytes:
        from .sprites import get_sprite

        return get_sprite(self, as_image=False)


@total_ordering
@dataclass(eq=False)
class Card:
    rank: Rank
    suit: Suit
    enhancement: Enhancement | None = None
    seal: Seal | None = None
    edition: Edition = Edition.BASE

    extra_chips: int = field(default=0, init=False, repr=False)
    is_debuffed: bool = field(default=False, init=False, repr=False)
    is_face_down: bool = field(default=False, init=False, repr=False)

    def __eq__(self, other: Card | Rank | Suit | Enhancement | Seal | Edition) -> bool:
        match other:
            case Card():
                return self is other
            case Rank():
                return (
                    not self.is_debuffed
                    and not self.is_stone_card
                    and self.rank is other
                )
            case Suit():
                return (
                    not self.is_debuffed
                    and not self.is_stone_card
                    and self.suit is other
                )
            case Enhancement():
                return not self.is_debuffed and self.enhancement is other
            case Seal():
                return not self.is_debuffed and self.seal is other
            case Edition():
                return not self.is_debuffed and self.edition is other

        return NotImplemented

    def __hash__(self) -> int:
        return id(self)

    def __lt__(self, other: Card) -> bool:
        match other:
            case Card():
                return self.rank.__lt__(other.rank)

        return NotImplemented

    def __str__(self) -> str:
        return f"{self.rank.value} of {self.suit.value}"

    def _repr_png_(self, card_back: Deck = Deck.RED) -> bytes:
        from .sprites import get_sprite

        return get_sprite(self, card_back=card_back, as_image=False)

    @property
    def chips(self) -> int:
        if self.is_debuffed:
            return 0
        return (50 if self.is_stone_card else self.rank.chips) + self.extra_chips

    @property
    def is_stone_card(self) -> bool:
        return self.enhancement is Enhancement.STONE


@dataclass(eq=False)
class ChallengeSetup:
    initial_consumables: list[Consumable] = field(default_factory=list)
    initial_jokers: list[BalatroJoker] = field(default_factory=list)
    initial_vouchers: set[Voucher] = field(default_factory=set)

    banned_blinds: set[Blind] = field(default_factory=set)
    banned_consumable_cards: set[Tarot | Planet | Spectral] = field(default_factory=set)
    banned_joker_types: set[type[BalatroJoker]] = field(default_factory=set)
    banned_packs: set[Pack] = field(default_factory=set)
    banned_tags: set[Tag] = field(default_factory=set)
    banned_vouchers: set[Voucher] = field(default_factory=set)

    deck_cards: list[Card] = field(
        default_factory=lambda: [Card(rank, suit) for suit in Suit for rank in Rank]
    )

    base_reroll_cost: int = 5
    consumable_slots: int = 2
    discards_per_round: int = 3
    hand_size: int = 8
    hands_per_round: int = 4
    joker_slots: int = 5
    starting_money: int = 4


@dataclass(eq=False)
class ChipsScalingJoker(BalatroJoker):
    chips: int = field(default=0, init=False, repr=False)

    def _independent_ability(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        self._run._chips += self.chips


@dataclass(eq=False)
class DynamicJoker(BalatroJoker, ABC):
    def _on_created_action(self) -> None:
        self._change_state()

    def _round_ended_action(self) -> None:
        self._change_state()

    @abstractmethod
    def _change_state(self) -> None:
        pass


@dataclass(eq=False)
class MultScalingJoker(BalatroJoker):
    mult: int = field(default=0, init=False, repr=False)

    def _independent_ability(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        self._run._mult += self.mult


@dataclass(eq=False)
class XMultScalingJoker(BalatroJoker):
    xmult: float = field(default=1.0, init=False, repr=False)

    def _independent_ability(
        self,
        played_cards: list[Card],
        scored_card_indices: list[int],
        poker_hands_played: list[PokerHand],
    ) -> None:
        self._run._mult *= self.xmult
