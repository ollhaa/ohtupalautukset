class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.points = [0,0]
    

    def won_point(self, player_name):
        if player_name == "player1":
            self.points[0] +=1
        else:
            self.points[1] +=1

    def get_score(self):
        
        def get_points_equal(points):
            point_table = {0:"Love-All", 1:"Fifteen-All", 2:"Thirty-All", 3: "Deuce"}
            if self.points[0] == 0:
                return point_table[0]
            elif self.points[0] == 1:
                return point_table[1]
            elif self.points[0] == 2:
                return point_table[2]
            else:
                return point_table[3]

        def get_points_equal_over4(points):
            point_table = {0:"Advantage player1", 1:"Advantage player2", 2:"Win for player1", 3:"Win for player2"}
            minus_result = points[0] - points[1]
            if minus_result == 1:
                return point_table[0]
            elif minus_result == -1:
                return point_table[1]
            elif minus_result >= 2:
                return point_table[2]
            else:
                return point_table[3]

        def get_points_less_4(points):
            point_table = {0:"Love", 1:"Fifteen", 2:"Thirty", 3: "Forty"}
            score = point_table[points[0]] + "-" + point_table[points[1]]
            return score

        if self.points[0] == self.points[1]: 
            score = get_points_equal(self.points)
        elif self.points[0] >=  4 or self.points[1] >= 4:
            score = get_points_equal_over4(self.points)
        else:
            score = get_points_less_4(self.points)
        return score



        