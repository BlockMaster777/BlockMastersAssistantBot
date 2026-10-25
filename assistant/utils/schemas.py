# -----------------------------------------------------------------------------------
#  BlockMastersAssistantBot
#  Copyright (C) 2026  BlockMaster
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------------
MainSchema = [
    {"l": "FaQ", "c": "faq"},
    {"l": "Report an issue", "c": "report"},
    {"l": "Utils", "c": "utils"},
    {"l": "No, Thanks", "c": "close"},
]

FAQSchema = [
    {
        "l": "Links",
        "a": "*Github*: https://github\\.com/BlockMaster777\n"
        + "*Telegram*: https://t\\.me/BlockMaster777\n"
        + "*Discord*: https://discord\\.gg/users/1251897007048626236\n"
        + "*Email* bl0ckmaster@duck\\.com\n"
        + "*BlockServices link*: https://blocksrv\\.duckdns\\.org\n"
        + "*DashBlocks link*: https://dashblocks\\.org\n",
        "c": "links",
    },
    {"l": "Other Bots", "a": "*Nope* 🥲", "c": "other_bots"},
]

UtilsSchema = [
    {"l": "Check DashBlocks health", "c": "check_dash"},
    {"l": "Generate JWT Secret token", "c": "generate_key"},
    {"l": "Encode to base 64", "c": "encode_b64"},
    {"l": "Decode from base 64", "c": "decode_b64"},
]
