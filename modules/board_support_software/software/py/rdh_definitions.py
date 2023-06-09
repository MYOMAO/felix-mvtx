"""File describing the RDH fields as described in the data format"""

from enum import IntEnum

class Rdh4ByteMap(IntEnum):
    """Byte map of the RDH version 4"""

    #GBT_WORD 0
    VERSION = 0
    SIZE = 1
    BLOCK_LEN_LSB = 2
    BLOCK_LEN_MSB = 3
    FEEID_LSB = 4
    FEEID_MSB = 5
    PRIORITY = 6
    NEXT_PACKET_OFFSET_LSB = 8
    NEXT_PACKET_OFFSET_MSB = 9
    MEMSIZE_LSB = 10
    MEMSIZE_MSB = 11
    LINKID = 12
    PACKET_COUNTER = 13
    CRUID_LSB = 14
    CRUID_MSB = 15
    DWRAPPERID = 15

    #GBT_WORD 1
    TRG_ORBIT_SB0 = 16
    TRG_ORBIT_SB1 = 17
    TRG_ORBIT_SB2 = 18
    TRG_ORBIT_SB3 = 19
    HB_ORBIT_SB0 = 20
    HB_ORBIT_SB1 = 21
    HB_ORBIT_SB2 = 22
    HB_ORBIT_SB3 = 23

    #GBT_WORD 2
    TRG_BC_LSB = 32
    TRG_BC_MSB = 33
    HB_BC_LSB = 34
    HB_BC_MSB = 35
    TRG_TYPE_SB0 = 36
    TRG_TYPE_SB1 = 37
    TRG_TYPE_SB2 = 38
    TRG_TYPE_SB3 = 39

    #GBT_WORD 3
    DET_FIELD_LSB = 48
    DET_FIELD_MSB = 49
    PAR_LSB = 50
    PAR_MSB = 51
    STOP = 52
    PAGE_CNT_LSB = 53
    PAGE_CNT_MSB = 54


class Rdh6ByteMap(IntEnum):
    """Byte map of the RDH version 6"""

    #GBT_WORD 0
    VERSION = 0
    SIZE = 1
    FEEID_LSB = 2
    FEEID_MSB = 3
    PRIORITY = 4
    SOURCE_ID = 5
    RESERVED_0_LSB = 6
    RESERVED_0_MSB = 7
    NEXT_PACKET_OFFSET_LSB = 8
    NEXT_PACKET_OFFSET_MSB = 9
    MEMSIZE_LSB = 10
    MEMSIZE_MSB = 11
    LINK_ID = 12
    PACKET_COUNTER = 13
    CRU_ID_LSB = 14
    CRU_ID_MSB = 15
    DWRAPPER_ID = 15


    #GBT_WORD 1
    BC_LSB = 16
    BC_MSB = 17
    RESERVED_1_LSB = 18
    RESERVED_1_MSB = 19
    ORBIT_SB0 = 20
    ORBIT_SB1 = 21
    ORBIT_SB2 = 22
    ORBIT_SB3 = 23
    RESERVED_2_SB0 = 24
    RESERVED_2_SB1 = 25
    RESERVED_2_SB2 = 26
    RESERVED_2_SB3 = 27
    RESERVED_2_SB4 = 28
    RESERVED_2_SB5 = 29
    RESERVED_2_SB6 = 30
    RESERVED_2_SB7 = 31

    #GBT_WORD 2
    TRG_TYPE_SB0 = 32
    TRG_TYPE_SB1 = 33
    TRG_TYPE_SB2 = 34
    TRG_TYPE_SB3 = 35
    PAGE_CNT_LSB = 36
    PAGE_CNT_MSB = 37
    STOP_BIT = 38
    RESERVED_3_SB0 = 39
    RESERVED_3_SB1 = 40
    RESERVED_3_SB2 = 41
    RESERVED_3_SB3 = 42
    RESERVED_3_SB4 = 43
    RESERVED_3_SB5 = 44
    RESERVED_3_SB6 = 45
    RESERVED_3_SB7 = 46
    RESERVED_3_SB8 = 47

    #GBT_WORD 3
    DET_FIELD_SB0 = 48
    DET_FIELD_SB1 = 49
    DET_FIELD_SB2 = 50
    DET_FIELD_SB3 = 51
    PAR_LSB = 52
    PAR_MSB = 53
    RESERVED_4_SB0 = 54
    RESERVED_4_SB1 = 55
    RESERVED_4_SB2 = 56
    RESERVED_4_SB3 = 57
    RESERVED_4_SB4 = 58
    RESERVED_4_SB5 = 59
    RESERVED_4_SB6 = 60
    RESERVED_4_SB7 = 61
    RESERVED_4_SB8 = 62
    RESERVED_4_SB9 = 63


class Rdh8ByteMap(IntEnum):
    """Byte map of the MVTX RDH version 8"""

    #GBT_WORD 0
    VERSION = 0
    SIZE = 1
    FEEID_LSB = 2
    FEEID_MSB = 3
    SOURCE_ID = 4
    DET_FIELD_SB0 = 5
    DET_FIELD_SB1 = 6
    DET_FIELD_SB2 = 7
    DET_FIELD_SB3 = 8
    RESERVED_0_LSB = 9

    #GBT_WORD 1
    BC_LSB = 10
    BC_MSB = 11
    RESERVED_1_LSB = 12
    RESERVED_1_MSB = 13
    ORBIT_SB0 = 14
    ORBIT_SB1 = 15
    ORBIT_SB2 = 16
    ORBIT_SB3 = 17
    ORBIT_SB4 = 18
    RESERVED_2_SB0 = 19

    #GBT_WORD 2
    TRG_TYPE_SB0 = 20
    TRG_TYPE_SB1 = 21
    TRG_TYPE_SB2 = 22
    TRG_TYPE_SB3 = 23
    PAGE_CNT_LSB = 24
    PAGE_CNT_MSB = 25
    STOP_BIT = 26
    PRIORITY = 27
    RESERVED_3_SB0 = 28
    RESERVED_3_SB1 = 29
    RESERVED_3_SB2 = 30
    RESERVED_3_SB3 = 31


class FLX1ByteMap(IntEnum):
    """Byte map of the FELIX Header version 1"""

    RESERVED_0_SB0 = 0
    RESERVED_0_SB1 = 1
    RESERVED_0_SB2 = 2
    RESERVED_0_SB3 = 3
    RESERVED_0_SB4 = 4
    RESERVED_0_SB5 = 5
    RESERVED_0_SB6 = 6
    RESERVED_0_SB7 = 7
    RESERVED_0_SB8 = 8
    RESERVED_0_SB9 = 9
    RESERVED_0_SB10 = 10
    RESERVED_0_SB11 = 11
    RESERVED_0_SB12 = 12
    RESERVED_0_SB13 = 13
    RESERVED_0_SB14 = 14
    RESERVED_0_SB15 = 15
    RESERVED_0_SB16 = 16
    RESERVED_0_SB17 = 17
    RESERVED_0_SB18 = 18
    RESERVED_0_SB19 = 19
    RESERVED_0_SB20 = 20
    RESERVED_0_SB21 = 21
    RESERVED_0_SB22 = 22
    FLXID = 23
    RESERVED_1 = 24
    DMA_WRD_CTR_LSB = 25
    DMA_WRD_CTR_MSB = 26
    RESERVED_2 = 27
    GBT_ID = 28
    RESERVED_3 = 29
    VERSION = 30
    HDR_CODE = 31
