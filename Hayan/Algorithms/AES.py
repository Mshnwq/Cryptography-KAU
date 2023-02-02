from copy import copy
import string
import random


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class AES:
    # substitution table
    sbox0 = [
        ["63", "7c", "77", "7b", "f2", "6b", "6f", "c5",
            "30", "01", "67", "2b", "fe", "d7", "ab", "76"],
        ["ca", "82", "c9", "7d", "fa", "59", "47", "f0",
            "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
        ["b7", "fd", "93", "26", "36", "3f", "f7", "cc",
            "34", "a5", "e5", "f1", "71", "d8", "31", "15"],
        ["04", "c7", "23", "c3", "18", "96", "05", "9a",
            "07", "12", "80", "e2", "eb", "27", "b2", "75"],
        ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0",
            "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],
        ["53", "d1", "00", "ed", "20", "fc", "b1", "5b",
            "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
        ["d0", "ef", "aa", "fb", "43", "4d", "33", "85",
            "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],
        ["51", "a3", "40", "8f", "92", "9d", "38", "f5",
            "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
        ["cd", "0c", "13", "ec", "5f", "97", "44", "17",
            "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],
        ["60", "81", "4f", "dc", "22", "2a", "90", "88",
            "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
        ["e0", "32", "3a", "0a", "49", "06", "24", "5c",
            "c2", "d3", "ac", "62", "91", "95", "e4", "79"],
        ["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9",
            "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
        ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6",
            "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],
        ["70", "3e", "b5", "66", "48", "03", "f6", "0e",
            "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
        ["e1", "f8", "98", "11", "69", "d9", "8e", "94",
            "9b", "1e", "87", "e9", "ce", "55", "28", "df"],
        ["8c", "a1", "89", "0d", "bf", "e6", "42", "68",
            "41", "99", "2d", "0f", "b0", "54", "bb", "16"],
    ]
    # inverse substitution table
    sbox1 = [
        ["52", "09", "6a", "d5", "30", "36", "a5", "38",
            "bf", "40", "a3", "9e", "81", "f3", "d7", "fb"],
        ["7c", "e3", "39", "82", "9b", "2f", "ff", "87",
            "34", "8e", "43", "44", "c4", "de", "e9", "cb"],
        ["54", "7b", "94", "32", "a6", "c2", "23", "3d",
            "ee", "4c", "95", "0b", "42", "fa", "c3", "4e"],
        ["08", "2e", "a1", "66", "28", "d9", "24", "b2",
            "76", "5b", "a2", "49", "6d", "8b", "d1", "25"],
        ["72", "f8", "f6", "64", "86", "68", "98", "16",
            "d4", "a4", "5c", "cc", "5d", "65", "b6", "92"],
        ["6c", "70", "48", "50", "fd", "ed", "b9", "da",
            "5e", "15", "46", "57", "a7", "8d", "9d", "84"],
        ["90", "d8", "ab", "00", "8c", "bc", "d3", "0a",
            "f7", "e4", "58", "05", "b8", "b3", "45", "06"],
        ["d0", "2c", "1e", "8f", "ca", "3f", "0f", "02",
            "c1", "af", "bd", "03", "01", "13", "8a", "6b"],
        ["3a", "91", "11", "41", "4f", "67", "dc", "ea",
            "97", "f2", "cf", "ce", "f0", "b4", "e6", "73"],
        ["96", "ac", "74", "22", "e7", "ad", "35", "85",
            "e2", "f9", "37", "e8", "1c", "75", "df", "6e"],
        ["47", "f1", "1a", "71", "1d", "29", "c5", "89",
            "6f", "b7", "62", "0e", "aa", "18", "be", "1b"],
        ["fc", "56", "3e", "4b", "c6", "d2", "79", "20",
            "9a", "db", "c0", "fe", "78", "cd", "5a", "f4"],
        ["1f", "dd", "a8", "33", "88", "07", "c7", "31",
            "b1", "12", "10", "59", "27", "80", "ec", "5f"],
        ["60", "51", "7f", "a9", "19", "b5", "4a", "0d",
            "2d", "e5", "7a", "9f", "93", "c9", "9c", "ef"],
        ["a0", "e0", "3b", "4d", "ae", "2a", "f5", "b0",
            "c8", "eb", "bb", "3c", "83", "53", "99", "61"],
        ["17", "2b", "04", "7e", "ba", "77", "d6", "26",
            "e1", "69", "14", "63", "55", "21", "0c", "7d"],
    ]
    gMulBy2 = [
        0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e,
        0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e,
        0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e,
        0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e,
        0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e,
        0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe,
        0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde,
        0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe,
        0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05,
        0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25,
        0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45,
        0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65,
        0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85,
        0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5,
        0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5,
        0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5,
    ]

    gMulBy3 = [
        0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11,
        0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21,
        0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71,
        0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41,
        0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1,
        0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1,
        0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1,
        0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81,
        0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a,
        0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba,
        0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea,
        0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda,
        0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a,
        0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a,
        0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a,
        0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a,
    ]

    gMulBy9 = [
        0x00, 0x09, 0x12, 0x1b, 0x24, 0x2d, 0x36, 0x3f, 0x48, 0x41, 0x5a, 0x53, 0x6c, 0x65, 0x7e, 0x77,
        0x90, 0x99, 0x82, 0x8b, 0xb4, 0xbd, 0xa6, 0xaf, 0xd8, 0xd1, 0xca, 0xc3, 0xfc, 0xf5, 0xee, 0xe7,
        0x3b, 0x32, 0x29, 0x20, 0x1f, 0x16, 0x0d, 0x04, 0x73, 0x7a, 0x61, 0x68, 0x57, 0x5e, 0x45, 0x4c,
        0xab, 0xa2, 0xb9, 0xb0, 0x8f, 0x86, 0x9d, 0x94, 0xe3, 0xea, 0xf1, 0xf8, 0xc7, 0xce, 0xd5, 0xdc,
        0x76, 0x7f, 0x64, 0x6d, 0x52, 0x5b, 0x40, 0x49, 0x3e, 0x37, 0x2c, 0x25, 0x1a, 0x13, 0x08, 0x01,
        0xe6, 0xef, 0xf4, 0xfd, 0xc2, 0xcb, 0xd0, 0xd9, 0xae, 0xa7, 0xbc, 0xb5, 0x8a, 0x83, 0x98, 0x91,
        0x4d, 0x44, 0x5f, 0x56, 0x69, 0x60, 0x7b, 0x72, 0x05, 0x0c, 0x17, 0x1e, 0x21, 0x28, 0x33, 0x3a,
        0xdd, 0xd4, 0xcf, 0xc6, 0xf9, 0xf0, 0xeb, 0xe2, 0x95, 0x9c, 0x87, 0x8e, 0xb1, 0xb8, 0xa3, 0xaa,
        0xec, 0xe5, 0xfe, 0xf7, 0xc8, 0xc1, 0xda, 0xd3, 0xa4, 0xad, 0xb6, 0xbf, 0x80, 0x89, 0x92, 0x9b,
        0x7c, 0x75, 0x6e, 0x67, 0x58, 0x51, 0x4a, 0x43, 0x34, 0x3d, 0x26, 0x2f, 0x10, 0x19, 0x02, 0x0b,
        0xd7, 0xde, 0xc5, 0xcc, 0xf3, 0xfa, 0xe1, 0xe8, 0x9f, 0x96, 0x8d, 0x84, 0xbb, 0xb2, 0xa9, 0xa0,
        0x47, 0x4e, 0x55, 0x5c, 0x63, 0x6a, 0x71, 0x78, 0x0f, 0x06, 0x1d, 0x14, 0x2b, 0x22, 0x39, 0x30,
        0x9a, 0x93, 0x88, 0x81, 0xbe, 0xb7, 0xac, 0xa5, 0xd2, 0xdb, 0xc0, 0xc9, 0xf6, 0xff, 0xe4, 0xed,
        0x0a, 0x03, 0x18, 0x11, 0x2e, 0x27, 0x3c, 0x35, 0x42, 0x4b, 0x50, 0x59, 0x66, 0x6f, 0x74, 0x7d,
        0xa1, 0xa8, 0xb3, 0xba, 0x85, 0x8c, 0x97, 0x9e, 0xe9, 0xe0, 0xfb, 0xf2, 0xcd, 0xc4, 0xdf, 0xd6,
        0x31, 0x38, 0x23, 0x2a, 0x15, 0x1c, 0x07, 0x0e, 0x79, 0x70, 0x6b, 0x62, 0x5d, 0x54, 0x4f, 0x46,
    ]

    gMulBy11 = [
        0x00, 0x0b, 0x16, 0x1d, 0x2c, 0x27, 0x3a, 0x31, 0x58, 0x53, 0x4e, 0x45, 0x74, 0x7f, 0x62, 0x69,
        0xb0, 0xbb, 0xa6, 0xad, 0x9c, 0x97, 0x8a, 0x81, 0xe8, 0xe3, 0xfe, 0xf5, 0xc4, 0xcf, 0xd2, 0xd9,
        0x7b, 0x70, 0x6d, 0x66, 0x57, 0x5c, 0x41, 0x4a, 0x23, 0x28, 0x35, 0x3e, 0x0f, 0x04, 0x19, 0x12,
        0xcb, 0xc0, 0xdd, 0xd6, 0xe7, 0xec, 0xf1, 0xfa, 0x93, 0x98, 0x85, 0x8e, 0xbf, 0xb4, 0xa9, 0xa2,
        0xf6, 0xfd, 0xe0, 0xeb, 0xda, 0xd1, 0xcc, 0xc7, 0xae, 0xa5, 0xb8, 0xb3, 0x82, 0x89, 0x94, 0x9f,
        0x46, 0x4d, 0x50, 0x5b, 0x6a, 0x61, 0x7c, 0x77, 0x1e, 0x15, 0x08, 0x03, 0x32, 0x39, 0x24, 0x2f,
        0x8d, 0x86, 0x9b, 0x90, 0xa1, 0xaa, 0xb7, 0xbc, 0xd5, 0xde, 0xc3, 0xc8, 0xf9, 0xf2, 0xef, 0xe4,
        0x3d, 0x36, 0x2b, 0x20, 0x11, 0x1a, 0x07, 0x0c, 0x65, 0x6e, 0x73, 0x78, 0x49, 0x42, 0x5f, 0x54,
        0xf7, 0xfc, 0xe1, 0xea, 0xdb, 0xd0, 0xcd, 0xc6, 0xaf, 0xa4, 0xb9, 0xb2, 0x83, 0x88, 0x95, 0x9e,
        0x47, 0x4c, 0x51, 0x5a, 0x6b, 0x60, 0x7d, 0x76, 0x1f, 0x14, 0x09, 0x02, 0x33, 0x38, 0x25, 0x2e,
        0x8c, 0x87, 0x9a, 0x91, 0xa0, 0xab, 0xb6, 0xbd, 0xd4, 0xdf, 0xc2, 0xc9, 0xf8, 0xf3, 0xee, 0xe5,
        0x3c, 0x37, 0x2a, 0x21, 0x10, 0x1b, 0x06, 0x0d, 0x64, 0x6f, 0x72, 0x79, 0x48, 0x43, 0x5e, 0x55,
        0x01, 0x0a, 0x17, 0x1c, 0x2d, 0x26, 0x3b, 0x30, 0x59, 0x52, 0x4f, 0x44, 0x75, 0x7e, 0x63, 0x68,
        0xb1, 0xba, 0xa7, 0xac, 0x9d, 0x96, 0x8b, 0x80, 0xe9, 0xe2, 0xff, 0xf4, 0xc5, 0xce, 0xd3, 0xd8,
        0x7a, 0x71, 0x6c, 0x67, 0x56, 0x5d, 0x40, 0x4b, 0x22, 0x29, 0x34, 0x3f, 0x0e, 0x05, 0x18, 0x13,
        0xca, 0xc1, 0xdc, 0xd7, 0xe6, 0xed, 0xf0, 0xfb, 0x92, 0x99, 0x84, 0x8f, 0xbe, 0xb5, 0xa8, 0xa3,
    ]

    gMulBy13 = [
        0x00, 0x0d, 0x1a, 0x17, 0x34, 0x39, 0x2e, 0x23, 0x68, 0x65, 0x72, 0x7f, 0x5c, 0x51, 0x46, 0x4b,
        0xd0, 0xdd, 0xca, 0xc7, 0xe4, 0xe9, 0xfe, 0xf3, 0xb8, 0xb5, 0xa2, 0xaf, 0x8c, 0x81, 0x96, 0x9b,
        0xbb, 0xb6, 0xa1, 0xac, 0x8f, 0x82, 0x95, 0x98, 0xd3, 0xde, 0xc9, 0xc4, 0xe7, 0xea, 0xfd, 0xf0,
        0x6b, 0x66, 0x71, 0x7c, 0x5f, 0x52, 0x45, 0x48, 0x03, 0x0e, 0x19, 0x14, 0x37, 0x3a, 0x2d, 0x20,
        0x6d, 0x60, 0x77, 0x7a, 0x59, 0x54, 0x43, 0x4e, 0x05, 0x08, 0x1f, 0x12, 0x31, 0x3c, 0x2b, 0x26,
        0xbd, 0xb0, 0xa7, 0xaa, 0x89, 0x84, 0x93, 0x9e, 0xd5, 0xd8, 0xcf, 0xc2, 0xe1, 0xec, 0xfb, 0xf6,
        0xd6, 0xdb, 0xcc, 0xc1, 0xe2, 0xef, 0xf8, 0xf5, 0xbe, 0xb3, 0xa4, 0xa9, 0x8a, 0x87, 0x90, 0x9d,
        0x06, 0x0b, 0x1c, 0x11, 0x32, 0x3f, 0x28, 0x25, 0x6e, 0x63, 0x74, 0x79, 0x5a, 0x57, 0x40, 0x4d,
        0xda, 0xd7, 0xc0, 0xcd, 0xee, 0xe3, 0xf4, 0xf9, 0xb2, 0xbf, 0xa8, 0xa5, 0x86, 0x8b, 0x9c, 0x91,
        0x0a, 0x07, 0x10, 0x1d, 0x3e, 0x33, 0x24, 0x29, 0x62, 0x6f, 0x78, 0x75, 0x56, 0x5b, 0x4c, 0x41,
        0x61, 0x6c, 0x7b, 0x76, 0x55, 0x58, 0x4f, 0x42, 0x09, 0x04, 0x13, 0x1e, 0x3d, 0x30, 0x27, 0x2a,
        0xb1, 0xbc, 0xab, 0xa6, 0x85, 0x88, 0x9f, 0x92, 0xd9, 0xd4, 0xc3, 0xce, 0xed, 0xe0, 0xf7, 0xfa,
        0xb7, 0xba, 0xad, 0xa0, 0x83, 0x8e, 0x99, 0x94, 0xdf, 0xd2, 0xc5, 0xc8, 0xeb, 0xe6, 0xf1, 0xfc,
        0x67, 0x6a, 0x7d, 0x70, 0x53, 0x5e, 0x49, 0x44, 0x0f, 0x02, 0x15, 0x18, 0x3b, 0x36, 0x21, 0x2c,
        0x0c, 0x01, 0x16, 0x1b, 0x38, 0x35, 0x22, 0x2f, 0x64, 0x69, 0x7e, 0x73, 0x50, 0x5d, 0x4a, 0x47,
        0xdc, 0xd1, 0xc6, 0xcb, 0xe8, 0xe5, 0xf2, 0xff, 0xb4, 0xb9, 0xae, 0xa3, 0x80, 0x8d, 0x9a, 0x97,
    ]

    gMulBy14 = [
        0x00, 0x0e, 0x1c, 0x12, 0x38, 0x36, 0x24, 0x2a, 0x70, 0x7e, 0x6c, 0x62, 0x48, 0x46, 0x54, 0x5a,
        0xe0, 0xee, 0xfc, 0xf2, 0xd8, 0xd6, 0xc4, 0xca, 0x90, 0x9e, 0x8c, 0x82, 0xa8, 0xa6, 0xb4, 0xba,
        0xdb, 0xd5, 0xc7, 0xc9, 0xe3, 0xed, 0xff, 0xf1, 0xab, 0xa5, 0xb7, 0xb9, 0x93, 0x9d, 0x8f, 0x81,
        0x3b, 0x35, 0x27, 0x29, 0x03, 0x0d, 0x1f, 0x11, 0x4b, 0x45, 0x57, 0x59, 0x73, 0x7d, 0x6f, 0x61,
        0xad, 0xa3, 0xb1, 0xbf, 0x95, 0x9b, 0x89, 0x87, 0xdd, 0xd3, 0xc1, 0xcf, 0xe5, 0xeb, 0xf9, 0xf7,
        0x4d, 0x43, 0x51, 0x5f, 0x75, 0x7b, 0x69, 0x67, 0x3d, 0x33, 0x21, 0x2f, 0x05, 0x0b, 0x19, 0x17,
        0x76, 0x78, 0x6a, 0x64, 0x4e, 0x40, 0x52, 0x5c, 0x06, 0x08, 0x1a, 0x14, 0x3e, 0x30, 0x22, 0x2c,
        0x96, 0x98, 0x8a, 0x84, 0xae, 0xa0, 0xb2, 0xbc, 0xe6, 0xe8, 0xfa, 0xf4, 0xde, 0xd0, 0xc2, 0xcc,
        0x41, 0x4f, 0x5d, 0x53, 0x79, 0x77, 0x65, 0x6b, 0x31, 0x3f, 0x2d, 0x23, 0x09, 0x07, 0x15, 0x1b,
        0xa1, 0xaf, 0xbd, 0xb3, 0x99, 0x97, 0x85, 0x8b, 0xd1, 0xdf, 0xcd, 0xc3, 0xe9, 0xe7, 0xf5, 0xfb,
        0x9a, 0x94, 0x86, 0x88, 0xa2, 0xac, 0xbe, 0xb0, 0xea, 0xe4, 0xf6, 0xf8, 0xd2, 0xdc, 0xce, 0xc0,
        0x7a, 0x74, 0x66, 0x68, 0x42, 0x4c, 0x5e, 0x50, 0x0a, 0x04, 0x16, 0x18, 0x32, 0x3c, 0x2e, 0x20,
        0xec, 0xe2, 0xf0, 0xfe, 0xd4, 0xda, 0xc8, 0xc6, 0x9c, 0x92, 0x80, 0x8e, 0xa4, 0xaa, 0xb8, 0xb6,
        0x0c, 0x02, 0x10, 0x1e, 0x34, 0x3a, 0x28, 0x26, 0x7c, 0x72, 0x60, 0x6e, 0x44, 0x4a, 0x58, 0x56,
        0x37, 0x39, 0x2b, 0x25, 0x0f, 0x01, 0x13, 0x1d, 0x47, 0x49, 0x5b, 0x55, 0x7f, 0x71, 0x63, 0x6d,
        0xd7, 0xd9, 0xcb, 0xc5, 0xef, 0xe1, 0xf3, 0xfd, 0xa7, 0xa9, 0xbb, 0xb5, 0x9f, 0x91, 0x83, 0x8d,
    ]

    def calcMixCols(self, a0, a1, a2, a3):
        # r0 = 2*a0 + 3*a1 + a2   + a3
        # r1 = a0   + 2*a1 + 3*a2 + a3
        # r2 = a0   + a1   + 2*a2 + 3*a3
        # r3 = 3*a0 + a1   + a2   + 2*a3
        r0 = self.gMulBy2[a0] ^ self.gMulBy3[a1] ^ a2 ^ a3
        r1 = a0 ^ self.gMulBy2[a1] ^ self.gMulBy3[a2] ^ a3
        r2 = a0 ^ a1 ^ self.gMulBy2[a2] ^ self.gMulBy3[a3]
        r3 = self.gMulBy3[a0] ^ a1 ^ a2 ^ self.gMulBy2[a3]
        return [hex(r0)[2:].zfill(2), hex(r1)[2:].zfill(2), hex(r2)[2:].zfill(2), hex(r3)[2:].zfill(2)]
    # Galois Multiplication

    def calcInvMixCols(self, a0, a1, a2, a3):
        # r0 = 14*a0 + 11*a1 + 13*a2 +  9*a3
        # r1 =  9*a0 + 14*a1 + 11*a2 + 13*a3
        # r2 = 13*a0 +  9*a1 + 14*a2 + 11*a3
        # r3 = 11*a0 + 13*a1 +  9*a2 + 14*a3
        r0 = self.gMulBy14[a0] ^ self.gMulBy11[a1] ^ self.gMulBy13[a2] ^ self.gMulBy9[a3]
        r1 = self.gMulBy9[a0] ^ self.gMulBy14[a1] ^ self.gMulBy11[a2] ^ self.gMulBy13[a3]
        r2 = self.gMulBy13[a0] ^ self.gMulBy9[a1] ^ self.gMulBy14[a2] ^ self.gMulBy11[a3]
        r3 = self.gMulBy11[a0] ^ self.gMulBy13[a1] ^ self.gMulBy9[a2] ^ self.gMulBy14[a3]
        return [hex(r0)[2:].zfill(2), hex(r1)[2:].zfill(2), hex(r2)[2:].zfill(2), hex(r3)[2:].zfill(2)]

    def rotate(self, l, n):
        return l[n:] + l[:n]

    def addRoundKey(self, state, roundkey, num):
        newState = state
        for i in range(4):
            col = state[0][i]+state[1][i]+state[2][i]+state[3][i]
            if i == 0:
                print("The col: ", col)
            # print("the Rou: ", roundkey[i])
            new = hex(int(col, 16) ^ int(roundkey[i], 16) | 0x00000000)[2:]
            new = new.zfill(8)
            # print("the new: ", new)
            newState[0][i] = new[:2]
            newState[1][i] = new[2:4]
            newState[2][i] = new[4:6]
            newState[3][i] = new[6:8]
        return newState

    def rotWord(self, word):
        return self.rotate(word, 2)

    def subWord(self, word):
        subbedWord = ""
        for i in range(0, 8, 2):
            row = int(word[i], 16)
            col = int(word[i+1], 16)
            subbedWord += self.sbox0[row][col]
        return subbedWord
    rcon = ['01000000', '02000000', '04000000', '08000000', '10000000',
            '20000000', '40000000', '80000000', '1b000000', '36000000',
            ]

    def generateTempWord(self, word, i):
        rotatedWord = self.rotWord(word)
        subWord = self.subWord(rotatedWord)
        result = hex(int(self.rcon[i-1], 16) ^ int(subWord, 16))
        return result.zfill(8)

    def keyExaption(self, key):
        """
        takes 128 bit key and expand it into 128*11 bit
        input key: in bytes form, each 1 digit is one byte
        return: is an array containing 44 128-bit keys 
                divided into words
        """
        outputArray = [0]*11
        # transfom key from byte to hex digits
        outputArray[0] = [key[0:8], key[8:16], key[16:24], key[24:32]]
        print(outputArray[0])
        for i in range(1, 11):
            temp = int(self.generateTempWord(outputArray[i-1][3], i), 16)
            w0 = hex(temp ^ int(outputArray[i-1][0], 16))[2:]
            w1 = hex(int(w0, 16) ^ int(outputArray[i-1][1], 16))[2:]
            w2 = hex(int(w1, 16) ^ int(outputArray[i-1][2], 16))[2:]
            w3 = hex(int(w2, 16) ^ int(outputArray[i-1][3], 16))[2:]
            outputArray[i] = [w0.zfill(8), w1.zfill(
                8), w2.zfill(8), w3.zfill(8)]
        return outputArray

    def subBytes(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                row = int(state[i][j][0], 16)
                col = int(state[i][j][1], 16)
                state[i][j] = self.sbox0[row][col]
        return state

    def invSubBytes(self, state):
        for i in range(len(state)):
            for j in range(len(state[i])):
                row = int(state[i][j][0], 16)
                col = int(state[i][j][1], 16)
                state[i][j] = self.sbox1[row][col]
                print("row: ", row, "col: ", col, "value: ", state[i][j])
        return state

    def shiftRow(self, subBytes):
        newArray = [1]*4  # mask array
        for i in range(len(subBytes)):
            newArray[i] = self.rotate(subBytes[i], i)
        return newArray

    def invShiftRow(self, subBytes):
        newArray = [1]*4  # mask array
        for i in range(len(subBytes)):
            newArray[i] = self.rotate(subBytes[i], i*-1)
        return newArray

    def mixColumns(self, lis):
        listHolder = [0]*4
        for i in range(len(lis)):
            resultCol = self.calcMixCols(int(lis[0][i], 16), int(
                lis[1][i], 16), int(lis[2][i], 16), int(lis[3][i], 16))
            listHolder[i] = resultCol
        return listHolder
    # state is the input matrix
# output is the output matrix after MixColumns operation

    def newMixColumns(self, state):
        output = [[0 for i in range(4)] for j in range(4)]
        for i in range(4):
            output[0][i] = hex(self.gf_mul(2, int(state[0][i], 16)) ^ self.gf_mul(
                3, int(state[1][i], 16)) ^ int(state[2][i], 16) ^ int(state[3][i], 16))[2:].zfill(2)
            output[1][i] = hex(int(state[0][i], 16) ^ self.gf_mul(2, int(state[1][i], 16)) ^
                               self.gf_mul(3, int(state[2][i], 16)) ^ int(state[3][i], 16))[2:].zfill(2)
            output[2][i] = hex(int(state[0][i], 16) ^ int(state[1][i], 16) ^ self.gf_mul(
                2, int(state[2][i], 16)) ^ self.gf_mul(3, int(state[3][i], 16)))[2:].zfill(2)
            output[3][i] = hex(self.gf_mul(3, int(state[0][i], 16)) ^ int(state[1][i], 16) ^
                               int(state[2][i], 16) ^ self.gf_mul(2, int(state[3][i], 16)))[2:].zfill(2)
        return output

    def invMixColumns(self, lis):
        listHolder = [0]*4
        for i in range(len(lis)):
            if i == 0:
                print(lis[0][i],
                      lis[1][i], lis[2][i], 16, lis[3][i])
            resultCol = self.calcInvMixCols(int(lis[0][i], 16), int(
                lis[1][i], 16), int(lis[2][i], 16), int(lis[3][i], 16))
            listHolder[i] = resultCol
        return listHolder

    # state is the input matrix
    # output is the output matrix after invMixColumns operation
    def newInvMixColumns(self, state):
        output = [[0 for i in range(4)] for j in range(4)]
        for i in range(4):
            print(state[0][i], state[1][i], state[2][i], state[3][i])
            output[0][i] = (hex(self.gf_mul(0x0e, int(state[0][i], 16)) ^ self.gf_mul(
                0x0b, int(state[1][i], 16)) ^ self.gf_mul(0x0d, int(state[2][i], 16)) ^ self.gf_mul(0x09, int(state[3][i], 16)))[2:]).zfill(2)
            output[1][i] = (hex(self.gf_mul(0x09, int(state[0][i], 16)) ^ self.gf_mul(
                0x0e, int(state[1][i], 16)) ^ self.gf_mul(0x0b, int(state[2][i], 16)) ^ self.gf_mul(0x0d, int(state[3][i], 16)))[2:]).zfill(2)
            output[2][i] = (hex(self.gf_mul(0x0d, int(state[0][i], 16)) ^ self.gf_mul(
                0x09, int(state[1][i], 16)) ^ self.gf_mul(0x0e, int(state[2][i], 16)) ^ self.gf_mul(0x0b, int(state[3][i], 16)))[2:]).zfill(2)
            output[3][i] = (hex(self.gf_mul(0x0b, int(state[0][i], 16)) ^ self.gf_mul(
                0x0d, int(state[1][i], 16)) ^ self.gf_mul(0x09, int(state[2][i], 16)) ^ self.gf_mul(0x0e, int(state[3][i], 16)))[2:]).zfill(2)
        print("the output: ", output)
        return output
    # gf_mul is a function that calculates multiplication over a finite field
# it takes two inputs and returns the multiplication result

    def gf_mul(self, a, b):
        p = 0
        for counter in range(8):
            if b & 1:
                p ^= a
            hi_bit_set = a & 0x80
            a <<= 1
            a &= 0xff
            if hi_bit_set:
                a ^= 0x1b
            b >>= 1
        return p

    def a2Hex(self, key):
        string = key.encode("utf-8")
        string = string.hex()
        return string

    def prepareText(self, plainText):
        textSize = len(plainText)
        hexString = self.stringToHex(plainText)
        if(textSize < 16):
            for i in range(textSize, 16):
                hexString += "00"
        elif textSize > 16 and textSize % 16 != 0:
            for i in range(textSize, (textSize + (16 - textSize % 16))):
                hexString += "00"
        return hexString

    def generateState(self, block):
        # create state from the block
        state = [[0 for x in range(4)] for y in range(4)]
        # print("original message: ", block)
        for k in range(int(len(block)/2)):
            state[k % 4][int(k/4)] = block[k*2:k*2+2]
            # transform key
        return state

    def encrypt(self, plainText, key, rounds):
        cipher_text = ""
        hexString = self.prepareText(plainText)
        print("plain: ", hexString)
        textSize = int(len(hexString)/2)
        # generate key
        hexKey = self.a2Hex(key)
        expKey = self.keyExaption(hexKey)
        for i in range(int(textSize/16)):  # loop through each block
            block = hexString[i*32: i*32+32]
            state = self.generateState(block)
            print("keys for round0: ", expKey[0])
            state = self.addRoundKey(state, expKey[0], 0)
            print("addKey0 state0: ", state)
            for i in range(1, 11):
                print("keys for round", i, ": ", expKey[i])
                subBytes = self.subBytes(state)
                print("subByte state"+str(i)+": ", subBytes)
                shifted = self.shiftRow(subBytes)
                print("shifted state"+str(i)+": ", shifted)
                if i != 10:
                    mixedColumn = self.newMixColumns(shifted)
                    print("mixCol state"+str(i)+": ", mixedColumn)
                    state = self.addRoundKey(mixedColumn, expKey[i], i)
                else:
                    state = self.addRoundKey(shifted, expKey[i], i)
                print("addKey state"+str(i)+": ", state)
            # transfer state into text
            textState = self.stringfyState(state)
            cipher_text += textState
        return cipher_text

    def decrypt(self, cipher, key):
        plainText = ""
        # hexString = self.prepareText(cipher)
        hexString = cipher
        hexKey = self.a2Hex(key)
        expKey = self.keyExaption(hexKey)
        expKey.reverse()
        textSize = int(len(hexString)/2)
        for i in range(int(textSize/16)):
            block = hexString[i*32: i*32+32]
            print("cipher: ", block, "size in hex: ", len(block))
            state = self.generateState(block)
            state = self.addRoundKey(state, expKey[0], 0)
            print("addKey state0: ", state)
            for i in range(1, 11):
                print("keys for round", i, ": ", expKey[i])
                shifted = self.invShiftRow(state)
                print("shifted state"+str(i)+": ", shifted)
                subBytes = self.invSubBytes(shifted)
                print("subByte state"+str(i)+": ", subBytes)
                state = self.addRoundKey(subBytes, expKey[i], i)
                print("withKey state"+str(i)+": ", state)
                if i != 10:
                    state = self.newInvMixColumns(state)
                    print("mixCol state"+str(i)+": ", state)
            textState = self.stringfyState(state)
            plainText += textState
        return plainText

    def stringfyState(self, state):
        text = ""
        for i in range(len(state)):
            text += state[i][0]
        for i in range(len(state)):
            text += state[i][1]
        for i in range(len(state)):
            text += state[i][2]
        for i in range(len(state)):
            text += state[i][3]
        return text

    def stringToHex(self, text):
        string = text.encode("utf-8")
        hexOut = string.hex()
        return hexOut

def getKeyBitSizes():
    return ['128', '192', '256']

def generateKey(size):
    if int(size) in list(map(int, getKeyBitSizes())):
        # generate random key
        numOfChar = int(int(size)/8)
        key = get_random_string(numOfChar)
        return key
    else:
        return "key size is not valid"

def isAsymmetric():
    return False

def construct():
    return AES()


# trd = AES().generateKey(256)
# print(trd)
# cipher = AES().encrypt("faisaljabushanab", "abc1234567890123", None)
# print("cipher:\t", cipher)
# hexe = "faisaljabushanab".encode().hex()
# print("hexText:\t", hexe)
# plain = AES().decrypt(
#     "2d96cd1d5f88861546821024df27b3bc", 'abc1234567890123')
# print("cipher:\t\t", "2d96cd1d5f88861546821024df27b3bc")
# print("plainText:\t", plain)
# hexe = "faisaljabushanab".encode().hex()
# print("hexText:\t", hexe)
# print(hexe == plain)
# # 580fd9329040973a395b9a5e17939f187f97c96c0f00ef42339add712f5b360b
