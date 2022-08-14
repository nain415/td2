# SQL Analysis of Legion TD 2
<h2 align="center">

Google Colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dwlAkNijM3ojzQPaMGoPHAqh7hWhJwxL?usp=sharing)
 
</h2>

<p float="left">
  <img src="https://user-images.githubusercontent.com/78244259/184516851-f0a3512e-fcc7-4e7a-a5fa-3bfdde512585.gif" width="450" />
  <img src="https://user-images.githubusercontent.com/78244259/184517075-f4c40acf-e600-43ec-b8c6-ef45659d111f.png" width="450" /> 
</p>



##### Purpose
This is a demonstration of my competency in SQL.  I pull data from an API, format & clean the data, input the data into an SQLite database, and then visually analyse the data using several Python libraries, alongside Python's SQLite3 interface in Google Collaboratory.

Each section in the Google Collaboratory notebook showcases command over different SQL features.

##### Project Structure
- The Google Collaboratory notebook contains the SQL analysis of the database.  The link is at the top of this README file.
- The file db_fns.py is a collection of functions for writing to the database, named 'td2.db'.  
- The file td2.py is the main program, which handles collecting data from this project's API, cleaning that data, and writing to the database through db_fns.py.

##### Choosing an RDBMS
I've chosen SQLite3 because it's light weight, and my data doesn't need future updates for this one-off analysis.  A 2015 presentation on SQLite by Dr. Richard Hipp is inspirational for this choice.  Otherwise, I'd have probably set up a PostgreSQL server on my spare computer, and ran a cron job for pulling data each day.  I'll reserve that for another time, because my objective here is primarily to display my competency in SQL.

##### Designing the schema
Designing my first database has been an illuminating task, because I need to consider making it both simple and efficient.  Simplicity is a concern because analyses on needlessly complicated databases will prove cumbersome.  Efficiency is a concern because some of the tables in here contain hundreds of thousands of records.

<p align="center">
<img src=https://user-images.githubusercontent.com/78244259/183784327-d59589e8-f450-4ed3-b1f2-a70e787a96dc.png>
</p>

After much contemplation and some research, I've arrived at this schema involving two one-to-many relationships.  Designing it in this manner greatly eases the burden of developing SQL queries because the Join clauses are quite simple; those queries are also blazing fast: queries involving hundreds of thousands of records take *milliseconds*, such as queries ran on on the Player table.

##### Choosing Interesting Questions

Choosing interesting questions that naturally involve disparate SQL techniques is another challenge for my presentation.  The questions that arise from the data are both influenced by my experience playing the game Legion TD 2 and SQLzoo's website, which is a website that contains various SQL tutorials.  I credit the tutorial-writers at SQLzoo for having given me some direction for the techniques I can portray in my queries.

##### Dealing with Legacy Data from the API and 504 Errors!

Issues that I face come from both data with missing fields, and error data resulting from an overloaded API server.  To meet these challenges, defensive code, try-catch structures, and some detailed comments are present in td2.py's code.

##### References:

[1] API Data-Source Documentation: https://swagger.legiontd2.com/

[2] Query inspiration: www.sqlzoo.net

[3] SQLite: The Database at the Edge of the Network with Dr. Richard Hipp: https://www.youtube.com/watch?v=Jib2AmRb_rk
