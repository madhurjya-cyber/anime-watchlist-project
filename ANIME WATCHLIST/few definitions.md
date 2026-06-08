Project Name

<!-- Anime Watchlist Database -->

Tables:
1. Genre
2. Users
3. Anime
4. Watchlist

Features:
- Track anime
- Store ratings
- Track watch status
- Query anime statistics

<!-- cursor.execute -->
Real-Life Analogy
Imagine:
You = Python
Restaurant Kitchen = MySQL Database
Waiter = Cursor
You don't walk into the kitchen yourself.
You tell the waiter:
"Bring me all anime records."
The waiter goes to the kitchen, gets the data, and returns it.
That's exactly what:
cursor.execute(...)
does.

<!-- rows = cursor.fetchall() -->
After:
cursor.execute("SELECT * FROM Anime")
MySQL has run the query, but Python doesn't have the results yet.
You need:
rows = cursor.fetchall()
to bring all the results from MySQL into Python.
Think of it like this:
Step 1: Execute Query
cursor.execute("SELECT * FROM Anime")
Equivalent to telling MySQL:
SELECT * FROM Anime;
MySQL prepares the results.
Step 2: Fetch Results
rows = cursor.fetchall()
Now Python receives all rows.

<!-- Good. If you've completed: -->

✓ view_anime()
✓ add_anime()
✓ view_watchlist()
✓ update_status()
✓ update_rating()

then the next logical function is:

delete_entry()

This completes CRUD.

Create  → add_anime()
Read    → view_anime()
          view_watchlist()
Update  → update_status()
           update_rating()
Delete  → delete_entry()
