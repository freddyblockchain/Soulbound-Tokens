
from typing import Literal
from pyteal import *


@Subroutine(TealType.uint64)
def transfer_asset() -> Expr:
    assetTotal = AssetParam.total(Txn.assets[0])
    assetDecimal = AssetParam.decimals(Txn.assets[0])
    assetManager = AssetParam.manager(Txn.assets[0])
    assetFreeze = AssetParam.freeze(Txn.assets[0])
    assetClawback = AssetParam.clawback(Txn.assets[0])

    return Seq([
        assetTotal,
        Assert(assetTotal.hasValue()),
        Assert(assetTotal.value() == Int(1)),
        assetDecimal,
        Assert(assetDecimal.hasValue()),
        Assert(assetDecimal.value() == Int(0)),
        assetManager,
        Assert(assetManager.hasValue()),
        Assert(assetManager.value() == Global.current_application_address()),
        assetFreeze,
        Assert(assetFreeze.hasValue()),
        Assert(assetFreeze.value() == Global.current_application_address()),
        assetClawback,
        Assert(assetClawback.hasValue()),
        Assert(assetClawback.value() == Global.current_application_address()),
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.AssetTransfer,
            TxnField.asset_sender: Txn.accounts[0],
            TxnField.asset_receiver: Txn.accounts[1],
            TxnField.asset_amount: Int(1),
            TxnField.xfer_asset: Txn.assets[0],
        }),
        InnerTxnBuilder.Next(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.AssetFreeze,
            TxnField.freeze_asset: Txn.assets[0],
            TxnField.freeze_asset_account: Txn.accounts[1],
            TxnField.freeze_asset_frozen: Int(1)
        }),
        InnerTxnBuilder.Next(),
        InnerTxnBuilder.SetFields({
            TxnField.type_enum: TxnType.AssetConfig,
            TxnField.config_asset: Txn.assets[0],
            TxnField.config_asset_manager: Global.zero_address(),
            TxnField.config_asset_reserve: Global.current_application_address(),
            TxnField.config_asset_freeze:  Global.zero_address(),
            TxnField.config_asset_clawback: Global.zero_address(),
        }),
        InnerTxnBuilder.Submit(),
        Return(Int(1))
    ])


def approval_program():

    handle_noop = Seq(
        Return(transfer_asset())
    )

    handle_optin = Seq([
        Return(Int(1))
    ])

    handle_closeout = Seq([
        Return(Int(1))
    ])

    handle_creation = Seq([
        Return(Int(1))
    ])

    handle_updateapp = Err()

    handle_deleteapp = Err()

    program = Cond(
        [Txn.application_id() == Int(0), handle_creation],
        [Txn.on_completion() == OnComplete.OptIn, handle_optin],
        [Txn.on_completion() == OnComplete.CloseOut, handle_closeout],
        [Txn.on_completion() == OnComplete.UpdateApplication, handle_updateapp],
        [Txn.on_completion() == OnComplete.DeleteApplication, handle_deleteapp],
        [Txn.on_completion() == OnComplete.NoOp, handle_noop],
    )
    return program


def clear_state_program():
    return Approve()


if __name__ == "__main__":
    with open("soulbound_approval2.teal", "w") as f:
        compiled = compileTeal(
            approval_program(), mode=Mode.Application, version=6)
        f.write(compiled)

    with open("soulbound_clear_state2.teal", "w") as f:
        compiled = compileTeal(clear_state_program(),
                               mode=Mode.Application, version=6)
        f.write(compiled)
