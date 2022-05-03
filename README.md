# **Rhythm Game Sheet Convert**

Hello! This is an interesting program that probably only has as use case with me BUT it's a fun project I wish to embark on. Basically, I have a problem I need to solve. I started storing all of my rhythm game scores from arcades and home-play in a spreadsheet years ago and making visuals in there. However, this has gotten to be very cumbersome to update as I get more and more scores as they go into the thousands of scores range. I need a more streamlined solution to not only hold all my scores but to also update them efficiently.

There is a website already that I have attempted to upload all of my scores to and  host the information for this called [Kamaitachi](https://kamaitachi.xyz/) but it lacks some statistics that I want to add myself and I also want full local control over all my scores and data. So this is where I make what I want myself! Kamaitachi does make it really easy to extract a .json file of all your scores though, so that should make it easier to do things I want with my scores and hopefully I can get some interesting things going on. I have some ideas...

I plan to support the following gamemodes as they are what I play and keep scores from: **Sound Voltex, Beatmania IIDX (SP and DP), and WACCA**. Additional games like DDR, Chunithum, and osu! are likely to be supported once I find a good way of obtaining my data from them, but that's a stretch goal for far in the future.

I am more beginner when it comes to coding and there's a <i>lot</i> I need to do, but I'm going to try to make a to-do list here to keep me on track and set some goals for myself! This will hopefully be a fun way to learn more about coding, databases, and visualizations that will help me be able to get skills for a data analyst job one day. At least I'm hoping. Anyway, here's what I need to do...

#### **TODO:**
- Loading the .json files properly, each gamemode has different ways (so possibly a class?)
- Once I figure this out, I might try making them SQL databases first, need to learn more SQL though and how to convert .json to SQL databases (also have no idea how github handles that)
- Take what I want from the data, and make pretty visuals! Use either MatPlotLib, plotly, Bokeh, or Altair... or learn R... probably learn R. In fact, I'll just add that here:
	* Learn R
- Make similar to visuals found in my spreadsheets already (matrices of lvl vs score, score vs source, etc.)
- Things that exist but I want to add myself:
	* Rating systems for all games (Volforce, Rate, DJ Points, etc.)
	* Histograms for all scores to compare across levels, scores, lamps, etc.
	* Other things from Kamaitachi, but implented in a way that works for me better visually
- Ideas:
	* In any game, what is my overall accuracy over all songs? Similar to overall accuracy in osu! (can sort by level played or by highest rating for weighted overall accuracy). This is calculated by the judgements in every song. Can use the overall score to estimate others that don't have this info
	* Improvement over time, but also highlight the most notable scores since last update to the database
	* For IIDX, show the rate graphs during play, but also show all of them as they switch dynamically on one graph
- Have all these visuals shown on one dashboard, possibly a locally hosted website? Can switch to different games with tabs. Maybe have a way to compare scores across all games, if thats a thing? Maybe accuracy across all games, or peak rating across all games and how they compare relatively to the top rating?
- Ability to update the database easily by just importing .json files
