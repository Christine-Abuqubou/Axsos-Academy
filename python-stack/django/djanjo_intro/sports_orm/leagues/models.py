from django.db import models
from django.db.models import Q, Count


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

# seconed part 

def atlantic_soccer():
    return Team.objects.filter(league__name="Atlantic Soccer Conference")

def boston_penguins():
    return Player.objects.filter(curr_team__team_name="Boston Penguins")

def icb_players():
    return Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference")

def acf_players():
    return Player.objects.filter(curr_team__league__name="American Conference of Amateur Football", last_name="Lopez")

def football_players():
    return Player.objects.filter(curr_team__league__sport__icontains="football")

def team_with_sophia():
    
    sophia_players = Player.objects.filter(first_name="Sophia")
    return Team.objects.filter(curr_players__in=sophia_players).distinct()

def league_with_sophia():
    sophia_players = Player.objects.filter(first_name="Sophia")
    return League.objects.filter(teams__curr_players__in=sophia_players).distinct()

def flores_not_roughriders():
    return Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Washington Roughriders")

def sam_teams():
    samuel_evans_players =Player.objects.filter(first_name="Samuel", last_name="Evans")
    return Team.objects.filter(
        Q(curr_players__in=samuel_evans_players) |
        Q(all_players__in=samuel_evans_players)
    ).distinct()

# def manitoba():
    # manitoba_team =Team.objects.get(team_name="Manitoba Tiger-Cats")
    # return Player.objects.filter(
    #     Q(curr_team=manitoba_team) | Q(all_teams=manitoba_team)
    # ).distinct()
# def formly():
#     wichita_team = Team.objects.get(team_name="Wichita Vikings")

#     return Player.objects.filter(
#         all_teams=wichita_team
#     ).exclude(curr_team='wichita_team').distinct()

# def jacob_teams():
#     jacob_gray = Player.objects.get(first_name="Jacob", last_name="Gray")
#     return jacob_gray.all_teams.exclude(team_name="Oregon Colts").distinct()

   
# def jash_atlantic():
#     return Player.objects.filter(
#         first_name="Joshua",
#         all_teams__league__name="Atlantic Federation of Amateur Baseball Players"
#     ).distinct()
    

# def teams_with_12plus():
#     return Team.objects.annotate(
#         num_players=players_count()
#     ).filter(num_players__gte=12)

# def players_count():
#     return Player.objects.annotate(
#         num_players=players_count()
#     ).order_by('-num_teams')