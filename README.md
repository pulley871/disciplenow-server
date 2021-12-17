#DiscipleNow

DiscipleNow is a platform where churches can launch and grow their disciplship training.
Church Discipleship is difficult because most of the time we have no way of holding one another accountable.
DiscipleNow is a team based platform where a team leader has the ability to see daily logs from their team members, leaders get informed if a team member has not logged in a certain amount of days, can message their team members to encourage them to continue on.

The structure is designed to where after a certain amount of time the team members can be promoted to a team leader and have their own team to watch out for, all while maintaining their spot in their original group.

##Local Setup

1. Clone this repository and change to the directory in the terminal.
2. Run `pipenv shell`
3. Run `pipenv install`
4. Run migrations and make migrations
5. Seed database with python3 manage.py loaddata {table name}

###LoadData Order
1.users
2.tokens
3.disciples
4.grouptypes
5.groups
6.disciplestogroup
7.messages
8.meetings
9.disciplestomeetings
10.entries
Now that your database is set up all you have to do is run the command:

```
python3 manage.py runserver
```
