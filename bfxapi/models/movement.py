"""
Module used to describe Movements as returned by Bitfinex API
"""

from enum import Enum, auto, unique


@unique
class MovementModel(Enum):
    """
    Model describing a movement.
    Reference here: https://docs.bitfinex.com/v2/reference#movements
    """
    ID = 0
    CURRENCY = auto()
    CURRENCY_NAME = auto()
    null1 = auto()
    null2 = auto()
    MTS_STARTED = auto()
    MTS_UPDATED = auto()
    null3 = auto()
    null4 = auto()
    STATUS = auto()
    null5 = auto()
    null6 = auto()
    AMOUNT = auto()
    FEES = auto()
    null7 = auto()
    null8 = auto()
    DESTINATION_ADDRESS = auto()
    null9 = auto()
    null10 = auto()
    null11 = auto()
    TRANSACTION_ID = auto()
    null12 = auto()

    def __int__(self):
        return self.value



class Movement:
    """
    ID  String  Movement identifier
    CURRENCY    String  The symbol of the currency (ex. "BTC")
    CURRENCY_NAME   String  The extended name of the currency (ex. "BITCOIN")
    MTS_STARTED Date    Movement started at
    MTS_UPDATED Date    Movement last updated at
    STATUS  String  Current status
    AMOUNT  String  Amount of funds moved. Negative numbers correspond to withdrawals
    FEES    String  Tx Fees applied
    DESTINATION_ADDRESS String  Destination address
    TRANSACTION_ID  String  Transaction identifier
    """
    def __init__(self, movement_id, currency, currency_name, movement_start_time,
                 movement_update_time, status, amount, fees, destination_address,
                 transaction_id):
        # pylint: disable=invalid-name
        self.id = movement_id
        self.currency = currency
        self.currency_name = currency_name
        self.movement_start_time = movement_start_time
        self.movement_update_time = movement_update_time
        self.status = status
        self.amount = amount
        self.fees = fees
        self.destination_address = destination_address
        self.transaction_id = transaction_id


    @staticmethod
    def from_raw_rest_movement(raw_movement):
        """
        Parse a raw movement array into an Movement object

        @return Movement
        """
        movement_id = raw_movement[int(MovementModel.ID)]
        currency = raw_movement[int(MovementModel.CURRENCY)]
        currency_name = raw_movement[int(MovementModel.CURRENCY_NAME)]
        mts_started = raw_movement[int(MovementModel.MTS_STARTED)]
        mts_updated = raw_movement[int(MovementModel.MTS_UPDATED)]
        status = raw_movement[int(MovementModel.STATUS)]
        amount = raw_movement[int(MovementModel.AMOUNT)]
        fees = raw_movement[int(MovementModel.FEES)]
        destination_address = raw_movement[int(MovementModel.DESTINATION_ADDRESS)]
        transaction_id = raw_movement[int(MovementModel.TRANSACTION_ID)]

        return Movement(movement_id, currency, currency_name, mts_started, mts_updated,
                        status, amount, fees, destination_address, transaction_id)


    def __str__(self):
        return "Movement {}: {} {} -> {} fees={}>".format(
            self.movement_start_time, self.amount, self.currency,
            self.destination_address, self.fees)
