from typing import Collection
from scripts.helpful_scripts import get_account
from brownie import Collection, RewardToken, Staking, accounts, config, network


def deploy_collection_token_and_staking():
    account = get_account()

    publish_source = config["networks"][network.show_active()]["verify"]

    collection = Collection.deploy(
        'Collection',
        'COLLECT',
        'https://gateway.pinata.cloud/ipfs/QmfAP8WZD1JZnEWMkczkGjDA9mJmULYAouw5LduGBfHXKV/',
        'https://gateway.pinata.cloud/ipfs/QmXPb49BYuQqmWtxUsud65wvrRMteS1N2i6J71ipRaMyeW',
        {"from": account},
        publish_source=publish_source
    )

    print(f'nft is deployed at {collection.address}')

    reward_token = RewardToken.deploy(
        'Reward Token',
        'REWARD',
        {"from": account},
        publish_source=publish_source
    )

    print(f'reward is deployed at {reward_token.address}')

    staking = Staking.deploy(
        collection.address,
        reward_token.address,
        {"from": account},
        publish_source=publish_source
    )

    print(f'staking contract is deployed at {staking.address}')


def main():
    deploy_collection_token_and_staking()
