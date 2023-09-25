import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import pandas as pd
import datetime


image_collection = io.imread_collection('E:/TSA/Arasbaran_NDVI/*tif')
print('Image Collection Shape : ', np.shape(image_collection))
print('Image Collection Size : ', np.size(image_collection))



#plt.figure(figsize=(15,10))
#plt.imshow(image_collection[1], cmap='gray')
#plt.title('Time 1')
#plt.axis('off')
#plt.show()


all_images = io.concatenate_images(image_collection)
data = all_images.reshape(all_images.shape[0], -1)
print('Reshape Image Collection Shape : ', np.shape(data) )


rescale = data / 10000
print('Rescale Images : ', np.shape(rescale))


arr = np.array(image_collection)
nums = np.count_nonzero(rescale >=0.5, axis=1)
print('Minimum Value : ',np.min(nums) )
print('Maximum Value : ',np.max(nums) )

dates = [i.split('doy')[1].split('_')[0] for i in image_collection.files]
print('Start Date : ', dates[0])
print('End Date : ', dates[-1])


df = pd.DataFrame()
df['Values(Km^2)'] = nums * 0.5 * 0.5
df['date'] = dates

def convert(date):
    new_date = datetime.datetime.strptime(str(date), '%Y%j')
    return new_date

df['date'] = df['date'].apply(convert)

print(df.head(5))

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Comic Sans MS'


df.plot(x='date', y='Values(Km^2)')
plt.title('NDVI Time Series 2010-2020')
plt.show()

df.to_csv('I:/Arasbaran_NDVI/NDVI_Stat.csv')
















