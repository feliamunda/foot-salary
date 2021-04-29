
# Create your models here.

class Calculator():
    
    @staticmethod
    def getPercentage(goal, objective):
        """Get the percentage of goals in relation to a objective

        Args:
            goal (Integer): Number of goals accomplished
            objective (Integer): Number of goals objective

        Returns:
            Float: Percentage in minimum decimals expression
        """
        percentage= 0
        if goal >= objective:
            percentage = 1
        else:
            percentage = goal /objective
        return percentage