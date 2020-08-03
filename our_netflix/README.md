# Our Netflix History

The other day, I found out that Netflix stores a history of all movies and series episodes watched on the platform. I share the account with my boyfriend since we started dating, and watching movies and binge-watch series are two of the things we always do. Then I thought: well, this is a good opportunity for data analysis (of our netflix history).

I checked the history for the two profiles: mine and his. However, I saw that it was not detailed enough. I tried to use the TMDB API, but it didn't work very well, I was only able to get details for a small set of records.

So I found an extension for google chrome, called [Netflix Viewing Stats](https://medium.com/@h_martos/netflix-viewing-stats-unleash-your-data-fa2adb33827c). It provides a more detailed history, containing the record's category (movie or series), duration, and when it was watched (the latter also exists in the standard Netflix history). The only thing I wanted but was missing was the movie/series genre. But I'll get to that part.

I downloaded the history for both profiles using the extension. The file is saved in CSV format. I had to do a 'manual curation' process to include a column indicating what we saw together. I also deleted the records dated before the day we started dating. Here I take the opportunity to say that the results are approximate since my memory is not the best, and the two files totaled more than 1800 records.

Getting back to the genres: I made a simple python code to concatenate these two files and, from the result, search for the genres. For this search, I used the Beautiful Soup module to scrape the Netflix website for each of the records.  I'm not sure if that was the best approach, but I couldn't find any other way to get that data. Using a loop, I iterated through each record to make this collection and add the result as a new column. It took a while, but I wasn't too concerned with the execution time. Parallelism remains as a suggestion for the future. It is important to mention that I also couldn't get the genre for some of the records, since some movies/series are no longer available on the platform. Finding another way to get this data is also future work.

Finally, with the final dataset, I built a dashboard using Tableau, and you can see it [here](https://public.tableau.com/profile/maria.luiza.mondelli?fbclid=IwAR2pYBPa93QjkQ0W7m1wWyZZ6gncPSV8V1jM2TIolTNqJb3UyyjARgWQLJ0#!/vizhome/us_15963351321780/DonaMariaeSeuZ)]. There I show the main statistics, the top 5 genres, and it is also possible to filter by year.

