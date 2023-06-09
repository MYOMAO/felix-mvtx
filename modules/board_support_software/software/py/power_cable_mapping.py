"""
Dictionary containing the power cable lengths in metres of each stave, indexed by layer and stave number.

cable_length_lut = {'layer': [
                    (stave number, lower, pp2 to pp3, pp1 to pp2), (stave number, upper, pp2 to pp3, pp1 to pp2), 
                    (stave number, lower, pp2 to pp3, pp1 to pp2), (stave number, upper, pp2 to pp3, pp1 to pp2),...
"""

from enum import IntEnum, unique


@unique
class Fields(IntEnum):
    stave_number = 0
    half_stave   = 1
    pp2_to_pp3   = 2
    pp1_to_pp2   = 3

cable_length_lut = {
'6': [
    (0, 'lower', 2.15, 5), (0, 'upper', 2.15, 5),
    (1, 'lower', 2.15, 5), (1, 'upper', 2.15, 5),
    (2, 'lower', 2.15, 5), (2, 'upper', 2.15, 5),
    (3, 'lower', 2.15, 5), (3, 'upper', 2.15, 5),
    (4, 'lower', 2.15, 5), (4, 'upper', 2.15, 5),
    (5, 'lower', 2.15, 5), (5, 'upper', 2.15, 5),
    (6, 'lower', 2.15, 4.5), (6, 'upper', 2.15, 4.5),
    (7, 'lower', 2.15, 4.5), (7, 'upper', 2.15, 4.5),
    (8, 'lower', 2.15, 4.5), (8, 'upper', 2.15, 4.5),
    (9, 'lower', 2.15, 4.5), (9, 'upper', 2.15, 4.5),
    (10, 'lower', 2.15, 4.5), (10, 'upper', 2.15, 4.5),
    (11, 'lower', 2.15, 4.5), (11, 'upper', 2.15, 4.5),
    (12, 'lower', 2.15, 4.5), (12, 'upper', 2.15, 4.5),
    (13, 'lower', 2.15, 4.5), (13, 'upper', 2.15, 4.5),
    (14, 'lower', 2.15, 4.5), (14, 'upper', 2.15, 4.5),
    (15, 'lower', 2.15, 4.5), (15, 'upper', 2.15, 4.5),
    (16, 'lower', 2.15, 4.5), (16, 'upper', 2.15, 4.5),
    (17, 'lower', 2.15, 4.5), (17, 'upper', 2.15, 4.5),
    (18, 'lower', 2.15, 5), (18, 'upper', 2.15, 5),
    (19, 'lower', 2.15, 5), (19, 'upper', 2.15, 5),
    (20, 'lower', 2.15, 5), (20, 'upper', 2.15, 5),
    (21, 'lower', 2.15, 5), (21, 'upper', 2.15, 5),
    (22, 'lower', 2.15, 5), (22, 'upper', 2.15, 5),
    (23, 'lower', 2.15, 5), (23, 'upper', 2.15, 5),
    (24, 'lower', 2.15, 4.5), (24, 'upper', 2.15, 4.5),
    (25, 'lower', 2.15, 4.5), (25, 'upper', 2.15, 4.5),
    (26, 'lower', 2.15, 4.5), (26, 'upper', 2.15, 4.5),
    (27, 'lower', 2.15, 4.5), (27, 'upper', 2.15, 4.5),
    (28, 'lower', 2.15, 4.5), (28, 'upper', 2.15, 4.5),
    (29, 'lower', 2.15, 4.5), (29, 'upper', 2.15, 4.5),
    (30, 'lower', 2.15, 4.5), (30, 'upper', 2.15, 4.5),
    (31, 'lower', 2.15, 4.5), (31, 'upper', 2.15, 4.5),
    (32, 'lower', 2.15, 4), (32, 'upper', 2.15, 4),
    (33, 'lower', 2.15, 4), (33, 'upper', 2.15, 4),
    (34, 'lower', 2.15, 4), (34, 'upper', 2.15, 4),
    (35, 'lower', 2.15, 4), (35, 'upper', 2.15, 4),
    (36, 'lower', 2.15, 4.5), (36, 'upper', 2.15, 4.5),
    (37, 'lower', 2.15, 4.5), (37, 'upper', 2.15, 4.5),
    (38, 'lower', 2.15, 4.5), (38, 'upper', 2.15, 4.5),
    (39, 'lower', 2.15, 4.5), (39, 'upper', 2.15, 4.5),
    (40, 'lower', 2.15, 4.5), (40, 'upper', 2.15, 4.5),
    (41, 'lower', 2.15, 4.5), (41, 'upper', 2.15, 4.5),
    (42, 'lower', 2.15, 5), (42, 'upper', 2.15, 5),
    (43, 'lower', 2.15, 5), (43, 'upper', 2.15, 5),
    (44, 'lower', 2.15, 5), (44, 'upper', 2.15, 5),
    (45, 'lower', 2.15, 5), (45, 'upper', 2.15, 5),
    (46, 'lower', 2.15, 5), (46, 'upper', 2.15, 5),
    (47, 'lower', 2.15, 5), (47, 'upper', 2.15, 5)
],
'5' : [
    (0, 'lower', 2.15, 5), (0, 'upper', 2.15, 5),
    (1, 'lower', 2.15, 5), (1, 'upper', 2.15, 5),
    (2, 'lower', 2.15, 5), (2, 'upper', 2.15, 5),
    (3, 'lower', 2.15, 5), (3, 'upper', 2.15, 5),
    (4, 'lower', 2.15, 5), (4, 'upper', 2.15, 5),
    (5, 'lower', 2.15, 4.5), (5, 'upper', 2.15, 4.5),
    (6, 'lower', 2.15, 4), (6, 'upper', 2.15, 4.5),
    (7, 'lower', 2.15, 4.5), (7, 'upper', 2.15, 4.5),
    (8, 'lower', 2.15, 4.5), (8, 'upper', 2.15, 4.5),
    (9, 'lower', 2.15, 4.5), (9, 'upper', 2.15, 4.5),
    (10, 'lower', 2.15, 4), (10, 'upper', 2.15, 4),
    (11, 'lower', 2.15, 4), (11, 'upper', 2.15, 4),
    (12, 'lower', 2.15, 4), (12, 'upper', 2.15, 4),
    (13, 'lower', 2.15, 4), (13, 'upper', 2.15, 4),
    (14, 'lower', 2.15, 4), (14, 'upper', 2.15, 4),
    (15, 'lower', 2.15, 4.5), (15, 'upper', 2.15, 4.5),
    (16, 'lower', 2.15, 4.5), (16, 'upper', 2.15, 4.5),
    (17, 'lower', 2.15, 4.5), (17, 'upper', 2.15, 4.5),
    (18, 'lower', 2.15, 4.5), (18, 'upper', 2.15, 4.5),
    (19, 'lower', 2.15, 4.5), (19, 'upper', 2.15, 4.5),
    (20, 'lower', 2.15, 4.5), (20, 'upper', 2.15, 4.5),
    (21, 'lower', 2.15, 4.5), (21, 'upper', 2.15, 4.5),
    (22, 'lower', 2.15, 4.5), (22, 'upper', 2.15, 4.5),
    (23, 'lower', 2.15, 4.5), (23, 'upper', 2.15, 4.5),
    (24, 'lower', 2.15, 4.5), (24, 'upper', 2.15, 4.5),
    (25, 'lower', 2.15, 4.5), (25, 'upper', 2.15, 4.5),
    (26, 'lower', 2.15, 4.5), (26, 'upper', 2.15, 4.5),
    (27, 'lower', 2.15, 4), (27, 'upper', 2.15, 4),
    (28, 'lower', 2.15, 4), (28, 'upper', 2.15, 4),
    (29, 'lower', 2.15, 4), (29, 'upper', 2.15, 4),
    (30, 'lower', 2.15, 4), (30, 'upper', 2.15, 4),
    (31, 'lower', 2.15, 4), (31, 'upper', 2.15, 4),
    (32, 'lower', 2.15, 4), (32, 'upper', 2.15, 4),
    (33, 'lower', 2.15, 4), (33, 'upper', 2.15, 4),
    (34, 'lower', 2.15, 4), (34, 'upper', 2.15, 4),
    (35, 'lower', 2.15, 4), (35, 'upper', 2.15, 4),
    (36, 'lower', 2.15, 4), (36, 'upper', 2.15, 4),
    (37, 'lower', 2.15, 4.5), (37, 'upper', 2.15, 4.5),
    (38, 'lower', 2.15, 4.5), (38, 'upper', 2.15, 4.5),
    (39, 'lower', 2.15, 4.5), (39, 'upper', 2.15, 4.5),
    (40, 'lower', 2.15, 4.5), (40, 'upper', 2.15, 4.5),
    (41, 'lower', 2.15, 4.5), (41, 'upper', 2.15, 4.5),
    (42, 'lower', 2.15, 4.5), (42, 'upper', 2.15, 4.5) # Lab1 (1/R-031) OL reference test setup
],
'4' : [
    (0, 'lower', 2.45, 4.4), (0, 'upper', 2.45, 4.4),
    (1, 'lower', 2.45, 4.4), (1, 'upper', 2.45, 4.4),
    (2, 'lower', 2.45, 4.4), (2, 'upper', 2.45, 4.4),
    (3, 'lower', 2.45, 4.4), (3, 'upper', 2.45, 4.4),
    (4, 'lower', 2.45, 4.4), (4, 'upper', 2.45, 4.4),
    (5, 'lower', 2.45, 4.4), (5, 'upper', 2.45, 4.4),
    (6, 'lower', 2.45, 4.4), (6, 'upper', 2.45, 4.4),
    (7, 'lower', 2.45, 4.4), (7, 'upper', 2.45, 4.4),
    (8, 'lower', 2.45, 4.4), (8, 'upper', 2.45, 4.4),
    (9, 'lower', 2.45, 4.4), (9, 'upper', 2.45, 4.4),
    (10, 'lower', 2.45, 4.4), (10, 'upper', 2.45, 4.4),
    (11, 'lower', 2.45, 4.4), (11, 'upper', 2.45, 4.4),
    (12, 'lower', 2.45, 4.4), (12, 'upper', 2.45, 4.4),
    (13, 'lower', 2.45, 4.4), (13, 'upper', 2.45, 4.4),
    (14, 'lower', 2.45, 4.4), (14, 'upper', 2.45, 4.4),
    (15, 'lower', 2.45, 4.4), (15, 'upper', 2.45, 4.4),
    (16, 'lower', 2.45, 4.4), (16, 'upper', 2.45, 4.4),
    (17, 'lower', 2.45, 4.4), (17, 'upper', 2.45, 4.4),
    (18, 'lower', 2.45, 4.4), (18, 'upper', 2.45, 4.4),
    (19, 'lower', 2.45, 4.4), (19, 'upper', 2.45, 4.4),
    (20, 'lower', 2.45, 4.4), (20, 'upper', 2.45, 4.4),
    (21, 'lower', 2.45, 4.4), (21, 'upper', 2.45, 4.4),
    (22, 'lower', 2.45, 4.4), (22, 'upper', 2.45, 4.4),
    (23, 'lower', 2.45, 4.4), (23, 'upper', 2.45, 4.4),
    (24, 'lower', 2.45, 4.4), (24, 'upper', 2.45, 4.4),
    (25, 'lower', 2.45, 4.4), (25, 'upper', 2.45, 4.4),
    (26, 'lower', 2.45, 4.4), (26, 'upper', 2.45, 4.4),
    (27, 'lower', 2.45, 4.4), (27, 'upper', 2.45, 4.4),
    (28, 'lower', 2.45, 4.4), (28, 'upper', 2.45, 4.4),
    (29, 'lower', 2.45, 4.4), (29, 'upper', 2.45, 4.4)
],
'3' : [
    (0, 'lower', 2.45, 4), (0, 'upper', 2.45, 4),
    (1, 'lower', 2.45, 4), (1, 'upper', 2.45, 4),
    (2, 'lower', 2.45, 4), (2, 'upper', 2.45, 4),
    (3, 'lower', 2.45, 4), (3, 'upper', 2.45, 4),
    (4, 'lower', 2.45, 4), (4, 'upper', 2.45, 4),
    (5, 'lower', 2.45, 4), (5, 'upper', 2.45, 4),
    (6, 'lower', 2.45, 4), (6, 'upper', 2.45, 4),
    (7, 'lower', 2.45, 4), (7, 'upper', 2.45, 4),
    (8, 'lower', 2.45, 4), (8, 'upper', 2.45, 4),
    (9, 'lower', 2.45, 4), (9, 'upper', 2.45, 4),
    (10, 'lower', 2.45, 4), (10, 'upper', 2.45, 4),
    (11, 'lower', 2.45, 4), (11, 'upper', 2.45, 4),
    (12, 'lower', 2.45, 4), (12, 'upper', 2.45, 4),
    (13, 'lower', 2.45, 4), (13, 'upper', 2.45, 4),
    (14, 'lower', 2.45, 4), (14, 'upper', 2.45, 4),
    (15, 'lower', 2.45, 4), (15, 'upper', 2.45, 4),
    (16, 'lower', 2.45, 4), (16, 'upper', 2.45, 4),
    (17, 'lower', 2.45, 4), (17, 'upper', 2.45, 4),
    (18, 'lower', 2.45, 4.4), (18, 'upper', 2.45, 4.4),
    (19, 'lower', 2.45, 4), (19, 'upper', 2.45, 4),
    (20, 'lower', 2.45, 4), (20, 'upper', 2.45, 4),
    (21, 'lower', 2.45, 4), (21, 'upper', 2.45, 4),
    (22, 'lower', 2.45, 4), (22, 'upper', 2.45, 4),
    (23, 'lower', 2.45, 4), (23, 'upper', 2.45, 4),
    (24, 'lower', 2.45, 4), (24, 'upper', 2.45, 4) # Lab1 (1/R-031) ML reference test setup
],
'2' : [
    (0, 'IB', 2.65, 4.95),
    (1, 'IB', 2.65, 4.95), 
    (2, 'IB', 2.65, 4.95), 
    (3, 'IB', 2.65, 4.95), 
    (4, 'IB', 2.65, 4.95), 
    (5, 'IB', 2.65, 4.55), 
    (6, 'IB', 2.65, 4.55), 
    (7, 'IB', 2.65, 4.55), 
    (8, 'IB', 2.65, 4.55), 
    (9, 'IB', 2.65, 4.55), 
    (10, 'IB', 2.65, 4.95), 
    (11, 'IB', 2.65, 4.95), 
    (12, 'IB', 2.65, 4.95), 
    (13, 'IB', 2.65, 4.95), 
    (14, 'IB', 2.65, 4.95),
    (15, 'IB', 2.65, 4.55),
    (16, 'IB', 2.65, 4.55),
    (17, 'IB', 2.65, 4.55),
    (18, 'IB', 2.65, 4.55),
    (19, 'IB', 2.65, 4.55),
],
'1' : [
    (0, 'IB', 2.65, 4.95), 
    (1, 'IB', 2.65, 4.95), 
    (2, 'IB', 2.65, 4.95), 
    (3, 'IB', 2.65, 4.95), 
    (4, 'IB', 2.65, 4.95), 
    (5, 'IB', 2.65, 4.95), 
    (6, 'IB', 2.65, 4.95), 
    (7, 'IB', 2.65, 4.55), 
    (8, 'IB', 2.65, 4.95), 
    (9, 'IB', 2.65, 4.95), 
    (10, 'IB', 2.65, 4.95),
    (11, 'IB', 2.65, 4.95),
    (12, 'IB', 2.65, 4.55),
    (13, 'IB', 2.65, 4.55),
    (14, 'IB', 2.65, 4.55),
    (15, 'IB', 2.65, 4.55),
],
'0' : [
    (0, 'IB', 2.65, 4.55),
    (1, 'IB', 2.65, 4.55),
    (2, 'IB', 2.65, 4.55), 
    (3, 'IB', 2.65, 4.55), 
    (4, 'IB', 2.65, 4.55), 
    (5, 'IB', 2.65, 4.55), 
    (6, 'IB', 2.65, 4.95), 
    (7, 'IB', 2.65, 4.95), 
    (8, 'IB', 2.65, 4.95), 
    (9, 'IB', 2.65, 4.95), 
    (10, 'IB', 2.65, 4.95),
    (11, 'IB', 2.65, 4.95),
    (12, 'IB', 2.65, 4.95), # Lab1 (1/R-031) IBS reference test setup
    (13, 'IB', 2.65, 4.95), # Lab1 (1/R-031) IBTable reference test setup
]
}
