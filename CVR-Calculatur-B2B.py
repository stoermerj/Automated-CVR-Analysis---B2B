#Analysis of Unique Page Views since launch of top 10 sites
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("pvBeforeCorona.xlsx", sheet_name="Dataset1")

# filter out sites that i do not wish to see
dfFilterPages=df[df["Page"].str.contains("sites|xml|redacted")==False]

#filter out sites not often visited
dfFilterViews= dfFilterPages[dfFilterPages["Unique Page Views"] > 5]

#filter out uniques
dfUniquePageViews = dfFilterViews.loc[:,("Page", "Unique Page Views")]

#filter out online antrag
onlyMaklerPages = dfUniquePageViews[dfUniquePageViews["Page"].str.contains("vpv") == False]

#filter out subdomain
onlyMaklerPages["Page"] = onlyMaklerPages["Page"].str.replace("makler.hiscox.de", "")
print(onlyMaklerPages)

#reset index 
onlyMaklerIndex = onlyMaklerPages.reset_index(drop=True)

#show only top 10 pages
top10MaklerPages = onlyMaklerIndex.head(10)

#create plot
sns.barplot(x="Page", y="Unique Page Views", data=top10MaklerPages, palette="Blues_d")
sns.axes_style("whitegrid")
plt.xlabel('Page')
plt.ylabel('Unique Page Views')
plt.xticks(rotation=90, fontsize=8)
plt.subplots_adjust(bottom=0.5)
plt.show()
