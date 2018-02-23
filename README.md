# Sodo - **Crowdfunding Sanitary Platform- Kenya**

![](https://sodo.mybluemix.net/static/images/sodo.png "Sodo Logo")

Sodo is a crowdfunding platform for the purpose of collection , management and distribution of Sanitary to women in Kenya.

Sodo is a swahili word that means "sanitary pads". sodo is also the name of the sanitary towel Crowdfunding platform created for women by women. sodo uses the power of project management and crowdsourcing to collect and distribute sanitary pads to the women.


# What key role does sodo play?

1.Creation of projects inorder to facilitate a certain area of study.sodo is a platform where an individual, an organization or a group of organizations can create a project focusing on Sanitary pads.

2.Creation of teams/collaborators.These can be an organization, a group of individuals or even both.A project will have these collaborators who will work on the project to ensure it is a success.

3.An location analytics section containing heat maps as well as graphs to determine the most critical areas that require sanitary towels and those that have already recieved.This will ensure equal distribution of resources especially to the areas where the availability of social amenities is low and level of poverty is high

4.Sex education to the Girl child as they receive the sanitary towels will be an additional feature as well as follow up on those that have received this sanitary facilities.This will reduce the chances of HIV/AIDS and STDS contraction at an early stage.

5.Sodo will also play a key role in aiding with disposing of used sanitary towels.

# Objectives of SODO

1.Keep the girl child in school. Ensure that no girl misses school due to lack of sanitary towels.

2.Ensure early sex education to reduce transmission of HIV/AIDS and STDs.

3.Ensure a clean and hygienic environment through correct disposal of sanitary towels.

4.Ensure transparency in the crowdfunding of sanitary resources.

# How to get Sodo up and running on your machine

1.Clone repository first

```git clone https://github.com/Grace-Amondi/SODO.git```

move to root of folder

```cd SODO```

2.Create virtual environment

```mkvirtualenv sodo```

3.Install requiremnets

```pip install -r requirements.txt```

4.Populate your database with fixtures

```python manage.py syncdb```

5.Migrate your apps

```python manage.py migrate```

6.Finally run your SDOD on localhost:8000

```python manage.py runserver```

[View Demo Here](https://sodo.mybluemix.net/)

