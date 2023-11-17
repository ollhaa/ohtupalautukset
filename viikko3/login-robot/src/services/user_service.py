from entities.user import User
import sys, pdb
import regex as re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        #pdb.Pdb(stdout=sys.__stdout__).set_trace()

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        numbers ="0123456789"
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) <3:
            raise UserInputError("Username is too short")
        if any(i in numbers for i in username):
            raise UserInputError("Username is not valid")
        if len(password) < 8:
            raise UserInputError("Password is too short")
        if not any(i in numbers for i in password):
            raise UserInputError("Password is not valid")
