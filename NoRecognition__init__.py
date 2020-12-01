import asyncio
import threading
import sys
import time

from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
import rclpy
from rclpy.node import Node

from string_interface.srv import MARCO
from std_msgs.msg import String

sys.path.insert(0,
                '/home/human/mycroft-core/skills/marco-chess-voice-skill/stockfish/')
from stockfishEngine import Stockfish


class MarcoChessVoice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        rclpy.init(args=None)
        self.log.info('*********** init ************')
        self.client = self.MarcoClientAsync()

        # init the stockfish chess engine
        self.active_game = False
        self.player_started = False
        self.converse = True
        self.last_evaluation = 0.0
        self.stockfish = Stockfish(
            "/home/human/Desktop/stockfish12",
            parameters={'Threads': 16,
                        'Write Debug Log': True})
        self.move_list = []


    @intent_handler(IntentBuilder('Greeting')
                    .require('hello'))
    def current_identity(self, message):

        self.speak_dialog('voice.chess.marco',
                          data={'name': ''},
                          wait=True)

    @intent_handler('voice.chess.marco.startGame.intent')
    def start_chess_game(self, message):
        self.converse = False
        if not self.active_game:
            self.active_game = True
            player_start = self.ask_yesno('voice.chess.marco.askStart',
                                          data={'name': ''})
            if player_start == 'no':
                self.speak_dialog('voice.chess.marco.start',
                                  data={'name': 'Ich'},
                                  wait=True)
                first_move = self.stockfish.get_best_move()
                self.move_list.append(first_move)
                self.speak_dialog('voice.chess.marco.moveFigure',
                                  data={'start': first_move[:2],
                                        'end': first_move[2:]},
                                  wait=True)
                self.stockfish.set_position(self.move_list)
            else:
                self.player_started = True
                self.speak_dialog('voice.chess.marco.start',
                                  data={'name': 'Du'},
                                  wait=True)
        else:
            self.speak_dialog('voice.chess.marco.alreadyPlaying',
                              wait=True)
        self.converse = True

    @intent_handler('voice.chess.marco.moveFigure.intent')
    def move_figure(self, message):
        self.converse = False
        if self.active_game:
            start = message.data.get('start')
            end = message.data.get('end')
            move = start + end
            if self.stockfish.is_move_correct(move):
                self.move_list.append(move)
                self.stockfish.set_position(self.move_list)

                self.speak_dialog('voice.chess.marco.moveFigure',
                                  data={'start': start, 'end': end},
                                  wait=True)

                current_evaluation = float(
                    self.stockfish.get_stockfish_evaluation())

                good_move = f'voice.chess.marco.emotion.goodMove'
                bad_move = f'voice.chess.marco.emotion.badMove'
                if self.player_started:
                    if self.last_evaluation > current_evaluation:
                        self.speak_dialog(good_move,
                                          wait=True)
                    else:
                        self.speak_dialog(bad_move,
                                          wait=True)
                else:
                    if self.last_evaluation < current_evaluation:
                        self.speak_dialog(good_move,
                                          wait=True)
                    else:
                        self.speak_dialog(bad_move,
                                          wait=True)

                marco_move = self.stockfish.get_best_move_time(10000)
                if marco_move:
                    self.move_list.append(marco_move)
                    self.speak_dialog('voice.chess.marco.moveFigure',
                                      data={'start': marco_move[:2],
                                            'end': marco_move[2:]},
                                      wait=True)
                    self.stockfish.set_position(self.move_list)
                    # sleep for 2 second after the move to wait for emotions
                    time.sleep(2)
                    own_move = f'voice.chess.marco.emotion.ownTurn'
                    self.speak_dialog(own_move,
                                      wait=True)
                    if not self.stockfish.get_best_move():
                        self.speak_dialog('voice.chess.marco.playerLost',
                                          wait=True)
                        self.active_game = False
                else:
                    self.speak_dialog('voice.chess.marco.lost',
                                      wait=True)
                    self.active_game = False

            else:
                self.speak_dialog('voice.chess.marco.invalidMove',
                                  wait=True)
        else:
            self.speak_dialog('voice.chess.marco.notPlaying',
                              wait=True)
        self.converse = True

    @intent_handler(IntentBuilder('getBoard')
                    .require('show')
                    .require('board'))
    def get_board(self, message):
        if self.active_game:
            self.log.info(self.stockfish.get_board_visual())
        else:
            self.speak_dialog('voice.chess.marco.notPlaying',
                              wait=True)

    @intent_handler('voice.chess.marco.surrender.intent')
    def surrender(self, message):
        if self.active_game:
            self.active_game = False
            self.speak_dialog('voice.chess.marco.surrender',
                              wait=True)
        self.speak_dialog('voice.chess.marco.notPlaying',
                          wait=True)

def create_skill():
    return MarcoChessVoice()
