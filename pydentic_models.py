from pydantic import BaseModel, validator, ValidationError, root_validator
from datetime import datetime
from typing import List, Optional


class User(BaseModel):
    id: int
    tg_ID:  int
    nick:   str = None
    create_date: datetime
    wallet: 'Wallet'
    sended_transactions: Optional[List['Transaction']] = None
    received_transactions: Optional[List['Transaction']] = None


class Transaction(BaseModel):
    id: int
    sender: User = None
    receiver: User = None
    sender_wallet: 'Wallet' = None
    receiver_wallet: 'Wallet' = None
    sender_address: str
    receiver_address: str
    amount_btc_with_fee: float
    amount_btc_without_fee: float
    fee: float
    date_of_transaction: datetime
    tx_hash: str


class Wallet(BaseModel):
    id: int
    user: User
    balance: float = 0.0
    private_key: str
    address: str
    sended_transactions: list[Transaction] = []
    received_transactions: list[Transaction] = []


class UserToUpdate(BaseModel):
    id: int
    tg_ID:  int = None
    nick:   str = None
    create_date: datetime = None
    wallet: 'Wallet' = None


class UserToCreate(BaseModel):
    tg_ID:  int = None
    nick:   str = None

    @validator('nick')
    def check_nick(cls, nick):
        if nick.isalpha():
            return nick
        else:
            raise ValueError('Ник должен состоять из букв')


class CreateTransaction(BaseModel):
    receiver_address: str
    amount_btc_without_fee: float


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class Admin(BaseModel):
    username: str


class UserInDB(Admin):
    hashed_password: str


UserToUpdate.update_forward_refs()
User.update_forward_refs()
UserToCreate.update_forward_refs()
Transaction.update_forward_refs()
CreateTransaction.update_forward_refs()
Wallet.update_forward_refs()
