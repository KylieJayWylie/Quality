from itertools import pairwise
from ssl import ALERT_DESCRIPTION_RECORD_OVERFLOW
import pandas as pd
import pingouin as pg  

# sample data (replace with your working data)
data = pd.DataFrame({
    'value':[10, 12, 15, 14, 13, 16, 18, 20, 19, 22],
    'group':['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']
    })

#perform one-way ANOVA
aov = pg.anova(data=data, dv='value', between='group')
print(aov)

#optional: perform post-hoc tests if ANOVA is significant

posthoc = pg.pairwise_tukey(data=data, dv='value', between='group')
print(posthoc);