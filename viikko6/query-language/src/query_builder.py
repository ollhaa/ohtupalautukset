from matchers import All, HasAtLeast, HasFewerThan, Or, PlaysIn, Not, And

class QueryBuilder:
    def __init__(self, pino =None):
        self.pino_olio = pino
        if pino is None: self.pino_olio = All()

    def playsIn(self, team):
        #self.pino_olio = QueryBuilder(PlaysIn(team))
        return QueryBuilder(And(self.pino_olio, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        #self.pino_olio = QueryBuilder(hasAtLeast(value, attr))
        return QueryBuilder(And(self.pino_olio, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        #self.pino_olio = QueryBuilder(HasFewerThan(value, attr))
        return QueryBuilder(And(self.pino_olio, HasFewerThan(value, attr)))

    def oneOf(self, *pino):
        return QueryBuilder(Or(*pino))

    def build(self):
        return self.pino_olio