import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
plt.style.use('ggplot')
pd.options.display.max_columns = 200

# bring in data
dataFrame = pd.read_csv('Datasets/coaster_db.csv')

# data understanding
#print(dataFrame.shape)
#print(dataFrame.head(20))
#print(dataFrame.columns)
#print(dataFrame.dtypes)
dataFrame = dataFrame[['coaster_name',
       # 'Length', 'Speed', 
       'Location', 
       'Status', 
       #'Opening date',
       #'Type', 
       #'Manufacturer', 'Height restriction', 'Model', 'Height',
       #'Inversions', 'Lift/launch system', 'Cost', 'Trains', 'Park section',
       #'Duration', 'Capacity', 'G-force', 'Designer', 'Max vertical angle',
       #'Drop', 'Soft opening date', 'Fast Lane available', 'Replaced',
       #'Track layout', 'Fastrack available', 'Soft opening date.1',
       #'Closing date',
         'Opened',
       #'Replaced by', 'Website',
       #'Flash Pass Available', 'Must transfer from wheelchair', 'Theme',
       #'Single rider line available', 'Restraint Style',
       #'Flash Pass available', 'Acceleration', 'Restraints', 'Name',
       'year_introduced', 
       'latitude', 
       'longitude', 
       'Type_Main',
       'opening_date_clean', 
       #'speed1', 'speed2', 'speed1_value', 'speed1_unit',
       'speed_mph', 
       #'height_value', 'height_unit', 
       'height_ft',
       'Inversions_clean', 'Gforce_clean']].copy()

# Change type of column
dataFrame['opening_date_clean'] = pd.to_datetime(dataFrame['opening_date_clean'])
#print(dataFrame['opening_date_clean'])


dataFrame = dataFrame.rename(columns={'coaster_name':'Coaster_Name',
                          'year_introduced':'Year_Introduced',
                          'latitude':'Latitude',
                          'longitude':'Longitude',
                          'opening_date_clean':'Opening_Date',
                          'speed_mph':'Speed_mph',
                          'height_ft':'Height_ft',
                          'Inversions_clean': 'Inversions',
                          'Gforce_clean':'Gforce'})
#print(dataFrame.shape)
#print(dataFrame.dtypes)
#print(dataFrame.columns)

# see missing values per column
#print(dataFrame.isna().sum())

# find duplicate Coaster_Name
#print(dataFrame.loc[dataFrame.duplicated(subset=['Coaster_Name'])])
# checking a duplicate
#print(dataFrame.query('Coaster_Name == "Crystal Beach Cyclone"'))
dataFrame = dataFrame.loc[~dataFrame.duplicated(subset=['Coaster_Name','Location','Opening_Date'])].reset_index(drop=True).copy()
#print(dataFrame.query('Coaster_Name == "Crystal Beach Cyclone"'))
#print(dataFrame.head)
#print(dataFrame.shape)

# Looking at the data
#print(dataFrame['Year_Introduced'].value_counts())

#ax = dataFrame['Year_Introduced'].value_counts() \
#  .head(10) \
#  .plot(kind='bar', title='Top 10 Years Coasters Introduced')
#ax.set_xlabel('Year Introduced')
#ax.set_ylabel('Count')
#plt.savefig('Year_Introduced')
#plt.show()


#ax2 = dataFrame['Speed_mph'].plot(kind='hist', bins=20, title='Coaster Speed (mph)')
#ax2.set_xlabel('Speed(mph)')
#plt.savefig('Speed_Distrabution')
#plt.show()

#ax3 = dataFrame['Speed_mph'].plot(kind='kde', title='Coaster Speed (mph)')
#ax3.set_xlabel('Speed(mph)')
#plt.savefig('Speed_Distrabution_kde')
#plt.show()

#ax4 = dataFrame.plot(kind='scatter', x='Speed_mph', y='Height_ft', title='Coaster Speed vs. Height')
#ax4.set_xlabel('Speed(mph)')
#ax4.set_ylabel('Height(ft)')
#plt.savefig('Speed_vs_Height')
#plt.show()

#sns.scatterplot(x='Speed_mph', y='Height_ft', hue='Year_Introduced', data=dataFrame)
#plt.savefig('Speed vs Height with Year Introduced')
#plt.show()

#sns.pairplot(dataFrame, hue='Type_Main',vars=['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce'])
#plt.savefig('5 variable')
#plt.show()

# find correlations
#df_corr = dataFrame[['Year_Introduced', 'Speed_mph', 'Height_ft', 'Inversions', 'Gforce']].dropna().corr()
#print(df_corr)
#sns.heatmap(df_corr, annot=True)
#plt.savefig('HeatMap')
#plt.show()

# what are the locations with the fastest roller coasters (minimum of 10)?
ax = dataFrame.query('Location != "Other"') \
            .groupby('Location')['Speed_mph'] \
            .agg(['mean', 'count']) \
            .query('count >= 10') \
            .sort_values('mean')['mean'] \
            .plot(kind='barh', figsize=(12,5), title='Average Coaster Speed by Location')
ax.set_xlabel('Average Coaster Speed')
plt.savefig('Fastest Locations')
plt.show()




# dropping column
# dataFrame.drop(['Opening date'], axis=1)