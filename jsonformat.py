#!/usr/bin/env python
jsonval = {
    "status": "succeeded",
    "createdDateTime": "2020-10-09T12:16:36Z",
    "lastUpdatedDateTime": "2020-10-09T12:16:37Z",
    "analyzeResult": {
        "version": "3.0.0",
        "readResults": [
            {
                "page": 1,
                "angle": -2.3778,
                "width": 4608,
                "height": 2176,
                "unit": "pixel",
                "lines": [
                    {
                        "boundingBox": [
                            342,
                            472,
                            3418,
                            459,
                            3419,
                            634,
                            343,
                            646
                        ],
                        "text": "Minoxidil 5%",
                        "words": [
                            {
                                "boundingBox": [
                                    365,
                                    481,
                                    1536,
                                    467,
                                    1535,
                                    641,
                                    366,
                                    646
                                ],
                                "text": "Minoxidil",
                                "confidence": 0.69
                            },
                            {
                                "boundingBox": [
                                    1755,
                                    465,
                                    2127,
                                    462,
                                    2125,
                                    639,
                                    1754,
                                    640
                                ],
                                "text": "5%",
                                "confidence": 0.887
                            },
                            {
                                "boundingBox": [
                                    2324,
                                    461,
                                    3419,
                                    460,
                                    3415,
                                    637,
                                    2322,
                                    639
                                ],
                                "text": "recognition",
                                "confidence": 0.652
                            }
                        ]
                    },
                    {
                        "boundingBox": [
                            371,
                            1244,
                            1959,
                            1188,
                            1970,
                            1356,
                            371,
                            1447
                        ],
                        "text": "Crocin - 200",
                        "words": [
                            {
                                "boundingBox": [
                                    386,
                                    1244,
                                    1198,
                                    1229,
                                    1203,
                                    1394,
                                    385,
                                    1447
                                ],
                                "text": "Crocin",
                                "confidence": 0.57
                            },
                            {
                                "boundingBox": [
                                    1238,
                                    1227,
                                    1441,
                                    1218,
                                    1448,
                                    1375,
                                    1243,
                                    1391
                                ],
                                "text": "-",
                                "confidence": 0.981
                            },
                            {
                                "boundingBox": [
                                    1589,
                                    1208,
                                    1954,
                                    1188,
                                    1965,
                                    1331,
                                    1597,
                                    1362
                                ],
                                "text": "200",
                                "confidence": 0.986
                            }
                        ]
                    },
                    {
                        "boundingBox": [
                            446,
                            1515,
                            2505,
                            1432,
                            2513,
                            1610,
                            454,
                            1698
                        ],
                        "text": "Rigene - 1 bottle",
                        "words": [
                            {
                                "boundingBox": [
                                    471,
                                    1515,
                                    1298,
                                    1490,
                                    1309,
                                    1659,
                                    485,
                                    1698
                                ],
                                "text": "Rigene",
                                "confidence": 0.722
                            },
                            {
                                "boundingBox": [
                                    1347,
                                    1489,
                                    1542,
                                    1481,
                                    1552,
                                    1648,
                                    1358,
                                    1656
                                ],
                                "text": "-",
                                "confidence": 0.985
                            },
                            {
                                "boundingBox": [
                                    1627,
                                    1477,
                                    1809,
                                    1469,
                                    1818,
                                    1636,
                                    1637,
                                    1644
                                ],
                                "text": "1",
                                "confidence": 0.559
                            },
                            {
                                "boundingBox": [
                                    1907,
                                    1465,
                                    2502,
                                    1433,
                                    2509,
                                    1609,
                                    1915,
                                    1632
                                ],
                                "text": "bottle",
                                "confidence": 0.786
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
allvals=[]
for val in jsonval["analyzeResult"]["readResults"][0]["lines"]:
    text = val['text'].split()
    for word in text:
        if(word.isalnum()):
            allvals.append(word.lower())
# print(allvals)
import difflib
mr = difflib.SequenceMatcher()
ratios = []
meds = ["minoxidil 5%","medall 200"]
final_meds = []
for medicine in meds:
    final_meds.extend(medicine.split())
print(final_meds)
# med = ["rantac","crocin","digene"]
for meds in allvals:
  for check_med in final_meds:
    seq = difflib.SequenceMatcher(None,meds,check_med)
    d = seq.ratio()*100
    ratios.append([meds,check_med,d])
# print(ratios)
allow=[]
for ratio in ratios:
  if(ratio[2]>60 and ratio[0].isalpha()):
    allow.append(ratio[0])
print(allow)
# print(allvals)

#  $command = escapeshellcmd('python3 /usr/custom/test.py');
#     $output = shell_exec($command);
#     echo $output;