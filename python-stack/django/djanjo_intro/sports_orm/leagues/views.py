from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q, Count

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
        
        
         
        "atlantic_soccer_conference_teams": atlantic_soccer(),
        "boston_penguins_players": boston_penguins(),
        "icbc_players":icb_players() ,
        "acaf_players_lopez":acf_players() ,
        "football_players":football_players() ,
        "teams_with_sophia":team_with_sophia() ,
        "leagues_with_sophia":league_with_sophia() ,

       
        "flores_not_roughriders":flores_not_roughriders() ,
        "samuel_evans_teams":sam_teams() ,
        # "manitoba_tiger_cats_players":manitoba() ,
        # "formerly_wichita_vikings":formly() ,
        # "jacob_gray_prev_teams":jacob_teams() ,
        # "joshua_atlantic_federation": jash_atlantic(),

        
        # "teams_with_12plus_players": teams_with_12plus(),
        # "players_team_count":players_count() ,

  
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")