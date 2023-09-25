import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from skimage import io
import pandas as pd
import datetime


image_collection = io.imread_collection('E:/TSA/Qazvin_ET/*.tif')
print('Image Collection Shape : ', np.shape(image_collection))




all_images = io.concatenate_images(image_collection)
all_images = all_images / 10

nums = [np.mean(i[i<=32761])for i in all_images]
nums = np.array(nums)

#stack = np.stack([image_collection[5], image_collection[10], image_collection[15]], axis=2)
#plt.figure()
#plt.imshow(image_collection[5], cmap='gray')
#plt.title(' Evapotranspiration Time Series')
#plt.axis('off')
#plt.show()


dates = [i.split('doy')[1].split('_')[0] for i in image_collection.files]
print('Start Date : ', dates[0])
print('End Date : ', dates[-1])




df = pd.DataFrame()
df['Kg/m2'] = nums
df['date'] = dates


def convert(date):
    new_date = datetime.datetime.strptime(str(date), '%Y%j')
    return new_date

df['date'] = df['date'].apply(convert)


#df.plot(x='date' , y='Kg/m2' )
#plt.title('Evapotranspiration Time Series')
#plt.show()

fig = plt.figure()
ax  = plt.axes(xlim=(np.datetime64(np.min(df['date'])),
np.datetime64(np.max(df['date']))), ylim=(min(df['Kg/m2']), 
max(df['Kg/m2'])))

line, = ax.plot([], [], lw=2)
xdata , ydata = [], []

def animate(i):
    x = np.datetime64(df['date'][i])
    y = df['Kg/m2'][i]
    
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

anim = ani.FuncAnimation(fig , animate, interval=10, blit=True)
plt.show()


