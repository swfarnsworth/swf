import datetime as dt
import json
import pprint as pp
import re
from pathlib import Path

import numpy as np
import pandas as pd

ip = get_ipython()
# display numbers with underscore separators
for cls in [int, float]:
    ip.display_formatter.formatters['text/plain'].for_type(cls, lambda number, printer, cycle: printer.text(f'{number:_}'))
