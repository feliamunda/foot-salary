from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Calculator

class PlayersNotDefined(Exception):
        """Raised when Players Not Defined"""
        pass

# Create your views here.
class CalculatorView(APIView):
    
    def get(self,request):
        try:
            level_table = {'A': 5, 'B':10, 'C':15, 'Cuauh': 20}
            data = request.data
            players = data['jugadores']
            team_goals = 0
            team_objective = 0
            for player in players:
                team_goals += player['goles']
                team_objective += level_table[player['nivel']]
            
            team_bonus_percentage = Calculator.getPercentage(team_goals, team_objective)
            
            for player in players:
                player_bonus_top = player['bono']
                player_goals = player['goles']
                player_objective = level_table[player['nivel']]
                player_bonus_percentage = Calculator.getPercentage(player_goals,player_objective)
                bonus_percentage = (player_bonus_percentage + team_bonus_percentage) / 2
                bonus = round(player_bonus_top * bonus_percentage, 2)
                player['sueldo_completo'] = player['sueldo'] + bonus

            data['jugadores'] = players
            return Response(data, content_type="application/json")
        except :
            return Response(status=500)