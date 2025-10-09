from django.db import models

class League(models.Model):
	name = models.CharField(max_length=50)
	sport = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
	location = models.CharField(max_length=50)
	team_name = models.CharField(max_length=50)
	league = models.ForeignKey(League, related_name="teams", on_delete = models.CASCADE)

class Player(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	curr_team = models.ForeignKey(Team, related_name="curr_players", on_delete = models.CASCADE)
	all_teams = models.ManyToManyField(Team, related_name="all_players")

def get_baseball_leagues():
    return League.objects.filter(sport__contains="Baseball")

def get_women_leagues():
    return League.objects.filter(name__icontains="Women")

def get_hockey_sport():
    return League.objects.filter(sport__icontains="hockey")

def get_not_in_football():
	return League.objects.exclude(sport__icontains="football")

def call_conferences():
    return  League.objects.filter(name__icontains="Conference")
def Atlantic():
    return League.objects.filter(name__icontains="Atlantic")

def Dallas_team():
    return Team.objects.filter(location__icontains="Dallas")

def raptors_team():
    return Team.objects.filter(team_name__icontains="Raptors")

def city_team():
    return Team.objects.filter(location__icontains="City")

def t_teams():
    return  Team.objects.filter(team_name__startswith="T")

def team_by_location():
    return Team.objects.order_by("location")

def teams_by_name():
    return Team.objects.order_by("-team_name")

def cooper_players():
    return Player.objects.filter(last_name__icontains="Cooper")

def Joshua_players():
    return  Player.objects.filter(first_name__icontains="Joshua")

def JoshuaCoper_exclude_players():
    return  Player.objects.filter(last_name__icontains="Cooper").exclude(first_name__icontains="Joshua")

def alexsender_players():
    return  Player.objects.filter(first_name__in=["Alexander", "Wyatt"])


