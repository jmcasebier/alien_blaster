#!/usr/bin/env python3

import pickle, os.path

main_dir = os.path.split(os.path.abspath(__file__))[0]

save_file = os.path.join(main_dir, 'data', 'data.p')

data = {0}

pickle.dump(data, open(save_file, 'wb'))
