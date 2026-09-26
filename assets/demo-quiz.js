/* A built-in sample quiz so the game can be tried before any quiz is saved: host.html?quiz=demo
   One of each party game: the race, Wipeout, Hot Potato, Nearest Wins, the Chase, a break, King of the Hill, Draw It, Blockbusters, the final Chase. */
window.DEMO_QUIZ = {
  "id": "demo",
  "title": "Demo quiz",
  "settings": {
    "maxPoints": 1000,
    "minPoints": 500,
    "defaultTime": 20,
    "showAnswersOnPhones": true,
    "rounds": [
      {
        "id": "r1",
        "title": "Party games",
        "intro": "The Race, Wipeout, Hot Potato, Nearest Wins and the first Chase, then a break",
        "brief": ""
      },
      {
        "id": "r2",
        "title": "Head to head",
        "intro": "King of the Hill, Draw It, Blockbusters and the final Chase",
        "brief": ""
      }
    ]
  },
  "questions": [
    {
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
    {
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
    {
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
    {
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
    {
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
    {
      "id": "dB",
      "round": "r1",
      "type": "slide",
      "text": "Half-time",
      "break": true,
      "breakMins": 1,
      "time": 15,
      "media": {
        "kind": "none"
      },
      "body": "Top up your drinks. Back when the clock runs out!"
    },
    {
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
    {
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
    {
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
    {
      "id": "d24",
      "round": "r2",
      "type": "chase",
      "text": "The Chase: the final chase",
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
          "id": "d24b0",
          "text": "Which band sang \"Hey Jude\"?",
          "options": [
            "The Beatles",
            "The Rolling Stones",
            "Queen",
            "The Who"
          ]
        },
        {
          "id": "d24b1",
          "text": "What is the capital of Ireland?",
          "options": [
            "Dublin",
            "Cork",
            "Belfast",
            "Galway"
          ]
        },
        {
          "id": "d24b2",
          "text": "How many centimetres are in a metre?",
          "options": [
            "100",
            "10",
            "1,000",
            "50"
          ]
        },
        {
          "id": "d24b3",
          "text": "Which animal is known as the King of the Jungle?",
          "options": [
            "Lion",
            "Tiger",
            "Gorilla",
            "Elephant"
          ]
        },
        {
          "id": "d24b4",
          "text": "What is the main ingredient of guacamole?",
          "options": [
            "Avocado",
            "Tomato",
            "Pea",
            "Lime"
          ]
        },
        {
          "id": "d24b5",
          "text": "Which ocean lies between Europe and America?",
          "options": [
            "Atlantic",
            "Pacific",
            "Indian",
            "Arctic"
          ]
        },
        {
          "id": "d24b6",
          "text": "Who painted the Mona Lisa?",
          "options": [
            "Leonardo da Vinci",
            "Michelangelo",
            "Raphael",
            "Botticelli"
          ]
        },
        {
          "id": "d24b7",
          "text": "Which gas do we breathe in to live?",
          "options": [
            "Oxygen",
            "Carbon dioxide",
            "Nitrogen",
            "Hydrogen"
          ]
        },
        {
          "id": "d24b8",
          "text": "What is the name of the UK parliament clock tower?",
          "options": [
            "Elizabeth Tower",
            "Victoria Tower",
            "Albert Tower",
            "Jewel Tower"
          ]
        },
        {
          "id": "d24b9",
          "text": "How many years are in a century?",
          "options": [
            "100",
            "10",
            "1,000",
            "50"
          ]
        },
        {
          "id": "d24b10",
          "text": "Which country is famous for tulips and windmills?",
          "options": [
            "The Netherlands",
            "Belgium",
            "Denmark",
            "Switzerland"
          ]
        },
        {
          "id": "d24b11",
          "text": "What is the fastest land animal?",
          "options": [
            "Cheetah",
            "Leopard",
            "Horse",
            "Greyhound"
          ]
        },
        {
          "id": "d24b12",
          "text": "Which Sunderland stadium opened in 1997?",
          "options": [
            "Stadium of Light",
            "Roker Park",
            "The Riverside",
            "St James' Park"
          ]
        },
        {
          "id": "d24b13",
          "text": "What is 12 × 12?",
          "options": [
            "144",
            "124",
            "132",
            "156"
          ]
        },
        {
          "id": "d24b14",
          "text": "Which is the largest bone in the human body?",
          "options": [
            "Femur",
            "Tibia",
            "Humerus",
            "Spine"
          ]
        },
        {
          "id": "d24b15",
          "text": "What is the capital of Canada?",
          "options": [
            "Ottawa",
            "Toronto",
            "Vancouver",
            "Montreal"
          ]
        },
        {
          "id": "d24b16",
          "text": "Which famous ship sank in 1912?",
          "options": [
            "Titanic",
            "Lusitania",
            "Mary Rose",
            "Bismarck"
          ]
        },
        {
          "id": "d24b17",
          "text": "How many strings does a violin have?",
          "options": [
            "Four",
            "Five",
            "Six",
            "Three"
          ]
        },
        {
          "id": "d24b18",
          "text": "Which planet is the hottest?",
          "options": [
            "Venus",
            "Mercury",
            "Mars",
            "Jupiter"
          ]
        },
        {
          "id": "d24b19",
          "text": "What do caterpillars turn into?",
          "options": [
            "Butterflies",
            "Beetles",
            "Spiders",
            "Worms"
          ]
        },
        {
          "id": "d24b20",
          "text": "Which country hosted the 2012 Olympics?",
          "options": [
            "Great Britain",
            "China",
            "Brazil",
            "Greece"
          ]
        },
        {
          "id": "d24b21",
          "text": "How many sides does a pentagon have?",
          "options": [
            "Five",
            "Six",
            "Four",
            "Eight"
          ]
        },
        {
          "id": "d24b22",
          "text": "Which snooker ball is worth the most?",
          "options": [
            "Black",
            "Pink",
            "Blue",
            "Brown"
          ]
        },
        {
          "id": "d24b23",
          "text": "What is the capital of Egypt?",
          "options": [
            "Cairo",
            "Alexandria",
            "Giza",
            "Luxor"
          ]
        }
      ]
    }
  ]
};
