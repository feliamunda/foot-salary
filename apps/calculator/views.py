from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.player.serializers import PlayerSerializer

from .models import Calculator

# Create your views here.
class CalculatorView(APIView):
    """This is the main view for Calculator
    """

    def get(self,request):
        """ This method process requests by the HTTP method GET
            It receives a request with a JSON Object and process it to fill 'sueldo_completo' field

        Args:
            request (Request): This is the request object sendend from client and must contain a JSON object with "jugadores" key an this
            should cointain a list of players with the next required fields:\n
            'nombre'    : String\n
            'nivel'     : String\n
            'goles'     : Integer\n
            'sueldo'    : Float\n
            'bono'      : Float\n
            'equipo'    : String\n

        Returns:
            Response: returns the same object with the field 'sueldo_completo' filled
        """
        try:
            data = request.data
            if 'jugadores' not in data:
                return Response({"error":"'jugadores' is not defined"}, status=status.HTTP_400_BAD_REQUEST)

            level_table = {'A': 5, 'B':10, 'C':15, 'Cuauh': 20}
            
            players = data['jugadores']
            team_goals = 0
            team_objective = 0

            serializer = PlayerSerializer(data=players, many =True)
            if (serializer.is_valid()):
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
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return Response(status=500)