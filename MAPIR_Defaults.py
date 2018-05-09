"""MAPIR_Defaults.py constains the default values for the survey 1,2,3 and kernal cameras

These defaults serve as substitutes for values that would be derived from the calibration targets
"""
# the following constants are default values for the camera if the target is not used

BASE_COEFF_SURVEY2_RED_JPG = [-2.55421832, 16.01240929, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_SURVEY2_GREEN_JPG = [0.0, 0.0, -0.60437250, 4.82869470, 0.0, 0.0]
BASE_COEFF_SURVEY2_BLUE_JPG = [0.0, 0.0, 0.0, 0.0, -0.39268985, 2.67916884]
BASE_COEFF_SURVEY2_NDVI_JPG = [-0.29870245, 6.51199915, 0.0, 0.0, -0.65112026, 10.30416005]
BASE_COEFF_SURVEY2_NIR_JPG = [-0.46967653, 7.13619139, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_SURVEY1_NDVI_JPG = [-6.33770486888, 331.759383023, 0.0, 0.0, -0.6931339436, 51.3264675118]
BASE_COEFF_SURVEY2_RED_TIF = [-5.09645820, 0.24177528, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_SURVEY2_GREEN_TIF = [0.0, 0.0, -1.39528479, 0.07640011, 0.0, 0.0]
BASE_COEFF_SURVEY2_BLUE_TIF = [0.0, 0.0, 0.0, 0.0, -0.67299134, 0.03943339]
BASE_COEFF_SURVEY2_NDVI_TIF = [3.21946584661, 1.06087488594, 0.0, 0.0, -43.6505776052, 1.46482226805]
BASE_COEFF_SURVEY2_NIR_TIF = [-2.24216724, 0.12962333, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_SURVEY3_W_NGB_TIF = [13.2610911247, 3.97721174076, 5.73811506234]
BASE_COEFF_SURVEY3_N_NGB_TIF = [13.2610911247, 3.97721174076, 5.73811506234]
BASE_COEFF_SURVEY3_W_RGN_TIF = [5.09994742157, 3.85344547793, 9.49432813587]
BASE_COEFF_SURVEY3_N_RGN_TIF = [5.09994742157, 3.85344547793, 9.49432813587]
BASE_COEFF_SURVEY3_N_NIR_TIF = [13.2610911247, 0.0, 0.0]
BASE_COEFF_DJIX3_NDVI_JPG = [-0.34430543, 4.63184993, 0.0, 0.0, -0.49413940, 16.36429964]
BASE_COEFF_DJIX3_NDVI_TIF = [-0.74925346, 0.01350319, 0.0, 0.0, -0.77810008, 0.03478272]
BASE_COEFF_DJIPHANTOM4_NDVI_JPG = [-1.17016961, 0.03333209, 0.0, 0.0, -0.99455214, 0.05373502]
BASE_COEFF_DJIPHANTOM4_NDVI_TIF = [-1.17016961, 0.03333209, 0.0, 0.0, -0.99455214, 0.05373502]
BASE_COEFF_DJIPHANTOM3_NDVI_JPG = [-1.54494979, 3.44708472, 0.0, 0.0, -1.40606832, 6.35407929]
BASE_COEFF_DJIPHANTOM3_NDVI_TIF = [-1.37495554, 0.01752340, 0.0, 0.0, -1.41073753, 0.03700812]
BASE_COEFF_KERNEL_F644 = [0.0, 0.0]
BASE_COEFF_KERNEL_F405 = [0.0, 0.0]
BASE_COEFF_KERNEL_F450 = [0.0, 0.0]
BASE_COEFF_KERNEL_F520 = [0.0, 0.0]
BASE_COEFF_KERNEL_F550 = [0.0, 0.0]
BASE_COEFF_KERNEL_F632 = [0.0, 0.0]
BASE_COEFF_KERNEL_F650 = [0.0, 0.0]
BASE_COEFF_KERNEL_F725 = [0.0, 0.0]
BASE_COEFF_KERNEL_F808 = [0.0, 0.0]
BASE_COEFF_KERNEL_F850 = [0.0, 0.0]
BASE_COEFF_KERNEL_F395_870 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_KERNEL_F475_850 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_KERNEL_F550_850 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_KERNEL_F660_850 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_KERNEL_F475_550_850 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
BASE_COEFF_KERNEL_F550_660_850 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

SQ_TO_TARG = 2.1875
SQ_TO_SQ = 5.0
CORNER_TO_CORNER = 5.25
CORNER_TO_TARG = 10.0
TARGET_LENGTH = 2.0
TARG_TO_TARG = 2.6


BandNames = {
        "RGB": [644, 0, 0],
        "405": [405, 0, 0],
        "450": [450, 0, 0],
        "490": [490, 0, 0],
        "518": [518, 0, 0],
        "550": [550, 0, 0],
        "590": [590, 0, 0],
        "615": [615, 0, 0],
        "632": [632, 0, 0],
        "650": [650, 0, 0],
        "685": [685, 0, 0],
        "725": [725, 0, 0],
        "780": [780, 0, 0],
        "808": [808, 0, 0],
        "850": [850, 0, 0],
        "880": [880, 0, 0],
        "940": [940, 0, 0],
        "945": [945, 0, 0],
        "UVR": [870, 0, 395],
        "NGB": [850, 550, 475],
        "RGN": [660, 550, 850],
        "OCN": [615, 490, 808],

    }
refindex = ["oldrefvalues", "newrefvalues"]
refvalues = {
    "oldrefvalues": {
        "660/850": [[0.87032549, 0.52135779, 0.23664799], [0, 0, 0], [0.8463514, 0.51950608, 0.22795518]],
        "446/800": [[0.8419608509, 0.520440145, 0.230113958], [0, 0, 0], [0.8645652801, 0.5037779363, 0.2359041624]],
        "850": [[0.8463514, 0.51950608, 0.22795518], [0, 0, 0], [0, 0, 0]],
        # "808": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        "650": [[0.87032549, 0.52135779, 0.23664799], [0, 0, 0], [0, 0, 0]],
        "550": [[0, 0, 0], [0.87415089, 0.51734381, 0.24032515], [0, 0, 0]],
        "450": [[0, 0, 0], [0, 0, 0], [0.86469794, 0.50392915, 0.23565447]],
        "Mono450": [0.8634818638, 0.5024087105, 0.2351860396],
        "Mono550": [0.8740616379, 0.5173070235, 0.2402423818],
        "Mono650": [0.8705783136, 0.5212290524, 0.2366437854],
        "Mono725": [0.8606071247, 0.521474266, 0.2337744252],
        "Mono808": [0.8406184266, 0.5203405498, 0.2297701185],
        "Mono850": [0.8481919553, 0.519491643, 0.2278713071],
        "Mono405": [0.8556905469, 0.4921243183, 0.2309899254],
        "Mono518": [0.8729814889, 0.5151370187, 0.2404729692],
        "Mono632": [0.8724034645, 0.5209649915, 0.2374529161],
        # "Mono660": [0.8704202831, 0.5212214688, 0.2365919358],
        "Mono590": [0.8747043911, 0.5195596573, 0.2392049856],
        "550/660/850": [[0.8474610999, 0.5196055607, 0.2279922965], [0.8699940018, 0.5212235151, 0.2364397706],
                        [0.8740311726, 0.5172611881, 0.2402870156]]

    },
    "newrefvalues": {
        "660/850": [[0.87032549, 0.52135779, 0.23664799], [0, 0, 0],
                    [0.8653063177, 0.2798126291, 0.2337498097, 0.0193295348]],
        "446/800": [[0.7882333002, 0.2501235178, 0.1848459584, 0.020036883], [0, 0, 0],
                    [0.8645652801, 0.5037779363, 0.2359041624]],
        "850": [[0.8649280907, 0.2800907016, 0.2340131491, 0.0195446727], [0, 0, 0], [0, 0, 0]],
        # "808": [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
        "650": [[0.8773469949, 0.2663571183, 0.199919444, 0.0192325637], [0, 0, 0], [0, 0, 0]],
        "550": [[0, 0, 0], [0.8686559344, 0.2655697585, 0.1960837144, 0.0195629009], [0, 0, 0]],
        "450": [[0, 0, 0], [0, 0, 0], [0.7882333002, 0.2501235178, 0.1848459584, 0.020036883]],
        "Mono405": [0.6959473282, 0.2437485737, 0.1799017476, 0.0205591758],
        "Mono450": [0.7882333002, 0.2501235178, 0.1848459584, 0.020036883],
        "Mono490": [0.8348841674, 0.2580074987, 0.1890252099, 0.01975703],
        "Mono518": [0.8572181897, 0.2628629357, 0.192259471, 0.0196629792],
        "Mono550": [0.8686559344, 0.2655697585, 0.1960837144, 0.0195629009],
        "Mono590": [0.874586922, 0.2676592931, 0.1993779934, 0.0193745668],
        "Mono615": [0.8748454449, 0.2673426216, 0.1996415667, 0.0192891156],
        "Mono632": [0.8758224323, 0.2670055225, 0.2023045295, 0.0192596465],
        "Mono650": [0.8773469949, 0.2663571183, 0.199919444, 0.0192325637],
        "Mono685": [0.8775925081, 0.2648548355, 0.1945563456, 0.0192860556],
        "Mono725": [0.8756774317, 0.266883373, 0.21603525, 0.194527158],
        "Mono780": [0.8722125382, 0.2721842015, 0.2238493387, 0.0196295938],
        "Mono808": [0.8699458632, 0.2780141682, 0.2283300902, 0.0216592377],
        "Mono850": [0.8649280907, 0.2800907016, 0.2340131491, 0.0195446727],
        "Mono880": [0.8577996233, 0.2673899041, 0.2371926238, 0.0202034892],
        "550/660/850": [[0.8689592421, 0.2656248359, 0.1961875592, 0.0195576511],
                        [0.8775934407, 0.2661207692, 0.1987265874, 0.0192249327],
                        [0.8653063177, 0.2798126291, 0.2337498097, 0.0193295348]],
        "490/615/808": [[0.8414604806, 0.2594283565, 0.1897271608, 0.0197180224],
                        [0.8751529643, 0.2673261446, 0.2007025375, 0.0192817427],
                        [0.868782908, 0.27845399, 0.2298671821, 0.0211305297]],
        "475/550/850": [[0.8348841674, 0.2580074987, 0.1890252099, 0.01975703],
                        [0.8689592421, 0.2656248359, 0.1961875592, 0.0195576511],
                        [0.8653063177, 0.2798126291, 0.2337498097, 0.0193295348]]
        # "Mono450": [10.137101, 24.131129, 2.500000],
        # "Mono550": [13.050459, 25.918403, 2.444385],
        # "Mono650": [42.873777, 25.681838, 2.400000],
        # "Mono725": [57.362319, 26.209292, 2.444148],
        # "Mono808": [80.761967, 27.552786, 2.522048],
        # "Mono850": [85.470884, 27.989664, 2.476279],
        # "Mono405": [10.419592, 23.297778, 2.579408],
        # "Mono518": [10.192879, 25.668374, 2.500000],
        # "Mono632": [40.314177, 25.624361, 2.400000],
        # "Mono615": [36.590561, 25.575475, 2.400000],
        #
        # "Mono590": [28.088219, 25.614054, 2.400000],
        # "Mono780": [72.470173, 27.114517, 2.500000],
        # "Mono880": [86.40861, 28.33615, 2.387391],
        # # "550/660/850": [[0.12730952, .2591748, 0.02444606], [0.42100882, 0.2567382, 0.0240000],
        # #                 [0.85491034, 0.27943831, 0.0247464]],
        # "550/660/850": [[12.730952, 25.91748, 2.444606], [42.100882, 25.67382, 2.40000],
        #                 [85.491034, 27.943831, 2.47464]],
        # "475/550/850": [[9.893005, 24.868873, 2.5], [14.1338, 25.919591, 2.440347],
        #                 [85.217001, 27.952459, 2.516666]]

    }}
pixel_min_max = {"redmax": 0.0, "redmin": 65535.0,
                 "greenmax": 0.0, "greenmin": 65535.0,
                 "bluemax": 0.0, "bluemin": 65535.0}
multiplication_values = {"Red": [0.00],
                         "Green": [0.00],
                         "Blue": [0.00],
                         "Mono": [0.00]}
monominmax = {"min": 65535.0, "max": 0.0}
