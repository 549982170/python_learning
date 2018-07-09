#!user/bin/python
# encoding:utf-8
import hashlib


def md5(string):
    """md5sum加密"""
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()


test = "wangxin02@soovii.com" + "123456"



# testchangedb

# INSERT INTO `gameadmin_trunk`.`uuser` (`id`, `appID`, `channelID`, `channelUserID`, `channelUserName`, `channelUserNick`, `createTime`, `lastLoginTime`, `name`, `token`, `password`, `idfa`, `idfv`, `status`, `rewardFlag`) VALUES ('64001', '1', '10', '5ed156f634b9c1c71a472ebeb19bfeb6', '5ed156f634b9c1c71a472ebeb19bfeb6', '九游玩家593049108', '2016-07-28 11:54:18', '1469681054301', '1469678058988.uc', '3cdbdff5ede80f904e43395a94a51f12', '6044535cda39493148713f9e3e5082bf', '867622024453238', NULL, '1', '0');

print md5(test)

# df9c1d2b1fc610e525cbc3165a22a969
