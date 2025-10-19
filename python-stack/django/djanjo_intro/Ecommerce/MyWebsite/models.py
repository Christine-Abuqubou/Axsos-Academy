from django.db import models
from django.db.models import Count
import bcrypt
import re
import datetime 


class UserManager(models.Manager):
    def basic_validator_login(self, postData):
        errors = {}
        user = User.objects.filter(email = postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Wrong email address!"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"    
        if len(postData['email']) == 0 :   
            errors["emailrequired"] = "Email is required!"  
        if len(postData['password']) == 0 :   
            errors["passwordrequired"] = "Password is required!"    
          
        if not len(user):
            errors['emailnewuser'] = "Email is not registered" 
        return errors

    def basic_validator_reg(self, postData):
        errors = {}
        new_user = User.objects.filter(email = postData['email'])
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"  
        if len(postData['confirmpassword']) < 8:
            errors["confirmpassword"] = "Confirm Password should be at least 8 characters" 
        if len(postData['lastname']) < 3:
            errors["lastname"] = "Last name should be at least 3 characters" 
        if len(postData['firstname']) < 3:
            errors["firstname"] = "First Name should be at least 3 characters" 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Wrong email address!"
        if postData['password'] != postData['confirmpassword']:
            errors['password_confirm'] = "Password Dosent Match!"
        if len(postData['email']) == 0 :   
            errors["emailrequired"] = "Email is required!"  
        if len(postData['password']) == 0 :   
            errors["passwordrequired"] = "Password is required!"
        if len(postData['confirmpassword']) == 0 :   
            errors["confirmpasswordrequired"] = "Confrim password is required!"
        if len(postData['lastname']) == 0 :   
            errors["lastnamerequired"] = "Last name is required!"
        if len(postData['firstname']) == 0 :   
            errors["firstnamerequired"] = "First name is required!"   
        if len(new_user):
            errors['emailnewuser'] = "Email already exist" 
        return errors
    
class User(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=10)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # liked_games = models.ManyToManyField(Game, related_name="liked_by_users")
    
    objects = UserManager() 

class Address(models.Model):
    country = models.CharField(max_length=25)
    state = models.CharField(max_length=40)
    city = models.CharField(max_length=25)
    street= models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="address" , on_delete= models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GameManager(models.Manager):
    def basic_validator_save_Game(self, postData):
        errors = {}
        if len(postData.get('game_name', '').strip()) == 0:
            errors["game_name"] = "Game name is required!"
        if len(postData.get('release_date', '').strip()) == 0:
            errors["release_date"] = "Game release date is required!"
        if len(postData.get('genre', '').strip()) == 0:
            errors["genre"] = "Game genre is required!"
        if len(postData.get('price', '').strip()) == 0:
            errors["price"] = "Game price is required!"

          
        return errors
    

class Game(models.Model):
    game_name=models.CharField(max_length=50)
    
    genre=models.CharField(max_length=30)
    release_date=models.DateField()
    created_by=models.ForeignKey(User, related_name="games_created", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=GameManager()
    users_who_liked = models.ManyToManyField(User, related_name="liked_games")
    
    
    
    

    

def login_user(post):
    user_exist = User.objects.filter(email=post.POST['email'])
    if user_exist:
        logged_user = user_exist[0] 
        if bcrypt.checkpw(post.POST['password'].encode(), logged_user.password.encode()):
            post.session['user_id'] = logged_user.id
            return True
        else:
            print("Failed password")    
            return False            
    else:
        return False     
    
def get_users():
    return User.objects.all()

def get_user(id):
    return User.objects.get(id = id)

def create_user(post):
    user_password = post['password']
    hash1 = bcrypt.hashpw(user_password.encode(), bcrypt.gensalt()).decode()
    return User.objects.create( firstname = post['firstname'], lastname= post['lastname'] , phonenumber = post['phonenumber'], email =  post['email'], date_of_birth = post['date_of_birth'], password = hash1)

def create_game(post):
    id = post.session['user_id'] 
    user = User.objects.get( id = id )
    Game.objects.create( game_name = post.POST['game_name'] , genre = post.POST['genre'], release_date= post.POST['release_date'], created_by = user   )

def get_games():
    return Game.objects.all()

def get_game(id):
    return Game.objects.get(id = id)

def update_game(post):
    
    game_id = post.get('gameid')
    if not game_id:
        print(" Missing gameid in POST data")
        
      
    returngame = Game.objects.get(id=game_id)

    returngame.game_name = post['game_name']
    returngame.genre = post['genre']
    returngame.release_date = post['release_date']
    returngame.save()
    
def delete_game(game_id):
    game = Game.objects.get( id = game_id)
    game.delete()
    
def favorite_game(user_id, game_id):    
    user = User.objects.get(id=user_id)
    game = Game.objects.get(id=game_id)
    user.liked_games.add(game)
    return game

def liked_games(user_id):
    user = User.objects.get(id=user_id)
    return user.liked_games.all()
