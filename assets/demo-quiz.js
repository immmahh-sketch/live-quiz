/* The built-in demo, playable without signing in: host.html?quiz=demo (the phone demo wraps it).
   A tick-box picker chooses question types; the demo then plays one sample question of each. */
window.DEMO_SAMPLES = {
 "twenty": {"id":"d_tq","type":"twenty","text":"20 Questions: who am I?","answers":["Gary Barlow","Barlow"],"what":"person","facts":{"p_man":true,"p_woman":false,"p_alive":true,"p_over50":true,"p_over70":false,"p_under30":false,"p_history":false,"p_british":true,"p_american":false,"p_irish":false,"p_knighted":false,"p_english":true,"p_scottish":false,"p_welsh":false,"p_northeast":false,"p_north":true,"p_london":false,"p_music":true,"p_actor":false,"p_sport":false,"p_tv":false,"p_comedy":false,"p_politics":false,"p_royal":false,"p_writer":false,"p_science":false,"p_business":false,"p_hero":false,"p_b1970":false,"p_b1980":false,"p_b1990":false,"p_b2000":true,"p_b2010":true,"p_band":true,"p_boyband":true,"p_frontman":true,"p_solo":true,"p_number1":true,"p_christmas1":false,"p_songwriter":true,"p_instrument":true,"p_pop":true,"p_rock":false,"p_rap":false,"p_soul":false,"p_dance":false,"p_talent":false,"p_judge":true,"p_acted":false,"p_brit":true,"p_grammy":false,"p_glasto":false,"p_active":true,"p_hollywood":false,"p_oscar":false,"p_soap":false,"p_sitcom":false,"p_funny":false,"p_action":false,"p_bond":false,"p_superhero":false,"p_potter":false,"p_whoactor":false,"p_voice":false,"p_sang":false,"p_period":false,"p_stage":false,"p_football":false,"p_cricket":false,"p_tennis":false,"p_rugby":false,"p_athletics":false,"p_boxing":false,"p_motor":false,"p_golf":false,"p_cycling":false,"p_swim":false,"p_cue":false,"p_country":false,"p_captain":false,"p_olympic":false,"p_world":false,"p_spoty":false,"p_retired":false,"p_pundit":false,"p_manager":false,"p_toon":false,"p_mackem":false,"p_prem":false,"p_manutd":false,"p_liverpool":false,"p_striker":false,"p_keeper":false,"p_reality":false,"p_gameshow":false,"p_chat":false,"p_saturday":false,"p_cook":false,"p_nature":false,"p_news":false,"p_duo":false,"p_strictly":false,"p_jungle":false,"p_daytime":false,"p_kidstv":false,"p_standup":false,"p_panel":false,"p_csitcom":false,"p_double":false,"p_characters":false,"p_silent":false,"p_cfilm":false,"p_pm":false,"p_president":false,"p_mp":false,"p_labour":false,"p_tory":false,"p_inoffice":false,"p_wartime":false,"p_resigned":false,"p_monarch":false,"p_heir":false,"p_marriedin":false,"p_tudor":false,"p_divorced":false,"p_kidsbooks":false,"p_crime":false,"p_poet":false,"p_plays":false,"p_fantasy":false,"p_filmed":false,"p_bookseries":false,"p_school":false,"p_invented":false,"p_theory":false,"p_space":false,"p_medicine":false,"p_nobel":false,"p_tvsci":false,"p_billion":false,"p_techco":false,"p_shopco":false,"p_den":false,"p_rocket":false,"p_sea":false,"p_war":false,"p_rescue":false,"p_explore":false,"p_astro":false,"p_nurse":false},"maxQ":20,"prize":1000,"prize2":500,"prize3":100,"penalty":200,"time":120,"media":{"kind":"none"},"partial":false},
 "choice": {
  "id": "q_cc8eeb0f",
  "tags": [
   "calendar"
  ],
  "text": "How many days are in a leap year?",
  "time": 25,
  "type": "choice",
  "media": {
   "kind": "none"
  },
  "correct": "o_c73aa489",
  "options": [
   {
    "id": "o_f549ec90",
    "text": "365"
   },
   {
    "id": "o_59ae8169",
    "text": "364"
   },
   {
    "id": "o_c73aa489",
    "text": "366"
   },
   {
    "id": "o_97c9a1ab",
    "text": "367"
   }
  ],
  "partial": false,
  "category": "General knowledge",
  "difficulty": "easy"
 },
 "text": {
  "ai": true,
  "id": "q_7a02f416",
  "tags": [
   "money"
  ],
  "text": "What is the name of the currency used in the USA?",
  "time": 25,
  "type": "text",
  "media": {
   "kind": "none"
  },
  "answers": [
   "Dollar",
   "US dollar",
   "Dollars"
  ],
  "partial": false,
  "category": "General knowledge",
  "difficulty": "easy"
 },
 "order": {
  "id": "q_3be3fe5b",
  "hint": "earliest to latest",
  "tags": [
   "Christmas"
  ],
  "text": "Put these Christmas events in order through December",
  "time": 25,
  "type": "order",
  "items": [
   {
    "id": "i_707efcf9",
    "text": "Advent Sunday"
   },
   {
    "id": "i_93451c9a",
    "text": "Christmas Eve"
   },
   {
    "id": "i_c5072d87",
    "text": "Christmas Day"
   },
   {
    "id": "i_2cf4ffd7",
    "text": "Boxing Day"
   }
  ],
  "media": {
   "kind": "none"
  },
  "partial": false,
  "category": "General knowledge",
  "difficulty": "easy"
 },
 "pin": {
  "id": "q_71ec49d4",
  "pin": {
   "x": 0.3553,
   "y": 0.9225
  },
  "tags": [
   "UK",
   "Britain",
   "counties",
   "cities",
   "rivers"
  ],
  "text": "Which island group lies about 28 miles south-west of Land's End?",
  "time": 25,
  "type": "pin",
  "media": {
   "url": "https://safcrtrfdzsnftghibot.supabase.co/storage/v1/object/public/quiz-media/maps/united-kingdom.png",
   "kind": "image",
   "credit": "Wikimedia Commons: the United Kingdom location map"
  },
  "place": "Isles of Scilly",
  "partial": false,
  "category": "UK geography",
  "mapBounds": {
   "top": 61,
   "left": -11,
   "right": 2.2,
   "bottom": 49
  },
  "mapRegion": "the United Kingdom",
  "difficulty": "easy",
  "radiusFull": 0.012,
  "radiusZero": 0.048
 },
 "match": {
  "id": "q_0879cc6e",
  "tags": [
   "general"
  ],
  "text": "Match each author to their detective",
  "time": 25,
  "type": "match",
  "media": {
   "kind": "none"
  },
  "pairs": [
   {
    "id": "p_605f9b0e",
    "left": "Arthur Conan Doyle",
    "right": {
     "kind": "text",
     "value": "Sherlock Holmes"
    }
   },
   {
    "id": "p_ba5e64b2",
    "left": "Agatha Christie",
    "right": {
     "kind": "text",
     "value": "Hercule Poirot"
    }
   },
   {
    "id": "p_acfdc78a",
    "left": "Ian Rankin",
    "right": {
     "kind": "text",
     "value": "John Rebus"
    }
   },
   {
    "id": "p_b6d15fb9",
    "left": "Colin Dexter",
    "right": {
     "kind": "text",
     "value": "Inspector Morse"
    }
   }
  ],
  "partial": false,
  "category": "General knowledge",
  "difficulty": "easy"
 },
 "tf": {
  "id": "q_d49ad3df",
  "tags": [
   "calendar"
  ],
  "text": "A leap year has 366 days.",
  "time": 25,
  "type": "tf",
  "media": {
   "kind": "none"
  },
  "answer": true,
  "partial": false,
  "category": "General knowledge",
  "difficulty": "easy"
 },
 "sort": {
  "id": "q_ad04df88",
  "tags": [
   "food",
   "Europe"
  ],
  "text": "Sort these into the right country",
  "time": 25,
  "type": "sort",
  "items": [
   {
    "id": "i_c21420d8",
    "text": "Croissant",
    "category": "c_a7208cca"
   },
   {
    "id": "i_815bf9ff",
    "text": "Risotto",
    "category": "c_100cd81e"
   },
   {
    "id": "i_9482e257",
    "text": "Paella",
    "category": "c_4300b65a"
   },
   {
    "id": "i_0e82c39f",
    "text": "Ratatouille",
    "category": "c_a7208cca"
   },
   {
    "id": "i_e40f47e1",
    "text": "Tiramisu",
    "category": "c_100cd81e"
   },
   {
    "id": "i_058c7e37",
    "text": "Gazpacho",
    "category": "c_4300b65a"
   }
  ],
  "media": {
   "kind": "none"
  },
  "partial": false,
  "category": "Food and drink",
  "categories": [
   {
    "id": "c_a7208cca",
    "name": "France"
   },
   {
    "id": "c_100cd81e",
    "name": "Italy"
   },
   {
    "id": "c_4300b65a",
    "name": "Spain"
   }
  ],
  "difficulty": "easy"
 },
 "smash": {
  "ai": true,
  "id": "q_350f8e92",
  "tags": [],
  "text": "Shakespeare's brooding Prince of Denmark",
  "time": 30,
  "type": "smash",
  "media": {
   "url": "https://safcrtrfdzsnftghibot.supabase.co/storage/v1/object/public/quiz-media/wiki/david-beckham-fe6a9bf0.jpg",
   "kind": "image",
   "credit": "Wikipedia / Wikimedia Commons: David Beckham",
   "source": "https://thumb.wikimedia.org/wikipedia/commons/thumb/8/81/David_Beckham%2C_Montreal_Impact_v_LA_Galaxy_01_May_2012.jpg/1920px-David_Beckham%2C_Montreal_Impact_v_LA_Galaxy_01_May_2012.jpg"
  },
  "smash": "David Beckhamlet",
  "partial": false,
  "category": "General knowledge",
  "clueAnswer": "Hamlet",
  "difficulty": "easy",
  "pictureAnswer": "David Beckham"
 },
 "wheel": {
  "ai": true,
  "id": "q_13a59054",
  "tags": [
   "general"
  ],
  "text": "BREAK THE ICE",
  "time": 25,
  "type": "wheel",
  "media": {
   "kind": "none"
  },
  "phrase": "BREAK THE ICE",
  "partial": false,
  "category": "General knowledge",
  "difficulty": "easy",
  "revealEvery": 4,
  "startLetters": ""
 },
 "highlow": {
  "ai": true,
  "id": "q_ede72d37",
  "tags": [
   "general"
  ],
  "text": "Which chemical element, atomic number 79, has the symbol Au?",
  "time": 40,
  "type": "highlow",
  "media": {
   "kind": "none"
  },
  "answers": [
   "Gold"
  ],
  "lowText": "What colour medal does the winner get at the Olympics?",
  "partial": false,
  "category": "General knowledge",
  "lowPoints": 500,
  "difficulty": "easy",
  "highPoints": 1000
 },
 "rhyme": {
  "ai": true,
  "id": "q_e4ac2683",
  "tags": [
   "music",
   "radio"
  ],
  "text": "'Starman' singer, David",
  "time": 25,
  "type": "rhyme",
  "media": {
   "kind": "none"
  },
  "text2": "Ball, the Radio 2 breakfast presenter",
  "answer1": "Bowie",
  "answer2": "Zoe",
  "partial": false,
  "category": "Pop music",
  "difficulty": "easy"
 },
 "club": {
  "ai": true,
  "id": "q_87329109",
  "pct": 90,
  "why": "Tom is taller than Sam and Sam is taller than Ali, so Ali is shorter than both.",
  "tags": [
   "general"
  ],
  "text": "Tom is taller than Sam, and Sam is taller than Ali. Who is the shortest?",
  "time": 30,
  "type": "club",
  "media": {
   "kind": "none"
  },
  "answers": [
   "Ali"
  ],
  "partial": false,
  "category": "General knowledge",
  "difficulty": "easy"
 },
 "dingbat": {
  "ai": true,
  "id": "q_ea370ae5",
  "tags": [
   "general"
  ],
  "text": "Say what you see",
  "time": 45,
  "type": "dingbat",
  "media": {
   "kind": "none"
  },
  "answers": [
   "Go for it"
  ],
  "partial": false,
  "category": "General knowledge",
  "elements": [
   {
    "s": 5,
    "t": "GO",
    "x": 25,
    "y": 50
   },
   {
    "s": 5,
    "t": "4",
    "x": 50,
    "y": 50
   },
   {
    "s": 5,
    "t": "IT",
    "x": 75,
    "y": 50
   }
  ],
  "difficulty": "easy"
 },
 "tune": {
  "ai": true,
  "id": "q_c25af0dc",
  "ask": "artist",
  "film": "",
  "tags": [
   "general"
  ],
  "text": "",
  "time": 30,
  "type": "tune",
  "year": 1976,
  "media": {
   "url": "https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview211/v4/ec/b1/63/ecb163bc-aff2-4dd2-d40b-c044f0b9fa4d/mzaf_4358783485405794088.plus.aac.p.m4a",
   "kind": "audio",
   "start": 0,
   "credit": "Preview via Apple Music",
   "length": 15,
   "artwork": "https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/60/f8/a6/60f8a6bc-e875-238d-f2f8-f34a6034e6d2/14UMGIM07615.rgb.jpg/100x100bb.jpg"
  },
  "track": "Dancing Queen",
  "artist": "ABBA",
  "answers": [
   "ABBA"
  ],
  "partial": false,
  "category": "General knowledge",
  "tolerance": 1,
  "difficulty": "easy"
 },
 "race": {
  "id": "d11",
  "round": "r1",
  "type": "race",
  "text": "The Race: capital cities",
  "time": 120,
  "media": {
   "kind": "none"
  },
  "target": 10,
  "perCorrect": 100,
  "prize": 500,
  "prize2": 200,
  "prize3": 100,
  "forfeit": 200,
  "bank": [
   {
    "id": "d11b0",
    "text": "Capital of France?",
    "options": [
     "Paris",
     "Lyon",
     "Marseille",
     "Nice"
    ]
   },
   {
    "id": "d11b1",
    "text": "Capital of Japan?",
    "options": [
     "Tokyo",
     "Osaka",
     "Kyoto",
     "Nagoya"
    ]
   },
   {
    "id": "d11b2",
    "text": "Capital of Australia?",
    "options": [
     "Canberra",
     "Sydney",
     "Melbourne",
     "Perth"
    ]
   },
   {
    "id": "d11b3",
    "text": "Capital of Canada?",
    "options": [
     "Ottawa",
     "Toronto",
     "Vancouver",
     "Montreal"
    ]
   },
   {
    "id": "d11b4",
    "text": "Capital of Brazil?",
    "options": [
     "Brasília",
     "Rio de Janeiro",
     "São Paulo",
     "Salvador"
    ]
   },
   {
    "id": "d11b5",
    "text": "Capital of Turkey?",
    "options": [
     "Ankara",
     "Istanbul",
     "Izmir",
     "Antalya"
    ]
   },
   {
    "id": "d11b6",
    "text": "Capital of Nigeria?",
    "options": [
     "Abuja",
     "Lagos",
     "Kano",
     "Ibadan"
    ]
   },
   {
    "id": "d11b7",
    "text": "Capital of Switzerland?",
    "options": [
     "Bern",
     "Zurich",
     "Geneva",
     "Basel"
    ]
   },
   {
    "id": "d11b8",
    "text": "Capital of Spain?",
    "options": [
     "Madrid",
     "Barcelona",
     "Seville",
     "Valencia"
    ]
   },
   {
    "id": "d11b9",
    "text": "Capital of Italy?",
    "options": [
     "Rome",
     "Milan",
     "Naples",
     "Turin"
    ]
   },
   {
    "id": "d11b10",
    "text": "Capital of Germany?",
    "options": [
     "Berlin",
     "Munich",
     "Hamburg",
     "Frankfurt"
    ]
   },
   {
    "id": "d11b11",
    "text": "Capital of Egypt?",
    "options": [
     "Cairo",
     "Alexandria",
     "Giza",
     "Luxor"
    ]
   },
   {
    "id": "d11b12",
    "text": "Capital of India?",
    "options": [
     "New Delhi",
     "Mumbai",
     "Kolkata",
     "Bangalore"
    ]
   },
   {
    "id": "d11b13",
    "text": "Capital of the USA?",
    "options": [
     "Washington, D.C.",
     "New York",
     "Los Angeles",
     "Chicago"
    ]
   },
   {
    "id": "d11b14",
    "text": "Capital of Argentina?",
    "options": [
     "Buenos Aires",
     "Córdoba",
     "Rosario",
     "Mendoza"
    ]
   },
   {
    "id": "d11b15",
    "text": "Capital of South Korea?",
    "options": [
     "Seoul",
     "Busan",
     "Incheon",
     "Daegu"
    ]
   },
   {
    "id": "d11b16",
    "text": "Capital of Kenya?",
    "options": [
     "Nairobi",
     "Mombasa",
     "Kisumu",
     "Nakuru"
    ]
   },
   {
    "id": "d11b17",
    "text": "Capital of Portugal?",
    "options": [
     "Lisbon",
     "Porto",
     "Faro",
     "Coimbra"
    ]
   },
   {
    "id": "d11b18",
    "text": "Capital of New Zealand?",
    "options": [
     "Wellington",
     "Auckland",
     "Christchurch",
     "Dunedin"
    ]
   },
   {
    "id": "d11b19",
    "text": "Capital of Scotland?",
    "options": [
     "Edinburgh",
     "Glasgow",
     "Aberdeen",
     "Dundee"
    ]
   }
  ]
 },
 "wipeout": {
  "id": "d10",
  "round": "r1",
  "type": "wipeout",
  "text": "Wipeout: countries in Africa",
  "time": 5,
  "media": {
   "kind": "none"
  },
  "pickPoints": 200,
  "penalty": 500,
  "right": [
   {
    "id": "d10r0",
    "text": "Nigeria"
   },
   {
    "id": "d10r1",
    "text": "Kenya"
   },
   {
    "id": "d10r2",
    "text": "Ghana"
   },
   {
    "id": "d10r3",
    "text": "Egypt"
   },
   {
    "id": "d10r4",
    "text": "Morocco"
   },
   {
    "id": "d10r5",
    "text": "Ethiopia"
   },
   {
    "id": "d10r6",
    "text": "Senegal"
   },
   {
    "id": "d10r7",
    "text": "Tanzania"
   },
   {
    "id": "d10r8",
    "text": "Uganda"
   },
   {
    "id": "d10r9",
    "text": "Zambia"
   },
   {
    "id": "d10r10",
    "text": "Namibia"
   },
   {
    "id": "d10r11",
    "text": "Botswana"
   },
   {
    "id": "d10r12",
    "text": "Mali"
   },
   {
    "id": "d10r13",
    "text": "Tunisia"
   },
   {
    "id": "d10r14",
    "text": "Angola"
   }
  ],
  "wrong": [
   {
    "id": "d10w0",
    "text": "Yemen"
   },
   {
    "id": "d10w1",
    "text": "Oman"
   },
   {
    "id": "d10w2",
    "text": "Suriname"
   },
   {
    "id": "d10w3",
    "text": "Nepal"
   },
   {
    "id": "d10w4",
    "text": "Georgia"
   }
  ]
 },
 "potato": {
  "id": "d20",
  "round": "r1",
  "type": "potato",
  "text": "Hot Potato: general knowledge",
  "time": 60,
  "media": {
   "kind": "none"
  },
  "fuseMin": 30,
  "fuseMax": 60,
  "perCorrect": 50,
  "penalty": 300,
  "bank": [
   {
    "id": "d20b0",
    "text": "How many sides does a hexagon have?",
    "options": [
     "Six",
     "Five",
     "Seven",
     "Eight"
    ]
   },
   {
    "id": "d20b1",
    "text": "What colour is a London bus?",
    "options": [
     "Red",
     "Blue",
     "Green",
     "Yellow"
    ]
   },
   {
    "id": "d20b2",
    "text": "Which planet is known as the Red Planet?",
    "options": [
     "Mars",
     "Venus",
     "Jupiter",
     "Saturn"
    ]
   },
   {
    "id": "d20b3",
    "text": "How many players does a football team have on the pitch?",
    "options": [
     "Eleven",
     "Ten",
     "Twelve",
     "Nine"
    ]
   },
   {
    "id": "d20b4",
    "text": "What is the capital of France?",
    "options": [
     "Paris",
     "Lyon",
     "Marseille",
     "Nice"
    ]
   },
   {
    "id": "d20b5",
    "text": "Which animal says \"moo\"?",
    "options": [
     "Cow",
     "Sheep",
     "Goat",
     "Horse"
    ]
   },
   {
    "id": "d20b6",
    "text": "What is 7 × 8?",
    "options": [
     "56",
     "54",
     "64",
     "48"
    ]
   },
   {
    "id": "d20b7",
    "text": "Which is the largest ocean?",
    "options": [
     "Pacific",
     "Atlantic",
     "Indian",
     "Arctic"
    ]
   },
   {
    "id": "d20b8",
    "text": "What is frozen water called?",
    "options": [
     "Ice",
     "Steam",
     "Snow",
     "Frost"
    ]
   },
   {
    "id": "d20b9",
    "text": "An apple a day keeps who away?",
    "options": [
     "The doctor",
     "The dentist",
     "The postman",
     "The vicar"
    ]
   },
   {
    "id": "d20b10",
    "text": "How many days are in a leap year?",
    "options": [
     "366",
     "365",
     "364",
     "367"
    ]
   },
   {
    "id": "d20b11",
    "text": "Which bird is the symbol of peace?",
    "options": [
     "Dove",
     "Eagle",
     "Robin",
     "Swan"
    ]
   },
   {
    "id": "d20b12",
    "text": "What is the largest mammal?",
    "options": [
     "Blue whale",
     "Elephant",
     "Giraffe",
     "Hippo"
    ]
   },
   {
    "id": "d20b13",
    "text": "Which city is home to Big Ben?",
    "options": [
     "London",
     "Manchester",
     "Edinburgh",
     "Cardiff"
    ]
   },
   {
    "id": "d20b14",
    "text": "How many legs does a spider have?",
    "options": [
     "Eight",
     "Six",
     "Ten",
     "Twelve"
    ]
   },
   {
    "id": "d20b15",
    "text": "Which gas do plants take in?",
    "options": [
     "Carbon dioxide",
     "Oxygen",
     "Nitrogen",
     "Helium"
    ]
   },
   {
    "id": "d20b16",
    "text": "Which river flows through Newcastle?",
    "options": [
     "Tyne",
     "Wear",
     "Tees",
     "Thames"
    ]
   },
   {
    "id": "d20b17",
    "text": "Which river flows through Sunderland?",
    "options": [
     "Wear",
     "Tyne",
     "Tees",
     "Mersey"
    ]
   },
   {
    "id": "d20b18",
    "text": "What is the square root of 81?",
    "options": [
     "Nine",
     "Eight",
     "Seven",
     "Six"
    ]
   },
   {
    "id": "d20b19",
    "text": "Which country is shaped like a boot?",
    "options": [
     "Italy",
     "Spain",
     "Greece",
     "Portugal"
    ]
   }
  ]
 },
 "nearest": {
  "id": "d25",
  "round": "r1",
  "type": "nearest",
  "text": "How many steps are there to the top of Grey's Monument in Newcastle?",
  "time": 25,
  "media": {
   "kind": "none"
  },
  "partial": false,
  "answer": "164",
  "unit": "steps",
  "spread": null
 },
 "chase": {
  "id": "d23",
  "round": "r1",
  "type": "chase",
  "text": "The Chase: before the break",
  "time": 15,
  "media": {
   "kind": "none"
  },
  "headStart": 2,
  "target": 5,
  "teamPrize": 1000,
  "chaserPrize": 200,
  "bank": [
   {
    "id": "d23b0",
    "text": "Which country is home to the kangaroo?",
    "options": [
     "Australia",
     "New Zealand",
     "South Africa",
     "Brazil"
    ]
   },
   {
    "id": "d23b1",
    "text": "How many continents are there?",
    "options": [
     "Seven",
     "Five",
     "Six",
     "Eight"
    ]
   },
   {
    "id": "d23b2",
    "text": "What is the capital of Scotland?",
    "options": [
     "Edinburgh",
     "Glasgow",
     "Aberdeen",
     "Dundee"
    ]
   },
   {
    "id": "d23b3",
    "text": "Which sport is played at Wimbledon?",
    "options": [
     "Tennis",
     "Cricket",
     "Golf",
     "Rugby"
    ]
   },
   {
    "id": "d23b4",
    "text": "How many hours are in a day?",
    "options": [
     "24",
     "12",
     "48",
     "36"
    ]
   },
   {
    "id": "d23b5",
    "text": "What colour do you get mixing blue and yellow?",
    "options": [
     "Green",
     "Purple",
     "Orange",
     "Brown"
    ]
   },
   {
    "id": "d23b6",
    "text": "Which is the tallest animal?",
    "options": [
     "Giraffe",
     "Elephant",
     "Camel",
     "Horse"
    ]
   },
   {
    "id": "d23b7",
    "text": "Who wrote Oliver Twist?",
    "options": [
     "Charles Dickens",
     "Jane Austen",
     "Thomas Hardy",
     "George Eliot"
    ]
   },
   {
    "id": "d23b8",
    "text": "What is the chemical symbol for water?",
    "options": [
     "H2O",
     "CO2",
     "O2",
     "NaCl"
    ]
   },
   {
    "id": "d23b9",
    "text": "Which planet do we live on?",
    "options": [
     "Earth",
     "Mars",
     "Venus",
     "Saturn"
    ]
   },
   {
    "id": "d23b10",
    "text": "How many weeks are in a year?",
    "options": [
     "52",
     "48",
     "50",
     "56"
    ]
   },
   {
    "id": "d23b11",
    "text": "Which instrument has pedals and 47 strings?",
    "options": [
     "Harp",
     "Piano",
     "Cello",
     "Guitar"
    ]
   },
   {
    "id": "d23b12",
    "text": "What is the capital of Wales?",
    "options": [
     "Cardiff",
     "Swansea",
     "Newport",
     "Bangor"
    ]
   },
   {
    "id": "d23b13",
    "text": "Which sea creature has eight arms?",
    "options": [
     "Octopus",
     "Squid",
     "Starfish",
     "Jellyfish"
    ]
   },
   {
    "id": "d23b14",
    "text": "In which city is the Colosseum?",
    "options": [
     "Rome",
     "Athens",
     "Paris",
     "Madrid"
    ]
   },
   {
    "id": "d23b15",
    "text": "What is the freezing point of water in Celsius?",
    "options": [
     "0",
     "10",
     "32",
     "-10"
    ]
   },
   {
    "id": "d23b16",
    "text": "Which fruit is dried to make a raisin?",
    "options": [
     "Grape",
     "Plum",
     "Apricot",
     "Fig"
    ]
   },
   {
    "id": "d23b17",
    "text": "How many players are on a netball team on court?",
    "options": [
     "Seven",
     "Five",
     "Six",
     "Nine"
    ]
   },
   {
    "id": "d23b18",
    "text": "Which bird lays the largest eggs?",
    "options": [
     "Ostrich",
     "Emu",
     "Eagle",
     "Swan"
    ]
   },
   {
    "id": "d23b19",
    "text": "What is the largest country in the world by area?",
    "options": [
     "Russia",
     "Canada",
     "China",
     "USA"
    ]
   },
   {
    "id": "d23b20",
    "text": "Which metal is liquid at room temperature?",
    "options": [
     "Mercury",
     "Lead",
     "Tin",
     "Zinc"
    ]
   },
   {
    "id": "d23b21",
    "text": "What do bees make?",
    "options": [
     "Honey",
     "Silk",
     "Wax only",
     "Nectar"
    ]
   },
   {
    "id": "d23b22",
    "text": "Which North East city is famous for its Angel sculpture nearby?",
    "options": [
     "Gateshead",
     "Durham",
     "Sunderland",
     "Middlesbrough"
    ]
   },
   {
    "id": "d23b23",
    "text": "How many sides does a triangle have?",
    "options": [
     "Three",
     "Four",
     "Two",
     "Five"
    ]
   }
  ]
 },
 "koth": {
  "id": "d21",
  "round": "r2",
  "type": "koth",
  "text": "King of the Hill: general knowledge",
  "time": 15,
  "media": {
   "kind": "none"
  },
  "target": 3,
  "prize": 1000,
  "answerSecs": 3,
  "bank": [
   {
    "id": "d21b0",
    "text": "Which is the smallest planet in our solar system?",
    "options": [
     "Mercury",
     "Mars",
     "Venus",
     "Pluto"
    ]
   },
   {
    "id": "d21b1",
    "text": "Who wrote Romeo and Juliet?",
    "options": [
     "Shakespeare",
     "Dickens",
     "Chaucer",
     "Marlowe"
    ]
   },
   {
    "id": "d21b2",
    "text": "What is the chemical symbol for gold?",
    "options": [
     "Au",
     "Ag",
     "Gd",
     "Go"
    ]
   },
   {
    "id": "d21b3",
    "text": "How many strings does a standard guitar have?",
    "options": [
     "Six",
     "Four",
     "Five",
     "Seven"
    ]
   },
   {
    "id": "d21b4",
    "text": "Which country gave the Statue of Liberty to the USA?",
    "options": [
     "France",
     "Britain",
     "Spain",
     "Italy"
    ]
   },
   {
    "id": "d21b5",
    "text": "What is the capital of Japan?",
    "options": [
     "Tokyo",
     "Osaka",
     "Kyoto",
     "Hiroshima"
    ]
   },
   {
    "id": "d21b6",
    "text": "Which club plays at St James' Park?",
    "options": [
     "Newcastle United",
     "Sunderland",
     "Middlesbrough",
     "Leeds United"
    ]
   },
   {
    "id": "d21b7",
    "text": "Which club plays at the Stadium of Light?",
    "options": [
     "Sunderland",
     "Newcastle United",
     "Hartlepool United",
     "Middlesbrough"
    ]
   },
   {
    "id": "d21b8",
    "text": "How many hearts does an octopus have?",
    "options": [
     "Three",
     "One",
     "Two",
     "Four"
    ]
   },
   {
    "id": "d21b9",
    "text": "What is the longest river in Africa?",
    "options": [
     "Nile",
     "Congo",
     "Niger",
     "Zambezi"
    ]
   },
   {
    "id": "d21b10",
    "text": "In which year did the Second World War end?",
    "options": [
     "1945",
     "1944",
     "1946",
     "1939"
    ]
   },
   {
    "id": "d21b11",
    "text": "What is the hardest natural substance?",
    "options": [
     "Diamond",
     "Granite",
     "Quartz",
     "Iron"
    ]
   },
   {
    "id": "d21b12",
    "text": "Which instrument has 88 keys?",
    "options": [
     "Piano",
     "Organ",
     "Accordion",
     "Harpsichord"
    ]
   },
   {
    "id": "d21b13",
    "text": "What is the capital of Australia?",
    "options": [
     "Canberra",
     "Sydney",
     "Melbourne",
     "Perth"
    ]
   },
   {
    "id": "d21b14",
    "text": "Which planet has the most famous rings?",
    "options": [
     "Saturn",
     "Jupiter",
     "Uranus",
     "Neptune"
    ]
   },
   {
    "id": "d21b15",
    "text": "How many minutes are there in a day?",
    "options": [
     "1,440",
     "1,200",
     "1,600",
     "1,340"
    ]
   },
   {
    "id": "d21b16",
    "text": "Who painted The Starry Night?",
    "options": [
     "Van Gogh",
     "Monet",
     "Picasso",
     "Dalí"
    ]
   },
   {
    "id": "d21b17",
    "text": "Which Newcastle bridge tilts to let boats through?",
    "options": [
     "Gateshead Millennium Bridge",
     "Tyne Bridge",
     "High Level Bridge",
     "Redheugh Bridge"
    ]
   },
   {
    "id": "d21b18",
    "text": "At what temperature in Celsius does water boil?",
    "options": [
     "100",
     "90",
     "212",
     "80"
    ]
   },
   {
    "id": "d21b19",
    "text": "Who was the first person to walk on the Moon?",
    "options": [
     "Neil Armstrong",
     "Buzz Aldrin",
     "Yuri Gagarin",
     "John Glenn"
    ]
   },
   {
    "id": "d21b20",
    "text": "Which is the only mammal that can truly fly?",
    "options": [
     "Bat",
     "Flying squirrel",
     "Sugar glider",
     "Colugo"
    ]
   },
   {
    "id": "d21b21",
    "text": "How many sides does a 50p coin have?",
    "options": [
     "Seven",
     "Six",
     "Eight",
     "Five"
    ]
   }
  ]
 },
 "draw": {
  "id": "d26",
  "round": "r2",
  "type": "draw",
  "text": "Draw It: anything goes",
  "time": 60,
  "media": {
   "kind": "none"
  },
  "partial": false,
  "turns": 3,
  "words": [],
  "guessPoints": 500,
  "drawerPoints": 100
 },
 "blockbusters": {
  "id": "d22",
  "round": "r2",
  "type": "blockbusters",
  "text": "Blockbusters: general knowledge",
  "time": 20,
  "media": {
   "kind": "none"
  },
  "teams": [
   {
    "name": "Newcastle",
    "color": "#f2f2f2"
   },
   {
    "name": "Sunderland",
    "color": "#e21b3c"
   }
  ],
  "hexPoints": 50,
  "prize": 500,
  "bank": [
   {
    "id": "d22b0",
    "text": "Seabird with the longest wingspan of any bird",
    "options": [
     "Albatross",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b1",
    "text": "Capital of Germany",
    "options": [
     "Berlin",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b2",
    "text": "Capital of Egypt",
    "options": [
     "Cairo",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b3",
    "text": "Country whose capital is Copenhagen",
    "options": [
     "Denmark",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b4",
    "text": "Tallest mountain in the world",
    "options": [
     "Everest",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b5",
    "text": "Country famous for the Eiffel Tower",
    "options": [
     "France",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b6",
    "text": "Hermione's surname in Harry Potter",
    "options": [
     "Granger",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b7",
    "text": "Gas used to fill party balloons",
    "options": [
     "Helium",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b8",
    "text": "Country whose capital is Rome",
    "options": [
     "Italy",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b9",
    "text": "Largest planet in our solar system",
    "options": [
     "Jupiter",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b10",
    "text": "Australian animal that carries its baby in a pouch",
    "options": [
     "Kangaroo",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b11",
    "text": "Capital of Portugal",
    "options": [
     "Lisbon",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b12",
    "text": "Planet closest to the Sun",
    "options": [
     "Mercury",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b13",
    "text": "Longest river in Africa",
    "options": [
     "Nile",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b14",
    "text": "Fruit that is also a colour",
    "options": [
     "Orange",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b15",
    "text": "Largest ocean on Earth",
    "options": [
     "Pacific",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b16",
    "text": "Capital of Italy",
    "options": [
     "Rome",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b17",
    "text": "Planet with the most famous rings",
    "options": [
     "Saturn",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b18",
    "text": "River that flows through Newcastle",
    "options": [
     "Tyne",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b19",
    "text": "Mythical horse with a single horn",
    "options": [
     "Unicorn",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b20",
    "text": "Italian city built on canals",
    "options": [
     "Venice",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b21",
    "text": "River that flows through Sunderland",
    "options": [
     "Wear",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b22",
    "text": "Colour of a ripe banana",
    "options": [
     "Yellow",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b23",
    "text": "Capital of Spain",
    "options": [
     "Madrid",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b24",
    "text": "Capital of Norway",
    "options": [
     "Oslo",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b25",
    "text": "Big cat with black stripes",
    "options": [
     "Tiger",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b26",
    "text": "Home city of the Beatles",
    "options": [
     "Liverpool",
     "",
     "",
     ""
    ]
   },
   {
    "id": "d22b27",
    "text": "Metal with the chemical symbol Fe",
    "options": [
     "Iron",
     "",
     "",
     ""
    ]
   }
  ]
 },
 "catchphrase": {
  "id": "d_cp",
  "type": "text",
  "kind": "catchphrase",
  "text": "Catchphrase: say what you see",
  "time": 50,
  "media": {
   "kind": "youtube",
   "url": "https://www.youtube.com/watch?v=wWwQNpoyNXI",
   "videoId": "wWwQNpoyNXI",
   "start": 0,
   "end": 50
  },
  "partial": false,
  "answers": [
   "Driving rain"
  ],
  "ai": true
 }
};
/** The types in the order the picker shows them, with the same labels and icons as the builder. */
window.DEMO_TYPES = [
  ['choice', 'Multiple choice', '◆'], ['text', 'Type the answer', '✎'], ['tf', 'True or false', '✓✗'], ['order', 'Put in order', '↕'],
  ['sort', 'Categorise', '🗂'], ['match', 'Match up', '⇄'], ['pin', 'Drop the pin', '📍'], ['highlow', 'Highbrow Lowbrow', '🎓'],
  ['smash', 'Answer Smash', '🔀'], ['rhyme', 'Rhyme Time', '🎤'], ['wheel', 'Wheel of Fortune', '🎡'], ['club', 'The 1% Club', '🧠'],
  ['dingbat', 'Dingbats', '🔤'], ['tune', 'Name That Tune', '🎵'], ['catchphrase', 'Catchphrase', '🗯️'], ['nearest', 'Nearest Wins', '🎯'],
  ['wipeout', 'Wipeout', '💥'], ['race', 'The Race', '🏁'], ['potato', 'Hot Potato', '💣'], ['koth', 'King of the Hill', '👑'],
  ['chase', 'The Chase', '🏃'], ['blockbusters', 'Blockbusters', '⬢'], ['draw', 'Draw It', '🎨'], ['twenty', '20 Questions', '🕵️'],
];
/** A demo quiz with one question of each chosen type, in picker order. */
window.demoQuiz = function (types) {
  const pick = window.DEMO_TYPES.map((t) => t[0]).filter((t) => types.includes(t) && window.DEMO_SAMPLES[t]);
  const questions = pick.map((t, i) => Object.assign(JSON.parse(JSON.stringify(window.DEMO_SAMPLES[t])), { id: 'd' + (i + 1), round: 'r1' }));
  return { id: 'demo', title: 'Demo quiz', settings: { maxPoints: 1000, minPoints: 500, defaultTime: 20, showAnswersOnPhones: true, rounds: [{ id: 'r1', title: 'Demo', intro: 'One question of each type you picked', brief: '' }] }, questions };
};
/** The last choice, kept on this device so the next demo starts from it. */
window.demoTypesSaved = function () {
  try { const s = JSON.parse(localStorage.getItem('lq_demo_types') || 'null'); if (Array.isArray(s) && s.length) return s; } catch {}
  return ['catchphrase', 'twenty'];
};
/** Tick boxes for the question types, then a Start button that hands the chosen types to onStart. */
window.demoPicker = function (el, onStart) {
  const chosen = new Set(window.demoTypesSaved());
  el.innerHTML = `<div style="max-width:880px;margin:0 auto;padding:18px 16px;color:#fff;font-family:Nunito,system-ui,sans-serif">
    <h1 style="margin:0 0 4px;font-size:clamp(1.4rem,4vw,2.2rem);font-weight:900">Try the demo</h1>
    <p style="margin:0 0 14px;opacity:.85;font-weight:700">Tick the question types to try. The demo plays one question of each.</p>
    <div style="display:flex;gap:8px;margin-bottom:12px"><button type="button" data-all style="${btn(false)}">Tick all</button><button type="button" data-none style="${btn(false)}">Clear</button></div>
    <div data-grid style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px"></div>
    <div style="display:flex;align-items:center;gap:12px;margin-top:16px"><button type="button" data-go style="${btn(true)}">Start demo ▶</button><span data-n style="font-weight:800;opacity:.85"></span></div></div>`;
  function btn(primary) { return `font:inherit;font-weight:900;border:0;border-radius:12px;padding:10px 18px;cursor:pointer;${primary ? 'background:#ffd60a;color:#17173a;font-size:1.15rem' : 'background:rgba(255,255,255,.15);color:#fff'}`; }
  const grid = el.querySelector('[data-grid]'), go = el.querySelector('[data-go]');
  function draw() {
    grid.innerHTML = window.DEMO_TYPES.map(([t, label, icon]) => { const on = chosen.has(t); return `<button type="button" role="checkbox" aria-checked="${on}" data-t="${t}" style="display:flex;align-items:center;gap:10px;text-align:left;font:inherit;font-weight:800;padding:10px 12px;border-radius:12px;cursor:pointer;border:2px solid ${on ? '#ffd60a' : 'rgba(255,255,255,.25)'};background:${on ? 'rgba(255,214,10,.18)' : 'rgba(255,255,255,.06)'};color:#fff"><span style="font-size:1.3rem;width:1.4em">${on ? '☑' : '☐'}</span><span>${icon} ${label}</span></button>`; }).join('');
    grid.querySelectorAll('[data-t]').forEach((b) => b.onclick = () => { chosen.has(b.dataset.t) ? chosen.delete(b.dataset.t) : chosen.add(b.dataset.t); draw(); const f = grid.querySelector(`[data-t="${b.dataset.t}"]`); f?.focus(); });
    el.querySelector('[data-n]').textContent = chosen.size ? `${chosen.size} question${chosen.size === 1 ? '' : 's'}` : 'Tick at least one type';
    go.disabled = !chosen.size; go.style.opacity = chosen.size ? '1' : '.5';
  }
  el.querySelector('[data-all]').onclick = () => { window.DEMO_TYPES.forEach(([t]) => chosen.add(t)); draw(); };
  el.querySelector('[data-none]').onclick = () => { chosen.clear(); draw(); };
  go.onclick = () => { if (!chosen.size) return; const list = window.DEMO_TYPES.map((t) => t[0]).filter((t) => chosen.has(t)); try { localStorage.setItem('lq_demo_types', JSON.stringify(list)); } catch {} onStart(list); };
  draw();
  (grid.querySelector('[data-t]') || go).focus();
};
/** Kept for anything that still reads the fixed demo: the saved choice (Catchphrase and 20 Questions the first time). */
window.DEMO_QUIZ = window.demoQuiz(window.demoTypesSaved());
