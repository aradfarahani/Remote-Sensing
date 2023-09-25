import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import pandas as pd
import datetime

image_collection = io.imread_collection('I:/Kermanshah_LST/*.tif')
#print('Image Collection Shape : ', np.shape(image_collection))

all_image = io.concatenate_images(image_collection)

all_image = all_image / 50

nums = [np.mean(i[i!=0])for i in all_image]
nums = np.array(nums) - 273.15


dates = [i.split('doy')[1].split('_')[0] for i in image_collection.files]


df = pd.DataFrame()

df['Value'] = nums
df['date']= dates

def datee(date):
    new_date = datetime.datetime.strptime(str(date), '%Y%j')
    return new_date

df['date'] = df['date'].apply(datee)


plt.rcParams['font.family']= 'sans-serif'
plt.rcParams['font.sans-serif']= 'Comic Sans MS'



df.plot(x='date', y='Value')
plt.title('Land Surface Tempreture Time Series')
plt.show()

