from utils.constants import *
from controllers.player_manager import PlayerManager
from tabulate import tabulate


class TournamentsViews:
    @staticmethod
    def view_list(headers, body):
        print(tabulate(body, headers=headers, tablefmt="double_grid"))

    def view_create(self, data):
        print(NEW_TOURNAMENT)

        for input_data in data:
            if 'slug' in input_data and input_data['slug'] == 'players':
                PlayerManager(MAIN_MENU).view_players()

            if not input_data['valid']:
                input_data['value'] = self.get_user_input(input_data['name'])

        return data

    @staticmethod
    def get_user_input(field_name):
        return input(f'{field_name}: ').strip()

    def input_info_tournament(self):
        return self.get_user_input('Nom du tournoi à afficher')

    @staticmethod
    def view_info_tournament(data_tournament):
        print(f'\n{data_tournament['name']}')
        print(f'Le tournoi se déroulera à {data_tournament['place']} du {data_tournament['dates'][0]} au {data_tournament['dates'][1]}\n')

    @staticmethod
    def view_players_tournament(data_tournament):
        pass
        # headers = ['Nom', 'Prénom']
        # print(tabulate(body, headers=headers, tablefmt="double_grid"))

    @staticmethod
    def view_start_tournament():
        name_tournament = input('Nom du tournoi que vous souhaitez démarrer ou passer au round suivant: ')
        return name_tournament

    @staticmethod
    def view_round(data_current_round):
        print(f'\nRound {data_current_round} \n')

    @staticmethod
    def message_user(message):
        print(message)

    @staticmethod
    def result_match(players):
        print(f'{players[0]['name_player']} vs {players[1]['name_player']}')
        result = input(f"Résultat du joueur {players[0]['name_player']} [1: Victoire / 0.5: Match nul / 0: Défaite]: ")
        return result
