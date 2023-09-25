import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import pandas as pd
import datetime
###################

image_collection = io.imread_collection('E:/TSA/Ardabil_Snow/*.tif')


#print(np.shape(image_collection))
#print(np.size(image_collection))

all_images = io.concatenate_images(image_collection)

data = all_images.reshape(all_images.shape[0], -1)
#print(np.shape(data))

arr = np.array(image_collection)
stack = np.stack([arr[500], arr[900], arr[1400]], axis=2)
#plt.figure()
#plt.imshow(stack)
#plt.title('MODIS RGB Time Series Images')
#plt.axis('off')
#plt.show()

nums = np.count_nonzero(data == 200, axis=1)
#print('Count NoN-ZerO : ', nums)


dates = [i.split('doy')[1].split('_')[0] for i in image_collection.files]
#print(dates)


df = pd.DataFrame()

df['values(Km^2)'] = nums * 0.5 * 0.5
df['date'] = dates
#print(df)

del image_collection, all_images, data, nums, dates

def convert(date):
    new_date = datetime.datetime.strptime(str(date), '%Y%j')
    return new_date


#print(df.head(10))
df['date'] = df['date'].apply(convert)
#print(df.head(10))
df.plot(x='date', y='values(Km^2)')
plt.show()
df.to_csv('E:/TSA/Ardabil_Snow/TimeSeries_Snow.csv')













