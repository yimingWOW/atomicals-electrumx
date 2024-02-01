import pytest

from electrumx.lib.atomicals_blueprint_builder import AtomicalsTransferBlueprintBuilder, get_nominal_token_value
from electrumx.lib.coins import Bitcoin
from electrumx.lib.hash import HASHX_LEN, hex_str_to_hash, hash_to_hex_str
from electrumx.lib.tx import Tx, TxInput, TxOutput

from electrumx.lib.util_atomicals import (
    location_id_bytes_to_compact,
    derive_bitwork_prefix_from_target,
    decode_bitwork_target_from_prefix,
    is_bitwork_subset,
    calculate_expected_bitwork
)

coin = Bitcoin
 
class MockLogger:
    def debug(self, msg):
        return 
    def info(self, msg):
        return 
    def warning(self, msg):
        return 

def test_derive_bitwork_prefix_from_target_exception():
    with pytest.raises(Exception):
        derive_bitwork_prefix_from_target('', 0)  
        derive_bitwork_prefix_from_target('', 15)  

def test_derive_bitwork_prefix_from_target_from_empty():
    testvec = [
        {
            'base': '',
            'inc': 16,
            'exp': '0'
        },
        {
            'base': '',
            'inc': 17,
            'exp': '0.1'
        },
        {
            'base': '',
            'inc': 18,
            'exp': '0.2'
        },
        {
            'base': '',
            'inc': 19,
            'exp': '0.3'
        },
        {
            'base': '',
            'inc': 20,
            'exp': '0.4'
        },
        {
            'base': '',
            'inc': 21,
            'exp': '0.5'
        },
        {
            'base': '',
            'inc': 22,
            'exp': '0.6'
        },
        {
            'base': '',
            'inc': 23,
            'exp': '0.7'
        },
        {
            'base': '',
            'inc': 24,
            'exp': '0.8'
        },
        {
            'base': '',
            'inc': 25,
            'exp': '0.9'
        },
        {
            'base': '',
            'inc': 26,
            'exp': '0.10'
        },
        {
            'base': '',
            'inc': 27,
            'exp': '0.11'
        },
        {
            'base': '',
            'inc': 28,
            'exp': '0.12',
        },
        {
            'base': '',
            'inc': 29,
            'exp': '0.13'
        },
        {
            'base': '',
            'inc': 30,
            'exp': '0.14'
        },
        {
            'base': '',
            'inc': 31,
            'exp': '0.15'
        },
        {
            'base': '',
            'inc': 32,
            'exp': '00'
        },
        {
            'base': '',
            'inc': 33,
            'exp': '00.1'
        },
        {
            'base': '',
            'inc': 34,
            'exp': '00.2'
        },
        {
            'base': '',
            'inc': 35,
            'exp': '00.3'
        },
        {
            'base': '',
            'inc': 36,
            'exp': '00.4'
        },
        {
            'base': '',
            'inc': 37,
            'exp': '00.5'
        },
        {
            'base': '',
            'inc': 38,
            'exp': '00.6'
        },
        {
            'base': '',
            'inc': 39,
            'exp': '00.7'
        },
        {
            'base': '',
            'inc': 40,
            'exp': '00.8'
        },
        {
            'base': '',
            'inc': 41,
            'exp': '00.9'
        },
        {
            'base': '',
            'inc': 42,
            'exp': '00.10'
        },
        {
            'base': '',
            'inc': 43,
            'exp': '00.11'
        },
        {
            'base': '',
            'inc': 44,
            'exp': '00.12'
        },
        {
            'base': '',
            'inc': 45,
            'exp': '00.13'
        },
        {
            'base': '',
            'inc': 46,
            'exp': '00.14'
        },
        {
            'base': '',
            'inc': 47,
            'exp': '00.15'
        },
        {
            'base': '',
            'inc': 48,
            'exp': '000'
        },
        {
            'base': '',
            'inc': 49,
            'exp': '000.1'
        },
        {
            'base': '',
            'inc': 50,
            'exp': '000.2'
        },
        {
            'base': '',
            'inc': 51,
            'exp': '000.3'
        },
        {
            'base': '',
            'inc': 52,
            'exp': '000.4'
        },
        {
            'base': '',
            'inc': 53,
            'exp': '000.5'
        },
        {
            'base': '',
            'inc': 54,
            'exp': '000.6'
        },
        {
            'base': '',
            'inc': 55,
            'exp': '000.7'
        },
        {
            'base': '',
            'inc': 56,
            'exp': '000.8'
        },
        {
            'base': '',
            'inc': 57,
            'exp': '000.9'
        },
        {
            'base': '',
            'inc': 58,
            'exp': '000.10'
        },
        {
            'base': '',
            'inc': 59,
            'exp': '000.11'
        },
        {
            'base': '',
            'inc': 60,
            'exp': '000.12'
        },
        {
            'base': '',
            'inc': 61,
            'exp': '000.13'
        },
        {
            'base': '',
            'inc': 62,
            'exp': '000.14'
        },
        {
            'base': '',
            'inc': 63,
            'exp': '000.15'
        },
        {
            'base': '',
            'inc': 64,
            'exp': '0000'
        },
        {
            'base': '',
            'inc': 65,
            'exp': '0000.1'
        }      
    ]

    for x in testvec:
        assert(derive_bitwork_prefix_from_target(x['base'], x['inc']) == x['exp'])
   
def test_derive_bitwork_prefix_from_target_misc():
    testvec = [
        {
            'base': 'abc',
            'inc': 64,
            'exp': 'abc0'
        },
        {
            'base': 'abcd',
            'inc': 64,
            'exp': 'abcd'
        },
        {
            'base': 'abcd',
            'inc': 65,
            'exp': 'abcd.1'
        },
        {
            'base': 'abcd',
            'inc': 80,
            'exp': 'abcd0'
        },
        {
            'base': 'abcd',
            'inc': 83,
            'exp': 'abcd0.3'
        },
        {
            'base': '0123456789abcdef',
            'inc': 128,
            'exp': '01234567'
        },
        {
            'base': '0123456789abcdef',
            'inc': 129,
            'exp': '01234567.1'
        },
        {
            'base': '0123456789abcdef',
            'inc': 256,
            'exp': '0123456789abcdef'
        },
        {
            'base': '0123456789abcdef',
            'inc': 257,
            'exp': '0123456789abcdef.1'
        },
        {
            'base': '0123456789abcdef',
            'inc': 273,
            'exp': '0123456789abcdef0.1'
        } 
    ]

    for x in testvec:
        assert(derive_bitwork_prefix_from_target(x['base'], x['inc']) == x['exp'])

def test_decode_bitwork_target_from_prefix_empty():
    with pytest.raises(Exception):
        decode_bitwork_target_from_prefix('z')
    with pytest.raises(Exception):
        decode_bitwork_target_from_prefix('.')
    with pytest.raises(Exception):
        decode_bitwork_target_from_prefix('0.')
    with pytest.raises(Exception):
        decode_bitwork_target_from_prefix('0.17')
    with pytest.raises(Exception):
        decode_bitwork_target_from_prefix('')
    with pytest.raises(Exception):
        decode_bitwork_target_from_prefix('00..0')

def test_decode_bitwork_target_from_prefix_valid():
    testvec = [
        {
            'bitwork': 'a',
            'target': 16
        },
        {
            'bitwork': 'a.0',
            'target': 16
        },
        {
            'bitwork': 'a.1',
            'target': 17
        },
        {
            'bitwork': 'a.2',
            'target': 18
        },
        {
            'bitwork': 'a.15',
            'target': 31
        },
        {
            'bitwork': 'ab',
            'target': 32
        },
        {
            'bitwork': 'ab.0',
            'target': 32
        },
        {
            'bitwork': 'abcd',
            'target': 64
        },
        {
            'bitwork': 'abcd.1',
            'target': 65
        },
        {
            'bitwork': 'abcd0123',
            'target': 128
        },
        {
            'bitwork': 'abcd0123.5',
            'target': 133
        } 
    ]

    for x in testvec:
        assert(decode_bitwork_target_from_prefix(x['bitwork']) == x['target'])

def test_is_bitwork_subset_fail():
    with pytest.raises(Exception):
        is_bitwork_subset('', '')

    assert(is_bitwork_subset('a', 'b') == False)
    assert(is_bitwork_subset('a', 'a') == True)
    assert(is_bitwork_subset('a', 'ab') == True)
    assert(is_bitwork_subset('a', 'a.1') == True)
    assert(is_bitwork_subset('ab', 'ab') == True)
    assert(is_bitwork_subset('ab', 'ab.1') == True)
    assert(is_bitwork_subset('ab.1', 'ab.2') == True)
    assert(is_bitwork_subset('ab.14', 'ab.15') == True)
    assert(is_bitwork_subset('ab.15', 'ab0') == True)
    assert(is_bitwork_subset('ab', 'ab') == True)
    assert(is_bitwork_subset('ab', 'ab.15') == True)
    assert(is_bitwork_subset('ab.15', 'ab') == False)
    assert(is_bitwork_subset('0000', '000') == False)
    assert(is_bitwork_subset('0000', '0000') == True)
    assert(is_bitwork_subset('0000', '00000') == True)
    assert(is_bitwork_subset('0000.5', '0000.6') == True)
    assert(is_bitwork_subset('0000.5', '0000.15') == True)
    assert(is_bitwork_subset('0000.5', '00008888') == True)

def test_calculate_expected_bitwork_base():
    with pytest.raises(Exception):
        calculate_expected_bitwork('', 0, 1, 1, 63)
    
    with pytest.raises(Exception):
        calculate_expected_bitwork('', 0, 1, 0, 64)

    assert(calculate_expected_bitwork('', 0, 1, 1, 64) == '0000')
    assert(calculate_expected_bitwork('a', 0, 1, 1, 64) == 'a000')
    assert(calculate_expected_bitwork('a', 1, 1, 1, 64) == 'a000.1')
    assert(calculate_expected_bitwork('a', 2, 1, 1, 64) == 'a000.2')
    assert(calculate_expected_bitwork('a', 2, 1, 2, 64) == 'a000.4')
    assert(calculate_expected_bitwork('abcd', 0, 1000, 1, 64) == 'abcd')
    assert(calculate_expected_bitwork('abcd', 1, 1000, 1, 64) == 'abcd')
    assert(calculate_expected_bitwork('abcd', 999, 1000, 1, 64) == 'abcd')
    assert(calculate_expected_bitwork('abcd', 1000, 1000, 1, 64) == 'abcd.1')
    assert(calculate_expected_bitwork('abcd', 1001, 1000, 1, 64) == 'abcd.1')
    assert(calculate_expected_bitwork('abcd', 1999, 1000, 1, 64) == 'abcd.1')
    assert(calculate_expected_bitwork('abcd', 2000, 1000, 1, 64) == 'abcd.2')
    assert(calculate_expected_bitwork('abcd', 15999, 1000, 1, 64) == 'abcd.15')
    assert(calculate_expected_bitwork('abcd', 16000, 1000, 1, 64) == 'abcd0')
    assert(calculate_expected_bitwork('abcd', 16001, 1000, 1, 64) == 'abcd0')
    assert(calculate_expected_bitwork('abcdef', 32000, 1000, 1, 64) == 'abcdef')
    assert(calculate_expected_bitwork('abcdefe', 32001, 1000, 2, 64) == 'abcdefe0')
    assert(calculate_expected_bitwork('abcdefe', 33000, 1000, 2, 64) == 'abcdefe0.2')
    assert(calculate_expected_bitwork('abcdefe', 33000, 1000, 3, 64) == 'abcdefe000.3')
    assert(calculate_expected_bitwork('abcdefe', 33000, 1000, 1, 127) == 'abcdefe000')
    assert(calculate_expected_bitwork('abcdefe', 33000, 1000, 3, 127) == 'abcdefe0000000.2')
     
