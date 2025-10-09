from django.shortcuts import render, redirect
from .models import *

from . import team_maker

def index(request):
	context = {
		"baseball_leagues": get_baseball_leagues(),
		"women_leagues": get_women_leagues(),
		"hockey_sport": get_hockey_sport(),
        "not_in_football":get_not_in_football(),
        "conferences_leagues":call_conferences(),
        "atlantic_region_leagues": Atlantic(),
        
        "dallas_teams":Dallas_team() ,
        "raptors_teams":raptors_team() ,
        "city_teams":city_team() ,
        "t_teams":t_teams(),
        "teams_by_location":team_by_location() ,
        "teams_by_name_desc":teams_by_name() ,
        
        "cooper_players": cooper_players(),
        "joshua_players":Joshua_players(),
        "cooper_not_joshua": JoshuaCoper_exclude_players(),
        "alexander_or_wyatt":alexsender_players(), 

  
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")